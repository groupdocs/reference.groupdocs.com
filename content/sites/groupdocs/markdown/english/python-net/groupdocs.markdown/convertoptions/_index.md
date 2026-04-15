---
title: ConvertOptions class
second_title: GroupDocs.Markdown for Python via .NET API References
description: 
type: docs
url: /python-net/groupdocs.markdown/convertoptions/
is_root: false
weight: 10
---


## ConvertOptions class

Provides options for customizing the document conversion process to Markdown format.

This class allows you to configure how documents are converted to Markdown, including how images are exported, how resource URIs are written, which pages to convert, and how heading levels are adjusted.

By default, images are embedded as Base64 strings in the Markdown output.

The ConvertOptions type exposes the following members:

### Constructors
| Constructor | Description |
| :- | :- |
| [__init__](/markdown/python-net/groupdocs.markdown/convertoptions/__init__/) | Initializes a new instance of the [`ConvertOptions`](/markdown/python-net/groupdocs.markdown/convertoptions/) class. |

### Properties
| Property | Description |
| :- | :- |
| [flavor](/markdown/python-net/groupdocs.markdown/convertoptions/flavor/) | The target Markdown dialect. Default is [`MarkdownFlavor.git_hub`](/markdown/python-net/groupdocs.markdown/markdownflavor/git_hub/). |
| [heading_level_offset](/markdown/python-net/groupdocs.markdown/convertoptions/heading_level_offset/) | The offset to apply to all heading levels in the Markdown output. Default is 0 (no change). |
| [image_export_strategy](/markdown/python-net/groupdocs.markdown/convertoptions/image_export_strategy/) | The strategy for handling images during conversion. Default is [`ExportImagesAsBase64Strategy`](/markdown/python-net/groupdocs.markdown/exportimagesasbase64strategy/). |
| [include_front_matter](/markdown/python-net/groupdocs.markdown/convertoptions/include_front_matter/) | The option indicating whether to prepend YAML front matter to the Markdown output. Default is False. |
| [include_hidden_sheets](/markdown/python-net/groupdocs.markdown/convertoptions/include_hidden_sheets/) | The property indicates whether hidden worksheets are included in spreadsheet conversions. |
| [max_columns](/markdown/python-net/groupdocs.markdown/convertoptions/max_columns/) | The maximum number of columns to include per table when converting spreadsheets; columns beyond this limit are truncated with an ellipsis indicator, and a value of 0 means unlimited (default). |
| [max_rows](/markdown/python-net/groupdocs.markdown/convertoptions/max_rows/) | The maximum number of data rows to include per worksheet when converting spreadsheets; rows beyond this limit are truncated with an ellipsis indicator, and a value of 0 means unlimited (default). |
| [page_numbers](/markdown/python-net/groupdocs.markdown/convertoptions/page_numbers/) | The page numbers to convert, as a list of 1‑based page or worksheet numbers. |
| [sheet_separator](/markdown/python-net/groupdocs.markdown/convertoptions/sheet_separator/) | The separator inserted between worksheets in spreadsheet conversions. |
| [uri_export_strategy](/markdown/python-net/groupdocs.markdown/convertoptions/uri_export_strategy/) | The strategy for customizing resource URIs written to Markdown output. |

### See Also
* module [`groupdocs.markdown`](/markdown/python-net/groupdocs.markdown/)
