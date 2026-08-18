---
title: MarkdownConverter
second_title: GroupDocs.Markdown for Java API Reference
description: Converts documents from Word, Excel, PDF, and other formats to Markdown. Provides both static one-liner methods and an instance-based API with full control over conversion options.
type: docs
weight: 26
url: /java/com.groupdocs.markdown/markdownconverter/
---
**Inheritance:**
java.lang.Object

**All Implemented Interfaces:**
java.lang.AutoCloseable
```
public class MarkdownConverter implements AutoCloseable
```

Converts documents from Word, Excel, PDF, and other formats to Markdown. Provides both static one-liner methods and an instance-based API with full control over conversion options.

## Constructors

| Constructor | Description |
| --- | --- |
| [MarkdownConverter(String sourcePath)](#MarkdownConverter-java.lang.String-) |  |
| [MarkdownConverter(InputStream sourceStream)](#MarkdownConverter-java.io.InputStream-) |  |
| [MarkdownConverter(String sourcePath, LoadOptions sourceLoadOptions)](#MarkdownConverter-java.lang.String-com.groupdocs.markdown.LoadOptions-) |  |
| [MarkdownConverter(InputStream sourceStream, LoadOptions sourceLoadOptions)](#MarkdownConverter-java.io.InputStream-com.groupdocs.markdown.LoadOptions-) |  |
## Methods

| Method | Description |
| --- | --- |
| [convert()](#convert--) |  |
| [convert(OutputStream outputStream)](#convert-java.io.OutputStream-) |  |
| [convert(String outputFilePath)](#convert-java.lang.String-) |  |
| [convert(DocumentConvertOptions convertOptions)](#convert-com.groupdocs.markdown.DocumentConvertOptions-) |  |
| [convert(OutputStream outputStream, DocumentConvertOptions convertOptions)](#convert-java.io.OutputStream-com.groupdocs.markdown.DocumentConvertOptions-) |  |
| [convert(String outputFilePath, DocumentConvertOptions convertOptions)](#convert-java.lang.String-com.groupdocs.markdown.DocumentConvertOptions-) |  |
| [getDocumentInfo()](#getDocumentInfo--) |  |
| [toMarkdown(String sourcePath)](#toMarkdown-java.lang.String-) |  |
| [toMarkdown(String sourcePath, LoadOptions loadOptions)](#toMarkdown-java.lang.String-com.groupdocs.markdown.LoadOptions-) |  |
| [toMarkdown(String sourcePath, DocumentConvertOptions convertOptions)](#toMarkdown-java.lang.String-com.groupdocs.markdown.DocumentConvertOptions-) |  |
| [toMarkdown(String sourcePath, LoadOptions loadOptions, DocumentConvertOptions convertOptions)](#toMarkdown-java.lang.String-com.groupdocs.markdown.LoadOptions-com.groupdocs.markdown.DocumentConvertOptions-) |  |
| [toFile(String sourcePath, String outputPath)](#toFile-java.lang.String-java.lang.String-) |  |
| [toFile(String sourcePath, String outputPath, DocumentConvertOptions convertOptions)](#toFile-java.lang.String-java.lang.String-com.groupdocs.markdown.DocumentConvertOptions-) |  |
| [toFile(String sourcePath, String outputPath, LoadOptions loadOptions, DocumentConvertOptions convertOptions)](#toFile-java.lang.String-java.lang.String-com.groupdocs.markdown.LoadOptions-com.groupdocs.markdown.DocumentConvertOptions-) |  |
| [getInfo(String sourcePath)](#getInfo-java.lang.String-) |  |
| [getInfo(String sourcePath, LoadOptions loadOptions)](#getInfo-java.lang.String-com.groupdocs.markdown.LoadOptions-) |  |
| [getSupportedFormats()](#getSupportedFormats--) |  |
| [fromMarkdown(String markdownPath, String outputPath)](#fromMarkdown-java.lang.String-java.lang.String-) |  |
| [fromMarkdown(String markdownPath, String outputPath, ExportOptions options)](#fromMarkdown-java.lang.String-java.lang.String-com.groupdocs.markdown.ExportOptions-) |  |
| [fromMarkdownString(String markdownContent, String outputPath)](#fromMarkdownString-java.lang.String-java.lang.String-) |  |
| [fromMarkdownString(String markdownContent, String outputPath, ExportOptions options)](#fromMarkdownString-java.lang.String-java.lang.String-com.groupdocs.markdown.ExportOptions-) |  |
| [fromMarkdownString(String markdownContent, OutputStream outputStream, ExportOptions options)](#fromMarkdownString-java.lang.String-java.io.OutputStream-com.groupdocs.markdown.ExportOptions-) |  |
| [close()](#close--) |  |
| [readAllBytes(InputStream inputStream)](#readAllBytes-java.io.InputStream-) |  |
### MarkdownConverter(String sourcePath) {#MarkdownConverter-java.lang.String-}
```
public MarkdownConverter(String sourcePath)
```


**Parameters:**
| Parameter | Type | Description |
| --- | --- | --- |
| sourcePath | java.lang.String |  |

### MarkdownConverter(InputStream sourceStream) {#MarkdownConverter-java.io.InputStream-}
```
public MarkdownConverter(InputStream sourceStream)
```


**Parameters:**
| Parameter | Type | Description |
| --- | --- | --- |
| sourceStream | java.io.InputStream |  |

### MarkdownConverter(String sourcePath, LoadOptions sourceLoadOptions) {#MarkdownConverter-java.lang.String-com.groupdocs.markdown.LoadOptions-}
```
public MarkdownConverter(String sourcePath, LoadOptions sourceLoadOptions)
```


**Parameters:**
| Parameter | Type | Description |
| --- | --- | --- |
| sourcePath | java.lang.String |  |
| sourceLoadOptions | [LoadOptions](../../com.groupdocs.markdown/loadoptions) |  |

### MarkdownConverter(InputStream sourceStream, LoadOptions sourceLoadOptions) {#MarkdownConverter-java.io.InputStream-com.groupdocs.markdown.LoadOptions-}
```
public MarkdownConverter(InputStream sourceStream, LoadOptions sourceLoadOptions)
```


**Parameters:**
| Parameter | Type | Description |
| --- | --- | --- |
| sourceStream | java.io.InputStream |  |
| sourceLoadOptions | [LoadOptions](../../com.groupdocs.markdown/loadoptions) |  |

### convert() {#convert--}
```
public DocumentConvertResult convert()
```




**Returns:**
[DocumentConvertResult](../../com.groupdocs.markdown/documentconvertresult)
### convert(OutputStream outputStream) {#convert-java.io.OutputStream-}
```
public DocumentConvertResult convert(OutputStream outputStream)
```




**Parameters:**
| Parameter | Type | Description |
| --- | --- | --- |
| outputStream | java.io.OutputStream |  |

**Returns:**
[DocumentConvertResult](../../com.groupdocs.markdown/documentconvertresult)
### convert(String outputFilePath) {#convert-java.lang.String-}
```
public DocumentConvertResult convert(String outputFilePath)
```




**Parameters:**
| Parameter | Type | Description |
| --- | --- | --- |
| outputFilePath | java.lang.String |  |

**Returns:**
[DocumentConvertResult](../../com.groupdocs.markdown/documentconvertresult)
### convert(DocumentConvertOptions convertOptions) {#convert-com.groupdocs.markdown.DocumentConvertOptions-}
```
public DocumentConvertResult convert(DocumentConvertOptions convertOptions)
```




**Parameters:**
| Parameter | Type | Description |
| --- | --- | --- |
| convertOptions | [DocumentConvertOptions](../../com.groupdocs.markdown/documentconvertoptions) |  |

**Returns:**
[DocumentConvertResult](../../com.groupdocs.markdown/documentconvertresult)
### convert(OutputStream outputStream, DocumentConvertOptions convertOptions) {#convert-java.io.OutputStream-com.groupdocs.markdown.DocumentConvertOptions-}
```
public DocumentConvertResult convert(OutputStream outputStream, DocumentConvertOptions convertOptions)
```




**Parameters:**
| Parameter | Type | Description |
| --- | --- | --- |
| outputStream | java.io.OutputStream |  |
| convertOptions | [DocumentConvertOptions](../../com.groupdocs.markdown/documentconvertoptions) |  |

**Returns:**
[DocumentConvertResult](../../com.groupdocs.markdown/documentconvertresult)
### convert(String outputFilePath, DocumentConvertOptions convertOptions) {#convert-java.lang.String-com.groupdocs.markdown.DocumentConvertOptions-}
```
public DocumentConvertResult convert(String outputFilePath, DocumentConvertOptions convertOptions)
```




**Parameters:**
| Parameter | Type | Description |
| --- | --- | --- |
| outputFilePath | java.lang.String |  |
| convertOptions | [DocumentConvertOptions](../../com.groupdocs.markdown/documentconvertoptions) |  |

**Returns:**
[DocumentConvertResult](../../com.groupdocs.markdown/documentconvertresult)
### getDocumentInfo() {#getDocumentInfo--}
```
public DocumentInfo getDocumentInfo()
```




**Returns:**
[DocumentInfo](../../com.groupdocs.markdown/documentinfo)
### toMarkdown(String sourcePath) {#toMarkdown-java.lang.String-}
```
public static String toMarkdown(String sourcePath)
```




**Parameters:**
| Parameter | Type | Description |
| --- | --- | --- |
| sourcePath | java.lang.String |  |

**Returns:**
java.lang.String
### toMarkdown(String sourcePath, LoadOptions loadOptions) {#toMarkdown-java.lang.String-com.groupdocs.markdown.LoadOptions-}
```
public static String toMarkdown(String sourcePath, LoadOptions loadOptions)
```




**Parameters:**
| Parameter | Type | Description |
| --- | --- | --- |
| sourcePath | java.lang.String |  |
| loadOptions | [LoadOptions](../../com.groupdocs.markdown/loadoptions) |  |

**Returns:**
java.lang.String
### toMarkdown(String sourcePath, DocumentConvertOptions convertOptions) {#toMarkdown-java.lang.String-com.groupdocs.markdown.DocumentConvertOptions-}
```
public static String toMarkdown(String sourcePath, DocumentConvertOptions convertOptions)
```




**Parameters:**
| Parameter | Type | Description |
| --- | --- | --- |
| sourcePath | java.lang.String |  |
| convertOptions | [DocumentConvertOptions](../../com.groupdocs.markdown/documentconvertoptions) |  |

**Returns:**
java.lang.String
### toMarkdown(String sourcePath, LoadOptions loadOptions, DocumentConvertOptions convertOptions) {#toMarkdown-java.lang.String-com.groupdocs.markdown.LoadOptions-com.groupdocs.markdown.DocumentConvertOptions-}
```
public static String toMarkdown(String sourcePath, LoadOptions loadOptions, DocumentConvertOptions convertOptions)
```




**Parameters:**
| Parameter | Type | Description |
| --- | --- | --- |
| sourcePath | java.lang.String |  |
| loadOptions | [LoadOptions](../../com.groupdocs.markdown/loadoptions) |  |
| convertOptions | [DocumentConvertOptions](../../com.groupdocs.markdown/documentconvertoptions) |  |

**Returns:**
java.lang.String
### toFile(String sourcePath, String outputPath) {#toFile-java.lang.String-java.lang.String-}
```
public static void toFile(String sourcePath, String outputPath)
```




**Parameters:**
| Parameter | Type | Description |
| --- | --- | --- |
| sourcePath | java.lang.String |  |
| outputPath | java.lang.String |  |

### toFile(String sourcePath, String outputPath, DocumentConvertOptions convertOptions) {#toFile-java.lang.String-java.lang.String-com.groupdocs.markdown.DocumentConvertOptions-}
```
public static void toFile(String sourcePath, String outputPath, DocumentConvertOptions convertOptions)
```




**Parameters:**
| Parameter | Type | Description |
| --- | --- | --- |
| sourcePath | java.lang.String |  |
| outputPath | java.lang.String |  |
| convertOptions | [DocumentConvertOptions](../../com.groupdocs.markdown/documentconvertoptions) |  |

### toFile(String sourcePath, String outputPath, LoadOptions loadOptions, DocumentConvertOptions convertOptions) {#toFile-java.lang.String-java.lang.String-com.groupdocs.markdown.LoadOptions-com.groupdocs.markdown.DocumentConvertOptions-}
```
public static void toFile(String sourcePath, String outputPath, LoadOptions loadOptions, DocumentConvertOptions convertOptions)
```




**Parameters:**
| Parameter | Type | Description |
| --- | --- | --- |
| sourcePath | java.lang.String |  |
| outputPath | java.lang.String |  |
| loadOptions | [LoadOptions](../../com.groupdocs.markdown/loadoptions) |  |
| convertOptions | [DocumentConvertOptions](../../com.groupdocs.markdown/documentconvertoptions) |  |

### getInfo(String sourcePath) {#getInfo-java.lang.String-}
```
public static DocumentInfo getInfo(String sourcePath)
```




**Parameters:**
| Parameter | Type | Description |
| --- | --- | --- |
| sourcePath | java.lang.String |  |

**Returns:**
[DocumentInfo](../../com.groupdocs.markdown/documentinfo)
### getInfo(String sourcePath, LoadOptions loadOptions) {#getInfo-java.lang.String-com.groupdocs.markdown.LoadOptions-}
```
public static DocumentInfo getInfo(String sourcePath, LoadOptions loadOptions)
```




**Parameters:**
| Parameter | Type | Description |
| --- | --- | --- |
| sourcePath | java.lang.String |  |
| loadOptions | [LoadOptions](../../com.groupdocs.markdown/loadoptions) |  |

**Returns:**
[DocumentInfo](../../com.groupdocs.markdown/documentinfo)
### getSupportedFormats() {#getSupportedFormats--}
```
public static List<FileFormat> getSupportedFormats()
```




**Returns:**
java.util.List<com.groupdocs.markdown.FileFormat>
### fromMarkdown(String markdownPath, String outputPath) {#fromMarkdown-java.lang.String-java.lang.String-}
```
public static void fromMarkdown(String markdownPath, String outputPath)
```




**Parameters:**
| Parameter | Type | Description |
| --- | --- | --- |
| markdownPath | java.lang.String |  |
| outputPath | java.lang.String |  |

### fromMarkdown(String markdownPath, String outputPath, ExportOptions options) {#fromMarkdown-java.lang.String-java.lang.String-com.groupdocs.markdown.ExportOptions-}
```
public static void fromMarkdown(String markdownPath, String outputPath, ExportOptions options)
```




**Parameters:**
| Parameter | Type | Description |
| --- | --- | --- |
| markdownPath | java.lang.String |  |
| outputPath | java.lang.String |  |
| options | [ExportOptions](../../com.groupdocs.markdown/exportoptions) |  |

### fromMarkdownString(String markdownContent, String outputPath) {#fromMarkdownString-java.lang.String-java.lang.String-}
```
public static void fromMarkdownString(String markdownContent, String outputPath)
```




**Parameters:**
| Parameter | Type | Description |
| --- | --- | --- |
| markdownContent | java.lang.String |  |
| outputPath | java.lang.String |  |

### fromMarkdownString(String markdownContent, String outputPath, ExportOptions options) {#fromMarkdownString-java.lang.String-java.lang.String-com.groupdocs.markdown.ExportOptions-}
```
public static void fromMarkdownString(String markdownContent, String outputPath, ExportOptions options)
```




**Parameters:**
| Parameter | Type | Description |
| --- | --- | --- |
| markdownContent | java.lang.String |  |
| outputPath | java.lang.String |  |
| options | [ExportOptions](../../com.groupdocs.markdown/exportoptions) |  |

### fromMarkdownString(String markdownContent, OutputStream outputStream, ExportOptions options) {#fromMarkdownString-java.lang.String-java.io.OutputStream-com.groupdocs.markdown.ExportOptions-}
```
public static void fromMarkdownString(String markdownContent, OutputStream outputStream, ExportOptions options)
```




**Parameters:**
| Parameter | Type | Description |
| --- | --- | --- |
| markdownContent | java.lang.String |  |
| outputStream | java.io.OutputStream |  |
| options | [ExportOptions](../../com.groupdocs.markdown/exportoptions) |  |

### close() {#close--}
```
public void close()
```




### readAllBytes(InputStream inputStream) {#readAllBytes-java.io.InputStream-}
```
public static byte[] readAllBytes(InputStream inputStream)
```




**Parameters:**
| Parameter | Type | Description |
| --- | --- | --- |
| inputStream | java.io.InputStream |  |

**Returns:**
byte[]
