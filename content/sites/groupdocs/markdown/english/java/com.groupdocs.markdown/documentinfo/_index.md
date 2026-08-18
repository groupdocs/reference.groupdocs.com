---
title: DocumentInfo
second_title: GroupDocs.Markdown for Java API Reference
description: Provides read-only metadata about a loaded document such as format page count title author and encryption status.
type: docs
weight: 16
url: /java/com.groupdocs.markdown/documentinfo/
---
**Inheritance:**
java.lang.Object
```
public class DocumentInfo
```

Provides read-only metadata about a loaded document, such as format, page count, title, author, and encryption status.

## Constructors

| Constructor | Description |
| --- | --- |
| [DocumentInfo(FileFormat fileFormat, int pageCount, String title, String author, boolean encrypted)](#DocumentInfo-com.groupdocs.markdown.FileFormat-int-java.lang.String-java.lang.String-boolean-) |  |
## Methods

| Method | Description |
| --- | --- |
| [getFileFormat()](#getFileFormat--) |  |
| [getPageCount()](#getPageCount--) |  |
| [getTitle()](#getTitle--) |  |
| [getAuthor()](#getAuthor--) |  |
| [isEncrypted()](#isEncrypted--) |  |
### DocumentInfo(FileFormat fileFormat, int pageCount, String title, String author, boolean encrypted) {#DocumentInfo-com.groupdocs.markdown.FileFormat-int-java.lang.String-java.lang.String-boolean-}
```
public DocumentInfo(FileFormat fileFormat, int pageCount, String title, String author, boolean encrypted)
```


**Parameters:**
| Parameter | Type | Description |
| --- | --- | --- |
| fileFormat | [FileFormat](../../com.groupdocs.markdown/fileformat) |  |
| pageCount | int |  |
| title | java.lang.String |  |
| author | java.lang.String |  |
| encrypted | boolean |  |

### getFileFormat() {#getFileFormat--}
```
public FileFormat getFileFormat()
```




**Returns:**
[FileFormat](../../com.groupdocs.markdown/fileformat)
### getPageCount() {#getPageCount--}
```
public int getPageCount()
```




**Returns:**
int
### getTitle() {#getTitle--}
```
public String getTitle()
```




**Returns:**
java.lang.String
### getAuthor() {#getAuthor--}
```
public String getAuthor()
```




**Returns:**
java.lang.String
### isEncrypted() {#isEncrypted--}
```
public boolean isEncrypted()
```




**Returns:**
boolean
