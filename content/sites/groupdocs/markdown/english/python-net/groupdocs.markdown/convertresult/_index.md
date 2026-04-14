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

All `Convert` methods throw on failure, so a returned [`ConvertResult`](/python-net/groupdocs.markdown/convertresult/) always represents a successful conversion. Use [`ConvertResult.content`](/python-net/groupdocs.markdown/convertresult/content/) to read the Markdown string (when converting to string) and [`ConvertResult.warnings`](/python-net/groupdocs.markdown/convertresult/warnings/) to check for non-fatal issues.

The ConvertResult type exposes the following members:

### Methods
| Method | Description |
| :- | :- |
| [failure](/python-net/groupdocs.markdown/convertresult/failure/#error_message-exception) | Creates a failed result with error information. |
| [success](/python-net/groupdocs.markdown/convertresult/success/) | Creates a successful result without content. |
| [success](/python-net/groupdocs.markdown/convertresult/success/#content) | Creates a successful result containing the converted Markdown content. |

### Properties
| Property | Description |
| :- | :- |
| [content](/python-net/groupdocs.markdown/convertresult/content/) | The converted Markdown content as a string. |
| [error_message](/python-net/groupdocs.markdown/convertresult/error_message/) | The error message if the conversion failed, or None if it succeeded. |
| [exception](/python-net/groupdocs.markdown/convertresult/exception/) | The exception that caused the conversion to fail, or None if the conversion succeeded. |
| [is_success](/python-net/groupdocs.markdown/convertresult/is_success/) | The conversion completed successfully, returning True if it succeeded and False otherwise. |
| [warnings](/python-net/groupdocs.markdown/convertresult/warnings/) | The list of non-fatal warnings that occurred during conversion. |

### See Also
* module [`groupdocs.markdown`](/python-net/groupdocs.markdown/)
