---
title: ConvertResult class
second_title: GroupDocs.Markdown for Python via .NET API References
description: 
type: docs
url: /python-net/groupdocs.markdown/convertresult/
is_root: false
weight: 20
---


## ConvertResult class

Contains the output of a successful document-to-Markdown conversion.

All `Convert` methods throw on failure, so a returned [`ConvertResult`](/markdown/python-net/groupdocs.markdown/convertresult/) always represents a successful conversion. Use [`ConvertResult.content`](/markdown/python-net/groupdocs.markdown/convertresult/content/) to read the Markdown string (when converting to string) and [`ConvertResult.warnings`](/markdown/python-net/groupdocs.markdown/convertresult/warnings/) to check for non-fatal issues.

The ConvertResult type exposes the following members:

### Methods
| Method | Description |
| :- | :- |
| [failure](/markdown/python-net/groupdocs.markdown/convertresult/failure/#error_message-exception) | Creates a failed result with error information. |
| [success](/markdown/python-net/groupdocs.markdown/convertresult/success/) | Creates a successful result without content. Used when the output was written to a stream or file. |
| [success](/markdown/python-net/groupdocs.markdown/convertresult/success/#content) | Creates a successful result containing the converted Markdown content. |

### Properties
| Property | Description |
| :- | :- |
| [content](/markdown/python-net/groupdocs.markdown/convertresult/content/) | The converted Markdown content as a string. |
| [error_message](/markdown/python-net/groupdocs.markdown/convertresult/error_message/) | The error message if the conversion failed, or None if it succeeded. |
| [exception](/markdown/python-net/groupdocs.markdown/convertresult/exception/) | The exception that caused the conversion to fail, or None if the conversion succeeded. |
| [is_success](/markdown/python-net/groupdocs.markdown/convertresult/is_success/) | The conversion succeeded flag indicating whether the conversion completed successfully. |
| [warnings](/markdown/python-net/groupdocs.markdown/convertresult/warnings/) | The non-fatal warnings that occurred during conversion. |

### See Also
* module [`groupdocs.markdown`](/markdown/python-net/groupdocs.markdown/)
