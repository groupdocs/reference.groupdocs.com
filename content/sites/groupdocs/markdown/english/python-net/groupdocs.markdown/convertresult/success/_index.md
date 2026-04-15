---
title: success method
second_title: GroupDocs.Markdown for Python via .NET API References
description: 
type: docs
url: /markdown/python-net/groupdocs.markdown/convertresult/success/
is_root: false
weight: 1020
---


## success

Creates a successful result without content. Used when the output was written to a stream or file.

```python
def success(cls):
    ...
```

**Returns:** ConvertResult: A result with `IsSuccess` set to `True` and `Content` set to `None`.

## success {#content}

Creates a successful result containing the converted Markdown content.

```python
def success(cls, content):
    ...
```

| Parameter | Type | Description |
| :- | :- | :- |
| content | `str` | The Markdown content produced by the conversion. |

**Returns:** ConvertResult: A result with `IsSuccess` set to True and the specified content.

### See Also
* class [`ConvertResult`](/markdown/python-net/groupdocs.markdown/convertresult/)
