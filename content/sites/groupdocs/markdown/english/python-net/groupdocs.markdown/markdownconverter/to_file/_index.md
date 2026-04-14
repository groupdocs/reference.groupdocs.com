---
title: to_file method
second_title: GroupDocs.Markdown for Python via .NET API References
description: 
type: docs
url: /python-net/groupdocs.markdown/markdownconverter/to_file/
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
| convert_options | `ConvertOptions` | Options that customize the conversion (image strategy, heading offset, page numbers). May be None. |

| Raises | Description |
| :- | :- |
| `GroupDocsMarkdownException` | Thrown when the conversion fails. |
| `NotImplementedError` | Thrown when the file format is not supported. |

## to_file {#source_path-output_path-load_options-convert_options}

Converts a document to Markdown with the specified load and conversion options, saving the result to a file. This is the most flexible static overload for file-based output.

```python
def to_file(cls, source_path, output_path, load_options, convert_options):
    ...
```

| Parameter | Type | Description |
| :- | :- | :- |
| source_path | `str` |  |
| output_path | `str` |  |
| load_options | `LoadOptions` |  |
| convert_options | `ConvertOptions` |  |

### See Also
* class [`MarkdownConverter`](/python-net/groupdocs.markdown/markdownconverter/)
