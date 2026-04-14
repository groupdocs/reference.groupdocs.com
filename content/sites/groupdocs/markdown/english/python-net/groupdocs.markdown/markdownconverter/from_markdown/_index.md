---
title: from_markdown method
second_title: GroupDocs.Markdown for Python via .NET API References
description: 
type: docs
url: /python-net/groupdocs.markdown/markdownconverter/from_markdown/
is_root: false
weight: 1030
---


## from_markdown {#markdown_path-output_path}

Converts a Markdown file to a document format, inferring the output format from the file extension of `output_path` (e.g. `.docx`, `.pdf`).

```python
def from_markdown(cls, markdown_path, output_path):
    ...
```

| Parameter | Type | Description |
| :- | :- | :- |
| markdown_path | `str` | Path to the source Markdown file. |
| output_path | `str` | Path where the output document will be saved. The extension determines the format. |

| Raises | Description |
| :- | :- |
| `GroupDocsMarkdownException` | Thrown when conversion fails. |
| `NotImplementedError` | Thrown when the output format is not supported. |

## from_markdown {#markdown_path-output_path-options}

Converts a Markdown file to a document format with the specified export options.

```python
def from_markdown(cls, markdown_path, output_path, options):
    ...
```

| Parameter | Type | Description |
| :- | :- | :- |
| markdown_path | `str` | Path to the source Markdown file. |
| output_path | `str` | Path where the output document will be saved. |
| options | `ExportOptions` | Export options. Use `ExportOptions.format` to override format detection, or pass `None` to infer from the output file extension. |

| Raises | Description |
| :- | :- |
| `GroupDocsMarkdownException` | Thrown when conversion fails. |
| `NotImplementedError` | Thrown when the output format is not supported. |

### See Also
* class [`MarkdownConverter`](/python-net/groupdocs.markdown/markdownconverter/)
