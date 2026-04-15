---
title: convert_async method
second_title: GroupDocs.Markdown for Python via .NET API References
description: 
type: docs
url: /markdown/python-net/groupdocs.markdown/markdownconverter/convert_async/
is_root: false
weight: 1020
---


## convert_async

Asynchronously converts the loaded document to Markdown and returns the result as a string.

```python
def convert_async(self):
    ...
```

**Returns:** str: The converted Markdown content.

## convert_async {#convert_options}

Asynchronously converts the loaded document to Markdown with the specified options.

```python
def convert_async(self, convert_options):
    ...
```

| Parameter | Type | Description |
| :- | :- | :- |
| convert_options | `ConvertOptions` | Options that control the conversion. |

## convert_async {#output_file_path-convert_options}

Asynchronously converts the loaded document and saves the result to a file.

```python
def convert_async(self, output_file_path, convert_options):
    ...
```

| Parameter | Type | Description |
| :- | :- | :- |
| output_file_path | `str` | The path where the Markdown file will be written. |
| convert_options | `ConvertOptions` | Options that control the conversion. Pass `None` for defaults. |

### See Also
* class [`MarkdownConverter`](/markdown/python-net/groupdocs.markdown/markdownconverter/)
