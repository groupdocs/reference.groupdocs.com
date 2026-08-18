---
title: CustomImagesStrategy
second_title: GroupDocs.Markdown for Java API Reference
description: Implements an image export strategy that gives you full control over how images are saved during conversion.
type: docs
weight: 11
url: /java/com.groupdocs.markdown/customimagesstrategy/
---
**Inheritance:**
java.lang.Object

**All Implemented Interfaces:**
[com.groupdocs.markdown.IImageExportStrategy](../../com.groupdocs.markdown/iimageexportstrategy)
```
public class CustomImagesStrategy implements IImageExportStrategy
```

Implements an image export strategy that gives you full control over how images are saved during conversion.


Supply an [IImageSavingHandler](../../com.groupdocs.markdown.imageexport/iimagesavinghandler) implementation to rename images, redirect them to a
custom stream, or apply any other custom logic when each image is encountered.

**Example:**

````

 IImageSavingHandler handler = new RenameHandler();

 ConvertOptions options = new ConvertOptions();
 options.setImageExportStrategy(new CustomImagesStrategy("images", handler));

 String markdown = MarkdownConverter.toMarkdown("document.docx", options);
 
````


## Constructors

| Constructor | Description |
| --- | --- |
| [CustomImagesStrategy(String imagesFolder, IImageSavingHandler handler)](#CustomImagesStrategy-java.lang.String-com.groupdocs.markdown.imageexport.IImageSavingHandler-) | Initializes a new instance of the  CustomImagesStrategy  class.
 |
## Methods

| Method | Description |
| --- | --- |
| [getImagesFolder()](#getImagesFolder--) | Gets the physical folder where images will be saved on disk.
 |
| [getImagesRelativePath()](#getImagesRelativePath--) | Gets or sets the path used in the Markdown image references.
 |
| [setImagesRelativePath(String imagesRelativePath)](#setImagesRelativePath-java.lang.String-) |  |
| [getImageStream(ImageExportContext context)](#getImageStream-com.groupdocs.markdown.ImageExportContext-) | Gets a stream for writing the exported image to the file system.
 |
| [getCustomHandler()](#getCustomHandler--) |  |
### CustomImagesStrategy(String imagesFolder, IImageSavingHandler handler) {#CustomImagesStrategy-java.lang.String-com.groupdocs.markdown.imageexport.IImageSavingHandler-}
```
public CustomImagesStrategy(String imagesFolder, IImageSavingHandler handler)
```


Initializes a new instance of the  CustomImagesStrategy  class.


**Parameters:**
| Parameter | Type | Description |
| --- | --- | --- |
| imagesFolder | java.lang.String | the folder where images will be exported
 |
| handler | [IImageSavingHandler](../../com.groupdocs.markdown.imageexport/iimagesavinghandler) | the handler that is called for each image during conversion
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


Gets or sets the path used in the Markdown image references. When null or empty, the full imagesFolder path is used.


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
### getCustomHandler() {#getCustomHandler--}
```
public IImageSavingHandler getCustomHandler()
```




**Returns:**
[IImageSavingHandler](../../com.groupdocs.markdown.imageexport/iimagesavinghandler)
