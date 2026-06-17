---
title: ArrowAnnotation class
second_title: GroupDocs.Annotation for Python via .NET API References
description: 
type: docs
url: /python-net/groupdocs.annotation.models.annotation_models/arrowannotation/
is_root: false
weight: 30
---


## ArrowAnnotation class

Represents arrow annotation properties.

Learn more

- More about annotation types and annotating PDF and Microsoft Word documents, Excel spreadsheets and PowerPoint Presentations: https://docs.groupdocs.com/display/annotationnet/Add+annotation+to+the+document
- More about adding arrow annotations to documents of various types: https://docs.groupdocs.com/display/annotationnet/Add+arrow+annotation

The ArrowAnnotation type exposes the following members:

### Constructors
| Constructor | Description |
| :- | :- |
| [__init__](/annotation/python-net/groupdocs.annotation.models.annotation_models/arrowannotation/__init__/) | Initializes a new [`ArrowAnnotation`](/annotation/python-net/groupdocs.annotation.models.annotation_models/arrowannotation/) instance. |

### Methods
| Method | Description |
| :- | :- |
| [clone](/annotation/python-net/groupdocs.annotation.models.annotation_models/arrowannotation/clone/) | Returns new instance with same values. |
| [equals](/annotation/python-net/groupdocs.annotation.models.annotation_models/arrowannotation/equals/#other) | Compares area annotation using IEquatable Equals method. |
| [equals](/annotation/python-net/groupdocs.annotation.models.annotation_models/arrowannotation/equals/#obj) | Compares arrow annotation using standard object Equals method. |
| [equals_arrow_annotation](/annotation/python-net/groupdocs.annotation.models.annotation_models/arrowannotation/equals_arrow_annotation/) |  |
| [equals_object](/annotation/python-net/groupdocs.annotation.models.annotation_models/arrowannotation/equals_object/) |  |
| [get_hash_code](/annotation/python-net/groupdocs.annotation.models.annotation_models/arrowannotation/get_hash_code/) | Returns HashCode of the arrow annotation. |
| [equals_annotation_base](/annotation/python-net/groupdocs.annotation.models.annotation_models/annotationbase/equals_annotation_base/) |  (inherited from [`AnnotationBase`](/annotation/python-net/groupdocs.annotation.models.annotation_models/annotationbase/)) |

### Properties
| Property | Description |
| :- | :- |
| [box](/annotation/python-net/groupdocs.annotation.models.annotation_models/arrowannotation/box/) | The arrow annotation position. |
| [opacity](/annotation/python-net/groupdocs.annotation.models.annotation_models/arrowannotation/opacity/) | The opacity of the arrow annotation. |
| [pen_color](/annotation/python-net/groupdocs.annotation.models.annotation_models/arrowannotation/pen_color/) | The arrow annotation pen color. |
| [pen_style](/annotation/python-net/groupdocs.annotation.models.annotation_models/arrowannotation/pen_style/) | The pen style of the arrow annotation. |
| [pen_width](/annotation/python-net/groupdocs.annotation.models.annotation_models/arrowannotation/pen_width/) | The pen width of the arrow annotation. |
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
from groupdocs.annotation.models.annotation_models import ArrowAnnotation
from groupdocs.pydrawing import Color

def add_arrow_annotation():
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

### Guides
Task guides that use `ArrowAnnotation`:

* [AI agents and LLM integration](/annotation/python-net/guides/agents-and-llm-integration/)
* [Add annotations](/annotation/python-net/guides/add-annotations/)

### See Also
* module [`groupdocs.annotation.models.annotation_models`](/annotation/python-net/groupdocs.annotation.models.annotation_models/)
