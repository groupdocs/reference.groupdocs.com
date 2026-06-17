---
title: AreaAnnotation class
second_title: GroupDocs.Annotation for Python via .NET API References
description: 
type: docs
url: /python-net/groupdocs.annotation.models.annotation_models/areaannotation/
is_root: false
weight: 20
---


## AreaAnnotation class

Represents area annotation properties.

Learn more

- More about annotation types and annotating PDF and Microsoft Word documents, Excel spreadsheets and PowerPoint Presentations: https://docs.groupdocs.com/display/annotationnet/Add+annotation+to+the+document
- More about adding area annotations to documents of various types: https://docs.groupdocs.com/display/annotationnet/Add+area+annotation

The AreaAnnotation type exposes the following members:

### Constructors
| Constructor | Description |
| :- | :- |
| [__init__](/annotation/python-net/groupdocs.annotation.models.annotation_models/areaannotation/__init__/) | Initializes new instance of [`AreaAnnotation`](/annotation/python-net/groupdocs.annotation.models.annotation_models/areaannotation/) class. |

### Methods
| Method | Description |
| :- | :- |
| [clone](/annotation/python-net/groupdocs.annotation.models.annotation_models/areaannotation/clone/) | Returns a new instance of the area annotation with the same values. |
| [equals](/annotation/python-net/groupdocs.annotation.models.annotation_models/areaannotation/equals/#other) | Compares area annotation using the IEquatable `Equals` method. |
| [equals](/annotation/python-net/groupdocs.annotation.models.annotation_models/areaannotation/equals/#obj) | Compares area annotation using the standard object Equals method. |
| [equals_area_annotation](/annotation/python-net/groupdocs.annotation.models.annotation_models/areaannotation/equals_area_annotation/) |  |
| [equals_object](/annotation/python-net/groupdocs.annotation.models.annotation_models/areaannotation/equals_object/) |  |
| [get_hash_code](/annotation/python-net/groupdocs.annotation.models.annotation_models/areaannotation/get_hash_code/) | Returns the hash code of the AreaAnnotation instance. |
| [equals_annotation_base](/annotation/python-net/groupdocs.annotation.models.annotation_models/annotationbase/equals_annotation_base/) |  (inherited from [`AnnotationBase`](/annotation/python-net/groupdocs.annotation.models.annotation_models/annotationbase/)) |

### Properties
| Property | Description |
| :- | :- |
| [background_color](/annotation/python-net/groupdocs.annotation.models.annotation_models/areaannotation/background_color/) | The background color of the area annotation. |
| [box](/annotation/python-net/groupdocs.annotation.models.annotation_models/areaannotation/box/) | The area annotation position. |
| [opacity](/annotation/python-net/groupdocs.annotation.models.annotation_models/areaannotation/opacity/) | The opacity of the area annotation. |
| [pen_color](/annotation/python-net/groupdocs.annotation.models.annotation_models/areaannotation/pen_color/) | The pen color of the area annotation. |
| [pen_style](/annotation/python-net/groupdocs.annotation.models.annotation_models/areaannotation/pen_style/) | The pen style of the area annotation. |
| [pen_width](/annotation/python-net/groupdocs.annotation.models.annotation_models/areaannotation/pen_width/) | The pen width of the area annotation. |
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
from groupdocs.annotation.models import Rectangle
from groupdocs.annotation.models.annotation_models import AreaAnnotation
from groupdocs.pydrawing import Color

area = AreaAnnotation()
area.box = Rectangle(100, 100, 200, 80)
area.background_color = Color.yellow.to_argb()
area.pen_color = Color.red.to_argb()
area.opacity = 0.7
area.page_number = 0
area.message = "Flagged region"

with Annotator("document.pdf") as annotator:
    annotator.add(area)
    annotator.save("annotated.pdf")
```

### Guides
Task guides that use `AreaAnnotation`:

* [AI agents and LLM integration](/annotation/python-net/guides/agents-and-llm-integration/)
* [Loading documents](/annotation/python-net/guides/loading-documents/)
* [Saving documents](/annotation/python-net/guides/saving-documents/)
* [Add annotations](/annotation/python-net/guides/add-annotations/)
* [Comments and replies](/annotation/python-net/guides/comments-and-replies/)
* [Hello, World!](/annotation/python-net/guides/hello-world/)
* [GroupDocs.Annotation for Python via .NET Overview](/annotation/python-net/guides/product-overview/)

### See Also
* module [`groupdocs.annotation.models.annotation_models`](/annotation/python-net/groupdocs.annotation.models.annotation_models/)
