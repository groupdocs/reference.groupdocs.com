---
title: get_info method
second_title: GroupDocs.Markdown for Python via .NET API References
description: 
type: docs
url: /python-net/groupdocs.markdown/markdownconverter/get_info/
is_root: false
weight: 1070
---


## get_info {#source_path}

Returns metadata about a document (format, page count, title, author, encryption status) without performing a full conversion.

```python
def get_info(cls, source_path):
    ...
```

| Parameter | Type | Description |
| :- | :- | :- |
| source_path | `str` | The path to the source document. |

**Returns:** DocumentInfo: A `DocumentInfo` with the detected format, page count, and other metadata.

| Raises | Description |
| :- | :- |
| `ValueError` | When `source_path` is None or empty. |
| `NotImplementedError` | When the file format is not supported. |

## get_info {#source_path-load_options}

Returns metadata about a document using the specified load options. Use this overload to supply a password when inspecting an encrypted document.

```python
def get_info(cls, source_path, load_options):
    ...
```

| Parameter | Type | Description |
| :- | :- | :- |
| source_path | `str` | The path to the source document. |
| load_options | `LoadOptions` | Options for loading the document (password, format hint). May be None. |

**Returns:** DocumentInfo: The detected format, page count, and other metadata.

| Raises | Description |
| :- | :- |
| `ValueError` | When `source_path` is None or empty. |
| `NotImplementedError` | When the file format is not supported. |

### See Also
* class [`MarkdownConverter`](/markdown/python-net/groupdocs.markdown/markdownconverter/)
