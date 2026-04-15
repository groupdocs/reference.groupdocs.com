---
title: to_file_async method
second_title: GroupDocs.Markdown for Python via .NET API References
description: 
type: docs
url: /python-net/groupdocs.markdown/markdownconverter/to_file_async/
is_root: false
weight: 1110
---


## to_file_async {#source_path-output_path-convert_options}

Asynchronously converts the document and saves the result to a file.

Both source reading and output writing are performed asynchronously.

```python
def to_file_async(cls, source_path, output_path, convert_options):
    ...
```

| Parameter | Type | Description |
| :- | :- | :- |
| source_path | `str` | The path to the source document. |
| output_path | `str` | The path where the Markdown file will be saved. |
| convert_options | `ConvertOptions` | Options for the conversion. May be None. |

| Raises | Description |
| :- | :- |
| `GroupDocsMarkdownException` | Thrown when conversion fails. |

### See Also
* class [`MarkdownConverter`](/markdown/python-net/groupdocs.markdown/markdownconverter/)
