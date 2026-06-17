---
title: add_image_to_document method
second_title: GroupDocs.Annotation for Python via .NET API References
description: 
type: docs
url: /python-net/groupdocs.annotation/document/add_image_to_document/
is_root: false
weight: 1010
---


## add_image_to_document {#data_dir-jpg_file_name-page_number-image_quality}

Change image quality and add image to document.

```python
def add_image_to_document(self, data_dir, jpg_file_name, page_number, image_quality):
    ...
```

| Parameter | Type | Description |
| :- | :- | :- |
| data_dir | `str` | Specify the path to the input PDF file. |
| jpg_file_name | `str` | The path to the JPG file. |
| page_number | `int` | Page where the image will be inserted. |
| image_quality | `int` | Set image quality from 1 to 100, 1 is the smallest resolution, 100 is the largest. |

### See Also
* class [`Document`](/annotation/python-net/groupdocs.annotation/document/)
