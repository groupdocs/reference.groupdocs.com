---
title: __init__ constructor
second_title: GroupDocs.Annotation for Python via .NET API References
description: 
type: docs
url: /python-net/groupdocs.annotation.models.annotation_models/arrowannotation/__init__/
is_root: false
weight: 10
---


## __init__

Initializes a new [`ArrowAnnotation`](/annotation/python-net/groupdocs.annotation.models.annotation_models/arrowannotation/) instance.

```python
def __init__(self):
    ...
```

### Example

```python
from groupdocs.annotation import Annotator
from groupdocs.annotation.models import Rectangle, PenStyle
from groupdocs.annotation.models.annotation_models import ArrowAnnotation
from groupdocs.pydrawing import Color

with Annotator("./sample.pdf") as annotator:
    arrow = ArrowAnnotation()
    arrow.box = Rectangle(100, 100, 100, 100)
    arrow.pen_color = Color.blue.to_argb()
    arrow.pen_width = 2
    arrow.pen_style = PenStyle.SOLID
    arrow.opacity = 0.9
    arrow.page_number = 0
    arrow.message = "This is an arrow annotation"
    annotator.add(arrow)
    annotator.save("./output.pdf")
```

### See Also
* class [`ArrowAnnotation`](/annotation/python-net/groupdocs.annotation.models.annotation_models/arrowannotation/)
