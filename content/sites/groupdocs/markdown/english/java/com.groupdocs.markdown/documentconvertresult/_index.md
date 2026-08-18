---
title: DocumentConvertResult
second_title: GroupDocs.Markdown for Java API Reference
description: Contains the output of a successful document-to-Markdown conversion.
type: docs
weight: 15
url: /java/com.groupdocs.markdown/documentconvertresult/
---
**Inheritance:**
java.lang.Object
```
public class DocumentConvertResult
```

Contains the output of a successful document-to-Markdown conversion.

## Methods

| Method | Description |
| --- | --- |
| [isSuccess()](#isSuccess--) |  |
| [getErrorMessage()](#getErrorMessage--) |  |
| [getContent()](#getContent--) |  |
| [getException()](#getException--) |  |
| [getWarnings()](#getWarnings--) |  |
| [success()](#success--) | Creates successful result without content.
 |
| [success(String content)](#success-java.lang.String-) | Creates successful result with content.
 |
| [failure(String errorMessage, Throwable exception)](#failure-java.lang.String-java.lang.Throwable-) | Creates failed result.
 |
### isSuccess() {#isSuccess--}
```
public boolean isSuccess()
```




**Returns:**
boolean
### getErrorMessage() {#getErrorMessage--}
```
public String getErrorMessage()
```




**Returns:**
java.lang.String
### getContent() {#getContent--}
```
public String getContent()
```




**Returns:**
java.lang.String
### getException() {#getException--}
```
public Throwable getException()
```




**Returns:**
java.lang.Throwable
### getWarnings() {#getWarnings--}
```
public List<String> getWarnings()
```




**Returns:**
java.util.List<java.lang.String>
### success() {#success--}
```
public static DocumentConvertResult success()
```


Creates successful result without content.


**Returns:**
[DocumentConvertResult](../../com.groupdocs.markdown/documentconvertresult)
### success(String content) {#success-java.lang.String-}
```
public static DocumentConvertResult success(String content)
```


Creates successful result with content.


**Parameters:**
| Parameter | Type | Description |
| --- | --- | --- |
| content | java.lang.String |  |

**Returns:**
[DocumentConvertResult](../../com.groupdocs.markdown/documentconvertresult)
### failure(String errorMessage, Throwable exception) {#failure-java.lang.String-java.lang.Throwable-}
```
public static DocumentConvertResult failure(String errorMessage, Throwable exception)
```


Creates failed result.


**Parameters:**
| Parameter | Type | Description |
| --- | --- | --- |
| errorMessage | java.lang.String |  |
| exception | java.lang.Throwable |  |

**Returns:**
[DocumentConvertResult](../../com.groupdocs.markdown/documentconvertresult)
