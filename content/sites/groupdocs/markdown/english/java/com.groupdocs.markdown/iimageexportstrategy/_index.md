---
title: IImageExportStrategy
second_title: GroupDocs.Markdown for Java API Reference
description: Defines a strategy for handling image export during document-to-Markdown conversion.
type: docs
weight: 32
url: /java/com.groupdocs.markdown/iimageexportstrategy/
---```
public interface IImageExportStrategy
```

Defines a strategy for handling image export during document-to-Markdown conversion. Implement this interface to control where and how images extracted from the source document are stored.

The library ships with several built-in strategies:

* [ExportImagesAsBase64Strategy](../../com.groupdocs.markdown/exportimagesasbase64strategy) \\u2014 embeds images inline as Base64, the default.
* [ExportImagesToFileSystemStrategy](../../com.groupdocs.markdown/exportimagestofilesystemstrategy) \\u2014 writes images to a folder on disk.
* [SkipImagesStrategy](../../com.groupdocs.markdown/skipimagesstrategy) \\u2014 omits images entirely.
* [CustomImagesStrategy](../../com.groupdocs.markdown/customimagesstrategy) \\u2014 delegates to a callback you supply.

Implement this interface directly when none of the built-in strategies meet your needs.

**Example:**

````

 public class CloudImageExportStrategy implements IImageExportStrategy {

     @Override
     public String getImagesFolder() {
         return "cloud-images";
     }

     @Override
     public OutputStream getImageStream(ImageExportContext context) {
         context.setImageFileName("doc-" + context.getImageFileName());

         return new ByteArrayOutputStream(); // replace with your cloud upload stream
     }
 }
 
````


## Methods

| Method | Description |
| --- | --- |
| [getImagesFolder()](#getImagesFolder--) | Gets the folder path where exported images will be stored.
 |
| [getImageStream(ImageExportContext context)](#getImageStream-com.groupdocs.markdown.ImageExportContext-) | Returns a writable stream for the image described by  context .
 |
### getImagesFolder() {#getImagesFolder--}
```
public abstract String getImagesFolder()
```


Gets the folder path where exported images will be stored.


**Returns:**
java.lang.String - a relative or absolute folder path. This value is used to construct image URIs in the Markdown output.

### getImageStream(ImageExportContext context) {#getImageStream-com.groupdocs.markdown.ImageExportContext-}
```
public abstract OutputStream getImageStream(ImageExportContext context)
```


Returns a writable stream for the image described by  context . The library writes the image bytes to this stream during conversion.


**Parameters:**
| Parameter | Type | Description |
| --- | --- | --- |
| context | [ImageExportContext](../../com.groupdocs.markdown/imageexportcontext) | The image export context containing the default image file name and other metadata. You may modify  imageFileName  before returning the stream to change the file name that appears in the Markdown output.
 |

**Returns:**
java.io.OutputStream - a writable stream where the image data will be written, or  null  to use the default behavior

