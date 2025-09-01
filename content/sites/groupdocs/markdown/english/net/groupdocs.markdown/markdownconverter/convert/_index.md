---
title: Convert
second_title: GroupDocs.Markdown for .NET API Reference
description: Converts the source document to Markdown format and returns the result as a string.
type: docs
weight: 20
url: /net/groupdocs.markdown/markdownconverter/convert/
---
## Convert() {#convert}

Converts the source document to Markdown format and returns the result as a string.

```csharp
public DocumentConverterResult Convert()
```

### Return Value

A [`DocumentConverterResult`](../../documentconverterresult) containing the converted Markdown content or error information.

### Examples

The following example shows how to convert a document to Markdown and get the result as a string:

```csharp
using (var converter = new MarkdownConverter("document.docx"))
{
    var result = converter.Convert();
    if (result.IsSuccess)
    {
        string markdown = result.Content;
        Console.WriteLine(markdown);
    }
    else
    {
        Console.WriteLine($"Conversion failed: {result.ErrorMessage}");
    }
}
```

### See Also

* class [DocumentConverterResult](../../documentconverterresult)
* class [MarkdownConverter](../../markdownconverter)
* namespace [GroupDocs.Markdown](../../../groupdocs.markdown)
* assembly [GroupDocs.Markdown](../../../)

---

## Convert(Stream) {#convert_2}

Converts the source document to Markdown format and writes the result to the specified output stream.

```csharp
public DocumentConverterResult Convert(Stream outputStream)
```

| Parameter | Type | Description |
| --- | --- | --- |
| outputStream | Stream | The stream to write the converted Markdown content to. |

### Return Value

A [`DocumentConverterResult`](../../documentconverterresult) indicating success or failure of the conversion.

### Exceptions

| exception | condition |
| --- | --- |
| ArgumentNullException | Thrown when outputStream is null. |

### Examples

The following example shows how to convert a document to Markdown and write to a stream:

```csharp
using (var converter = new MarkdownConverter("document.docx"))
using (var outputStream = new MemoryStream())
{
    var result = converter.Convert(outputStream);
    if (result.IsSuccess)
    {
        // Process the output stream
    }
}
```

### See Also

* class [DocumentConverterResult](../../documentconverterresult)
* class [MarkdownConverter](../../markdownconverter)
* namespace [GroupDocs.Markdown](../../../groupdocs.markdown)
* assembly [GroupDocs.Markdown](../../../)

---

## Convert(string) {#convert_4}

Converts the source document to Markdown format and saves it to the specified file path.

```csharp
public DocumentConverterResult Convert(string outputFilePath)
```

| Parameter | Type | Description |
| --- | --- | --- |
| outputFilePath | String | The path where the converted Markdown file will be saved. |

### Return Value

A [`DocumentConverterResult`](../../documentconverterresult) indicating success or failure of the conversion.

### Exceptions

| exception | condition |
| --- | --- |
| ArgumentNullException | Thrown when outputFilePath is null or empty. |
| IOException | Thrown when there is an error writing to the output file. |

### Examples

The following example shows how to convert a document to Markdown and save to a file:

```csharp
using (var converter = new MarkdownConverter("document.docx"))
{
    var result = converter.Convert("output.md");
    if (result.IsSuccess)
    {
        Console.WriteLine("Conversion completed successfully");
    }
}
```

### See Also

* class [DocumentConverterResult](../../documentconverterresult)
* class [MarkdownConverter](../../markdownconverter)
* namespace [GroupDocs.Markdown](../../../groupdocs.markdown)
* assembly [GroupDocs.Markdown](../../../)

---

## Convert(DocumentConverterOptions) {#convert_1}

Converts the source document to Markdown format using the specified conversion options and returns the result as a string.

```csharp
public DocumentConverterResult Convert(DocumentConverterOptions converterOptions)
```

| Parameter | Type | Description |
| --- | --- | --- |
| converterOptions | DocumentConverterOptions | The options to use for the conversion process. |

