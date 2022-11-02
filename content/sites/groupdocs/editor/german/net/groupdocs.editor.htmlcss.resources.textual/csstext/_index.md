---
title: CssText
second_title: GroupDocs.Editor für .NET-API-Referenz
description: Repräsentiert eine CSSTextressource
type: docs
weight: 480
url: /de/net/groupdocs.editor.htmlcss.resources.textual/csstext/
---
## CssText class

Repräsentiert eine CSS-Textressource

```csharp
public sealed class CssText : TextResourceBase
```

## Eigenschaften

| Name | Beschreibung |
| --- | --- |
| [ByteContent](../../groupdocs.editor.htmlcss.resources.textual/textresourcebase/bytecontent) { get; } | Gibt den Inhalt dieser Textressource als Bytestrom mit Originalcodierung zurück |
| [Encoding](../../groupdocs.editor.htmlcss.resources.textual/textresourcebase/encoding) { get; } | Gibt die Codierung dieser Textressource zurück. Gibt normalerweise UTF-8. zurück |
| [FilenameWithExtension](../../groupdocs.editor.htmlcss.resources.textual/textresourcebase/filenamewithextension) { get; } | Gibt den korrekten Dateinamen dieser Textressource zurück, der aus Name und Erweiterung besteht |
| [IsDisposed](../../groupdocs.editor.htmlcss.resources.textual/textresourcebase/isdisposed) { get; } | Bestimmt, ob diese Textressource verworfen wird oder nicht |
| [Name](../../groupdocs.editor.htmlcss.resources.textual/textresourcebase/name) { get; } | Gibt den Namen dieser Textressource ohne Dateierweiterung zurück |
| [TextContent](../../groupdocs.editor.htmlcss.resources.textual/textresourcebase/textcontent) { get; } | Gibt den Inhalt dieser Textressource als Standard-String zurück |
| override [Type](../../groupdocs.editor.htmlcss.resources.textual/csstext/type) { get; } | Gibt TextType.Css zurück |

## Methoden

| Name | Beschreibung |
| --- | --- |
| [Dispose](../../groupdocs.editor.htmlcss.resources.textual/textresourcebase/dispose)() | Verwirft diese Textressource, verwirft ihren Inhalt und macht die meisten Methoden und Eigenschaften funktionsunfähig. Tolerant gegenüber mehreren Aufrufen. |
| [Equals](../../groupdocs.editor.htmlcss.resources.textual/textresourcebase/equals)(IHtmlResource) | Prüft diese Instanz mit Angabe auf Gleichheit. |
| [Save](../../groupdocs.editor.htmlcss.resources.textual/textresourcebase/save)(string) | Speichert diese Textressource in der angegebenen Datei |

## Veranstaltungen

| Name | Beschreibung |
| --- | --- |
| event [Disposed](../../groupdocs.editor.htmlcss.resources.textual/textresourcebase/disposed) | Ereignis, das eintritt, wenn diese Textressource entsorgt wird |

### Siehe auch

* class [TextResourceBase](../textresourcebase)
* namensraum [GroupDocs.Editor.HtmlCss.Resources.Textual](../../groupdocs.editor.htmlcss.resources.textual)
* Montage [GroupDocs.Editor](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Editor.dll -->