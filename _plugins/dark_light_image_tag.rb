require 'cgi'

module Jekyll
  class DarkLightImageTag < Liquid::Tag
    def initialize(tag_name, args, tokens)
      super
      @args = parse_arguments(args)
      @image_title = @args['image']
      @alt = @args['alt'] || ''
      @width = @args['width'] || '100%'
      @subtitle = @args['subtitle'] || ''
    end

    def parse_arguments(args)
      args.split(";").map do |arg|
        key, value = arg.split("=")
        [key.strip, value.strip[1...-1].gsub(/\\(.)/, '\1')] if key && value
      end.compact.to_h
    end

    def render(context)
      ext = File.extname(@image_title)
      image_path = @image_title.sub(ext, '')

      image_tag = "![#{@alt}](#{image_path}_light#{ext}){: width='#{@width}' .light}"
      dark_image_tag = "![#{@alt}](#{image_path}_dark#{ext}){: width='#{@width}' .dark}"

      "#{image_tag}\n#{dark_image_tag}\n_#{@subtitle}_"
    end
  end
end

Liquid::Template.register_tag('dark_light_image', Jekyll::DarkLightImageTag)

