---
title: ResourcesRedactionAnnotation class
second_title: GroupDocs.Annotation for Python via .NET API References
description: 
type: docs
url: /python-net/groupdocs.annotation.models.annotation_models/resourcesredactionannotation/
is_root: false
weight: 120
---


## ResourcesRedactionAnnotation class

Represents resources redaction annotation properties.

Learn more:

- More about annotation types and annotating PDF and Microsoft Word documents, Excel spreadsheets and PowerPoint Presentations: https://docs.groupdocs.com/display/annotationnet/Add+annotation+to+the+document
- More about adding resource redaction annotations to documents of various types: https://docs.groupdocs.com/display/annotationnet/Add+resource+redaction+annotation

The ResourcesRedactionAnnotation type exposes the following members:

### Constructors
| Constructor | Description |
| :- | :- |
| [__init__](/annotation/python-net/groupdocs.annotation.models.annotation_models/resourcesredactionannotation/__init__/) | Initializes a new [`ResourcesRedactionAnnotation`](/annotation/python-net/groupdocs.annotation.models.annotation_models/resourcesredactionannotation/) instance. |

### Methods
| Method | Description |
| :- | :- |
| [clone](/annotation/python-net/groupdocs.annotation.models.annotation_models/resourcesredactionannotation/clone/) | Returns a new instance with the same values. |
| [equals](/annotation/python-net/groupdocs.annotation.models.annotation_models/resourcesredactionannotation/equals/#other) | Compares resource redaction annotation using IEquatable Equals method. |
| [equals](/annotation/python-net/groupdocs.annotation.models.annotation_models/resourcesredactionannotation/equals/#obj) | Compares resource redaction annotation using standard object Equals method. |
| [equals_object](/annotation/python-net/groupdocs.annotation.models.annotation_models/resourcesredactionannotation/equals_object/) |  |
| [equals_resources_redaction_annotation](/annotation/python-net/groupdocs.annotation.models.annotation_models/resourcesredactionannotation/equals_resources_redaction_annotation/) |  |
| [get_hash_code](/annotation/python-net/groupdocs.annotation.models.annotation_models/resourcesredactionannotation/get_hash_code/) | Returns the hash code of the resource redaction annotation. |
| [equals_annotation_base](/annotation/python-net/groupdocs.annotation.models.annotation_models/annotationbase/equals_annotation_base/) |  (inherited from [`AnnotationBase`](/annotation/python-net/groupdocs.annotation.models.annotation_models/annotationbase/)) |

### Properties
| Property | Description |
| :- | :- |
| [box](/annotation/python-net/groupdocs.annotation.models.annotation_models/resourcesredactionannotation/box/) | The resource redaction annotation position as a [`Rectangle`](/annotation/python-net/groupdocs.annotation.models/rectangle/). |
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
from groupdocs.annotation.models.annotation_models import ResourcesRedactionAnnotation

def add_resources_redaction_annotation():
    with Annotator("./sample.pdf") as annotator:
        redaction = ResourcesRedactionAnnotation()
        redaction.box = Rectangle(100, 100, 200, 80)
        redaction.page_number = 0
        redaction.message = "This is a resources redaction annotation"
        annotator.add(redaction)
        annotator.save("./output.pdf")
```

### Guides
Task guides that use `ResourcesRedactionAnnotation`:

* [AI agents and LLM integration](/annotation/python-net/guides/agents-and-llm-integration/)
* [Add annotations](/annotation/python-net/guides/add-annotations/)

### See Also
* module [`groupdocs.annotation.models.annotation_models`](/annotation/python-net/groupdocs.annotation.models.annotation_models/)