### Return Value

A [`DocumentConverterResult`](../../documentconverterresult) containing the converted Markdown content or error information.

### Exceptions

| exception | condition |
| --- | --- |
| ArgumentNullException | Thrown when converterOptions is null. |

### Examples

The following example shows how to convert a document to Markdown with custom options:

```csharp
var options = new DocumentConverterOptions
{
    // Configure conversion options
};

using (var converter = new MarkdownConverter("document.docx"))
{
    var result = converter.Convert(options);
    if (result.IsSuccess)
    {
        string markdown = result.Content;
        Console.WriteLine(markdown);
    }
}
```

### See Also

* class [DocumentConverterResult](../../documentconverterresult)
* class [DocumentConverterOptions](../../documentconverteroptions)
* class [MarkdownConverter](../../markdownconverter)
* namespace [GroupDocs.Markdown](../../../groupdocs.markdown)
* assembly [GroupDocs.Markdown](../../../)

---

## Convert(Stream, DocumentConverterOptions) {#convert_3}

Converts the source document to Markdown format using the specified conversion options and writes the result to the specified output stream.

```csharp
public DocumentConverterResult Convert(Stream outputStream, 
    DocumentConverterOptions converterOptions)
```

| Parameter | Type | Description |
| --- | --- | --- |
| outputStream | Stream | The stream to write the converted Markdown content to. |
| converterOptions | DocumentConverterOptions | The options to use for the conversion process. |

### Return Value

A [`DocumentConverterResult`](../../documentconverterresult) indicating success or failure of the conversion.

### Exceptions

| exception | condition |
| --- | --- |
| ArgumentNullException | Thrown when outputStream or converterOptions is null. |

### Examples

The following example shows how to convert a document to Markdown with custom options and write to a stream:

```csharp
var options = new DocumentConverterOptions
{
    // Configure conversion options
};

using (var converter = new MarkdownConverter("document.docx"))
using (var outputStream = new MemoryStream())
{
    var result = converter.Convert(outputStream, options);
    if (result.IsSuccess)
    {
        // Process the output stream
    }
}
```

### See Also

* class [DocumentConverterResult](../../documentconverterresult)
* class [DocumentConverterOptions](../../documentconverteroptions)
* class [MarkdownConverter](../../markdownconverter)
* namespace [GroupDocs.Markdown](../../../groupdocs.markdown)
* assembly [GroupDocs.Markdown](../../../)

---

## Convert(string, DocumentConverterOptions) {#convert_5}

Converts the source document to Markdown format using the specified conversion options and saves it to the specified file path.

```csharp
public DocumentConverterResult Convert(string outputFilePath, 
    DocumentConverterOptions converterOptions)
```

| Parameter | Type | Description |
| --- | --- | --- |
| outputFilePath | String | The path where the converted Markdown file will be saved. |
| converterOptions | DocumentConverterOptions | The options to use for the conversion process. |

### Return Value

A [`DocumentConverterResult`](../../documentconverterresult) indicating success or failure of the conversion.

### Exceptions

| exception | condition |
| --- | --- |
| ArgumentNullException | Thrown when outputFilePath is null or empty, or converterOptions is null. |
| IOException | Thrown when there is an error writing to the output file. |

### Examples

The following example shows how to convert a document to Markdown with custom options and save to a file:

```csharp
var options = new DocumentConverterOptions
{
    // Configure conversion options
};

using (var converter = new MarkdownConverter("document.docx"))
{
    var result = converter.Convert("output.md", options);
    if (result.IsSuccess)
    {
        Console.WriteLine("Conversion completed successfully");
    }
}
```

### See Also

* class [DocumentConverterResult](../../documentconverterresult)
* class [DocumentConverterOptions](../../documentconverteroptions)
* class [MarkdownConverter](../../markdownconverter)
* namespace [GroupDocs.Markdown](../../../groupdocs.markdown)
* assembly [GroupDocs.Markdown](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Markdown.dll -->
