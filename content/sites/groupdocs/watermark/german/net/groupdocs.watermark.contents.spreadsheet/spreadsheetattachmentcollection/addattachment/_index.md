---
title: AddAttachment
second_title: GroupDocs.Watermark für .NET-API-Referenz
description: Fügt einen Anhang hinzuSpreadsheetWorksheetgroupdocs.watermark.contents.spreadsheet/spreadsheetworksheet .
type: docs
weight: 10
url: /de/net/groupdocs.watermark.contents.spreadsheet/spreadsheetattachmentcollection/addattachment/
---
## SpreadsheetAttachmentCollection.AddAttachment method

Fügt einen Anhang hinzu[`SpreadsheetWorksheet`](../../spreadsheetworksheet) .

```csharp
public void AddAttachment(byte[] fileContent, string sourceFullName, byte[] previewImageContent, 
    double x, double y, double width, double height)
```

| Parameter | Typ | Beschreibung |
| --- | --- | --- |
| fileContent | Byte[] | Der Inhalt der anzuhängenden Datei. |
| sourceFullName | String | Der vollständige Name der angehängten Datei (Die Erweiterung wird verwendet, um die geeignete Anwendung zum Öffnen der Datei zu bestimmen). |
| previewImageContent | Byte[] | Das Vorschaubild der angehängten Datei als Byte-Array. |
| x | Double | Die x-Koordinate des Befestigungsrahmens (in Punkten). |
| y | Double | Die y-Koordinate des Befestigungsrahmens (in Punkten). |
| width | Double | Die Breite des Befestigungsrahmens in Punkten. |
| height | Double | Die Höhe des Anbaurahmens in Punkten. |

### Siehe auch

* class [SpreadsheetAttachmentCollection](../../spreadsheetattachmentcollection)
* namensraum [GroupDocs.Watermark.Contents.Spreadsheet](../../spreadsheetattachmentcollection)
* Montage [GroupDocs.Watermark](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Watermark.dll -->