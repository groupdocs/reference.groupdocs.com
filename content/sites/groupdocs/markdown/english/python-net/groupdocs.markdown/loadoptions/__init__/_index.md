---
title: __init__ constructor
second_title: GroupDocs.Markdown for Python via .NET API References
description: 
type: docs
url: /python-net/groupdocs.markdown/loadoptions/__init__/
is_root: false
weight: 10
---


## __init__

Initializes a new instance of the [`LoadOptions`](/markdown/python-net/groupdocs.markdown/loadoptions/) class with automatic format detection.

```python
def __init__(self):
    ...
```

## __init__ {#file_format}

Initializes a new instance of the [`LoadOptions`](/markdown/python-net/groupdocs.markdown/loadoptions/) class with an explicit file format.

```python
def __init__(self, file_format):
    ...
```

| Parameter | Type | Description |
| :- | :- | :- |
| file_format | `FileFormat` | The file format of the document to load. This bypasses automatic format detection, which is especially useful when loading documents from streams that lack a file extension. |

### See Also
* class [`LoadOptions`](/markdown/python-net/groupdocs.markdown/loadoptions/)
