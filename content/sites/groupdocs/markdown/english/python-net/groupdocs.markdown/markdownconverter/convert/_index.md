---
title: convert method
second_title: GroupDocs.Markdown for Python via .NET API References
description: 
type: docs
url: /python-net/groupdocs.markdown/markdownconverter/convert/
is_root: false
weight: 1010
---


## convert

Converts the loaded document to Markdown using default options and returns the result with the Markdown content in [`ConvertResult.content`](/python-net/groupdocs.markdown/convertresult/content/).

```python
def convert(self):
    ...
```

**Returns:** A `ConvertResult` whose `ConvertResult.is_success` indicates whether the conversion succeeded. On success, `ConvertResult.content` contains the Markdown string.

## convert {#output_stream}

Converts the loaded document to Markdown and writes the output to the specified stream.

The [`ConvertResult.content`](/python-net/groupdocs.markdown/convertresult/content/) property will be None; the Markdown bytes are written directly to `output_stream`.

```python
def convert(self, output_stream):
    ...
```

| Parameter | Type | Description |
| :- | :- | :- |
| output_stream | `io.RawIOBase` | A writable stream that will receive the UTF-8 encoded Markdown output. |

**Returns:** ConvertResult: A result indicating success or failure. On success, `ConvertResult.content` is None because the output was written to the stream.

## convert {#output_file_path}

Converts the loaded document to Markdown and saves the result to a file at the specified output_file_path.

```python
def convert(self, output_file_path):
    ...
```

| Parameter | Type | Description |
| :- | :- | :- |
| output_file_path | `str` | The path where the Markdown file will be written. |

**Returns:** ConvertResult: A `ConvertResult` indicating success or failure. On success, `ConvertResult.content` is None because the output was written to the file.

## convert {#convert_options}

Converts the loaded document to Markdown with the specified options and returns the result with the Markdown content in [`ConvertResult.content`](/python-net/groupdocs.markdown/convertresult/content/).

```python
def convert(self, convert_options):
    ...
```

| Parameter | Type | Description |
| :- | :- | :- |
| convert_options | `ConvertOptions` | Options that control the conversion, such as `ConvertOptions.heading_level_offset`, `ConvertOptions.image_export_strategy`, and `ConvertOptions.page_numbers`. Pass `None` to use defaults. |

**Returns:** ConvertResult: A `ConvertResult` whose `ConvertResult.content` contains the Markdown string on success.

## convert {#output_stream-convert_options}

Converts the loaded document to Markdown with the specified options, writing the output to a stream.

```python
def convert(self, output_stream, convert_options):
    ...
```

| Parameter | Type | Description |
| :- | :- | :- |
| output_stream | `io.RawIOBase` | A writable stream that will receive the UTF-8 encoded Markdown output. |
| convert_options | `ConvertOptions` | Options that control the conversion. Pass None to use defaults. |

**Returns:** ConvertResult: A `ConvertResult` indicating success or failure. `ConvertResult.content` is None because the output was written to the stream.

## convert {#output_file_path-convert_options}

Converts the loaded document to Markdown with the specified options and saves the result to a file.

The file is created (or overwritten) at `output_file_path`.

```python
def convert(self, output_file_path, convert_options):
    ...
```

| Parameter | Type | Description |
| :- | :- | :- |
| output_file_path | `str` | The path where the Markdown file will be written. |
| convert_options | `ConvertOptions` | Options that control the conversion. Pass None to use defaults. |

**Returns:** ConvertResult: Indicates success or failure. `ConvertResult.content` is None because the output was written to the file.

### See Also
* class [`MarkdownConverter`](/python-net/groupdocs.markdown/markdownconverter/)
