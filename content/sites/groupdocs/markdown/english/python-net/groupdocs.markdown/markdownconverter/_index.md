---
title: MarkdownConverter class
second_title: GroupDocs.Markdown for Python via .NET API References
description: 
type: docs
url: /python-net/groupdocs.markdown/markdownconverter/
is_root: false
weight: 180
---


## MarkdownConverter class

Converts documents from Word, Excel, PDF, and other formats to Markdown, offering static one-liner methods and an instance-based API with full control over conversion options.

Supported input formats include Word (DOC, DOCX, DOCM, DOT, DOTX, DOTM, RTF, ODT, OTT), Excel (XLS, XLSX, XLSB, XLSM, CSV, TSV, ODS, OTS), PDF, e‑books (EPUB, MOBI), plain text (TXT), and CHM help files. Call [`MarkdownConverter.get_supported_formats`](/python-net/groupdocs.markdown/markdownconverter/get_supported_formats/) for the full list.

For quick, one‑shot conversions use the static methods `MarkdownConverter.to_markdown(str)`, `MarkdownConverter.to_file(str, str)`, and `MarkdownConverter.get_info(str)`. When you need to customize the conversion (image handling, heading offsets, page selection) or retrieve document metadata alongside conversion, create an instance and call [`MarkdownConverter.convert`](/python-net/groupdocs.markdown/markdownconverter/convert/) or [`MarkdownConverter.get_document_info`](/python-net/groupdocs.markdown/markdownconverter/get_document_info/).

The instance follows the disposable pattern; dispose it when finished, preferably using a context manager.

The MarkdownConverter type exposes the following members:

