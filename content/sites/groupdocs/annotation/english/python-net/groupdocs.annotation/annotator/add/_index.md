---
title: add method
second_title: GroupDocs.Annotation for Python via .NET API References
description: 
type: docs
url: /python-net/groupdocs.annotation/annotator/add/
is_root: false
weight: 1010
---


## add {#annotation}

Adds annotation to document.

Learn more

- More about how to add annotation to document: How to annotate document in C# (https://docs.groupdocs.com/display/annotationnet/Add+annotation+to+the+document)

```python
def add(self, annotation):
    ...
```

| Parameter | Type | Description |
| :- | :- | :- |
| annotation | `AnnotationBase` | The annotation to add. |

**Returns:** None.

### Example

```python
from groupdocs.annotation import Annotator
from groupdocs.annotation.models import Rectangle
from groupdocs.annotation.models.annotation_models import PointAnnotation

with Annotator("./sample.pdf") as annotator:
    point = PointAnnotation()
    point.box = Rectangle(100, 100, 0, 0)
    point.page_number = 0
    point.message = "This is a point annotation"
    annotator.add(point)
    annotator.save("./output.pdf")
```

## add {#annotations}

Adds a collection of annotations to a document.

Learn more

- More about how to add annotation to document: [How to annotate document in C#](https://docs.groupdocs.com/display/annotationnet/Add+annotation+to+the+document)

```python
def add(self, annotations):
    ...
```

| Parameter | Type | Description |
| :- | :- | :- |
| annotations | `List[AnnotationBase]` | The annotations list to add. |

**Returns:** None.

### Example

```python
from groupdocs.annotation import Annotator
from groupdocs.annotation.models import Rectangle
from groupdocs.annotation.models.annotation_models import PointAnnotation

def add_point_annotation():
    with Annotator("./sample.pdf") as annotator:
        point = PointAnnotation()
        point.box = Rectangle(100, 100, 0, 0)   # a point is positioned by its box origin
        point.page_number = 0
        point.message = "This is a point annotation"
        annotator.add([point])
        annotator.save("./output.pdf")
```

### See Also
* class [`Annotator`](/annotation/python-net/groupdocs.annotation/annotator/)
