---
title: StrikeoutAnnotation class
second_title: GroupDocs.Annotation for Python via .NET API References
description: 
type: docs
url: /python-net/groupdocs.annotation.models.annotation_models/strikeoutannotation/
is_root: false
weight: 150
---


## StrikeoutAnnotation class

Represents strikeout annotation properties.

Learn more

- More about annotation types and annotating PDF and Microsoft Word documents, Excel spreadsheets and PowerPoint Presentations: https://docs.groupdocs.com/display/annotationnet/Add+annotation+to+the+document
- More about adding strikeout annotations to documents of various types: https://docs.groupdocs.com/display/annotationnet/Add+strikeout+annotation

The StrikeoutAnnotation type exposes the following members:

### Constructors
| Constructor | Description |
| :- | :- |
| [__init__](/annotation/python-net/groupdocs.annotation.models.annotation_models/strikeoutannotation/__init__/) | Initializes a new instance of [`StrikeoutAnnotation`](/annotation/python-net/groupdocs.annotation.models.annotation_models/strikeoutannotation/) class. |

### Methods
| Method | Description |
| :- | :- |
| [clone](/annotation/python-net/groupdocs.annotation.models.annotation_models/strikeoutannotation/clone/) | Returns a new instance with the same values. |
| [equals](/annotation/python-net/groupdocs.annotation.models.annotation_models/strikeoutannotation/equals/#other) | Compares the strikeout annotation with another using the IEquatable Equals method. |
| [equals](/annotation/python-net/groupdocs.annotation.models.annotation_models/strikeoutannotation/equals/#obj) | Compares strikeout annotation using standard object Equals method. |
| [equals_object](/annotation/python-net/groupdocs.annotation.models.annotation_models/strikeoutannotation/equals_object/) |  |
| [equals_strikeout_annotation](/annotation/python-net/groupdocs.annotation.models.annotation_models/strikeoutannotation/equals_strikeout_annotation/) |  |
| [get_hash_code](/annotation/python-net/groupdocs.annotation.models.annotation_models/strikeoutannotation/get_hash_code/) | Returns the hash code of the strikeout annotation. |
| [equals_annotation_base](/annotation/python-net/groupdocs.annotation.models.annotation_models/annotationbase/equals_annotation_base/) |  (inherited from [`AnnotationBase`](/annotation/python-net/groupdocs.annotation.models.annotation_models/annotationbase/)) |

### Properties
| Property | Description |
| :- | :- |
| [background_color](/annotation/python-net/groupdocs.annotation.models.annotation_models/strikeoutannotation/background_color/) | The background color of the strikeout annotation text. |
| [font_color](/annotation/python-net/groupdocs.annotation.models.annotation_models/strikeoutannotation/font_color/) | The font color of the strikeout annotation text. |
| [opacity](/annotation/python-net/groupdocs.annotation.models.annotation_models/strikeoutannotation/opacity/) | The opacity of the strikeout annotation. |
| [points](/annotation/python-net/groupdocs.annotation.models.annotation_models/strikeoutannotation/points/) | The collection of points that describe rectangles with text. |
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
from groupdocs.annotation.models.annotation_models import StrikeoutAnnotation
from groupdocs.pydrawing import Color

def add_strikeout_annotation():
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

### Guides
Task guides that use `StrikeoutAnnotation`:

* [AI agents and LLM integration](/annotation/python-net/guides/agents-and-llm-integration/)
* [Add annotations](/annotation/python-net/guides/add-annotations/)

### See Also
* module [`groupdocs.annotation.models.annotation_models`](/annotation/python-net/groupdocs.annotation.models.annotation_models/)
