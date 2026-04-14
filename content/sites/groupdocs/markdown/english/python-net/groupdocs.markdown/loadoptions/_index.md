---
title: LoadOptions class
second_title: GroupDocs.Markdown for Python via .NET API References
description: 
type: docs
url: /python-net/groupdocs.markdown/loadoptions/
is_root: false
weight: 170
---


## LoadOptions class

Specifies additional options for loading a document, such as an explicit file format or a password for encrypted files.

By default, the library detects the file format automatically from the file extension or content. Use this class when you need to override automatic detection (for example, when loading from a stream without a file name) or when the document is password‑protected.

The LoadOptions type exposes the following members:

### Constructors
| Constructor | Description |
| :- | :- |
| [__init__](/python-net/groupdocs.markdown/loadoptions/__init__/) | Initializes a new instance of the LoadOptions class with automatic format detection. |
| [__init__](/python-net/groupdocs.markdown/loadoptions/__init__/#file_format) | Initializes a new instance of the LoadOptions class with an explicit file format. |

### Properties
| Property | Description |
| :- | :- |
| [file_format](/python-net/groupdocs.markdown/loadoptions/file_format/) | The file format of the document to load. |
| [password](/python-net/groupdocs.markdown/loadoptions/password/) | The password used to open an encrypted document. |

### See Also
* module [`groupdocs.markdown`](/python-net/groupdocs.markdown/)
