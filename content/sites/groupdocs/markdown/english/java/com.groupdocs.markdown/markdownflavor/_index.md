---
title: MarkdownFlavor
second_title: GroupDocs.Markdown for Java API Reference
description: Specifies the target Markdown dialect for the conversion output.
type: docs
weight: 35
url: /java/com.groupdocs.markdown/markdownflavor/
---
**Inheritance:**
java.lang.Object, java.lang.Enum
```
public enum MarkdownFlavor extends Enum<MarkdownFlavor>
```

Specifies the target Markdown dialect for the conversion output.

## Fields

| Field | Description |
| --- | --- |
| [GITHUB](#GITHUB) | GitHub Flavored Markdown \\u2014 supports tables, strikethrough, and task lists.
 |
| [COMMON_MARK](#COMMON-MARK) | Strict CommonMark output.
 |
## Methods

| Method | Description |
| --- | --- |
| [values()](#values--) |  |
| [valueOf(String name)](#valueOf-java.lang.String-) |  |
### GITHUB {#GITHUB}
```
public static final MarkdownFlavor GITHUB
```


GitHub Flavored Markdown \\u2014 supports tables, strikethrough, and task lists. This is the default.


### COMMON_MARK {#COMMON-MARK}
```
public static final MarkdownFlavor COMMON_MARK
```


Strict CommonMark output. Tables are rendered as code blocks since CommonMark does not have native table syntax.


### values() {#values--}
```
public static MarkdownFlavor[] values()
```




**Returns:**
com.groupdocs.markdown.MarkdownFlavor[]
### valueOf(String name) {#valueOf-java.lang.String-}
```
public static MarkdownFlavor valueOf(String name)
```




**Parameters:**
| Parameter | Type | Description |
| --- | --- | --- |
| name | java.lang.String |  |

**Returns:**
[MarkdownFlavor](../../com.groupdocs.markdown/markdownflavor)
