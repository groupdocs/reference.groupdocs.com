---
title: HighlightAnnotation class
second_title: GroupDocs.Annotation for Python via .NET API References
description: 
type: docs
url: /python-net/groupdocs.annotation.models.annotation_models/highlightannotation/
is_root: false
weight: 60
---


## HighlightAnnotation class

Represents highlight annotation properties.

Learn more
- More about annotation types and annotating PDF and Microsoft Word documents, Excel spreadsheets and PowerPoint Presentations: https://docs.groupdocs.com/display/annotationnet/Add+annotation+to+the+document
- More about adding highlight annotations to documents of various types: https://docs.groupdocs.com/display/annotationnet/Add+highlight+annotation

The HighlightAnnotation type exposes the following members:

### Constructors
| Constructor | Description |
| :- | :- |
| [__init__](/annotation/python-net/groupdocs.annotation.models.annotation_models/highlightannotation/__init__/) | Initializes a new instance of [`HighlightAnnotation`](/annotation/python-net/groupdocs.annotation.models.annotation_models/highlightannotation/). |

### Methods
| Method | Description |
| :- | :- |
| [clone](/annotation/python-net/groupdocs.annotation.models.annotation_models/highlightannotation/clone/) | Returns a new instance with the same values. |
| [equals](/annotation/python-net/groupdocs.annotation.models.annotation_models/highlightannotation/equals/#other) | Compares highlight annotation using IEquatable Equals method. |
| [equals](/annotation/python-net/groupdocs.annotation.models.annotation_models/highlightannotation/equals/#obj) | Compares highlight annotations using the standard object `Equals` method. |
| [equals_highlight_annotation](/annotation/python-net/groupdocs.annotation.models.annotation_models/highlightannotation/equals_highlight_annotation/) |  |
| [equals_object](/annotation/python-net/groupdocs.annotation.models.annotation_models/highlightannotation/equals_object/) |  |
| [get_hash_code](/annotation/python-net/groupdocs.annotation.models.annotation_models/highlightannotation/get_hash_code/) | Returns the hash code of the highlight annotation. |
| [equals_annotation_base](/annotation/python-net/groupdocs.annotation.models.annotation_models/annotationbase/equals_annotation_base/) |  (inherited from [`AnnotationBase`](/annotation/python-net/groupdocs.annotation.models.annotation_models/annotationbase/)) |

### Properties
| Property | Description |
| :- | :- |
| [background_color](/annotation/python-net/groupdocs.annotation.models.annotation_models/highlightannotation/background_color/) | The background color of the highlight annotation as an ARGB integer. |
| [font_color](/annotation/python-net/groupdocs.annotation.models.annotation_models/highlightannotation/font_color/) | The highlight annotation text font color. |
| [opacity](/annotation/python-net/groupdocs.annotation.models.annotation_models/highlightannotation/opacity/) | The opacity of the highlight annotation. |
| [points](/annotation/python-net/groupdocs.annotation.models.annotation_models/highlightannotation/points/) | The collection of [`Point`](/annotation/python-net/groupdocs.annotation.models/point/) objects that describe rectangles with text. |
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
from groupdocs.annotation.models.annotation_models import HighlightAnnotation
from groupdocs.pydrawing import Color


def add_highlight_annotation():
    with Annotator("./sample.pdf") as annotator:
        highlight = HighlightAnnotation()
        # Text-markup annotations are positioned by the corner points of the
        # text region: top-left, top-right, bottom-left, bottom-right
        highlight.points = [
            Point(80, 600), Point(300, 600),
            Point(80, 575), Point(300, 575),
        ]
        highlight.background_color = Color.yellow.to_argb()
        highlight.opacity = 0.7
        highlight.page_number = 0
        highlight.message = "This is a highlight annotation"
        annotator.add(highlight)
        annotator.save("./output.pdf")
```

### Guides
Task guides that use `HighlightAnnotation`:

* [AI agents and LLM integration](/annotation/python-net/guides/agents-and-llm-integration/)
* [Add annotations](/annotation/python-net/guides/add-annotations/)
* [GroupDocs.Annotation for Python via .NET Overview](/annotation/python-net/guides/product-overview/)

### See Also
* module [`groupdocs.annotation.models.annotation_models`](/annotation/python-net/groupdocs.annotation.models.annotation_models/)
