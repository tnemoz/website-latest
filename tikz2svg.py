import argparse
import os
import re
from subprocess import Popen, PIPE

FONTS = {
    "light": [52, 52, 60],
    "dark": [175, 176, 177]
}

BACKGROUND = {
    "light": [255, 255, 255],
    "dark": [27, 27, 30]
}

EXTENSION = ".to_draw"

parser = argparse.ArgumentParser()

parser.add_argument(
    "folder",
    help=f"The folder containing the {EXTENSION} files quantikz code to convert",
    metavar="FOLDER",
)
parser.add_argument(
    "-r",
    "--recurse",
    help="If active, the script will recursively look for all files in the subfolders",
    action="store_true"
)
parser.add_argument(
    "-v",
    "--verbosity",
    help="If active, it will display additional information when running the script",
    action="count",
    default=0
)

args = parser.parse_args()

draw_folder = args.folder
gen = os.walk(draw_folder)

if not args.recurse:
    gen = [next(gen)]

for dirpath, dirnames, filenames in gen:
    if args.verbosity >= 1:
        print(f"Analyzing {dirpath}...")

    for filename in filenames:
        filename_draw = os.path.join(dirpath, filename)
        basename, ext = os.path.splitext(filename)

        if not ext == EXTENSION:
            continue

        tmp_folder = os.path.join("/tmp", dirpath)

        if not os.path.isdir(tmp_folder):
            os.makedirs(tmp_folder)

        with open(filename_draw, "r") as f:
            content = f.read()

        for theme in ["light", "dark"]:
            filename_theme = os.path.join(tmp_folder, f"{basename}_{theme}.tex")

            with open(filename_theme, "w") as f:
                f.write(r"""\documentclass{standalone}
\usepackage[utf8]{inputenc}

\usepackage{tikz}
\usetikzlibrary{quantikz2}

\usepackage{xcolor}

\definecolor{font}{RGB}{"""
                )
                f.write(", ".join(str(x) for x in FONTS[theme]))
                f.write(r"""}
\definecolor{background}{RGB}{"""
                )
                f.write(", ".join(str(x) for x in BACKGROUND[theme]))
                f.write("""}\n""")
                f.write(content)

            if args.verbosity >= 2:
                print(f"Compiling {filename_theme}...")

            process = Popen(["latexmk", "-halt-on-error", "-pdf", "-cd", filename_theme], stdout=PIPE, stderr=PIPE)
            _, stderr = process.communicate()

            if stderr:
                print(f"Error while compiling: {stderr}. Skipping {filename_theme}...")
                continue

            svg_filename = os.path.join(tmp_folder, f"{basename}_{theme}.svg")

            if args.verbosity >= 2:
                print("Converting to SVG...")
            
            process = Popen(
                [
                    "pdf2svg",
                    os.path.join(tmp_folder, f"{os.path.splitext(filename_theme)[0]}.pdf"),
                    svg_filename
                ],
                stderr=PIPE
            )
            _, stderr = process.communicate()

            if stderr:
                print(f"Error while converting to SVG: {stderr}. Skipping...")
                continue

            with open(svg_filename, "r") as f:
                content_svg = f.read()

            search = re.search(r"<svg.*width=\"([0-9]*\.?[0-9]*)\".*height=\"([0-9]*\.?[0-9]*)\"", content_svg)
            width_span = search.span(1)
            height_span = search.span(2)

            new_content_svg = content_svg[:width_span[0]]
            new_content_svg += "100%"
            new_content_svg += content_svg[width_span[1]:height_span[0]]
            new_content_svg += "100%"
            new_content_svg += content_svg[height_span[1]:]
            generated_name = os.path.split(svg_filename)[1]
            generated_name = "generated-" + generated_name

            with open(os.path.join(dirpath, generated_name), "w") as f:
                f.write(new_content_svg)

