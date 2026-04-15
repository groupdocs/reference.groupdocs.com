---
title: handle method
second_title: GroupDocs.Markdown for Python via .NET API References
description: 
type: docs
url: /markdown/python-net/groupdocs.markdown/iimagesavinghandler/handle/
is_root: false
weight: 1010
---


## handle {#args}

Called once for each image found in the source document during conversion.

```python
def handle(self, args):
    ...
```

| Parameter | Type | Description |
| :- | :- | :- |
| args | `CustomImageSavingArgs` | Provides the default image file name and allows you to override the file name via `CustomImageSavingArgs.set_output_image_file_name` or redirect the output via `CustomImageSavingArgs.set_output_stream`. |

### See Also
* class [`IImageSavingHandler`](/markdown/python-net/groupdocs.markdown/iimagesavinghandler/)
