---
title: ImageAnnotation class
second_title: GroupDocs.Annotation for Python via .NET API References
description: 
type: docs
url: /python-net/groupdocs.annotation.models.annotation_models/imageannotation/
is_root: false
weight: 70
---


## ImageAnnotation class

Represents image annotation properties.

Learn more

- More about annotation types and annotating PDF and Microsoft Word documents, Excel spreadsheets and PowerPoint Presentations: https://docs.groupdocs.com/display/annotationnet/Add+annotation+to+the+document
- More about adding image annotations to documents of various types: https://docs.groupdocs.com/display/annotationnet/Add+image+annotation

The ImageAnnotation type exposes the following members:

### Constructors
| Constructor | Description |
| :- | :- |
| [__init__](/annotation/python-net/groupdocs.annotation.models.annotation_models/imageannotation/__init__/) | Initializes a new ImageAnnotation instance. |

### Methods
| Method | Description |
| :- | :- |
| [clone](/annotation/python-net/groupdocs.annotation.models.annotation_models/imageannotation/clone/) | Returns a new instance with the same values. |
| [equals](/annotation/python-net/groupdocs.annotation.models.annotation_models/imageannotation/equals/#other) | Compares image annotation using IEquatable Equals method. |
| [equals](/annotation/python-net/groupdocs.annotation.models.annotation_models/imageannotation/equals/#obj) | Compares image annotation using standard object Equals method. |
| [equals_image_annotation](/annotation/python-net/groupdocs.annotation.models.annotation_models/imageannotation/equals_image_annotation/) |  |
| [equals_object](/annotation/python-net/groupdocs.annotation.models.annotation_models/imageannotation/equals_object/) |  |
| [get_hash_code](/annotation/python-net/groupdocs.annotation.models.annotation_models/imageannotation/get_hash_code/) | Returns the hash code of the image annotation. |
| [get_image](/annotation/python-net/groupdocs.annotation.models.annotation_models/imageannotation/get_image/) | Gets image object. |
| [equals_annotation_base](/annotation/python-net/groupdocs.annotation.models.annotation_models/annotationbase/equals_annotation_base/) |  (inherited from [`AnnotationBase`](/annotation/python-net/groupdocs.annotation.models.annotation_models/annotationbase/)) |

### Properties
| Property | Description |
| :- | :- |
| [angle](/annotation/python-net/groupdocs.annotation.models.annotation_models/imageannotation/angle/) | The image annotation rotation angle. |
| [box](/annotation/python-net/groupdocs.annotation.models.annotation_models/imageannotation/box/) | The image annotation position. |
| [image_data](/annotation/python-net/groupdocs.annotation.models.annotation_models/imageannotation/image_data/) | The image annotation data. |
| [image_extension](/annotation/python-net/groupdocs.annotation.models.annotation_models/imageannotation/image_extension/) | The image extensions (png, jpg, svg etc). |
| [image_path](/annotation/python-net/groupdocs.annotation.models.annotation_models/imageannotation/image_path/) | The image annotation path. |
| [opacity](/annotation/python-net/groupdocs.annotation.models.annotation_models/imageannotation/opacity/) | The opacity of the image annotation. |
| [zindex](/annotation/python-net/groupdocs.annotation.models.annotation_models/imageannotation/zindex/) | The image annotation z-index. Default value is 0. |
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
from groupdocs.annotation.models.annotation_models import ImageAnnotation


def add_image_annotation():
    with Annotator("./sample.pdf") as annotator:
        image = ImageAnnotation()
        image.box = Rectangle(100, 100, 100, 100)
        image.image_path = "./stamp.png"
        image.opacity = 0.9
        image.angle = 0.0
        image.page_number = 0
        image.message = "This is an image annotation"
        annotator.add(image)
        annotator.save("./output.pdf")


if __name__ == "__main__":
    add_image_annotation()
```

### Guides
Task guides that use `ImageAnnotation`:

* [AI agents and LLM integration](/annotation/python-net/guides/agents-and-llm-integration/)
* [Add annotations](/annotation/python-net/guides/add-annotations/)

### See Also
* module [`groupdocs.annotation.models.annotation_models`](/annotation/python-net/groupdocs.annotation.models.annotation_models/)
