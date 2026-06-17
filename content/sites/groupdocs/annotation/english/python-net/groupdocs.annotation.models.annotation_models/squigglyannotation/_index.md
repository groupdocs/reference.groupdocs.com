---
title: SquigglyAnnotation class
second_title: GroupDocs.Annotation for Python via .NET API References
description: 
type: docs
url: /python-net/groupdocs.annotation.models.annotation_models/squigglyannotation/
is_root: false
weight: 140
---


## SquigglyAnnotation class

Represents squiggly annotation properties.

Learn more

- More about annotation types and annotating PDF and Microsoft Word documents, Excel spreadsheets and PowerPoint Presentations: https://docs.groupdocs.com/display/annotationnet/Add+annotation+to+the+document
- More about adding squiggly annotations to documents of various types: https://docs.groupdocs.com/annotation/net/add-squiggly-annotation/

The SquigglyAnnotation type exposes the following members:

### Constructors
| Constructor | Description |
| :- | :- |
| [__init__](/annotation/python-net/groupdocs.annotation.models.annotation_models/squigglyannotation/__init__/) | Initializes a new instance of [`SquigglyAnnotation`](/annotation/python-net/groupdocs.annotation.models.annotation_models/squigglyannotation/). |

### Methods
| Method | Description |
| :- | :- |
| [clone](/annotation/python-net/groupdocs.annotation.models.annotation_models/squigglyannotation/clone/) | Returns a new instance with the same values. |
| [equals](/annotation/python-net/groupdocs.annotation.models.annotation_models/squigglyannotation/equals/#other) | Compares this squiggly annotation with another [`SquigglyAnnotation`](/annotation/python-net/groupdocs.annotation.models.annotation_models/squigglyannotation/) using the IEquatable Equals method. |
| [equals](/annotation/python-net/groupdocs.annotation.models.annotation_models/squigglyannotation/equals/#obj) | Compares the squiggly annotation with another object using the standard object Equals method. |
| [equals_object](/annotation/python-net/groupdocs.annotation.models.annotation_models/squigglyannotation/equals_object/) |  |
| [equals_squiggly_annotation](/annotation/python-net/groupdocs.annotation.models.annotation_models/squigglyannotation/equals_squiggly_annotation/) |  |
| [get_hash_code](/annotation/python-net/groupdocs.annotation.models.annotation_models/squigglyannotation/get_hash_code/) | Returns the hash code of the squiggly annotation. |
| [equals_annotation_base](/annotation/python-net/groupdocs.annotation.models.annotation_models/annotationbase/equals_annotation_base/) |  (inherited from [`AnnotationBase`](/annotation/python-net/groupdocs.annotation.models.annotation_models/annotationbase/)) |

### Properties
| Property | Description |
| :- | :- |
| [background_color](/annotation/python-net/groupdocs.annotation.models.annotation_models/squigglyannotation/background_color/) | The background color of the squiggly annotation text. |
| [font_color](/annotation/python-net/groupdocs.annotation.models.annotation_models/squigglyannotation/font_color/) | The font color of the squiggly annotation text. |
| [opacity](/annotation/python-net/groupdocs.annotation.models.annotation_models/squigglyannotation/opacity/) | The opacity of the squiggly annotation. |
| [points](/annotation/python-net/groupdocs.annotation.models.annotation_models/squigglyannotation/points/) | The collection of points that describe rectangles with text. |
| [squiggly_color](/annotation/python-net/groupdocs.annotation.models.annotation_models/squigglyannotation/squiggly_color/) | The color of the squiggly annotation. |
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
from groupdocs.annotation.models.annotation_models import SquigglyAnnotation
from groupdocs.pydrawing import Color


def add_squiggly_annotation():
    with Annotator("./sample.pdf") as annotator:
        squiggly = SquigglyAnnotation()
        squiggly.points = [
            Point(80, 600), Point(300, 600),
            Point(80, 575), Point(300, 575),
        ]
        squiggly.squiggly_color = Color.red.to_argb()
        squiggly.opacity = 0.9
        squiggly.page_number = 0
        squiggly.message = "This is a squiggly annotation"
        annotator.add(squiggly)
        annotator.save("./output.pdf")


if __name__ == "__main__":
    add_squiggly_annotation()
```

### Guides
Task guides that use `SquigglyAnnotation`:

* [AI agents and LLM integration](/annotation/python-net/guides/agents-and-llm-integration/)
* [Add annotations](/annotation/python-net/guides/add-annotations/)

### See Also
* module [`groupdocs.annotation.models.annotation_models`](/annotation/python-net/groupdocs.annotation.models.annotation_models/)
