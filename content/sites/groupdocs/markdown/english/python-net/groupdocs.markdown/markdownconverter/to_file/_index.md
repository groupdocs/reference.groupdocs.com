---
title: to_file method
second_title: GroupDocs.Markdown for Python via .NET API References
description: 
type: docs
url: /markdown/python-net/groupdocs.markdown/markdownconverter/to_file/
is_root: false
weight: 1100
---


## to_file {#source_path-output_path}

Converts a document to Markdown and saves the result directly to a file.

```python
def to_file(cls, source_path, output_path):
    ...
```

| Parameter | Type | Description |
| :- | :- | :- |
| source_path | `str` | The path to the source document (e.g. `"report.pdf"`). |
| output_path | `str` | The path where the Markdown file will be created or overwritten. |

| Raises | Description |
| :- | :- |
| `GroupDocsMarkdownException` | Thrown when the conversion fails. |
| `ValueError` | Thrown when `source_path` is None or empty. |
| `NotImplementedError` | Thrown when the file format is not supported. |

## to_file {#source_path-output_path-convert_options}

Converts a document to Markdown with the specified conversion options and saves the result to a file.

```python
def to_file(cls, source_path, output_path, convert_options):
    ...
```

| Parameter | Type | Description |
| :- | :- | :- |
| source_path | `str` | The path to the source document. |
| output_path | `str` | The path where the Markdown file will be created or overwritten. |
| convert_options | `ConvertOptions` | Options that customize the conversion (image strategy, heading offset, page numbers). May be `None`. |

| Raises | Description |
| :- | :- |
| `GroupDocsMarkdownException` | Thrown when the conversion fails. |
| `NotImplementedError` | Thrown when the file format is not supported. |

## to_file {#source_path-output_path-load_options-convert_options}

Converts a document to Markdown with the specified load and conversion options, saving the result to a file.

```python
def to_file(cls, source_path, output_path, load_options, convert_options):
    ...
```

| Parameter | Type | Description |
| :- | :- | :- |
| source_path | `str` | The path to the source document. |
| output_path | `str` | The path where the Markdown file will be created or overwritten. |
| load_options | `LoadOptions` | Options for loading the document (password, format hint). May be None. |
| convert_options | `ConvertOptions` | Options that customize the conversion. May be None. |

| Raises | Description |
| :- | :- |
| `GroupDocsMarkdownException` | Thrown when the conversion fails. |
| `NotImplementedError` | Thrown when the file format is not supported. |

### See Also
* class [`MarkdownConverter`](/markdown/python-net/groupdocs.markdown/markdownconverter/)
