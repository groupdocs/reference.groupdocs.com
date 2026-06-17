---
title: UnderlineAnnotation class
second_title: GroupDocs.Annotation for Python via .NET API References
description: 
type: docs
url: /python-net/groupdocs.annotation.models.annotation_models/underlineannotation/
is_root: false
weight: 180
---


## UnderlineAnnotation class

Represents underline annotation properties.

Learn more

- More about annotation types and annotating PDF and Microsoft Word documents, Excel spreadsheets and PowerPoint Presentations: https://docs.groupdocs.com/display/annotationnet/Add+annotation+to+the+document
- More about adding underline annotations to documents of various types: https://docs.groupdocs.com/display/annotationnet/Add+underline+annotation

The UnderlineAnnotation type exposes the following members:

### Constructors
| Constructor | Description |
| :- | :- |
| [__init__](/annotation/python-net/groupdocs.annotation.models.annotation_models/underlineannotation/__init__/) | Initializes a new [`UnderlineAnnotation`](/annotation/python-net/groupdocs.annotation.models.annotation_models/underlineannotation/) instance. |

### Methods
| Method | Description |
| :- | :- |
| [clone](/annotation/python-net/groupdocs.annotation.models.annotation_models/underlineannotation/clone/) | Returns new instance with the same values. |
| [equals](/annotation/python-net/groupdocs.annotation.models.annotation_models/underlineannotation/equals/#other) | Compares this underline annotation with another underline annotation. |
| [equals](/annotation/python-net/groupdocs.annotation.models.annotation_models/underlineannotation/equals/#obj) | Compares underline annotation using the standard object Equals method. |
| [equals_object](/annotation/python-net/groupdocs.annotation.models.annotation_models/underlineannotation/equals_object/) |  |
| [equals_underline_annotation](/annotation/python-net/groupdocs.annotation.models.annotation_models/underlineannotation/equals_underline_annotation/) |  |
| [get_hash_code](/annotation/python-net/groupdocs.annotation.models.annotation_models/underlineannotation/get_hash_code/) | Returns HashCode of the underline annotation. |
| [equals_annotation_base](/annotation/python-net/groupdocs.annotation.models.annotation_models/annotationbase/equals_annotation_base/) |  (inherited from [`AnnotationBase`](/annotation/python-net/groupdocs.annotation.models.annotation_models/annotationbase/)) |

### Properties
| Property | Description |
| :- | :- |
| [background_color](/annotation/python-net/groupdocs.annotation.models.annotation_models/underlineannotation/background_color/) | The underline annotation text background color. |
| [font_color](/annotation/python-net/groupdocs.annotation.models.annotation_models/underlineannotation/font_color/) | The text color of the underline annotation. |
| [opacity](/annotation/python-net/groupdocs.annotation.models.annotation_models/underlineannotation/opacity/) | The underline annotation opacity. |
| [points](/annotation/python-net/groupdocs.annotation.models.annotation_models/underlineannotation/points/) | The collection of points that describe rectangles with text. |
| [underline_color](/annotation/python-net/groupdocs.annotation.models.annotation_models/underlineannotation/underline_color/) | The underline annotation color as an ARGB integer. |
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
from groupdocs.annotation.models import Point
from groupdocs.annotation.models.annotation_models import UnderlineAnnotation
from groupdocs.pydrawing import Color


def add_underline_annotation():
    with Annotator("./sample.pdf") as annotator:
        underline = UnderlineAnnotation()
        underline.points = [
            Point(80, 600), Point(300, 600),
            Point(80, 575), Point(300, 575),
        ]
        underline.underline_color = Color.red.to_argb()
        underline.opacity = 0.9
        underline.page_number = 0
        underline.message = "This is an underline annotation"
        annotator.add(underline)
        annotator.save("./output.pdf")
```

### Guides
Task guides that use `UnderlineAnnotation`:

* [AI agents and LLM integration](/annotation/python-net/guides/agents-and-llm-integration/)
* [Add annotations](/annotation/python-net/guides/add-annotations/)

### See Also
* module [`groupdocs.annotation.models.annotation_models`](/annotation/python-net/groupdocs.annotation.models.annotation_models/)
