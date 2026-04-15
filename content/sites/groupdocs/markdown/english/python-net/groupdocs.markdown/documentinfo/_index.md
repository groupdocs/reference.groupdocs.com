---
title: DocumentInfo class
second_title: GroupDocs.Markdown for Python via .NET API References
description: 
type: docs
url: /python-net/groupdocs.markdown/documentinfo/
is_root: false
weight: 70
---


## DocumentInfo class

Provides read-only metadata about a loaded document, such as its format, page count, title, and encryption status.

Use [`MarkdownConverter.get_document_info`](/markdown/python-net/groupdocs.markdown/markdownconverter/get_document_info/) or [`MarkdownConverter.get_info`](/markdown/python-net/groupdocs.markdown/markdownconverter/get_info/) to obtain an instance of this class. The information is extracted from the source document without performing a full conversion, so it is a lightweight way to inspect a file before converting it.

The DocumentInfo type exposes the following members:

### Properties
| Property | Description |
| :- | :- |
| [author](/markdown/python-net/groupdocs.markdown/documentinfo/author/) | The document author extracted from its metadata, or an empty string if no author is available. |
| [file_format](/markdown/python-net/groupdocs.markdown/documentinfo/file_format/) | The detected file format of the document. |
| [is_encrypted](/markdown/python-net/groupdocs.markdown/documentinfo/is_encrypted/) | The document is password-protected. Returns True if the document requires a password to open; otherwise, False. |
| [page_count](/markdown/python-net/groupdocs.markdown/documentinfo/page_count/) | The number of pages in the document, or the number of worksheets for spreadsheets, as a non‑negative integer. |
| [title](/markdown/python-net/groupdocs.markdown/documentinfo/title/) | The document title extracted from its metadata, or an empty string if no title is available. |

### See Also
* module [`groupdocs.markdown`](/markdown/python-net/groupdocs.markdown/)
