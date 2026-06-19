---
title: ToMarkdown
second_title: GroupDocs.Markdown for .NET API Reference
description: Converts a document to Markdown in a single call and returns the Markdown string. This is the simplest way to convert a file. The format is detected automatically.
type: docs
weight: 140
url: /net/groupdocs.markdown/markdownconverter/tomarkdown/
---
## ToMarkdown(string) {#tomarkdown}

Converts a document to Markdown in a single call and returns the Markdown string. This is the simplest way to convert a file. The format is detected automatically.

```csharp
public static string ToMarkdown(string sourcePath)
```

| Parameter | Type | Description |
| --- | --- | --- |
| sourcePath | String | The path to the source document (e.g. `"report.docx"`). |

### Return Value

The converted Markdown content as a UTF-8 string.

### Exceptions

| exception | condition |
| --- | --- |
| [GroupDocsMarkdownException](../../groupdocsmarkdownexception) | Thrown when the conversion fails. |
| ArgumentNullException | Thrown when *sourcePath* is `null` or empty. |
| NotSupportedException | Thrown when the file format is not supported. |

### Examples

```csharp
string markdown = MarkdownConverter.ToMarkdown("document.docx");
Console.WriteLine(markdown);
```

### See Also

* class [MarkdownConverter](../../markdownconverter)
* namespace [GroupDocs.Markdown](../../../groupdocs.markdown)
* assembly [GroupDocs.Markdown](../../../)

---

## ToMarkdown(string, LoadOptions) {#tomarkdown_2}

Converts a document to Markdown using the specified load options and returns the Markdown string. Use this overload to supply a password for encrypted documents or to specify the file format explicitly.

```csharp
public static string ToMarkdown(string sourcePath, LoadOptions loadOptions)
```

| Parameter | Type | Description |
| --- | --- | --- |
| sourcePath | String | The path to the source document. |
| loadOptions | LoadOptions | Options for loading the document (password, format hint). May be `null`. |

### Return Value

The converted Markdown content as a UTF-8 string.

### Exceptions

| exception | condition |
| --- | --- |
| [GroupDocsMarkdownException](../../groupdocsmarkdownexception) | Thrown when the conversion fails. |
| NotSupportedException | Thrown when the file format is not supported. |

### Examples

```csharp
var loadOptions = new LoadOptions(FileFormat.Docx) { Password = "secret" };
string markdown = MarkdownConverter.ToMarkdown("encrypted.docx", loadOptions);
```

### See Also

* class [LoadOptions](../../loadoptions)
* class [MarkdownConverter](../../markdownconverter)
* namespace [GroupDocs.Markdown](../../../groupdocs.markdown)
* assembly [GroupDocs.Markdown](../../../)

---

## ToMarkdown(string, ConvertOptions) {#tomarkdown_1}

Converts a document to Markdown using the specified conversion options and returns the Markdown string. Use this overload to control image handling, heading offsets, or page selection.

```csharp
public static string ToMarkdown(string sourcePath, ConvertOptions convertOptions)
```

| Parameter | Type | Description |
| --- | --- | --- |
| sourcePath | String | The path to the source document. |
| convertOptions | ConvertOptions | Options that customize the conversion (image strategy, heading offset, page numbers). May be `null`. |

### Return Value

The converted Markdown content as a UTF-8 string.

### Exceptions

| exception | condition |
| --- | --- |
| [GroupDocsMarkdownException](../../groupdocsmarkdownexception) | Thrown when the conversion fails. |
| NotSupportedException | Thrown when the file format is not supported. |

### Examples

```csharp
var options = new ConvertOptions { HeadingLevelOffset = 2 };
string markdown = MarkdownConverter.ToMarkdown("document.docx", options);
```

### See Also

* class [ConvertOptions](../../convertoptions)
* class [MarkdownConverter](../../markdownconverter)
* namespace [GroupDocs.Markdown](../../../groupdocs.markdown)
* assembly [GroupDocs.Markdown](../../../)

---

## ToMarkdown(string, LoadOptions, ConvertOptions) {#tomarkdown_3}

Converts a document to Markdown using the specified load and conversion options, and returns the Markdown string. This is the most flexible static overload, combining format/password control with full conversion customization.

```csharp
public static string ToMarkdown(string sourcePath, LoadOptions loadOptions, 
    ConvertOptions convertOptions)
```

| Parameter | Type | Description |
| --- | --- | --- |
| sourcePath | String | The path to the source document. |
| loadOptions | LoadOptions | Options for loading the document (password, format hint). May be `null`. |
| convertOptions | ConvertOptions | Options that customize the conversion. May be `null`. |

### Return Value

The converted Markdown content as a UTF-8 string.

### Exceptions

| exception | condition |
| --- | --- |
| [GroupDocsMarkdownException](../../groupdocsmarkdownexception) | Thrown when the conversion fails. |
| NotSupportedException | Thrown when the file format is not supported. |

### See Also

* class [LoadOptions](../../loadoptions)
* class [ConvertOptions](../../convertoptions)
* class [MarkdownConverter](../../markdownconverter)
* namespace [GroupDocs.Markdown](../../../groupdocs.markdown)
* assembly [GroupDocs.Markdown](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Markdown.dll -->
