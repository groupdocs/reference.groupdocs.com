---
title: LoadOptions
second_title: GroupDocs.Markdown for Java API Reference
description: Specifies additional options for loading a document such as an explicit file format or a password for encrypted files.
type: docs
weight: 25
url: /java/com.groupdocs.markdown/loadoptions/
---
**Inheritance:**
java.lang.Object
```
public class LoadOptions
```

Specifies additional options for loading a document, such as an explicit file format or a password for encrypted files.

## Constructors

| Constructor | Description |
| --- | --- |
| [LoadOptions()](#LoadOptions--) | Creates load options with automatic format detection.
 |
| [LoadOptions(FileFormat fileFormat)](#LoadOptions-com.groupdocs.markdown.FileFormat-) | Creates load options with explicit file format.
 |
## Methods

| Method | Description |
| --- | --- |
| [getPassword()](#getPassword--) |  |
| [setPassword(String password)](#setPassword-java.lang.String-) |  |
| [getFileFormat()](#getFileFormat--) |  |
| [getExtension()](#getExtension--) |  |
| [getMimeType()](#getMimeType--) |  |
| [getFileFormatFromExtension(String extension)](#getFileFormatFromExtension-java.lang.String-) |  |
### LoadOptions() {#LoadOptions--}
```
public LoadOptions()
```


Creates load options with automatic format detection.


### LoadOptions(FileFormat fileFormat) {#LoadOptions-com.groupdocs.markdown.FileFormat-}
```
public LoadOptions(FileFormat fileFormat)
```


Creates load options with explicit file format.


**Parameters:**
| Parameter | Type | Description |
| --- | --- | --- |
| fileFormat | [FileFormat](../../com.groupdocs.markdown/fileformat) | document file format
 |

### getPassword() {#getPassword--}
```
public String getPassword()
```




**Returns:**
java.lang.String
### setPassword(String password) {#setPassword-java.lang.String-}
```
public void setPassword(String password)
```




**Parameters:**
| Parameter | Type | Description |
| --- | --- | --- |
| password | java.lang.String |  |

### getFileFormat() {#getFileFormat--}
```
public FileFormat getFileFormat()
```




**Returns:**
[FileFormat](../../com.groupdocs.markdown/fileformat)
### getExtension() {#getExtension--}
```
public String getExtension()
```




**Returns:**
java.lang.String
### getMimeType() {#getMimeType--}
```
public String getMimeType()
```




**Returns:**
java.lang.String
### getFileFormatFromExtension(String extension) {#getFileFormatFromExtension-java.lang.String-}
```
public static FileFormat getFileFormatFromExtension(String extension)
```




**Parameters:**
| Parameter | Type | Description |
| --- | --- | --- |
| extension | java.lang.String |  |

**Returns:**
[FileFormat](../../com.groupdocs.markdown/fileformat)
