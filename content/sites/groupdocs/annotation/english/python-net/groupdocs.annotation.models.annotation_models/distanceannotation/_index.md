---
title: DistanceAnnotation class
second_title: GroupDocs.Annotation for Python via .NET API References
description: 
type: docs
url: /python-net/groupdocs.annotation.models.annotation_models/distanceannotation/
is_root: false
weight: 40
---


## DistanceAnnotation class

Represents distance annotation properties.

Learn more:

- More about annotation types and annotating PDF and Microsoft Word documents, Excel spreadsheets and PowerPoint Presentations: [How to annotate documents using GroupDocs.Annotation for .NET](https://docs.groupdocs.com/display/annotationnet/Add+annotation+to+the+document)
- More about adding distance annotations to documents of various types: [How to add distance annotations in C#](https://docs.groupdocs.com/display/annotationnet/Add+distance+annotation)

The DistanceAnnotation type exposes the following members:

### Constructors
| Constructor | Description |
| :- | :- |
| [__init__](/annotation/python-net/groupdocs.annotation.models.annotation_models/distanceannotation/__init__/) | Initializes a new instance of [`DistanceAnnotation`](/annotation/python-net/groupdocs.annotation.models.annotation_models/distanceannotation/). |

### Methods
| Method | Description |
| :- | :- |
| [clone](/annotation/python-net/groupdocs.annotation.models.annotation_models/distanceannotation/clone/) | Returns a new instance with the same values. |
| [equals](/annotation/python-net/groupdocs.annotation.models.annotation_models/distanceannotation/equals/#other) | Compares this distance annotation with another using the IEquatable Equals method. |
| [equals](/annotation/python-net/groupdocs.annotation.models.annotation_models/distanceannotation/equals/#obj) | Compares distance annotation using standard object Equals method. |
| [equals_distance_annotation](/annotation/python-net/groupdocs.annotation.models.annotation_models/distanceannotation/equals_distance_annotation/) |  |
| [equals_object](/annotation/python-net/groupdocs.annotation.models.annotation_models/distanceannotation/equals_object/) |  |
| [get_hash_code](/annotation/python-net/groupdocs.annotation.models.annotation_models/distanceannotation/get_hash_code/) | Returns HashCode of the distance annotation. |
| [equals_annotation_base](/annotation/python-net/groupdocs.annotation.models.annotation_models/annotationbase/equals_annotation_base/) |  (inherited from [`AnnotationBase`](/annotation/python-net/groupdocs.annotation.models.annotation_models/annotationbase/)) |

### Properties
| Property | Description |
| :- | :- |
| [box](/annotation/python-net/groupdocs.annotation.models.annotation_models/distanceannotation/box/) | The distance annotation position. |
| [opacity](/annotation/python-net/groupdocs.annotation.models.annotation_models/distanceannotation/opacity/) | The opacity of the distance annotation. |
| [pen_color](/annotation/python-net/groupdocs.annotation.models.annotation_models/distanceannotation/pen_color/) | The pen color of the distance annotation. |
| [pen_style](/annotation/python-net/groupdocs.annotation.models.annotation_models/distanceannotation/pen_style/) | The pen style of the distance annotation. |
| [pen_width](/annotation/python-net/groupdocs.annotation.models.annotation_models/distanceannotation/pen_width/) | The distance annotation pen width. |
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
from groupdocs.annotation.models.annotation_models import DistanceAnnotation
from groupdocs.pydrawing import Color

def add_distance_annotation():
    with Annotator("./sample.pdf") as annotator:
        distance = DistanceAnnotation()
        distance.box = Rectangle(100, 100, 100, 100)
        distance.pen_color = Color.blue.to_argb()
        distance.pen_width = 2
        distance.pen_style = PenStyle.SOLID
        distance.opacity = 0.7
        distance.page_number = 0
        distance.message = "This is a distance annotation"
        annotator.add(distance)
        annotator.save("./output.pdf")
```

### Guides
Task guides that use `DistanceAnnotation`:

* [AI agents and LLM integration](/annotation/python-net/guides/agents-and-llm-integration/)
* [Add annotations](/annotation/python-net/guides/add-annotations/)

### See Also
* module [`groupdocs.annotation.models.annotation_models`](/annotation/python-net/groupdocs.annotation.models.annotation_models/)
