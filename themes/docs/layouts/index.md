{{- /* Home-page Markdown output.
       - Product builds: the home IS the product family landing (layout: family) whose content
         lives entirely in front matter — render that data as real Markdown (mirrors family.html)
         instead of dumping front matter.
       - Site-root build: the home is the landing page (layout: full-width) whose body is
         hand-authored HTML + a products-grid shortcode that .RawContent cannot expand —
         render a clean Markdown index instead (products from data/products.toml; the AI and
         Developer-Resources sections mirror the curated content body).
       - Any other home: generic fallback, identical to _default/list.md. */ -}}
{{- if eq .Layout "family" -}}
# {{ .Title }}
{{ with (or .Params.lead .Description) }}
{{ . }}
{{ end }}
{{- with .Params.platforms }}
## Choose your platform
{{ range . }}
### {{ .name }}{{ with .version }} — v{{ . }}{{ end }}
{{ with .install }}
```
{{ . }}
```
{{ end }}
{{- $u := .ref | strings.TrimPrefix "/" | absURL | strings.TrimRight "/" -}}
[Browse API reference]({{ $u }}.md)
{{ end }}
{{ end -}}
{{- with .Params.capabilities }}
## Key capabilities
{{ range . }}
- {{ . }}
{{- end }}
{{ end -}}
{{- with .Params.formats }}
## Supported formats
{{ delimit . ", " }}
{{ end -}}
{{- with .Params.resources }}
## Resources
{{ range . }}
- [{{ .name }}]({{ .url }})
{{- end }}
{{ end -}}
{{- else if and (eq .Layout "full-width") .Site.Data.products -}}
# {{ .Title }}
{{ with .Description }}
{{ . }}
{{ end }}
## Products
{{ range sort .Site.Data.products.product "weight" }}
- [{{ .title }}]({{ .url | strings.TrimPrefix "/" | absURL | strings.TrimRight "/" }}.md): {{ .description }}
{{- end }}

## AI Agents & LLM Friendly

GroupDocs products plug straight into AI agents, LLMs, and automated document pipelines.

- [MCP Server](https://docs.groupdocs.com/mcp): LLMs query GroupDocs documentation on demand via the Model Context Protocol, reducing token usage and improving accuracy.
- [AGENTS.md](https://docs.groupdocs.com/): Machine-readable docs bundled into Python packages for automatic discovery by AI coding assistants like Claude, Copilot, and Cursor.
- [llms.txt](https://docs.groupdocs.com/llms.txt): Full documentation as llms.txt and llms-full.txt for direct LLM consumption — also available per product.

## Developer Resources

- [Documentation](https://docs.groupdocs.com/)
- [Releases & Downloads](https://releases.groupdocs.com/)
- [Product Site](https://products.groupdocs.com/)
- [Blog](https://blog.groupdocs.com/)
- [Support Forum](https://forum.groupdocs.com/)
{{- else -}}
# {{ partial "utils/title" . }}
{{ with .Description }}
{{ . }}
{{ end }}
{{ partial "md/abs-content.txt" . }}
{{ if and (not .Params.hideChildren) (.Pages) }}
## Contents
{{ range .Pages.ByWeight }}
- [{{ partial "utils/title" . }}]({{ strings.TrimRight "/" .Permalink }}.md)
{{- end }}
{{ end }}
{{- end -}}
