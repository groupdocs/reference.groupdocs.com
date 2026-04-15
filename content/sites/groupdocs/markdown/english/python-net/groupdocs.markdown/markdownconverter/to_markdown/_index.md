---
title: to_markdown method
second_title: GroupDocs.Markdown for Python via .NET API References
description: 
type: docs
url: /markdown/python-net/groupdocs.markdown/markdownconverter/to_markdown/
is_root: false
weight: 1120
---


## to_markdown {#source_path}

Converts a document to Markdown in a single call and returns the Markdown string.

```python
def to_markdown(cls, source_path):
    ...
```

| Parameter | Type | Description |
| :- | :- | :- |
| source_path | `str` | The path to the source document (e.g. `"report.docx"`). |

**Returns:** str: The converted Markdown content as a UTF-8 string.

| Raises | Description |
| :- | :- |
| `GroupDocsMarkdownException` | Thrown when the conversion fails. |
| `ValueError` | Thrown when `source_path` is None or empty. |
| `NotImplementedError` | Thrown when the file format is not supported. |

## to_markdown {#source_path-load_options}

Converts a document to Markdown using the specified load options and returns the Markdown string.

Use this overload to supply a password for encrypted documents or to specify the file format explicitly.

```python
def to_markdown(cls, source_path, load_options):
    ...
```

| Parameter | Type | Description |
| :- | :- | :- |
| source_path | `str` | The path to the source document. |
| load_options | `LoadOptions` | Options for loading the document (password, format hint). May be None. |

**Returns:** str: The converted Markdown content as a UTF-8 string.

| Raises | Description |
| :- | :- |
| `GroupDocsMarkdownException` | Thrown when the conversion fails. |
| `NotImplementedError` | Thrown when the file format is not supported. |

## to_markdown {#source_path-convert_options}

Converts a document to Markdown using the specified conversion options and returns the Markdown string.

Use this overload to control image handling, heading offsets, or page selection.

```python
def to_markdown(cls, source_path, convert_options):
    ...
```

| Parameter | Type | Description |
| :- | :- | :- |
| source_path | `str` | The path to the source document. |
| convert_options | `ConvertOptions` | Options that customize the conversion (image strategy, heading offset, page numbers). May be None. |

**Returns:** str: The converted Markdown content as a UTF-8 string.

| Raises | Description |
| :- | :- |
| `GroupDocsMarkdownException` | Thrown when the conversion fails. |
| `NotImplementedError` | Thrown when the file format is not supported. |

## to_markdown {#source_path-load_options-convert_options}

Converts a document to Markdown using the specified load and conversion options, and returns the Markdown string.

```python
def to_markdown(cls, source_path, load_options, convert_options):
    ...
```

| Parameter | Type | Description |
| :- | :- | :- |
| source_path | `str` | The path to the source document. |
| load_options | `LoadOptions` | Options for loading the document (password, format hint). May be None. |
| convert_options | `ConvertOptions` | Options that customize the conversion. May be None. |

**Returns:** str: The converted Markdown content as a UTF-8 string.

| Raises | Description |
| :- | :- |
| `NotImplementedError` | Thrown when the file format is not supported. |

### See Also
* class [`MarkdownConverter`](/markdown/python-net/groupdocs.markdown/markdownconverter/)
