---
title: FontResourceBase
second_title: GroupDocs.Editor voor .NET API-referentie
description: Basisklasse voor elk ondersteund lettertype als bron voor het HTMLdocument met al zijn eigenschappen
type: docs
weight: 370
url: /nl/net/groupdocs.editor.htmlcss.resources.fonts/fontresourcebase/
---
## FontResourceBase class

Basisklasse voor elk ondersteund lettertype als bron voor het HTML-document met al zijn eigenschappen

```csharp
public abstract class FontResourceBase : IEquatable<FontResourceBase>, IHtmlResource
```

## Eigenschappen

| Naam | Beschrijving |
| --- | --- |
| [ByteContent](../../groupdocs.editor.htmlcss.resources.fonts/fontresourcebase/bytecontent) { get; } | Retourneert de inhoud van dit lettertype als bytestream |
| [FilenameWithExtension](../../groupdocs.editor.htmlcss.resources.fonts/fontresourcebase/filenamewithextension) { get; } | Retourneert de juiste bestandsnaam van deze lettertyperesource, die bestaat uit naam en extensie. Theoretisch kan afwijken van de naam. |
| [IsDisposed](../../groupdocs.editor.htmlcss.resources.fonts/fontresourcebase/isdisposed) { get; } | Bepaalt of dit lettertype is verwijderd of niet |
| [Name](../../groupdocs.editor.htmlcss.resources.fonts/fontresourcebase/name) { get; } | Retourneert de naam van deze lettertyperesource. Bevat meestal geen bestandsnaamextensie en kan theoretisch verschillen van bestandsnaam. |
| [TextContent](../../groupdocs.editor.htmlcss.resources.fonts/fontresourcebase/textcontent) { get; } | Retourneert de inhoud van dit lettertype als base64-gecodeerde tekenreeks. Deze waarde wordt na de eerste aanroep in de cache opgeslagen. |
| abstract [Type](../../groupdocs.editor.htmlcss.resources.fonts/fontresourcebase/type) { get; } | Bij het implementeren moet type informatie over het type van een specifieke fontresource retourneren als een instantie van een specifiek FontType-type, dat alle typespecifieke info omvat |

## methoden

| Naam | Beschrijving |
| --- | --- |
| [Dispose](../../groupdocs.editor.htmlcss.resources.fonts/fontresourcebase/dispose)() | Verwijdert deze lettertyperesource, verwijdert de inhoud ervan en zorgt ervoor dat de meeste methoden en eigenschappen niet werken |
| [Equals](../../groupdocs.editor.htmlcss.resources.fonts/fontresourcebase/equals#equals)(FontResourceBase) | Controleert deze instantie met opgegeven lettertyperesource op referentie-equity |
| [Equals](../../groupdocs.editor.htmlcss.resources.fonts/fontresourcebase/equals#equals_1)(IHtmlResource) | Controleert deze instantie met gespecificeerde HTML-resource op referentie-equity |
| [Save](../../groupdocs.editor.htmlcss.resources.fonts/fontresourcebase/save)(string) | Slaat dit lettertype op in het opgegeven bestand |

## Evenementen

| Naam | Beschrijving |
| --- | --- |
| event [Disposed](../../groupdocs.editor.htmlcss.resources.fonts/fontresourcebase/disposed) | Gebeurtenis die optreedt wanneer dit lettertype wordt weggegooid |

### Zie ook

* interface [IHtmlResource](../../groupdocs.editor.htmlcss.resources/ihtmlresource)
* naamruimte [GroupDocs.Editor.HtmlCss.Resources.Fonts](../../groupdocs.editor.htmlcss.resources.fonts)
* montage [GroupDocs.Editor](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Editor.dll -->
