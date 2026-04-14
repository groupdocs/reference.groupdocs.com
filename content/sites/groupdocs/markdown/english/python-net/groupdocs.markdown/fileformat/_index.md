---
title: FileFormat class
second_title: GroupDocs.Markdown for Python via .NET API References
description: 
type: docs
url: /python-net/groupdocs.markdown/fileformat/
is_root: false
weight: 120
---


## FileFormat class

Specifies a document file format. Used both as input format (when loading a document for conversion to Markdown) and as output format (when exporting Markdown to a document).

Pass a value from this enum to the `LoadOptions.__init__(FileFormat)` constructor to explicitly specify the source document format, or use [`FileFormat.unknown`](/python-net/groupdocs.markdown/fileformat/unknown/) to let the library detect it automatically.

Use [`MarkdownConverter.get_supported_formats`](/python-net/groupdocs.markdown/markdownconverter/get_supported_formats/) to retrieve all formats supported for conversion.

The FileFormat type exposes the following members:

### Fields
| Field | Description |
| :- | :- |
| [Unknown](/python-net/groupdocs.markdown/fileformat/unknown/) | The file format is not specified; the library will attempt to detect the format automatically. |
| [Doc](/python-net/groupdocs.markdown/fileformat/doc/) | Microsoft Word 97-2003 Document (.doc). |
| [Docx](/python-net/groupdocs.markdown/fileformat/docx/) | Microsoft Word Document (.docx). |
| [Docm](/python-net/groupdocs.markdown/fileformat/docm/) | Microsoft Word Macro-Enabled Document (.docm). |
| [Dot](/python-net/groupdocs.markdown/fileformat/dot/) | Microsoft Word 97-2003 Template (.dot). |
| [Dotx](/python-net/groupdocs.markdown/fileformat/dotx/) | Microsoft Word Template (.dotx). |
| [Dotm](/python-net/groupdocs.markdown/fileformat/dotm/) | Microsoft Word Macro-Enabled Template (.dotm). |
| [Rtf](/python-net/groupdocs.markdown/fileformat/rtf/) | Rich Text Format (.rtf). |
| [Odt](/python-net/groupdocs.markdown/fileformat/odt/) | OpenDocument Text (.odt). |
| [Ott](/python-net/groupdocs.markdown/fileformat/ott/) | OpenDocument Text Template (.ott). |
| [Xlsx](/python-net/groupdocs.markdown/fileformat/xlsx/) | Microsoft Excel Spreadsheet (.xlsx). |
| [Xls](/python-net/groupdocs.markdown/fileformat/xls/) | Microsoft Excel 97-2003 Spreadsheet (.xls). |
| [Xlsb](/python-net/groupdocs.markdown/fileformat/xlsb/) | Microsoft Excel Binary Spreadsheet (.xlsb). |
| [Xlsm](/python-net/groupdocs.markdown/fileformat/xlsm/) | Microsoft Excel Macro-Enabled Spreadsheet (.xlsm). |
| [Csv](/python-net/groupdocs.markdown/fileformat/csv/) | Comma-Separated Values (.csv). |
| [Tsv](/python-net/groupdocs.markdown/fileformat/tsv/) | Tab-Separated Values (.tsv). |
| [Ods](/python-net/groupdocs.markdown/fileformat/ods/) | OpenDocument Spreadsheet (.ods). |
| [Ots](/python-net/groupdocs.markdown/fileformat/ots/) | OpenDocument Spreadsheet Template (.ots). |
| [Pdf](/python-net/groupdocs.markdown/fileformat/pdf/) | The Portable Document Format (.pdf). |
| [Epub](/python-net/groupdocs.markdown/fileformat/epub/) | Electronic Publication (.epub). |
| [Mobi](/python-net/groupdocs.markdown/fileformat/mobi/) | Mobipocket E-Book (.mobi). |
| [Txt](/python-net/groupdocs.markdown/fileformat/txt/) | Plain Text (.txt). |
| [Md](/python-net/groupdocs.markdown/fileformat/md/) | Markdown (.md). Used as input format for reverse conversion (Markdown to document). |
| [Chm](/python-net/groupdocs.markdown/fileformat/chm/) | Compiled HTML Help (.chm). |

### See Also
* module [`groupdocs.markdown`](/python-net/groupdocs.markdown/)
