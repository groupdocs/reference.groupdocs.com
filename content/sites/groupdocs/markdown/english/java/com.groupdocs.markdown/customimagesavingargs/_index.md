---
title: CustomImageSavingArgs
second_title: GroupDocs.Markdown for Java API Reference
description: Provides information and controls for saving a single image during document-to-Markdown conversion.
type: docs
weight: 10
url: /java/com.groupdocs.markdown/customimagesavingargs/
---
**Inheritance:**
java.lang.Object
```
public class CustomImageSavingArgs
```

Provides information and controls for saving a single image during document-to-Markdown conversion.


An instance of this class is passed to the callback registered with 
CustomImagesStrategy

for each image found in the source document.


Use #setOutputImageFileName(String).setOutputImageFileName(String) to change the file name the image is saved under,
or #setOutputStream(OutputStream).setOutputStream(OutputStream) to redirect the image data to a custom stream.
If neither method is called, the library uses the defaults provided by

imageFileName
 and 
outputDirectory
.

**Example:**

````

 CustomImagesStrategy strategy = new CustomImagesStrategy(args -> {
     args.setOutputImageFileName("thumb-" + args.getImageFileName());
 });

 ConvertOptions options = new ConvertOptions();
 options.setImageExportStrategy(strategy);
 
````


## Constructors

| Constructor | Description |
| --- | --- |
| [CustomImageSavingArgs(String suggestedFileName, String shapeType, String outputDirectory)](#CustomImageSavingArgs-java.lang.String-java.lang.String-java.lang.String-) |  |
## Methods

| Method | Description |
| --- | --- |
| [getImageFileName()](#getImageFileName--) | Gets the default file name (without path) suggested by the library for this image.
 |
| [getShapeType()](#getShapeType--) | Gets the type of the shape that contains the image in the source document (for example, "Picture" or "Shape").
 |
| [getOutputDirectory()](#getOutputDirectory--) | Gets the output directory where images are being saved.
 |
| [getImageFileNameOutput()](#getImageFileNameOutput--) | Gets the overridden file name, or  null  if no override was specified.
 |
| [getOutputStream()](#getOutputStream--) | Gets the custom output stream, or  null  if not specified.
 |
| [getReplacementImageStream()](#getReplacementImageStream--) | Gets the replacement image stream, or  null  if not specified.
 |
| [setOutputImageFileName(String fileName)](#setOutputImageFileName-java.lang.String-) | Overrides the default file name for this image.
 |
| [setOutputStream(OutputStream stream)](#setOutputStream-java.io.OutputStream-) | Redirects the image data to a custom writable stream instead of file output.
 |
| [setReplacementImage(InputStream imageStream)](#setReplacementImage-java.io.InputStream-) | Provides a replacement image instead of the original.
 |
### CustomImageSavingArgs(String suggestedFileName, String shapeType, String outputDirectory) {#CustomImageSavingArgs-java.lang.String-java.lang.String-java.lang.String-}
```
public CustomImageSavingArgs(String suggestedFileName, String shapeType, String outputDirectory)
```


**Parameters:**
| Parameter | Type | Description |
| --- | --- | --- |
| suggestedFileName | java.lang.String |  |
| shapeType | java.lang.String |  |
| outputDirectory | java.lang.String |  |

### getImageFileName() {#getImageFileName--}
```
public String getImageFileName()
```


Gets the default file name (without path) suggested by the library for this image.


**Returns:**
java.lang.String
### getShapeType() {#getShapeType--}
```
public String getShapeType()
```


Gets the type of the shape that contains the image in the source document (for example, "Picture" or "Shape").


**Returns:**
java.lang.String
### getOutputDirectory() {#getOutputDirectory--}
```
public String getOutputDirectory()
```


Gets the output directory where images are being saved.


**Returns:**
java.lang.String
### getImageFileNameOutput() {#getImageFileNameOutput--}
```
public String getImageFileNameOutput()
```


Gets the overridden file name, or  null  if no override was specified.


**Returns:**
java.lang.String
### getOutputStream() {#getOutputStream--}
```
public OutputStream getOutputStream()
```


Gets the custom output stream, or  null  if not specified.


**Returns:**
java.io.OutputStream
### getReplacementImageStream() {#getReplacementImageStream--}
```
public InputStream getReplacementImageStream()
```


Gets the replacement image stream, or  null  if not specified.


**Returns:**
java.io.InputStream
### setOutputImageFileName(String fileName) {#setOutputImageFileName-java.lang.String-}
```
public void setOutputImageFileName(String fileName)
```


Overrides the default file name for this image.


**Parameters:**
| Parameter | Type | Description |
| --- | --- | --- |
| fileName | java.lang.String | new file name (without path)
 |

### setOutputStream(OutputStream stream) {#setOutputStream-java.io.OutputStream-}
```
public void setOutputStream(OutputStream stream)
```


Redirects the image data to a custom writable stream instead of file output.


**Parameters:**
| Parameter | Type | Description |
| --- | --- | --- |
| stream | java.io.OutputStream | writable stream
 |

### setReplacementImage(InputStream imageStream) {#setReplacementImage-java.io.InputStream-}
```
public void setReplacementImage(InputStream imageStream)
```


Provides a replacement image instead of the original.


**Parameters:**
| Parameter | Type | Description |
| --- | --- | --- |
| imageStream | java.io.InputStream | readable stream with image data
 |

