---
title: TextType
second_title: Referencia de API de GroupDocs.Editor para .NET
description: Representa un tipo de recurso textual compatible
type: docs
weight: 650
url: /es/net/groupdocs.editor.htmlcss.resources.textual/texttype/
---
## TextType structure

Representa un tipo de recurso textual compatible

```csharp
public struct TextType : IEquatable<TextType>, IResourceType
```

## Propiedades

| Nombre | Descripción |
| --- | --- |
| static [Css](../../groupdocs.editor.htmlcss.resources.textual/texttype/css) { get; } | Tipo CSS del recurso textual |
| static [Undefined](../../groupdocs.editor.htmlcss.resources.textual/texttype/undefined) { get; } | Valor especial, que marca recurso textual no definido, desconocido o no soportado |
| static [Xml](../../groupdocs.editor.htmlcss.resources.textual/texttype/xml) { get; } | Tipo XML del recurso textual |
| [FileExtension](../../groupdocs.editor.htmlcss.resources.textual/texttype/fileextension) { get; } | Extensión de archivo (sin carácter de punto inicial) de un recurso textual particular |
| [FormalName](../../groupdocs.editor.htmlcss.resources.textual/texttype/formalname) { get; } | Devuelve un nombre formal de este tipo de recurso textual |
| [MimeCode](../../groupdocs.editor.htmlcss.resources.textual/texttype/mimecode) { get; } | Código MIME de un tipo de recurso textual en particular |

## Métodos

| Nombre | Descripción |
| --- | --- |
| static [ParseFromFilenameWithExtension](../../groupdocs.editor.htmlcss.resources.textual/texttype/parsefromfilenamewithextension)(string) | Devuelve el valor TextType, que es equivalente a la extensión del nombre de archivo, que se extrae del nombre de archivo especificado con extensión o extensión pura |
| override [Equals](../../groupdocs.editor.htmlcss.resources.textual/texttype/equals#equals_1)(object) | Determina si esta instancia es igual al objeto no emitido especificado, que presumiblemente es otra instancia de "TextType" |
| [Equals](../../groupdocs.editor.htmlcss.resources.textual/texttype/equals#equals)(TextType) | Determina si esta instancia es igual a la instancia "TextType" especificada |
| override [GetHashCode](../../groupdocs.editor.htmlcss.resources.textual/texttype/gethashcode)() | Devuelve un código hash, que es un número constante para este valor específico type |
| [operator ==](../../groupdocs.editor.htmlcss.resources.textual/texttype/op_equality) | Define si dos instancias específicas de "TextType" son iguales |
| [operator !=](../../groupdocs.editor.htmlcss.resources.textual/texttype/op_inequality) | Define si dos instancias específicas de "TextType" no son iguales |

### Ver también

* interface [IResourceType](../../groupdocs.editor.htmlcss.resources/iresourcetype)
* espacio de nombres [GroupDocs.Editor.HtmlCss.Resources.Textual](../../groupdocs.editor.htmlcss.resources.textual)
* asamblea [GroupDocs.Editor](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Editor.dll -->
