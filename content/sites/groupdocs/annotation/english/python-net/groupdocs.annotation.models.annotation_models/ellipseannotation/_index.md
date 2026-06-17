---
title: EllipseAnnotation class
second_title: GroupDocs.Annotation for Python via .NET API References
description: 
type: docs
url: /python-net/groupdocs.annotation.models.annotation_models/ellipseannotation/
is_root: false
weight: 50
---


## EllipseAnnotation class

Represents ellipse annotation properties.

Learn more

- More about annotation types and annotating PDF and Microsoft Word documents, Excel spreadsheets and PowerPoint Presentations: https://docs.groupdocs.com/display/annotationnet/Add+annotation+to+the+document
- More about adding ellipse annotations to documents of various types: https://docs.groupdocs.com/display/annotationnet/Add+ellipse+annotation

The EllipseAnnotation type exposes the following members:

### Constructors
| Constructor | Description |
| :- | :- |
| [__init__](/annotation/python-net/groupdocs.annotation.models.annotation_models/ellipseannotation/__init__/) | Initializes new instance of [`EllipseAnnotation`](/annotation/python-net/groupdocs.annotation.models.annotation_models/ellipseannotation/) class. |

### Methods
| Method | Description |
| :- | :- |
| [clone](/annotation/python-net/groupdocs.annotation.models.annotation_models/ellipseannotation/clone/) | Returns a new instance with the same values. |
| [equals](/annotation/python-net/groupdocs.annotation.models.annotation_models/ellipseannotation/equals/#other) | Compares this ellipse annotation with another using the IEquatable Equals method. |
| [equals](/annotation/python-net/groupdocs.annotation.models.annotation_models/ellipseannotation/equals/#obj) | Compares the ellipse annotation with another object using the standard object Equals method. |
| [equals_ellipse_annotation](/annotation/python-net/groupdocs.annotation.models.annotation_models/ellipseannotation/equals_ellipse_annotation/) |  |
| [equals_object](/annotation/python-net/groupdocs.annotation.models.annotation_models/ellipseannotation/equals_object/) |  |
| [get_hash_code](/annotation/python-net/groupdocs.annotation.models.annotation_models/ellipseannotation/get_hash_code/) | Returns the hash code of the ellipse annotation. |
| [equals_annotation_base](/annotation/python-net/groupdocs.annotation.models.annotation_models/annotationbase/equals_annotation_base/) |  (inherited from [`AnnotationBase`](/annotation/python-net/groupdocs.annotation.models.annotation_models/annotationbase/)) |

### Properties
| Property | Description |
| :- | :- |
| [background_color](/annotation/python-net/groupdocs.annotation.models.annotation_models/ellipseannotation/background_color/) | The background color of the ellipse annotation. |
| [box](/annotation/python-net/groupdocs.annotation.models.annotation_models/ellipseannotation/box/) | The ellipse annotation position. |
| [opacity](/annotation/python-net/groupdocs.annotation.models.annotation_models/ellipseannotation/opacity/) | The opacity of the annotation. |
| [pen_color](/annotation/python-net/groupdocs.annotation.models.annotation_models/ellipseannotation/pen_color/) | The pen color of the ellipse annotation. |
| [pen_style](/annotation/python-net/groupdocs.annotation.models.annotation_models/ellipseannotation/pen_style/) | The pen style of the ellipse annotation. |
| [pen_width](/annotation/python-net/groupdocs.annotation.models.annotation_models/ellipseannotation/pen_width/) | The pen width of the ellipse annotation. |
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
from groupdocs.annotation.models.annotation_models import EllipseAnnotation
from groupdocs.pydrawing import Color


def add_ellipse_annotation():
    with Annotator("./sample.pdf") as annotator:
        ellipse = EllipseAnnotation()
        ellipse.box = Rectangle(100, 100, 200, 120)
        ellipse.background_color = Color.from_argb(255, 144, 238, 144).to_argb()
        ellipse.pen_color = Color.green.to_argb()
        ellipse.pen_width = 2
        ellipse.pen_style = PenStyle.SOLID
        ellipse.opacity = 0.7
        ellipse.page_number = 0
        ellipse.message = "This is an ellipse annotation"
        annotator.add(ellipse)
        annotator.save("./output.pdf")


if __name__ == "__main__":
    add_ellipse_annotation()
```

### Guides
Task guides that use `EllipseAnnotation`:

* [AI agents and LLM integration](/annotation/python-net/guides/agents-and-llm-integration/)
* [Saving documents](/annotation/python-net/guides/saving-documents/)
* [Add annotations](/annotation/python-net/guides/add-annotations/)

### See Also
* module [`groupdocs.annotation.models.annotation_models`](/annotation/python-net/groupdocs.annotation.models.annotation_models/)
