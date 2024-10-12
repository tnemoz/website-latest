---
# the default layout is 'page'
icon: fas fa-book
order: 3
---

{% include lang.html %}

<div class="publications-container">
    {% assign publications = site.publications | sort: "year" | reverse %}
    {% assign row_index = 1 %}
    {% for paper in publications %}
  <div class="publications-first-column {% if row_index > 1 %}publications-first-row{% endif %}" style="grid-row: {{ row_index }}">
    {% assign first_row_index = row_index %}
    {% assign row_index = row_index | plus: 1 %}
      <a target="_blank" rel="noopener noreferrer" href="{{ paper.abstracturl }}">
        {{ paper.title }}
      </a>
  </div>
  <div class="publications-first-column" style="grid-row: {{ row_index }}">
      {% assign row_index = row_index | plus: 1 %}
      {{ paper.authors }}
  </div>
  {% if paper.publishedin %}
  <div class="publications-first-column" style="grid-row: {{ row_index }}">
    {% assign row_index = row_index | plus: 1 %}
    In 
      {% if paper.publishedinurl %}
      <a href="{{ paper.publishedinurl }}">
      {% endif %}
      {{ paper.publishedin }}
      {% if paper.publishedinurl %}
      </a>
      {% endif %}
  </div>
  {% endif %}
  {% capture bibtexcode %}
```bibtex
{{ paper.bibtex }}
```
{: .nolineno }
{%endcapture%}
  <div class="publications-first-column" style="grid-row: {{ row_index }}; display: none" id="bibtex-code-{{ paper.title }}">
    {% assign row_index = row_index | plus: 1 %}
    {{ bibtexcode | markdownify }}
  </div>
  <div {% if first_row_index > 1 %}class="publications-first-row"{% endif %} style="grid-column: 2; grid-row: {{ first_row_index }}">
      <a target="_blank" rel="noopener noreferrer" href="{{ paper.pdfurl }}" class="publications-table-icon" title="PDF File">
        <i class="fa-fw fas fa-file-pdf">
        </i>
      </a>
    </div>
    <div {% if first_row_index > 1 %}class="publications-first-row"{% endif %} style="grid-column: 3; grid-row: {{ first_row_index }}">
      <a href="#" class="publications-table-icon" title="BibTex entry" onclick="showBibTeXCode('{{ paper.title }}')">
        <i class="fa-fw fas fa-quote-right">
        </i>
      </a>
    </div>
{% endfor %}
</div>
<script type="text/javascript">
  function showBibTeXCode(title) {
    var elt = document.getElementById("bibtex-code-" + title);

    if (elt.style.display == "none") {
      elt.style.display = "block";
    } else {
      elt.style.display = "none";
    }
  }
</script>
<link rel="stylesheet" href="{{ '/assets/css/publications.css' | relative_url }}"/>
