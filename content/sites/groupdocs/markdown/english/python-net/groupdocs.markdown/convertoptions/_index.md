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
| [__init__](/python-net/groupdocs.markdown/convertoptions/__init__/) | Initializes a new instance of the [`ConvertOptions`](/python-net/groupdocs.markdown/convertoptions/) class. |

### Properties
| Property | Description |
| :- | :- |
| [flavor](/python-net/groupdocs.markdown/convertoptions/flavor/) | The target Markdown dialect. |
| [heading_level_offset](/python-net/groupdocs.markdown/convertoptions/heading_level_offset/) | The offset to apply to all heading levels in the Markdown output. |
| [image_export_strategy](/python-net/groupdocs.markdown/convertoptions/image_export_strategy/) | The strategy for handling images during conversion. The default is [`ExportImagesAsBase64Strategy`](/python-net/groupdocs.markdown/exportimagesasbase64strategy/). |
| [include_front_matter](/python-net/groupdocs.markdown/convertoptions/include_front_matter/) | The value indicating whether to prepend YAML front matter to the Markdown output. Default is False. |
| [include_hidden_sheets](/python-net/groupdocs.markdown/convertoptions/include_hidden_sheets/) | The option indicating whether hidden worksheets are included in spreadsheet conversions. |
| [max_columns](/python-net/groupdocs.markdown/convertoptions/max_columns/) | The maximum number of columns to include per table when converting spreadsheets. Columns beyond this limit are truncated with an ellipsis indicator. 0 means unlimited (default). |
| [max_rows](/python-net/groupdocs.markdown/convertoptions/max_rows/) | The maximum number of data rows to include per worksheet when converting spreadsheets. |
| [page_numbers](/python-net/groupdocs.markdown/convertoptions/page_numbers/) | The array of 1-based page or worksheet numbers to convert; set to None to convert all pages. |
| [sheet_separator](/python-net/groupdocs.markdown/convertoptions/sheet_separator/) | The separator inserted between worksheets in spreadsheet conversions. |
| [uri_export_strategy](/python-net/groupdocs.markdown/convertoptions/uri_export_strategy/) | The strategy for customizing resource URIs written to Markdown output. |

### See Also
* module [`groupdocs.markdown`](/python-net/groupdocs.markdown/)
