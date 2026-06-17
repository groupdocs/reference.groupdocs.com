---
title: __init__ constructor
second_title: GroupDocs.Annotation for Python via .NET API References
description: 
type: docs
url: /python-net/groupdocs.annotation.models.annotation_models/resourcesredactionannotation/__init__/
is_root: false
weight: 10
---


## __init__

Initializes a new [`ResourcesRedactionAnnotation`](/annotation/python-net/groupdocs.annotation.models.annotation_models/resourcesredactionannotation/) instance.

```python
def __init__(self):
    ...
```

### Example

```python
from groupdocs.annotation import Annotator
from groupdocs.annotation.models import Rectangle
from groupdocs.annotation.models.annotation_models import ResourcesRedactionAnnotation

with Annotator("./sample.pdf") as annotator:
    redaction = ResourcesRedactionAnnotation()
    redaction.box = Rectangle(100, 100, 200, 80)
    redaction.page_number = 0
    redaction.message = "This is a resources redaction annotation"
    annotator.add(redaction)
    annotator.save("./output.pdf")
```

### See Also
* class [`ResourcesRedactionAnnotation`](/annotation/python-net/groupdocs.annotation.models.annotation_models/resourcesredactionannotation/)
