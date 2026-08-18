---
title: ExportImagesToFileSystemStrategy
second_title: GroupDocs.Markdown for Java API Reference
description: Saves images to a folder on disk during conversion.
type: docs
weight: 19
url: /java/com.groupdocs.markdown/exportimagestofilesystemstrategy/
---
**Inheritance:**
java.lang.Object

**All Implemented Interfaces:**
[com.groupdocs.markdown.IImageExportStrategy](../../com.groupdocs.markdown/iimageexportstrategy)
```
public class ExportImagesToFileSystemStrategy implements IImageExportStrategy
```

Saves images to a folder on disk during conversion.


By default, the Markdown output references images using the full 
imagesFolder
 path.
Set 
imagesRelativePath
 to control the path that appears in the Markdown image links
\\u2014 typically a path relative to the output .md file.

**Example:**

````

 ExportImagesToFileSystemStrategy strategy =
     new ExportImagesToFileSystemStrategy("c:/output/images");

 strategy.setImagesRelativePath("images");

 ConvertOptions options = new ConvertOptions();
 options.setImageExportStrategy(strategy);

 MarkdownConverter.toFile("document.docx", "c:/output/doc.md", options);
 // Markdown: ![](../images/img-001.png)
 // File:     c:/output/images/img-001.png
 
````


## Constructors

| Constructor | Description |
| --- | --- |
| [ExportImagesToFileSystemStrategy(String imagesFolder)](#ExportImagesToFileSystemStrategy-java.lang.String-) | Initializes a new instance.
 |
## Methods

| Method | Description |
| --- | --- |
| [getImagesFolder()](#getImagesFolder--) | Gets the physical folder where images will be saved on disk.
 |
| [getImagesRelativePath()](#getImagesRelativePath--) | Gets or sets the path used in Markdown image references.
 |
| [setImagesRelativePath(String imagesRelativePath)](#setImagesRelativePath-java.lang.String-) |  |
| [getImageStream(ImageExportContext context)](#getImageStream-com.groupdocs.markdown.ImageExportContext-) | Gets a stream for writing the exported image to the file system.
 |
### ExportImagesToFileSystemStrategy(String imagesFolder) {#ExportImagesToFileSystemStrategy-java.lang.String-}
```
public ExportImagesToFileSystemStrategy(String imagesFolder)
```


Initializes a new instance.


**Parameters:**
| Parameter | Type | Description |
| --- | --- | --- |
| imagesFolder | java.lang.String | physical folder where images will be saved
 |

### getImagesFolder() {#getImagesFolder--}
```
public String getImagesFolder()
```


Gets the physical folder where images will be saved on disk.


**Returns:**
java.lang.String
### getImagesRelativePath() {#getImagesRelativePath--}
```
public String getImagesRelativePath()
```


Gets or sets the path used in Markdown image references.


**Returns:**
java.lang.String
### setImagesRelativePath(String imagesRelativePath) {#setImagesRelativePath-java.lang.String-}
```
public void setImagesRelativePath(String imagesRelativePath)
```




**Parameters:**
| Parameter | Type | Description |
| --- | --- | --- |
| imagesRelativePath | java.lang.String |  |

### getImageStream(ImageExportContext context) {#getImageStream-com.groupdocs.markdown.ImageExportContext-}
```
public OutputStream getImageStream(ImageExportContext context)
```


Gets a stream for writing the exported image to the file system.


**Parameters:**
| Parameter | Type | Description |
| --- | --- | --- |
| context | [ImageExportContext](../../com.groupdocs.markdown/imageexportcontext) |  |

**Returns:**
java.io.OutputStream
