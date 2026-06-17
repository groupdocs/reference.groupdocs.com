---
title: PolylineAnnotation class
second_title: GroupDocs.Annotation for Python via .NET API References
description: 
type: docs
url: /python-net/groupdocs.annotation.models.annotation_models/polylineannotation/
is_root: false
weight: 100
---


## PolylineAnnotation class

Represents polyline annotation properties.

Learn more:

- More about annotation types and annotating PDF and Microsoft Word documents, Excel spreadsheets and PowerPoint Presentations: https://docs.groupdocs.com/display/annotationnet/Add+annotation+to+the+document
- More about adding polyline annotations to documents of various types: https://docs.groupdocs.com/display/annotationnet/Add+polyline+annotation

The PolylineAnnotation type exposes the following members:

### Constructors
| Constructor | Description |
| :- | :- |
| [__init__](/annotation/python-net/groupdocs.annotation.models.annotation_models/polylineannotation/__init__/) | Initializes a new instance of [`AreaAnnotation`](/annotation/python-net/groupdocs.annotation.models.annotation_models/areaannotation/) class. |

### Methods
| Method | Description |
| :- | :- |
| [clone](/annotation/python-net/groupdocs.annotation.models.annotation_models/polylineannotation/clone/) | Returns new instance with the same values. |
| [equals](/annotation/python-net/groupdocs.annotation.models.annotation_models/polylineannotation/equals/#other) | Compares this polyline annotation with another using the IEquatable Equals method. |
| [equals](/annotation/python-net/groupdocs.annotation.models.annotation_models/polylineannotation/equals/#obj) | Compares polyline annotation using standard object Equals method. |
| [equals_object](/annotation/python-net/groupdocs.annotation.models.annotation_models/polylineannotation/equals_object/) |  |
| [equals_polyline_annotation](/annotation/python-net/groupdocs.annotation.models.annotation_models/polylineannotation/equals_polyline_annotation/) |  |
| [get_hash_code](/annotation/python-net/groupdocs.annotation.models.annotation_models/polylineannotation/get_hash_code/) | Returns hash code of the polyline annotation. |
| [equals_annotation_base](/annotation/python-net/groupdocs.annotation.models.annotation_models/annotationbase/equals_annotation_base/) |  (inherited from [`AnnotationBase`](/annotation/python-net/groupdocs.annotation.models.annotation_models/annotationbase/)) |

### Properties
| Property | Description |
| :- | :- |
| [box](/annotation/python-net/groupdocs.annotation.models.annotation_models/polylineannotation/box/) | The polyline annotation position as a [`Rectangle`](/annotation/python-net/groupdocs.annotation.models/rectangle/). |
| [opacity](/annotation/python-net/groupdocs.annotation.models.annotation_models/polylineannotation/opacity/) | The polyline annotation opacity. |
| [pen_color](/annotation/python-net/groupdocs.annotation.models.annotation_models/polylineannotation/pen_color/) | The pen color of the polyline annotation. |
| [pen_style](/annotation/python-net/groupdocs.annotation.models.annotation_models/polylineannotation/pen_style/) | The pen style of the polyline annotation. |
| [pen_width](/annotation/python-net/groupdocs.annotation.models.annotation_models/polylineannotation/pen_width/) | The polyline annotation pen width. |
| [svg_path](/annotation/python-net/groupdocs.annotation.models.annotation_models/polylineannotation/svg_path/) | The SVG path of the polyline annotation. |
| [created_on](/annotation/python-net/groupdocs.annotation.models.annotation_models/annotationbase/created_on/) | The annotation creation date. (inherited from [`AnnotationBase`](/annotation/python-net/groupdocs.annotation.models.annotation_models/annotationbase/)) |
| [id](/annotation/python-net/groupdocs.annotation.models.annotation_models/annotationbase/id/) | The annotation unique identifier. This field is auto-incremented. (inherited from [`AnnotationBase`](/annotation/python-net/groupdocs.annotation.models.annotation_models/annotationbase/)) |
| [message](/annotation/python-net/groupdocs.annotation.models.annotation_models/annotationbase/message/) | The annotation message. (inherited from [`AnnotationBase`](/annotation/python-net/groupdocs.annotation.models.annotation_models/annotationbase/)) |
| [page_number](/annotation/python-net/groupdocs.annotation.models.annotation_models/annotationbase/page_number/) | The page number where the annotation should be located. (inherited from [`AnnotationBase`](/annotation/python-net/groupdocs.annotation.models.annotation_models/annotationbase/)) |
| [replies](/annotation/python-net/groupdocs.annotation.models.annotation_models/annotationbase/replies/) | The list of replies (comments) attached to the annotation. (inherited from [`AnnotationBase`](/annotation/python-net/groupdocs.annotation.models.annotation_models/annotationbase/)) |
| [state_before_annotation](/annotation/python-net/groupdocs.annotation.models.annotation_models/annotationbase/state_before_annotation/) | The previous state of the text before annotating. (inherited from [`AnnotationBase`](/annotation/python-net/groupdocs.annotation.models.annotation_models/annotationbase/)) |
| [type](/annotation/python-net/groupdocs.annotation.models.annotation_models/annotationbase/type/) | The annotation type. (inherited from [`AnnotationBase`](/annotation/python-net/groupdocs.annotation.models.annotation_models/annotationbase/)) |
| [user](/annotation/python-net/groupdocs.annotation.models.annotation_models/annotationbase/user/) | The annotation author. (inherited from [`AnnotationBase`](/annotation/python-net/groupdocs.annotation.models.annotation_models/annotationbase/)) |

### Example

```python
from groupdocs.annotation import Annotator
from groupdocs.annotation.models import Rectangle, PenStyle
from groupdocs.annotation.models.annotation_models import PolylineAnnotation
from groupdocs.pydrawing import Color


def add_polyline_annotation():
    with Annotator("./sample.pdf") as annotator:
        polyline = PolylineAnnotation()
        polyline.box = Rectangle(100, 100, 200, 100)
        polyline.svg_path = "M 0 0 L 50 50 L 100 0 L 150 50"
        polyline.pen_color = Color.purple.to_argb()
        polyline.pen_width = 2
        polyline.pen_style = PenStyle.SOLID
        polyline.opacity = 0.9
        polyline.page_number = 0
        polyline.message = "This is a polyline annotation"
        annotator.add(polyline)
        annotator.save("./output.pdf")


if __name__ == "__main__":
    add_polyline_annotation()
```

### Guides
Task guides that use `PolylineAnnotation`:

* [AI agents and LLM integration](/annotation/python-net/guides/agents-and-llm-integration/)
* [Add annotations](/annotation/python-net/guides/add-annotations/)

### See Also
* module [`groupdocs.annotation.models.annotation_models`](/annotation/python-net/groupdocs.annotation.models.annotation_models/)
