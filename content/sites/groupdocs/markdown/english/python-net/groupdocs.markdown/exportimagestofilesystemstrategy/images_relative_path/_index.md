---
title: images_relative_path property
second_title: GroupDocs.Markdown for Python via .NET API References
description: 
type: docs
url: /python-net/groupdocs.markdown/exportimagestofilesystemstrategy/images_relative_path/
is_root: false
weight: 2020
---


## images_relative_path property

The path used in the Markdown image references.

When `None` or empty, the full [`ExportImagesToFileSystemStrategy.images_folder`](/python-net/groupdocs.markdown/exportimagestofilesystemstrategy/images_folder/) path is used (which may be absolute). Set this to a relative path (e.g., `"images"`) so the Markdown output contains portable references. Default is `None` (uses [`ExportImagesToFileSystemStrategy.images_folder`](/python-net/groupdocs.markdown/exportimagestofilesystemstrategy/images_folder/) as‑is).

### Definition:
```python
@property
def images_relative_path(self):
    ...
@images_relative_path.setter
def images_relative_path(self, value):
    ...
```

### See Also
* class [`ExportImagesToFileSystemStrategy`](/python-net/groupdocs.markdown/exportimagestofilesystemstrategy/)
