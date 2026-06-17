---
title: FileType class
second_title: GroupDocs.Annotation for Python via .NET API References
description: 
type: docs
url: /python-net/groupdocs.annotation/filetype/
is_root: false
weight: 70
---


## FileType class

Information about file, such as type, extension, etc.

The FileType type exposes the following members:

### Methods
| Method | Description |
| :- | :- |
| [equals](/annotation/python-net/groupdocs.annotation/filetype/equals/#other) | File type equivalence check. |
| [equals](/annotation/python-net/groupdocs.annotation/filetype/equals/#obj) | Equivalence check with object. |
| [equals_file_type](/annotation/python-net/groupdocs.annotation/filetype/equals_file_type/) |  |
| [equals_object](/annotation/python-net/groupdocs.annotation/filetype/equals_object/) |  |
| [from_file_name_or_extension](/annotation/python-net/groupdocs.annotation/filetype/from_file_name_or_extension/#file_name_or_extension) | Return FileType based on file name or extension. |
| [get_hash_code](/annotation/python-net/groupdocs.annotation/filetype/get_hash_code/) | Get hash code. |
| [get_supported_file_types](/annotation/python-net/groupdocs.annotation/filetype/get_supported_file_types/) | Get supported file types enumeration. |
| [to_string](/annotation/python-net/groupdocs.annotation/filetype/to_string/) | Returns a string that represents the file type. |

### Properties
| Property | Description |
| :- | :- |
| [extension](/annotation/python-net/groupdocs.annotation/filetype/extension/) | The file extension. |
| [file_format](/annotation/python-net/groupdocs.annotation/filetype/file_format/) | The file format. |

### Example

```python
from groupdocs.annotation import FileType

# Retrieve a list of all supported file types
supported = FileType.get_supported_file_types()
print(supported)
```

### See Also
* module [`groupdocs.annotation`](/annotation/python-net/groupdocs.annotation/)
