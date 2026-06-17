---
title: __init__ constructor
second_title: GroupDocs.Annotation for Python via .NET API References
description: 
type: docs
url: /python-net/groupdocs.annotation.models.annotation_models/strikeoutannotation/__init__/
is_root: false
weight: 10
---


## __init__

Initializes a new instance of [`StrikeoutAnnotation`](/annotation/python-net/groupdocs.annotation.models.annotation_models/strikeoutannotation/) class.

```python
def __init__(self):
    ...
```

### Example

```python
from groupdocs.annotation import Annotator
from groupdocs.annotation.models import Point
from groupdocs.annotation.models.annotation_models import StrikeoutAnnotation
from groupdocs.pydrawing import Color

with Annotator("./sample.pdf") as annotator:
    strikeout = StrikeoutAnnotation()
    strikeout.points = [
        Point(80, 600), Point(300, 600),
        Point(80, 575), Point(300, 575),
    ]
    strikeout.font_color = Color.red.to_argb()
    strikeout.opacity = 0.9
    strikeout.page_number = 0
    strikeout.message = "This is a strikeout annotation"
    annotator.add(strikeout)
    annotator.save("./output.pdf")
```

### See Also
* class [`StrikeoutAnnotation`](/annotation/python-net/groupdocs.annotation.models.annotation_models/strikeoutannotation/)
