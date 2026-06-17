---
title: ReplacementAnnotation class
second_title: GroupDocs.Annotation for Python via .NET API References
description: 
type: docs
url: /python-net/groupdocs.annotation.models.annotation_models/replacementannotation/
is_root: false
weight: 110
---


## ReplacementAnnotation class

Represents replacement annotation properties.

Learn more

- More about annotation types and annotating PDF and Microsoft Word documents, Excel spreadsheets and PowerPoint Presentations: https://docs.groupdocs.com/display/annotationnet/Add+annotation+to+the+document
- More about adding replacement annotations to documents of various types: https://docs.groupdocs.com/display/annotationnet/Add+replacement+annotation

The ReplacementAnnotation type exposes the following members:

### Constructors
| Constructor | Description |
| :- | :- |
| [__init__](/annotation/python-net/groupdocs.annotation.models.annotation_models/replacementannotation/__init__/) | Initializes a new instance of [`ReplacementAnnotation`](/annotation/python-net/groupdocs.annotation.models.annotation_models/replacementannotation/). |

### Methods
| Method | Description |
| :- | :- |
| [clone](/annotation/python-net/groupdocs.annotation.models.annotation_models/replacementannotation/clone/) | Returns new instance with the same values. |
| [equals](/annotation/python-net/groupdocs.annotation.models.annotation_models/replacementannotation/equals/#other) | Compares replacement annotation using IEquatable Equals method. |
| [equals](/annotation/python-net/groupdocs.annotation.models.annotation_models/replacementannotation/equals/#obj) | Compares the replacement annotation with another object using the standard object Equals method. |
| [equals_object](/annotation/python-net/groupdocs.annotation.models.annotation_models/replacementannotation/equals_object/) |  |
| [equals_replacement_annotation](/annotation/python-net/groupdocs.annotation.models.annotation_models/replacementannotation/equals_replacement_annotation/) |  |
| [get_hash_code](/annotation/python-net/groupdocs.annotation.models.annotation_models/replacementannotation/get_hash_code/) | Returns the hash code of the replacement annotation. |
| [equals_annotation_base](/annotation/python-net/groupdocs.annotation.models.annotation_models/annotationbase/equals_annotation_base/) |  (inherited from [`AnnotationBase`](/annotation/python-net/groupdocs.annotation.models.annotation_models/annotationbase/)) |

### Properties
| Property | Description |
| :- | :- |
| [background_color](/annotation/python-net/groupdocs.annotation.models.annotation_models/replacementannotation/background_color/) | The background color of the replacement annotation. |
| [font_color](/annotation/python-net/groupdocs.annotation.models.annotation_models/replacementannotation/font_color/) | The replacement annotation text color. |
| [font_size](/annotation/python-net/groupdocs.annotation.models.annotation_models/replacementannotation/font_size/) | The replacement annotation text size. |
| [opacity](/annotation/python-net/groupdocs.annotation.models.annotation_models/replacementannotation/opacity/) | The replacement annotation opacity. |
| [points](/annotation/python-net/groupdocs.annotation.models.annotation_models/replacementannotation/points/) | The collection of points that describe rectangles with text. |
| [text_to_replace](/annotation/python-net/groupdocs.annotation.models.annotation_models/replacementannotation/text_to_replace/) | The text to be replaced. |
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
from groupdocs.annotation.models.annotation_models import ReplacementAnnotation
from groupdocs.pydrawing import Color


def add_replacement_annotation():
    with Annotator("./sample.pdf") as annotator:
        replacement = ReplacementAnnotation()
        replacement.points = [
            Point(80, 600), Point(300, 600),
            Point(80, 575), Point(300, 575),
        ]
        replacement.text_to_replace = "replacement text"
        replacement.font_color = Color.black.to_argb()
        replacement.font_size = 12.0
        replacement.opacity = 0.9
        replacement.page_number = 0
        replacement.message = "This is a text replacement annotation"
        annotator.add(replacement)
        annotator.save("./output.pdf")


if __name__ == "__main__":
    add_replacement_annotation()
```

### Guides
Task guides that use `ReplacementAnnotation`:

* [AI agents and LLM integration](/annotation/python-net/guides/agents-and-llm-integration/)
* [Add annotations](/annotation/python-net/guides/add-annotations/)

### See Also
* module [`groupdocs.annotation.models.annotation_models`](/annotation/python-net/groupdocs.annotation.models.annotation_models/)
