---
title: MarkdownConverter
second_title: GroupDocs.Markdown for .NET API Reference
description: Initializes a new instance of the MarkdownConvertergroupdocs.markdown/markdownconverter class.
type: docs
weight: 10
url: /net/groupdocs.markdown/markdownconverter/markdownconverter/
---
## MarkdownConverter(string) {#constructor_2}

Initializes a new instance of the [`MarkdownConverter`](../../markdownconverter) class.

```csharp
public MarkdownConverter(string sourcePath)
```

| Parameter | Type | Description |
| --- | --- | --- |
| sourcePath | String | The path to the source document. Must not be null or empty. |

### Exceptions

| exception | condition |
| --- | --- |
| ArgumentNullException | Thrown when sourcePath is null or empty. |
| FileNotFoundException | Thrown when the source file does not exist. |
| NotSupportedException | Thrown when no suitable converter is found for the file type. |

### Remarks

If the file name does not have an extension, GroupDocs.Markdown will attempt to detect the file type automatically. If file type detection fails, a NotSupportedException will be thrown.

### Examples

The following example shows how to create a converter from a file path:

```csharp
using (var converter = new MarkdownConverter("document.docx"))
{
    // Use the converter
}
```

### See Also

* class [MarkdownConverter](../../markdownconverter)
* namespace [GroupDocs.Markdown](../../../groupdocs.markdown)
* assembly [GroupDocs.Markdown](../../../)

---

## MarkdownConverter(Stream) {#constructor}

Initializes a new instance of the [`MarkdownConverter`](../../markdownconverter) class.

```csharp
public MarkdownConverter(Stream sourceStream)
```

| Parameter | Type | Description |
| --- | --- | --- |
| sourceStream | Stream | The source stream containing the document data. Must not be null. |

### Exceptions

| exception | condition |
| --- | --- |
| ArgumentNullException | Thrown when sourceStream is null. |
| NotSupportedException | Thrown when no suitable converter is found for the stream type. |

### Remarks

GroupDocs.Markdown will attempt to detect the file type automatically from the stream content. If file type detection fails, a NotSupportedException will be thrown. Note: GroupDocs.Markdown does not take ownership of the provided stream. The caller is responsible for disposing the stream after the converter is no longer needed.

### Examples

The following example shows how to create a converter from a stream:

```csharp
using (var fileStream = File.OpenRead("document.docx"))
using (var converter = new MarkdownConverter(fileStream))
{
    // Use the converter
}
```

### See Also

* class [MarkdownConverter](../../markdownconverter)
* namespace [GroupDocs.Markdown](../../../groupdocs.markdown)
* assembly [GroupDocs.Markdown](../../../)

---

## MarkdownConverter(string, LoadOptions) {#constructor_3}

Initializes a new instance of the [`MarkdownConverter`](../../markdownconverter) class.

```csharp
public MarkdownConverter(string sourcePath, LoadOptions loadOptions)
```

| Parameter | Type | Description |
| --- | --- | --- |
| sourcePath | String | The path to the source document. Must not be null or empty. |
| loadOptions | LoadOptions | Additional information about the source file. Must not be null. |

### Exceptions

| exception | condition |
| --- | --- |
| ArgumentNullException | Thrown when sourcePath is null or empty, or streamInfo is null. |
| FileNotFoundException | Thrown when the source file does not exist. |
| NotSupportedException | Thrown when no suitable converter is found for the file type. |

### Remarks

If the file name does not have an extension or if the provided *loadOptions* does not specify an Extension or MediaType, GroupDocs.Markdown will attempt to detect the file type automatically. If file type detection fails, a NotSupportedException will be thrown.

### Examples

The following example shows how to create a converter with stream information:

```csharp
var streamInfo = new StreamInfo
{
    Extension = ".docx",
    Password = "password123"
};

using (var converter = new MarkdownConverter("document.docx", streamInfo))
{
    // Use the converter
}
```

### See Also

* class [LoadOptions](../../loadoptions)
* class [MarkdownConverter](../../markdownconverter)
* namespace [GroupDocs.Markdown](../../../groupdocs.markdown)
* assembly [GroupDocs.Markdown](../../../)

---

## MarkdownConverter(Stream, LoadOptions) {#constructor_1}

Initializes a new instance of the [`MarkdownConverter`](../../markdownconverter) class.

```csharp
public MarkdownConverter(Stream sourceStream, LoadOptions loadOptions)
```

| Parameter | Type | Description |
| --- | --- | --- |
| sourceStream | Stream | The source stream containing the document data. Must not be null. |
| loadOptions | LoadOptions | Additional information about the source file. Must not be null. |

### Exceptions

| exception | condition |
| --- | --- |
| ArgumentNullException | Thrown when sourceStream or streamInfo is null. |
| NotSupportedException | Thrown when no suitable converter is found for the stream type. |

### Remarks

If the provided *loadOptions* does not specify an Extension or MediaType, GroupDocs.Markdown will attempt to detect the file type automatically from the stream content. If file type detection fails, a NotSupportedException will be thrown. Note: GroupDocs.Markdown does not take ownership of the provided stream. The caller is responsible for disposing the stream after the converter is no longer needed.

### Examples

The following example shows how to create a converter from a stream with stream information:

```csharp
var streamInfo = new StreamInfo
{
    Extension = ".docx",
    Password = "password123"
};

using (var fileStream = File.OpenRead("document.docx"))
using (var converter = new MarkdownConverter(fileStream, streamInfo))
{
    // Use the converter
}
```

### See Also

* class [LoadOptions](../../loadoptions)
* class [MarkdownConverter](../../markdownconverter)
* namespace [GroupDocs.Markdown](../../../groupdocs.markdown)
* assembly [GroupDocs.Markdown](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Markdown.dll -->
