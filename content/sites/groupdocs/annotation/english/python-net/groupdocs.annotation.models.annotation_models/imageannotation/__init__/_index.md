---
title: __init__ constructor
second_title: GroupDocs.Annotation for Python via .NET API References
description: 
type: docs
url: /python-net/groupdocs.annotation.models.annotation_models/imageannotation/__init__/
is_root: false
weight: 10
---


## __init__

Initializes a new ImageAnnotation instance.

```python
def __init__(self):
    ...
```

### Example

```python
from groupdocs.annotation import Annotator
from groupdocs.annotation.models import Rectangle
from groupdocs.annotation.models.annotation_models import ImageAnnotation

def add_image_annotation():
    with Annotator("./sample.pdf") as annotator:
        image = ImageAnnotation()
        image.box = Rectangle(100, 100, 100, 100)
        image.image_path = "./stamp.png"
        image.opacity = 0.9
        image.angle = 0.0
        image.page_number = 0
        image.message = "This is an image annotation"
        annotator.add(image)
        annotator.save("./output.pdf")
```

### See Also
* class [`ImageAnnotation`](/annotation/python-net/groupdocs.annotation.models.annotation_models/imageannotation/)
