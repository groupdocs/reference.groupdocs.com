---
title: AddAttachment
second_title: GroupDocs.Watermark for .NET API-referens
description: Lägger till en bilaga tillSpreadsheetWorksheetgroupdocs.watermark.contents.spreadsheet/spreadsheetworksheet .
type: docs
weight: 10
url: /sv/net/groupdocs.watermark.contents.spreadsheet/spreadsheetattachmentcollection/addattachment/
---
## SpreadsheetAttachmentCollection.AddAttachment method

Lägger till en bilaga till[`SpreadsheetWorksheet`](../../spreadsheetworksheet) .

```csharp
public void AddAttachment(byte[] fileContent, string sourceFullName, byte[] previewImageContent, 
    double x, double y, double width, double height)
```

| Parameter | Typ | Beskrivning |
| --- | --- | --- |
| fileContent | Byte[] | Innehållet i filen som ska bifogas. |
| sourceFullName | String | Det fullständiga namnet på den bifogade filen (tillägget används för att bestämma lämpligt program för att öppna filen). |
| previewImageContent | Byte[] | Den bifogade filens förhandsvisningsbild som en byte-array. |
| x | Double | X-koordinaten för fästramen (i punkter). |
| y | Double | Y-koordinaten för fästramen (i punkter). |
| width | Double | Fästramens bredd i punkter. |
| height | Double | Höjden på fästramen i punkter. |

### Se även

* class [SpreadsheetAttachmentCollection](../../spreadsheetattachmentcollection)
* namnutrymme [GroupDocs.Watermark.Contents.Spreadsheet](../../spreadsheetattachmentcollection)
* hopsättning [GroupDocs.Watermark](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Watermark.dll -->
