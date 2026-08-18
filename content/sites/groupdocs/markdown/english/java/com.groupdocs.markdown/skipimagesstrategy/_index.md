---
title: SkipImagesStrategy
second_title: GroupDocs.Markdown for Java API Reference
description: Implements an image export strategy that skips saving images during document conversion.
type: docs
weight: 29
url: /java/com.groupdocs.markdown/skipimagesstrategy/
---
**Inheritance:**
java.lang.Object

**All Implemented Interfaces:**
[com.groupdocs.markdown.IImageExportStrategy](../../com.groupdocs.markdown/iimageexportstrategy)
```
public class SkipImagesStrategy implements IImageExportStrategy
```

Implements an image export strategy that skips saving images during document conversion.


This strategy is useful when you want to convert a document to Markdown without saving the actual image files.
When this strategy is used, the output Markdown will still contain image references
(e.g., 
![](../img-001.png)
), but the actual image files will not be saved to disk.

**Example:**

````

 ConvertOptions options = new ConvertOptions();
 options.setImageExportStrategy(new SkipImagesStrategy());

 String markdown = MarkdownConverter.toMarkdown("document.docx", options);
 // Image references remain in the markdown but no files are written
 
````


## Constructors

| Constructor | Description |
| --- | --- |
| [SkipImagesStrategy()](#SkipImagesStrategy--) |  |
## Methods

| Method | Description |
| --- | --- |
| [getImagesFolder()](#getImagesFolder--) | Returns an empty string since this strategy does not use an images folder.
 |
| [getImageStream(ImageExportContext context)](#getImageStream-com.groupdocs.markdown.ImageExportContext-) | Returns null to indicate that the image should be skipped.
 |
### SkipImagesStrategy() {#SkipImagesStrategy--}
```
public SkipImagesStrategy()
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


Returns null to indicate that the image should be skipped.


**Parameters:**
| Parameter | Type | Description |
| --- | --- | --- |
| context | [ImageExportContext](../../com.groupdocs.markdown/imageexportcontext) |  |

**Returns:**
java.io.OutputStream
