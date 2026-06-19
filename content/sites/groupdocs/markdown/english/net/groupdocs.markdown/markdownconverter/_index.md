---
title: MarkdownConverter
second_title: GroupDocs.Markdown for .NET API Reference
description: Converts documents from Word Excel PDF and other formats to Markdown. Provides both static oneliner methods and an instancebased API with full control over conversion options.
type: docs
weight: 220
url: /net/groupdocs.markdown/markdownconverter/
---
## MarkdownConverter class

Converts documents from Word, Excel, PDF, and other formats to Markdown. Provides both static one-liner methods and an instance-based API with full control over conversion options.

```csharp
public class MarkdownConverter : IDisposable
```

## Constructors

| Name | Description |
| --- | --- |
| [MarkdownConverter](markdownconverter#constructor)(Stream) | Creates a new converter that reads the document from the supplied stream. The file format is detected automatically from the stream content. If automatic detection is not possible, use the [`MarkdownConverter`](./markdownconverter) overload and specify the format via [`LoadOptions`](../loadoptions). |
| [MarkdownConverter](markdownconverter#constructor_2)(string) | Creates a new converter for the document at the specified file path. The file format is detected automatically from the file extension and content. |
| [MarkdownConverter](markdownconverter#constructor_1)(Stream, LoadOptions) | Creates a new converter that reads the document from the supplied stream, using the given load options. Use this overload when reading from a MemoryStream, network stream, or any non-file stream where format detection from a file name is not available. |
| [MarkdownConverter](markdownconverter#constructor_3)(string, LoadOptions) | Creates a new converter for the document at the specified file path, using the given load options. Use this overload to supply a password for encrypted documents or to explicitly specify the file format. |

## Methods

| Name | Description |
| --- | --- |
| [Convert](../../groupdocs.markdown/markdownconverter/convert#convert)() | Converts the loaded document to Markdown using default options and returns the result with the Markdown content in [`Content`](../convertresult/content). |
| [Convert](../../groupdocs.markdown/markdownconverter/convert#convert_1)(ConvertOptions) | Converts the loaded document to Markdown with the specified options and returns the result with the Markdown content in [`Content`](../convertresult/content). |
| [Convert](../../groupdocs.markdown/markdownconverter/convert#convert_2)(Stream) | Converts the loaded document to Markdown and writes the output to the specified stream. The [`Content`](../convertresult/content) property will be `null`; the Markdown bytes are written directly to *outputStream*. |
| [Convert](../../groupdocs.markdown/markdownconverter/convert#convert_4)(string) | Converts the loaded document to Markdown and saves the result to a file. The file is created (or overwritten) at *outputFilePath*. |
| [Convert](../../groupdocs.markdown/markdownconverter/convert#convert_3)(Stream, ConvertOptions) | Converts the loaded document to Markdown with the specified options, writing the output to a stream. |
| [Convert](../../groupdocs.markdown/markdownconverter/convert#convert_5)(string, ConvertOptions) | Converts the loaded document to Markdown with the specified options and saves the result to a file. The file is created (or overwritten) at *outputFilePath*. |
| [ConvertAsync](../../groupdocs.markdown/markdownconverter/convertasync#convertasync_2)(CancellationToken) | Asynchronously converts the loaded document to Markdown and returns the result as a string. |
| [ConvertAsync](../../groupdocs.markdown/markdownconverter/convertasync#convertasync)(ConvertOptions, CancellationToken) | Asynchronously converts the loaded document to Markdown with the specified options. |
| [ConvertAsync](../../groupdocs.markdown/markdownconverter/convertasync#convertasync_1)(string, ConvertOptions, CancellationToken) | Asynchronously converts the loaded document and saves the result to a file. The source file read and output file write are performed asynchronously. |
| [Dispose](../../groupdocs.markdown/markdownconverter/dispose)() | Releases all resources used by this [`MarkdownConverter`](../markdownconverter) instance, including the internal copy of the source document stream. Always call [`Dispose`](./dispose) when you are finished, or use a `using` statement to ensure timely cleanup. |
| [GetDocumentInfo](../../groupdocs.markdown/markdownconverter/getdocumentinfo)() | Retrieves metadata about the loaded document without performing a full conversion. Use this to inspect properties such as page count, title, author, and whether the document is encrypted before deciding how to convert. |
| [GetDocumentInfoAsync](../../groupdocs.markdown/markdownconverter/getdocumentinfoasync)(CancellationToken) | Asynchronously retrieves metadata about the loaded document. |
| static [FromMarkdown](../../groupdocs.markdown/markdownconverter/frommarkdown#frommarkdown)(string, string) | Converts a Markdown file to a document format. The output format is inferred from the file extension of *outputPath* (e.g. `.docx`, `.pdf`). |
| static [FromMarkdown](../../groupdocs.markdown/markdownconverter/frommarkdown#frommarkdown_1)(string, string, ExportOptions) | Converts a Markdown file to a document format with the specified export options. |
| static [FromMarkdownString](../../groupdocs.markdown/markdownconverter/frommarkdownstring#frommarkdownstring)(string, Stream, ExportOptions) | Converts a Markdown string to a document and writes it to a stream. |
| static [FromMarkdownString](../../groupdocs.markdown/markdownconverter/frommarkdownstring#frommarkdownstring_1)(string, string, ExportOptions) | Converts a Markdown string to a document and saves it to a file. |
| static [GetInfo](../../groupdocs.markdown/markdownconverter/getinfo#getinfo)(string) | Returns metadata about a document (format, page count, title, author, encryption status) without performing a full conversion. This is a lightweight way to inspect a file. |
| static [GetInfo](../../groupdocs.markdown/markdownconverter/getinfo#getinfo_1)(string, LoadOptions) | Returns metadata about a document using the specified load options. Use this overload to supply a password when inspecting an encrypted document. |
| static [GetInfoAsync](../../groupdocs.markdown/markdownconverter/getinfoasync)(string, LoadOptions, CancellationToken) | Asynchronously retrieves metadata about the document at the specified path. |
| static [GetSupportedFormats](../../groupdocs.markdown/markdownconverter/getsupportedformats)() | Returns the complete list of [`FileFormat`](../fileformat) values that can be converted to Markdown. Use this to check at runtime whether a particular format is supported before attempting conversion. |
| static [ToFile](../../groupdocs.markdown/markdownconverter/tofile#tofile)(string, string) | Converts a document to Markdown and saves the result directly to a file. This is the simplest way to produce a Markdown file from a supported document format. |
| static [ToFile](../../groupdocs.markdown/markdownconverter/tofile#tofile_1)(string, string, ConvertOptions) | Converts a document to Markdown with the specified conversion options and saves the result to a file. |
| static [ToFile](../../groupdocs.markdown/markdownconverter/tofile#tofile_2)(string, string, LoadOptions, ConvertOptions) | Converts a document to Markdown with the specified load and conversion options, saving the result to a file. This is the most flexible static overload for file-based output. |
| static [ToFileAsync](../../groupdocs.markdown/markdownconverter/tofileasync)(string, string, ConvertOptions, CancellationToken) | Asynchronously converts the document and saves the result to a file. Both source reading and output writing are performed asynchronously. |
| static [ToMarkdown](../../groupdocs.markdown/markdownconverter/tomarkdown#tomarkdown)(string) | Converts a document to Markdown in a single call and returns the Markdown string. This is the simplest way to convert a file. The format is detected automatically. |
| static [ToMarkdown](../../groupdocs.markdown/markdownconverter/tomarkdown#tomarkdown_1)(string, ConvertOptions) | Converts a document to Markdown using the specified conversion options and returns the Markdown string. Use this overload to control image handling, heading offsets, or page selection. |
| static [ToMarkdown](../../groupdocs.markdown/markdownconverter/tomarkdown#tomarkdown_2)(string, LoadOptions) | Converts a document to Markdown using the specified load options and returns the Markdown string. Use this overload to supply a password for encrypted documents or to specify the file format explicitly. |
| static [ToMarkdown](../../groupdocs.markdown/markdownconverter/tomarkdown#tomarkdown_3)(string, LoadOptions, ConvertOptions) | Converts a document to Markdown using the specified load and conversion options, and returns the Markdown string. This is the most flexible static overload, combining format/password control with full conversion customization. |
| static [ToMarkdownAsync](../../groupdocs.markdown/markdownconverter/tomarkdownasync#tomarkdownasync_1)(string, CancellationToken) | Asynchronously converts the document at the specified path to Markdown. File reading is performed asynchronously. |
| static [ToMarkdownAsync](../../groupdocs.markdown/markdownconverter/tomarkdownasync#tomarkdownasync)(string, LoadOptions, ConvertOptions, CancellationToken) | Asynchronously converts the document at the specified path to Markdown. File reading is performed asynchronously; conversion runs on the thread pool. |

### Remarks

Supported input formats include Word (DOC, DOCX, DOCM, DOT, DOTX, DOTM, RTF, ODT, OTT), Excel (XLS, XLSX, XLSB, XLSM, CSV, TSV, ODS, OTS), PDF, e-books (EPUB, MOBI), plain text (TXT), and CHM help files. Call [`GetSupportedFormats`](./getsupportedformats) for the full list.

For quick, one-shot conversions use the static methods [`ToMarkdown`](./tomarkdown), [`ToFile`](./tofile), and [`GetInfo`](./getinfo). When you need to customize the conversion (image handling, heading offsets, page selection) or retrieve document metadata alongside conversion, create an instance and call [`Convert`](./convert) or [`GetDocumentInfo`](./getdocumentinfo).

The instance implements IDisposable. Always dispose it when you are done, preferably with a `using` statement.

### Examples

Convert a document to a Markdown string in one line:

```csharp
string md = MarkdownConverter.ToMarkdown("document.docx");
```

Convert a document and save the result directly to a file:

```csharp
MarkdownConverter.ToFile("document.docx", "output.md");
```

Use the instance API with options for full control:

```csharp
using var converter = new MarkdownConverter("document.docx");
var result = converter.Convert(new ConvertOptions { HeadingLevelOffset = 1 });
if (result.IsSuccess)
    Console.WriteLine(result.Content);
```

### See Also

* namespace [GroupDocs.Markdown](../../groupdocs.markdown)
* assembly [GroupDocs.Markdown](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Markdown.dll -->
