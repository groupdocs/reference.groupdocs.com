---
title: Convert
second_title: GroupDocs.Markdown for .NET API Reference
description: Converts the loaded document to Markdown using default options and returns the result with the Markdown content in Contentgroupdocs.markdown/convertresult/content.
type: docs
weight: 20
url: /net/groupdocs.markdown/markdownconverter/convert/
---
## Convert() {#convert}

Converts the loaded document to Markdown using default options and returns the result with the Markdown content in [`Content`](../../convertresult/content).

```csharp
public ConvertResult Convert()
```

### Return Value

A [`ConvertResult`](../../convertresult) whose [`IsSuccess`](../../convertresult/issuccess) indicates whether the conversion succeeded. On success, [`Content`](../../convertresult/content) contains the Markdown string.

### Examples

```csharp
using var converter = new MarkdownConverter("report.pdf");
ConvertResult result = converter.Convert();
if (result.IsSuccess)
    File.WriteAllText("report.md", result.Content);
```

### See Also

* class [ConvertResult](../../convertresult)
* class [MarkdownConverter](../../markdownconverter)
* namespace [GroupDocs.Markdown](../../../groupdocs.markdown)
* assembly [GroupDocs.Markdown](../../../)

---

## Convert(Stream) {#convert_2}

Converts the loaded document to Markdown and writes the output to the specified stream. The [`Content`](../../convertresult/content) property will be `null`; the Markdown bytes are written directly to *outputStream*.

```csharp
public ConvertResult Convert(Stream outputStream)
```

| Parameter | Type | Description |
| --- | --- | --- |
| outputStream | Stream | A writable stream that will receive the UTF-8 encoded Markdown output. |

### Return Value

A [`ConvertResult`](../../convertresult) indicating success or failure. On success, [`Content`](../../convertresult/content) is `null` because the output was written to the stream.

### See Also

* class [ConvertResult](../../convertresult)
* class [MarkdownConverter](../../markdownconverter)
* namespace [GroupDocs.Markdown](../../../groupdocs.markdown)
* assembly [GroupDocs.Markdown](../../../)

---

## Convert(string) {#convert_4}

Converts the loaded document to Markdown and saves the result to a file. The file is created (or overwritten) at *outputFilePath*.

```csharp
public ConvertResult Convert(string outputFilePath)
```

| Parameter | Type | Description |
| --- | --- | --- |
| outputFilePath | String | The path where the Markdown file will be written. |

### Return Value

A [`ConvertResult`](../../convertresult) indicating success or failure. On success, [`Content`](../../convertresult/content) is `null` because the output was written to the file.

### See Also

* class [ConvertResult](../../convertresult)
* class [MarkdownConverter](../../markdownconverter)
* namespace [GroupDocs.Markdown](../../../groupdocs.markdown)
* assembly [GroupDocs.Markdown](../../../)

---

## Convert(ConvertOptions) {#convert_1}

Converts the loaded document to Markdown with the specified options and returns the result with the Markdown content in [`Content`](../../convertresult/content).

```csharp
public ConvertResult Convert(ConvertOptions convertOptions)
```

| Parameter | Type | Description |
| --- | --- | --- |
| convertOptions | ConvertOptions | Options that control the conversion, such as [`HeadingLevelOffset`](../../convertoptions/headingleveloffset), [`ImageExportStrategy`](../../convertoptions/imageexportstrategy), and [`PageNumbers`](../../convertoptions/pagenumbers). Pass `null` to use defaults. |

### Return Value

A [`ConvertResult`](../../convertresult) whose [`Content`](../../convertresult/content) contains the Markdown string on success.

### Examples

```csharp
using var converter = new MarkdownConverter("document.docx");
var options = new ConvertOptions
{
    HeadingLevelOffset = 1,
    PageNumbers = new[] { 1, 2, 3 }
};
ConvertResult result = converter.Convert(options);
```

### See Also

* class [ConvertResult](../../convertresult)
* class [ConvertOptions](../../convertoptions)
* class [MarkdownConverter](../../markdownconverter)
* namespace [GroupDocs.Markdown](../../../groupdocs.markdown)
* assembly [GroupDocs.Markdown](../../../)

---

## Convert(Stream, ConvertOptions) {#convert_3}

Converts the loaded document to Markdown with the specified options, writing the output to a stream.

```csharp
public ConvertResult Convert(Stream outputStream, ConvertOptions convertOptions)
```

| Parameter | Type | Description |
| --- | --- | --- |
| outputStream | Stream | A writable stream that will receive the UTF-8 encoded Markdown output. |
| convertOptions | ConvertOptions | Options that control the conversion. Pass `null` to use defaults. |

### Return Value

A [`ConvertResult`](../../convertresult) indicating success or failure. [`Content`](../../convertresult/content) is `null` because the output was written to the stream.

### See Also

* class [ConvertResult](../../convertresult)
* class [ConvertOptions](../../convertoptions)
* class [MarkdownConverter](../../markdownconverter)
* namespace [GroupDocs.Markdown](../../../groupdocs.markdown)
* assembly [GroupDocs.Markdown](../../../)

---

## Convert(string, ConvertOptions) {#convert_5}

Converts the loaded document to Markdown with the specified options and saves the result to a file. The file is created (or overwritten) at *outputFilePath*.

```csharp
public ConvertResult Convert(string outputFilePath, ConvertOptions convertOptions)
```

| Parameter | Type | Description |
| --- | --- | --- |
| outputFilePath | String | The path where the Markdown file will be written. |
| convertOptions | ConvertOptions | Options that control the conversion. Pass `null` to use defaults. |

### Return Value

A [`ConvertResult`](../../convertresult) indicating success or failure. [`Content`](../../convertresult/content) is `null` because the output was written to the file.

### Examples

```csharp
using var converter = new MarkdownConverter("spreadsheet.xlsx");
var options = new ConvertOptions
{
    ImageExportStrategy = new ExportImagesToFileSystemStrategy("images")
};
converter.Convert("output.md", options);
```

### See Also

* class [ConvertResult](../../convertresult)
* class [ConvertOptions](../../convertoptions)
* class [MarkdownConverter](../../markdownconverter)
* namespace [GroupDocs.Markdown](../../../groupdocs.markdown)
* assembly [GroupDocs.Markdown](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Markdown.dll -->
