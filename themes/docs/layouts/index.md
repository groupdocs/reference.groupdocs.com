{{- /* Home-page Markdown output.
       Product builds: the home IS the product family landing (layout: family) whose content
       lives entirely in front matter — render that data as real Markdown (mirrors family.html
       and products/ layouts/partials/md/layout-family.txt) so the .md is useful instead of a
       front-matter dump. Otherwise (site-root landing, layout: full-width) fall back to the
       generic body, identical to _default/list.md. */ -}}
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
