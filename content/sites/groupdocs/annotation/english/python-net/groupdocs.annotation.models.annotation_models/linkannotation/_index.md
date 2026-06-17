---
title: LinkAnnotation class
second_title: GroupDocs.Annotation for Python via .NET API References
description: 
type: docs
url: /python-net/groupdocs.annotation.models.annotation_models/linkannotation/
is_root: false
weight: 80
---


## LinkAnnotation class

Represents link annotation properties.

Learn more

- More about annotation types and annotating PDF and Microsoft Word documents, Excel spreadsheets and PowerPoint Presentations: https://docs.groupdocs.com/display/annotationnet/Add+annotation+to+the+document
- More about adding link annotations to documents of various types: https://docs.groupdocs.com/display/annotationnet/Add+link+annotation

The LinkAnnotation type exposes the following members:

### Constructors
| Constructor | Description |
| :- | :- |
| [__init__](/annotation/python-net/groupdocs.annotation.models.annotation_models/linkannotation/__init__/) | Initializes a new instance of [`LinkAnnotation`](/annotation/python-net/groupdocs.annotation.models.annotation_models/linkannotation/). |

### Methods
| Method | Description |
| :- | :- |
| [clone](/annotation/python-net/groupdocs.annotation.models.annotation_models/linkannotation/clone/) | Returns a new instance with the same values. |
| [equals](/annotation/python-net/groupdocs.annotation.models.annotation_models/linkannotation/equals/#other) | Compares this link annotation with another using the IEquatable Equals method. |
| [equals](/annotation/python-net/groupdocs.annotation.models.annotation_models/linkannotation/equals/#obj) | Compares link annotation using standard object Equals method. |
| [equals_link_annotation](/annotation/python-net/groupdocs.annotation.models.annotation_models/linkannotation/equals_link_annotation/) |  |
| [equals_object](/annotation/python-net/groupdocs.annotation.models.annotation_models/linkannotation/equals_object/) |  |
| [get_hash_code](/annotation/python-net/groupdocs.annotation.models.annotation_models/linkannotation/get_hash_code/) | Returns HashCode of link annotation. |
| [equals_annotation_base](/annotation/python-net/groupdocs.annotation.models.annotation_models/annotationbase/equals_annotation_base/) |  (inherited from [`AnnotationBase`](/annotation/python-net/groupdocs.annotation.models.annotation_models/annotationbase/)) |

### Properties
| Property | Description |
| :- | :- |
| [background_color](/annotation/python-net/groupdocs.annotation.models.annotation_models/linkannotation/background_color/) | The background color of the link annotation. |
| [font_color](/annotation/python-net/groupdocs.annotation.models.annotation_models/linkannotation/font_color/) | The text color of the link annotation. |
| [opacity](/annotation/python-net/groupdocs.annotation.models.annotation_models/linkannotation/opacity/) | The opacity of the link annotation. |
| [points](/annotation/python-net/groupdocs.annotation.models.annotation_models/linkannotation/points/) | The link annotation coordinates as a list of points. |
| [url](/annotation/python-net/groupdocs.annotation.models.annotation_models/linkannotation/url/) | The annotation link URL. |
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
from groupdocs.annotation.models.annotation_models import LinkAnnotation
from groupdocs.pydrawing import Color

def add_link_annotation():
    with Annotator("./sample.pdf") as annotator:
        link = LinkAnnotation()
        link.points = [
            Point(80, 600), Point(300, 600),
            Point(80, 575), Point(300, 575),
        ]
        link.url = "https://www.groupdocs.com"
        link.background_color = Color.azure.to_argb()
        link.opacity = 0.7
        link.page_number = 0
        link.message = "This is a link annotation"
        annotator.add(link)
        annotator.save("./output.pdf")
```

### Guides
Task guides that use `LinkAnnotation`:

* [AI agents and LLM integration](/annotation/python-net/guides/agents-and-llm-integration/)
* [Add annotations](/annotation/python-net/guides/add-annotations/)

### See Also
* module [`groupdocs.annotation.models.annotation_models`](/annotation/python-net/groupdocs.annotation.models.annotation_models/)
