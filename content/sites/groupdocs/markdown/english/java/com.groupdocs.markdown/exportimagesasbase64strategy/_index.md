---
title: ExportImagesAsBase64Strategy
second_title: GroupDocs.Markdown for Java API Reference
description: Implements an image export strategy that embeds images as Base64 strings directly in the Markdown.
type: docs
weight: 18
url: /java/com.groupdocs.markdown/exportimagesasbase64strategy/
---
**Inheritance:**
java.lang.Object

**All Implemented Interfaces:**
[com.groupdocs.markdown.IImageExportStrategy](../../com.groupdocs.markdown/iimageexportstrategy)
```
public class ExportImagesAsBase64Strategy implements IImageExportStrategy
```

Implements an image export strategy that embeds images as Base64 strings directly in the Markdown.


This strategy converts all images to Base64 format and embeds them directly in the Markdown document
using the data URI scheme. This eliminates the need for separate image files, making the Markdown
document self-contained. However, this approach increases the size of the Markdown file and may
not be supported by all Markdown viewers.

**Example:**

````

 ConvertOptions options = new ConvertOptions();
 options.setImageExportStrategy(new ExportImagesAsBase64Strategy());

 String markdown = MarkdownConverter.toMarkdown("document.docx", options);
 
````


## Constructors

| Constructor | Description |
| --- | --- |
| [ExportImagesAsBase64Strategy()](#ExportImagesAsBase64Strategy--) |  |
## Methods

| Method | Description |
| --- | --- |
| [getImagesFolder()](#getImagesFolder--) | Returns an empty string since this strategy does not use an images folder.
 |
| [getImageStream(ImageExportContext context)](#getImageStream-com.groupdocs.markdown.ImageExportContext-) | Returns null to indicate that the image should be embedded as Base64.
 |
### ExportImagesAsBase64Strategy() {#ExportImagesAsBase64Strategy--}
```
public ExportImagesAsBase64Strategy()
```


### getImagesFolder() {#getImagesFolder--}
```
public String getImagesFolder()
```


Returns an empty string since this strategy does not use an images folder.


**Returns:**
java.lang.String
### getImageStream(ImageExportContext context) {#getImageStream-com.groupdocs.markdown.ImageExportContext-}
```
public OutputStream getImageStream(ImageExportContext context)
```


Returns null to indicate that the image should be embedded as Base64.


**Parameters:**
| Parameter | Type | Description |
| --- | --- | --- |
| context | [ImageExportContext](../../com.groupdocs.markdown/imageexportcontext) |  |

**Returns:**
java.io.OutputStream
