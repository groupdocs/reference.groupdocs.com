---
title: SpreadsheetPreviewOptions
second_title: GroupDocs.Watermark for Java API Reference
description: Provides options to sets requirements and stream delegates for preview generation of Spreadsheet document.
type: docs
weight: 52
url: /java/com.groupdocs.watermark.options/spreadsheetpreviewoptions/
---
**Inheritance:**
java.lang.Object, [com.groupdocs.watermark.options.PreviewOptions](../../com.groupdocs.watermark.options/previewoptions)
```
public class SpreadsheetPreviewOptions extends PreviewOptions
```

Provides options to sets requirements and stream delegates for preview generation of Spreadsheet document.
## Constructors

| Constructor | Description |
| --- | --- |
| [SpreadsheetPreviewOptions(ICreatePageStream createPageStream)](#SpreadsheetPreviewOptions-com.groupdocs.watermark.options.ICreatePageStream-) | Initializes a new instance of the `[SpreadsheetPreviewOptions](../../com.groupdocs.watermark.options/spreadsheetpreviewoptions)` class causing the output stream to be closed. |
| [SpreadsheetPreviewOptions(ICreatePageStream createPageStream, IReleasePageStream releasePageStream)](#SpreadsheetPreviewOptions-com.groupdocs.watermark.options.ICreatePageStream-com.groupdocs.watermark.options.IReleasePageStream-) | Initializes a new instance of `[SpreadsheetPreviewOptions](../../com.groupdocs.watermark.options/spreadsheetpreviewoptions)` class causing the output stream to be returned to the client for further use. |
## Fields

| Field | Description |
| --- | --- |
| [DefaultResolution](#DefaultResolution) | Default resolution in dots per inch. |
## Methods

| Method | Description |
| --- | --- |
| [getResolution()](#getResolution--) | Gets the resolution for the generated images, in dots per inch. |
| [setResolution(int value)](#setResolution-int-) | Sets the resolution for the generated images, in dots per inch. |
| [getOnlyDataArea()](#getOnlyDataArea--) | Gets the flag for rendering the data area only without headers, footers, margins. |
| [setOnlyDataArea(boolean value)](#setOnlyDataArea-boolean-) | Sets the flag for rendering the data area only without headers, footers, margins. |
### SpreadsheetPreviewOptions(ICreatePageStream createPageStream) {#SpreadsheetPreviewOptions-com.groupdocs.watermark.options.ICreatePageStream-}
```
public SpreadsheetPreviewOptions(ICreatePageStream createPageStream)
```


Initializes a new instance of the `[SpreadsheetPreviewOptions](../../com.groupdocs.watermark.options/spreadsheetpreviewoptions)` class causing the output stream to be closed.

**Parameters:**
| Parameter | Type | Description |
| --- | --- | --- |
| createPageStream | [ICreatePageStream](../../com.groupdocs.watermark.options/icreatepagestream) | Creates a stream for a specific page preview. |

### SpreadsheetPreviewOptions(ICreatePageStream createPageStream, IReleasePageStream releasePageStream) {#SpreadsheetPreviewOptions-com.groupdocs.watermark.options.ICreatePageStream-com.groupdocs.watermark.options.IReleasePageStream-}
```
public SpreadsheetPreviewOptions(ICreatePageStream createPageStream, IReleasePageStream releasePageStream)
```


Initializes a new instance of `[SpreadsheetPreviewOptions](../../com.groupdocs.watermark.options/spreadsheetpreviewoptions)` class causing the output stream to be returned to the client for further use.

**Parameters:**
| Parameter | Type | Description |
| --- | --- | --- |
| createPageStream | [ICreatePageStream](../../com.groupdocs.watermark.options/icreatepagestream) | Creates a stream for a specific page preview. |
| releasePageStream | [IReleasePageStream](../../com.groupdocs.watermark.options/ireleasepagestream) | Notifies that the page preview generation is done and gets the output stream. |

### DefaultResolution {#DefaultResolution}
```
public static final int DefaultResolution
```


Default resolution in dots per inch.

### getResolution() {#getResolution--}
```
public final int getResolution()
```


Gets the resolution for the generated images, in dots per inch.

**Returns:**
int - The resolution for the generated images, in dots per inch.

--------------------

The default value is 96.
### setResolution(int value) {#setResolution-int-}
```
public final void setResolution(int value)
```


Sets the resolution for the generated images, in dots per inch.

**Parameters:**
| Parameter | Type | Description |
| --- | --- | --- |
| value | int | The resolution for the generated images, in dots per inch.

--------------------

The default value is 96. |

### getOnlyDataArea() {#getOnlyDataArea--}
```
public final boolean getOnlyDataArea()
```


Gets the flag for rendering the data area only without headers, footers, margins.

**Returns:**
boolean - The flag for rendering the data area only without headers, footers, margins.

--------------------

This flags leads to rendering the whole worksheet on one page. The default value is  false .
### setOnlyDataArea(boolean value) {#setOnlyDataArea-boolean-}
```
public final void setOnlyDataArea(boolean value)
```


Sets the flag for rendering the data area only without headers, footers, margins.

**Parameters:**
| Parameter | Type | Description |
| --- | --- | --- |
| value | boolean | The flag for rendering the data area only without headers, footers, margins.

--------------------

This flags leads to rendering the whole worksheet on one page. The default value is  false . |

