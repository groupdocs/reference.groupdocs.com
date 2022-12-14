---
title: SpreadsheetPreviewOptions
second_title: GroupDocs.Watermark for .NET API Reference
description: Initializes a new instance of the SpreadsheetPreviewOptionsgroupdocs.watermark.options.spreadsheet/spreadsheetpreviewoptions class causing the output stream to be closed.
type: docs
weight: 10
url: /net/groupdocs.watermark.options.spreadsheet/spreadsheetpreviewoptions/spreadsheetpreviewoptions/
---
## SpreadsheetPreviewOptions(CreatePageStream) {#constructor}

Initializes a new instance of the [`SpreadsheetPreviewOptions`](../../spreadsheetpreviewoptions) class causing the output stream to be closed.

```csharp
public SpreadsheetPreviewOptions(CreatePageStream createPageStream)
```

| Parameter | Type | Description |
| --- | --- | --- |
| createPageStream | CreatePageStream | Creates a stream for a specific page preview. |

### See Also

* delegate [CreatePageStream](../../../groupdocs.watermark.options/createpagestream)
* class [SpreadsheetPreviewOptions](../../spreadsheetpreviewoptions)
* namespace [GroupDocs.Watermark.Options.Spreadsheet](../../spreadsheetpreviewoptions)
* assembly [GroupDocs.Watermark](../../../)

---

## SpreadsheetPreviewOptions(CreatePageStream, ReleasePageStream) {#constructor_1}

Initializes a new instance of [`SpreadsheetPreviewOptions`](../../spreadsheetpreviewoptions) class causing the output stream to be returned to the client for further use.

```csharp
public SpreadsheetPreviewOptions(CreatePageStream createPageStream, 
    ReleasePageStream releasePageStream)
```

| Parameter | Type | Description |
| --- | --- | --- |
| createPageStream | CreatePageStream | Creates a stream for a specific page preview. |
| releasePageStream | ReleasePageStream | Notifies that the page preview generation is done and gets the output stream. |

### See Also

* delegate [CreatePageStream](../../../groupdocs.watermark.options/createpagestream)
* delegate [ReleasePageStream](../../../groupdocs.watermark.options/releasepagestream)
* class [SpreadsheetPreviewOptions](../../spreadsheetpreviewoptions)
* namespace [GroupDocs.Watermark.Options.Spreadsheet](../../spreadsheetpreviewoptions)
* assembly [GroupDocs.Watermark](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.watermark.dll -->
