---
title: __init__ constructor
second_title: GroupDocs.Markdown for Python via .NET API References
description: 
type: docs
url: /markdown/python-net/groupdocs.markdown/markdownconverter/__init__/
is_root: false
weight: 10
---


## __init__ {#source_path}

Initializes a new converter for the document at the specified file path.

The file format is detected automatically from the file extension and content.

```python
def __init__(self, source_path):
    ...
```

| Parameter | Type | Description |
| :- | :- | :- |
| source_path | `str` | Absolute or relative path to the source document (e.g. `"report.docx"`). |

| Raises | Description |
| :- | :- |
| `ValueError` | When `source_path` is None or empty. |
| `FileNotFoundError` | When the file at `source_path` does not exist. |
| `NotImplementedError` | When the file format is not supported. Call `MarkdownConverter.get_supported_formats` to see which formats are accepted. |

## __init__ {#source_stream}

Initializes a new converter that reads the document from the supplied stream. The file format is detected automatically from the stream content. If automatic detection is not possible, use the `MarkdownConverter.__init__(io.RawIOBase, LoadOptions)` overload and specify the format via [`LoadOptions`](/markdown/python-net/groupdocs.markdown/loadoptions/).

```python
def __init__(self, source_stream):
    ...
```

| Parameter | Type | Description |
| :- | :- | :- |
| source_stream | `io.RawIOBase` | A readable stream containing the document data. The stream is copied internally, so the caller may close it after construction. |

| Raises | Description |
| :- | :- |
| `ValueError` | When `source_stream` is None. |
| `NotImplementedError` | When the file format cannot be detected or is not supported. |

## __init__ {#source_path-load_options}

Initializes a new converter for the document at the specified file path, using the given load options.

```python
def __init__(self, source_path, load_options):
    ...
```

| Parameter | Type | Description |
| :- | :- | :- |
| source_path | `str` | Absolute or relative path to the source document. |
| load_options | `LoadOptions` | Options that control how the document is loaded. Pass a `LoadOptions` with `LoadOptions.password` set to open encrypted files, or with a specific `FileFormat` to override automatic format detection. May be None. |

| Raises | Description |
| :- | :- |
| `ValueError` | When `source_path` is None or empty. |
| `FileNotFoundError` | When the file at `source_path` does not exist. |
| `NotImplementedError` | When the file format is not supported. |

## __init__ {#source_stream-load_options}

Initializes a new converter that reads the document from the supplied stream, using the given load options.

Use this overload when reading from a `io.BytesIO`, network stream, or any non‑file stream where format detection from a file name is not available.

```python
def __init__(self, source_stream, load_options):
    ...
```

| Parameter | Type | Description |
| :- | :- | :- |
| source_stream | `io.RawIOBase` | A readable stream containing the document data. The stream is copied internally, so the caller may close it after construction. |
| load_options | `LoadOptions` | Options that control how the document is loaded. Specify `LoadOptions.password` for encrypted files or a `FileFormat` to override automatic detection. May be `None`. |

| Raises | Description |
| :- | :- |
| `ValueError` | If `source_stream` is `None`. |
| `NotImplementedError` | If the file format cannot be detected or is not supported. |

### See Also
* class [`MarkdownConverter`](/markdown/python-net/groupdocs.markdown/markdownconverter/)