### Constructors
| Constructor | Description |
| :- | :- |
| [__init__](/python-net/groupdocs.markdown/markdownconverter/__init__/#source_path) | Initializes a new converter for the document at the specified file path. |
| [__init__](/python-net/groupdocs.markdown/markdownconverter/__init__/#source_stream) | Initializes a new converter that reads the document from the supplied stream, automatically detecting the file format. |
| [__init__](/python-net/groupdocs.markdown/markdownconverter/__init__/#source_path-load_options) | Initializes a new converter for the document at the specified file path, using the given load options. |
| [__init__](/python-net/groupdocs.markdown/markdownconverter/__init__/#source_stream-load_options) | Initializes a new converter that reads the document from the supplied stream, using the given load options. |

### Methods
| Method | Description |
| :- | :- |
| [convert](/python-net/groupdocs.markdown/markdownconverter/convert/) | Converts the loaded document to Markdown using default options and returns the result with the Markdown content in [`ConvertResult.content`](/python-net/groupdocs.markdown/convertresult/content/). |
| [convert](/python-net/groupdocs.markdown/markdownconverter/convert/#output_stream) | Converts the loaded document to Markdown and writes the output to the specified stream. |
| [convert](/python-net/groupdocs.markdown/markdownconverter/convert/#output_file_path) | Converts the loaded document to Markdown and saves the result to a file at the specified output_file_path. |
| [convert](/python-net/groupdocs.markdown/markdownconverter/convert/#convert_options) | Converts the loaded document to Markdown with the specified options and returns the result with the Markdown content in [`ConvertResult.content`](/python-net/groupdocs.markdown/convertresult/content/). |
| [convert](/python-net/groupdocs.markdown/markdownconverter/convert/#output_stream-convert_options) | Converts the loaded document to Markdown with the specified options, writing the output to a stream. |
| [convert](/python-net/groupdocs.markdown/markdownconverter/convert/#output_file_path-convert_options) | Converts the loaded document to Markdown with the specified options and saves the result to a file. |
| [convert_async](/python-net/groupdocs.markdown/markdownconverter/convert_async/) | Asynchronously converts the loaded document to Markdown and returns the result as a string. |
| [convert_async](/python-net/groupdocs.markdown/markdownconverter/convert_async/#convert_options) | Asynchronously converts the loaded document to Markdown with the specified options. |
| [convert_async](/python-net/groupdocs.markdown/markdownconverter/convert_async/#output_file_path-convert_options) | Asynchronously converts the loaded document and saves the result to a file. The source file read and output file write are performed asynchronously. |
| [from_markdown](/python-net/groupdocs.markdown/markdownconverter/from_markdown/#markdown_path-output_path) | Converts a Markdown file to a document format, inferring the output format from the file extension of `output_path` (e.g. `.docx`, `.pdf`). |
| [from_markdown](/python-net/groupdocs.markdown/markdownconverter/from_markdown/#markdown_path-output_path-options) | Converts a Markdown file to a document format with the specified export options. |
| [from_markdown_string](/python-net/groupdocs.markdown/markdownconverter/from_markdown_string/#markdown_content-output_path-options) | Converts a Markdown string to a document and saves it to a file. |
| [from_markdown_string](/python-net/groupdocs.markdown/markdownconverter/from_markdown_string/#markdown_content-output_stream-options) | Converts a Markdown string to a document and writes it to a stream. |
| [get_document_info](/python-net/groupdocs.markdown/markdownconverter/get_document_info/) | Retrieves metadata about the loaded document without performing a full conversion. |
| [get_document_info_async](/python-net/groupdocs.markdown/markdownconverter/get_document_info_async/) | Asynchronously retrieves metadata about the loaded document. |
| [get_info](/python-net/groupdocs.markdown/markdownconverter/get_info/#source_path) | Returns metadata about a document (format, page count, title, author, encryption status) without performing a full conversion. |
| [get_info](/python-net/groupdocs.markdown/markdownconverter/get_info/#source_path-load_options) | Returns metadata about a document using the specified load options, and can supply a password when inspecting an encrypted document. |
| [get_info_async](/python-net/groupdocs.markdown/markdownconverter/get_info_async/#source_path-load_options) | Asynchronously retrieves metadata about the document at the specified path. |
| [get_supported_formats](/python-net/groupdocs.markdown/markdownconverter/get_supported_formats/) | Returns the complete list of [`FileFormat`](/python-net/groupdocs.markdown/fileformat/) values that can be converted to Markdown. |
| [to_file](/python-net/groupdocs.markdown/markdownconverter/to_file/#source_path-output_path) | Converts a document to Markdown and saves the result directly to a file. |
| [to_file](/python-net/groupdocs.markdown/markdownconverter/to_file/#source_path-output_path-convert_options) | Converts a document to Markdown with the specified conversion options and saves the result to a file. |
| [to_file](/python-net/groupdocs.markdown/markdownconverter/to_file/#source_path-output_path-load_options-convert_options) | Converts a document to Markdown with the specified load and conversion options, saving the result to a file. This is the most flexible static overload for file-based output. |
| [to_file_async](/python-net/groupdocs.markdown/markdownconverter/to_file_async/#source_path-output_path-convert_options) | Asynchronously converts the document and saves the result to a file. |
| [to_markdown](/python-net/groupdocs.markdown/markdownconverter/to_markdown/#source_path) | Converts a document to Markdown in a single call, automatically detecting the format, and returns the Markdown string. |
| [to_markdown](/python-net/groupdocs.markdown/markdownconverter/to_markdown/#source_path-load_options) | Converts a document to Markdown using the specified load options and returns the Markdown string. |
| [to_markdown](/python-net/groupdocs.markdown/markdownconverter/to_markdown/#source_path-convert_options) | Converts a document to Markdown using the specified conversion options and returns the Markdown string. |
| [to_markdown](/python-net/groupdocs.markdown/markdownconverter/to_markdown/#source_path-load_options-convert_options) | Converts a document to Markdown using the specified load and conversion options, and returns the Markdown string. |
| [to_markdown_async](/python-net/groupdocs.markdown/markdownconverter/to_markdown_async/#source_path) | Asynchronously converts the document at the specified path to Markdown. File reading is performed asynchronously. |
| [to_markdown_async](/python-net/groupdocs.markdown/markdownconverter/to_markdown_async/#source_path-load_options-convert_options) | Asynchronously converts the document at the specified path to Markdown. |

### See Also
* module [`groupdocs.markdown`](/python-net/groupdocs.markdown/)
