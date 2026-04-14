---
title: from_markdown_string method
second_title: GroupDocs.Markdown for Python via .NET API References
description: 
type: docs
url: /python-net/groupdocs.markdown/markdownconverter/from_markdown_string/
is_root: false
weight: 1040
---


## from_markdown_string {#markdown_content-output_path-options}

Converts a Markdown string to a document and saves it to a file.

```python
def from_markdown_string(cls, markdown_content, output_path, options):
    ...
```

| Parameter | Type | Description |
| :- | :- | :- |
| markdown_content | `str` | The Markdown content as a string. |
| output_path | `str` | Path where the output document will be saved. |
| options | `ExportOptions` | Export options, or `None` to infer format from the file extension. |

| Raises | Description |
| :- | :- |
| `GroupDocsMarkdownException` | Thrown when conversion fails. |
| `NotImplementedError` | Thrown when the output format is not supported. |

## from_markdown_string {#markdown_content-output_stream-options}

Converts a Markdown string to a document and writes it to a stream.

```python
def from_markdown_string(cls, markdown_content, output_stream, options):
    ...
```

| Parameter | Type | Description |
| :- | :- | :- |
| markdown_content | `str` | The Markdown content as a string. |
| output_stream | `io.RawIOBase` | A writable stream that will receive the document bytes. |
| options | `ExportOptions` | Export options. `ExportOptions.format` must be set since there is no file extension to infer from. |

| Raises | Description |
| :- | :- |
| `GroupDocsMarkdownException` | Thrown when conversion fails. |
| `ValueError` | Thrown when `options` is None or `ExportOptions.format` is `FileFormat.unknown`. |

### See Also
* class [`MarkdownConverter`](/python-net/groupdocs.markdown/markdownconverter/)
