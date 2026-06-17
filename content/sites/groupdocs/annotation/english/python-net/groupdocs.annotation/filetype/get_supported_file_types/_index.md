---
title: get_supported_file_types method
second_title: GroupDocs.Annotation for Python via .NET API References
description: 
type: docs
url: /python-net/groupdocs.annotation/filetype/get_supported_file_types/
is_root: false
weight: 1060
---


## get_supported_file_types

Get supported file types enumeration.

```python
def get_supported_file_types(cls):
    ...
```

**Returns:** Iterable[FileType]: Enumeration of supported file types.

### Example

```python
    from groupdocs.annotation import FileType

    supported_formats = FileType.get_supported_file_types()
    for fmt in supported_formats:
        print(fmt)
    ```

### See Also
* class [`FileType`](/annotation/python-net/groupdocs.annotation/filetype/)
