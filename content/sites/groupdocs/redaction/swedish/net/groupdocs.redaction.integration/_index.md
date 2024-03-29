---
title: GroupDocs.Redaction.Integration
second_title: GroupDocs.Redaction för .NET API-referens
description: DenIntegrationnamnrymden tillhandahåller gränssnitt och klasser som används för att integrera dokument i olika format med GroupDocs.Redaction.
type: docs
weight: 40
url: /sv/net/groupdocs.redaction.integration/
---
DenIntegrationnamnrymden tillhandahåller gränssnitt och klasser som används för att integrera dokument i olika format med GroupDocs.Redaction.

## Klasser

| Klass | Beskrivning |
| --- | --- |
| [DocumentFormatInstance](./documentformatinstance) | Representerar ett specifikt format för ett dokument. Implementera den här klassen för att lägga till dina egna dokumenttyper. |
| [MetadataCollection](./metadatacollection) | Representerar en ordbok för[`MetadataItem`](../groupdocs.redaction.integration/metadataitem) med dess titel som nyckel. |
| [MetadataItem](./metadataitem) | Representerar en metadatapost, gemensam för alla format som stöds och används i metadataredigering. |
## Gränssnitt

| Gränssnitt | Beskrivning |
| --- | --- |
| [IAnnotatedDocument](./iannotateddocument) | Definierar metoder som krävs för åtkomst till kommentarer, till exempel kommentarer. Behöver implementeras av[`DocumentFormatInstance`](../groupdocs.redaction.integration/documentformatinstance) -härledd klass för att utföra anteckningsredigeringar. |
| [ICellularFormatInstance](./icellularformatinstance) | Definierar metoder som krävs för åtkomst till kalkylbladsformat, med ett eller flera kalkylblad. |
| [IImageFormatInstance](./iimageformatinstance) | Definierar metoder som krävs för redigering av rasterbildsformat. |
| [IMetadataAccess](./imetadataaccess) | Definierar metoder som krävs för åtkomst till metadata för ett dokument, om formatet stöder det. |
| [IPaginatedDocument](./ipaginateddocument) | Definierar metoder som krävs för att manipulera ett dokuments sidor. Behöver implementeras av[`DocumentFormatInstance`](../groupdocs.redaction.integration/documentformatinstance) -härledd klass för att utföra sidredigeringar. |
| [IPreviewable](./ipreviewable) | Definierar metoder för att skapa förhandsvisning av dokumentet. |
| [IRasterizableDocument](./irasterizabledocument) | Definierar metoder som krävs för att spara dokument i vilken binär form som helst. Inbyggda typer sparar ett dokument som en PDF med bilder av dess sidor. |
| [ITextualFormatInstance](./itextualformatinstance) | Definierar metoder som krävs för att redigera textdata i alla dokument som innehåller text. |

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Redaction.dll -->
