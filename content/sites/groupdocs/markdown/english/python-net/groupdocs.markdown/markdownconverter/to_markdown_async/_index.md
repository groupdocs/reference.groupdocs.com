---
title: to_markdown_async method
second_title: GroupDocs.Markdown for Python via .NET API References
description: 
type: docs
url: /markdown/python-net/groupdocs.markdown/markdownconverter/to_markdown_async/
is_root: false
weight: 1130
---


## to_markdown_async {#source_path}

Asynchronously converts the document at the specified path to Markdown. File reading is performed asynchronously.

```python
def to_markdown_async(cls, source_path):
    ...
```

| Parameter | Type | Description |
| :- | :- | :- |
| source_path | `str` | The path to the source document. |

**Returns:** str: The converted Markdown content.

| Raises | Description |
| :- | :- |
| `GroupDocsMarkdownException` | Thrown when conversion fails. |

## to_markdown_async {#source_path-load_options-convert_options}

Asynchronously converts the document at the specified path to Markdown.

```python
def to_markdown_async(cls, source_path, load_options, convert_options):
    ...
```

| Parameter | Type | Description |
| :- | :- | :- |
| source_path | `str` | The path to the source document. |
| load_options | `LoadOptions` | Options for loading the document. May be None. |
| convert_options | `ConvertOptions` | Options for the conversion. May be None. |

**Returns:** str: The converted Markdown content.

| Raises | Description |
| :- | :- |
| `GroupDocsMarkdownException` | Thrown when conversion fails. |

### See Also
* class [`MarkdownConverter`](/markdown/python-net/groupdocs.markdown/markdownconverter/)
