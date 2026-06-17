---
title: __init__ constructor
second_title: GroupDocs.Annotation for Python via .NET API References
description: 
type: docs
url: /python-net/groupdocs.annotation.models.annotation_models/pointannotation/__init__/
is_root: false
weight: 10
---


## __init__

Initializes a new PointAnnotation instance.

```python
def __init__(self):
    ...
```

### Example

```python
from groupdocs.annotation import Annotator
from groupdocs.annotation.models import Rectangle
from groupdocs.annotation.models.annotation_models import PointAnnotation

with Annotator("./sample.pdf") as annotator:
    point = PointAnnotation()
    point.box = Rectangle(100, 100, 0, 0)   # positioned by box origin
    point.page_number = 0
    point.message = "This is a point annotation"
    annotator.add(point)
    annotator.save("./output.pdf")
```

### See Also
* class [`PointAnnotation`](/annotation/python-net/groupdocs.annotation.models.annotation_models/pointannotation/)
