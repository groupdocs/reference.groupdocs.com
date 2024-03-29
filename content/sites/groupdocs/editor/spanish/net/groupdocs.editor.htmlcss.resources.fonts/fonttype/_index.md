---
title: FontType
second_title: Referencia de API de GroupDocs.Editor para .NET
description: Representa un tipo de fuente compatible
type: docs
weight: 380
url: /es/net/groupdocs.editor.htmlcss.resources.fonts/fonttype/
---
## FontType structure

Representa un tipo de fuente compatible

```csharp
public struct FontType : IEquatable<FontType>, IResourceType
```

## Propiedades

| Nombre | Descripción |
| --- | --- |
| static [Eot](../../groupdocs.editor.htmlcss.resources.fonts/fonttype/eot) { get; } | Representa un tipo de fuente EOT (OpenType incrustado) |
| static [Otf](../../groupdocs.editor.htmlcss.resources.fonts/fonttype/otf) { get; } | Representa un tipo de fuente OTF (OpenType Font) |
| static [Ttf](../../groupdocs.editor.htmlcss.resources.fonts/fonttype/ttf) { get; } | Representa un tipo de fuente TTF (fuente TrueType) |
| static [Undefined](../../groupdocs.editor.htmlcss.resources.fonts/fonttype/undefined) { get; } | Valor especial, que marca fuente no definida, desconocida o no admitida resource |
| static [Woff](../../groupdocs.editor.htmlcss.resources.fonts/fonttype/woff) { get; } | Representa un tipo de fuente WOFF (Web Open Font Format) |
| static [Woff2](../../groupdocs.editor.htmlcss.resources.fonts/fonttype/woff2) { get; } | Representa un tipo de fuente WOFF2 (Web Open Font Format versión 2) |
| [CssName](../../groupdocs.editor.htmlcss.resources.fonts/fonttype/cssname) { get; } | Devuelve el nombre compatible con CSS de este tipo de fuente, que se usa en @font-face at-rule |
| [FileExtension](../../groupdocs.editor.htmlcss.resources.fonts/fonttype/fileextension) { get; } | Extensión de nombre de archivo (sin carácter de punto) para este tipo de fuente |
| [FontFormat](../../groupdocs.editor.htmlcss.resources.fonts/fonttype/fontformat) { get; } | Formato de fuente para @font-face format |
| [FormalName](../../groupdocs.editor.htmlcss.resources.fonts/fonttype/formalname) { get; } | Devuelve un nombre formal de este tipo de fuente |
| [MimeCode](../../groupdocs.editor.htmlcss.resources.fonts/fonttype/mimecode) { get; } | código MIME de un tipo de fuente particular |

## Métodos

| Nombre | Descripción |
| --- | --- |
| static [GetFirstDefined](../../groupdocs.editor.htmlcss.resources.fonts/fonttype/getfirstdefined)(params FontType[]) | Devuelve un primer tipo de fuente del conjunto especificado, que no es un valor "Indefinido" o un tipo de fuente "Indefinido" (cuando todos los elementos son "Indefinidos") |
| static [ParseFromCssName](../../groupdocs.editor.htmlcss.resources.fonts/fonttype/parsefromcssname)(string) | Devuelve el valor de FontType, que es equivalente al nombre especificado compatible con CSS del tipo de fuente |
| static [ParseFromFilenameWithExtension](../../groupdocs.editor.htmlcss.resources.fonts/fonttype/parsefromfilenamewithextension)(string) | Devuelve el valor de FontType, que es equivalente a la extensión del nombre de archivo, que se extrae del nombre de archivo especificado |
| static [ParseFromMime](../../groupdocs.editor.htmlcss.resources.fonts/fonttype/parsefrommime)(string) | Devuelve el valor de FontType, que es equivalente al código MIME especificado |
| [Equals](../../groupdocs.editor.htmlcss.resources.fonts/fonttype/equals#equals)(FontType) | Determina si esta instancia es igual a la instancia "FontType" especificada |
| override [Equals](../../groupdocs.editor.htmlcss.resources.fonts/fonttype/equals#equals_1)(object) | Determina si esta instancia es igual al objeto no emitido especificado, que presumiblemente es otra instancia "FontType" |
| override [GetHashCode](../../groupdocs.editor.htmlcss.resources.fonts/fonttype/gethashcode)() | Devuelve un código hash, que es un número constante para este valor específico type |
| [operator ==](../../groupdocs.editor.htmlcss.resources.fonts/fonttype/op_equality) | Comprueba si dos valores de "FontType" son iguales |
| [operator !=](../../groupdocs.editor.htmlcss.resources.fonts/fonttype/op_inequality) | Comprueba si dos valores de "FontType" no son iguales |

### Ver también

* interface [IResourceType](../../groupdocs.editor.htmlcss.resources/iresourcetype)
* espacio de nombres [GroupDocs.Editor.HtmlCss.Resources.Fonts](../../groupdocs.editor.htmlcss.resources.fonts)
* asamblea [GroupDocs.Editor](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Editor.dll -->
