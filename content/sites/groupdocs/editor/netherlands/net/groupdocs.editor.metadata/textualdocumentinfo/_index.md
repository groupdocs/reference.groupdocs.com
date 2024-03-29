---
title: TextualDocumentInfo
second_title: GroupDocs.Editor voor .NET API-referentie
description: Vertegenwoordigt metadata van één tekstdocument zoals XML HTML of platte tekst TXT
type: docs
weight: 780
url: /nl/net/groupdocs.editor.metadata/textualdocumentinfo/
---
## TextualDocumentInfo structure

Vertegenwoordigt metadata van één tekstdocument zoals XML, HTML of platte tekst (TXT)

```csharp
public struct TextualDocumentInfo : IDocumentInfo
```

## Eigenschappen

| Naam | Beschrijving |
| --- | --- |
| [Encoding](../../groupdocs.editor.metadata/textualdocumentinfo/encoding) { get; } | Retourneert gedetecteerde vermoedelijke codering van het tekstdocument |
| [Format](../../groupdocs.editor.metadata/textualdocumentinfo/format) { get; } | Retourneert een indeling van dit tekstuele document. Kan in sommige gevallen niet 100% correct zijn. |
| [IsEncrypted](../../groupdocs.editor.metadata/textualdocumentinfo/isencrypted) { get; } | Geeft altijd ` terug`vals` `, omdat tekstuele documenten niet kunnen worden versleuteld |
| [PageCount](../../groupdocs.editor.metadata/textualdocumentinfo/pagecount) { get; } | Geeft altijd 1 terug |
| [Size](../../groupdocs.editor.metadata/textualdocumentinfo/size) { get; } | Retourneert de grootte in bytes (niet het aantal tekens) van dit tekstuele document |

### Zie ook

* interface [IDocumentInfo](../idocumentinfo)
* naamruimte [GroupDocs.Editor.Metadata](../../groupdocs.editor.metadata)
* montage [GroupDocs.Editor](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Editor.dll -->
