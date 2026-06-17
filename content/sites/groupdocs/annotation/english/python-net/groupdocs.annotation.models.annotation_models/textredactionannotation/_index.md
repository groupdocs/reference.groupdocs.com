---
title: TextRedactionAnnotation class
second_title: GroupDocs.Annotation for Python via .NET API References
description: 
type: docs
url: /python-net/groupdocs.annotation.models.annotation_models/textredactionannotation/
is_root: false
weight: 170
---


## TextRedactionAnnotation class

Represents text redaction annotation properties.

Learn more

- More about annotation types and annotating PDF and Microsoft Word documents, Excel spreadsheets and PowerPoint Presentations: https://docs.groupdocs.com/display/annotationnet/Add+annotation+to+the+document
- More about adding text redaction annotations to documents of various types: https://docs.groupdocs.com/display/annotationnet/Add+text+redaction+annotation

The TextRedactionAnnotation type exposes the following members:

### Constructors
| Constructor | Description |
| :- | :- |
| [__init__](/annotation/python-net/groupdocs.annotation.models.annotation_models/textredactionannotation/__init__/) | Initializes a new [`TextRedactionAnnotation`](/annotation/python-net/groupdocs.annotation.models.annotation_models/textredactionannotation/) instance. |

### Methods
| Method | Description |
| :- | :- |
| [clone](/annotation/python-net/groupdocs.annotation.models.annotation_models/textredactionannotation/clone/) | Returns a new instance with the same values. |
| [equals](/annotation/python-net/groupdocs.annotation.models.annotation_models/textredactionannotation/equals/#other) | Compares this text redaction annotation with another using the IEquatable Equals method. |
| [equals](/annotation/python-net/groupdocs.annotation.models.annotation_models/textredactionannotation/equals/#obj) | Compares text redaction annotation using standard object Equals method. |
| [equals_object](/annotation/python-net/groupdocs.annotation.models.annotation_models/textredactionannotation/equals_object/) |  |
| [equals_text_redaction_annotation](/annotation/python-net/groupdocs.annotation.models.annotation_models/textredactionannotation/equals_text_redaction_annotation/) |  |
| [get_hash_code](/annotation/python-net/groupdocs.annotation.models.annotation_models/textredactionannotation/get_hash_code/) | Returns hash code of the text redaction annotation. |
| [equals_annotation_base](/annotation/python-net/groupdocs.annotation.models.annotation_models/annotationbase/equals_annotation_base/) |  (inherited from [`AnnotationBase`](/annotation/python-net/groupdocs.annotation.models.annotation_models/annotationbase/)) |

### Properties
| Property | Description |
| :- | :- |
| [font_color](/annotation/python-net/groupdocs.annotation.models.annotation_models/textredactionannotation/font_color/) | The text font color of the text redaction annotation. |
| [points](/annotation/python-net/groupdocs.annotation.models.annotation_models/textredactionannotation/points/) | The collection of points that describe rectangles with text. |
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
from groupdocs.annotation.models.annotation_models import TextRedactionAnnotation
from groupdocs.pydrawing import Color


def add_text_redaction_annotation():
    with Annotator("./sample.pdf") as annotator:
        redaction = TextRedactionAnnotation()
        redaction.points = [
            Point(80, 600), Point(300, 600),
            Point(80, 575), Point(300, 575),
        ]
        redaction.font_color = Color.black.to_argb()
        redaction.page_number = 0
        redaction.message = "This is a text redaction annotation"
        annotator.add(redaction)
        annotator.save("./output.pdf")


if __name__ == "__main__":
    add_text_redaction_annotation()
```

### Guides
Task guides that use `TextRedactionAnnotation`:

* [AI agents and LLM integration](/annotation/python-net/guides/agents-and-llm-integration/)
* [Add annotations](/annotation/python-net/guides/add-annotations/)

### See Also
* module [`groupdocs.annotation.models.annotation_models`](/annotation/python-net/groupdocs.annotation.models.annotation_models/)
