---
title: __init__ constructor
second_title: GroupDocs.Markdown for Python via .NET API References
description: 
type: docs
url: /python-net/groupdocs.markdown/customimagesstrategy/__init__/
is_root: false
weight: 10
---


## __init__ {#images_folder-handler}

Initializes a new instance of the CustomImagesStrategy class.

```python
def __init__(self, images_folder, handler):
    ...
```

| Parameter | Type | Description |
| :- | :- | :- |
| images_folder | `str` | The folder where images will be exported. |
| handler | `IImageSavingHandler` | The handler that is called for each image during conversion. |

| Raises | Description |
| :- | :- |
| `ValueError` | Thrown when `images_folder` is None. |

### See Also
* class [`CustomImagesStrategy`](/markdown/python-net/groupdocs.markdown/customimagesstrategy/)
