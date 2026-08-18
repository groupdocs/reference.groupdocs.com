---
title: DocumentProtectedException
second_title: GroupDocs.Markdown for Java API Reference
description: Thrown when a document is password-protected and no password or an incorrect password was provided via LoadOptions.setPassword....
type: docs
weight: 17
url: /java/com.groupdocs.markdown/documentprotectedexception/
---
**Inheritance:**
java.lang.Object, java.lang.Throwable, java.lang.Exception, java.lang.RuntimeException, [com.groupdocs.markdown.GroupDocsMarkdownException](../../com.groupdocs.markdown/groupdocsmarkdownexception)
```
public final class DocumentProtectedException extends GroupDocsMarkdownException
```

Thrown when a document is password-protected and no password (or an incorrect password) was provided via LoadOptions.setPassword(...).

## Constructors

| Constructor | Description |
| --- | --- |
| [DocumentProtectedException()](#DocumentProtectedException--) | Creates exception with default message.
 |
| [DocumentProtectedException(String message, Throwable cause)](#DocumentProtectedException-java.lang.String-java.lang.Throwable-) | Creates exception with custom message and cause.
 |
### DocumentProtectedException() {#DocumentProtectedException--}
```
public DocumentProtectedException()
```


Creates exception with default message.


### DocumentProtectedException(String message, Throwable cause) {#DocumentProtectedException-java.lang.String-java.lang.Throwable-}
```
public DocumentProtectedException(String message, Throwable cause)
```


Creates exception with custom message and cause.


**Parameters:**
| Parameter | Type | Description |
| --- | --- | --- |
| message | java.lang.String | the error message
 |
| cause | java.lang.Throwable | the underlying exception
 |

