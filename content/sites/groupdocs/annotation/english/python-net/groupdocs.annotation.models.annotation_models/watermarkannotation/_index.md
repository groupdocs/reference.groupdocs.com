---
title: WatermarkAnnotation class
second_title: GroupDocs.Annotation for Python via .NET API References
description: 
type: docs
url: /python-net/groupdocs.annotation.models.annotation_models/watermarkannotation/
is_root: false
weight: 190
---


## WatermarkAnnotation class

Represents watermark annotation properties.

- More about annotation types and annotating PDF and Microsoft Word documents, Excel spreadsheets and PowerPoint Presentations: https://docs.groupdocs.com/display/annotationnet/Add+annotation+to+the+document
- More about adding watermark annotations to documents of various types: https://docs.groupdocs.com/display/annotationnet/Add+watermark+annotation

The WatermarkAnnotation type exposes the following members:

### Constructors
| Constructor | Description |
| :- | :- |
| [__init__](/annotation/python-net/groupdocs.annotation.models.annotation_models/watermarkannotation/__init__/) | Initializes new instance of WatermarkAnnotation class. |

### Methods
| Method | Description |
| :- | :- |
| [clone](/annotation/python-net/groupdocs.annotation.models.annotation_models/watermarkannotation/clone/) | Returns a new instance with the same values. |
| [equals](/annotation/python-net/groupdocs.annotation.models.annotation_models/watermarkannotation/equals/#other) | Compares watermark annotation using IEquatable Equals method. |
| [equals](/annotation/python-net/groupdocs.annotation.models.annotation_models/watermarkannotation/equals/#obj) | Compares watermark annotation using the standard object Equals method. |
| [equals_object](/annotation/python-net/groupdocs.annotation.models.annotation_models/watermarkannotation/equals_object/) |  |
| [equals_watermark_annotation](/annotation/python-net/groupdocs.annotation.models.annotation_models/watermarkannotation/equals_watermark_annotation/) |  |
| [get_hash_code](/annotation/python-net/groupdocs.annotation.models.annotation_models/watermarkannotation/get_hash_code/) | Returns the hash code of the watermark annotation. |
| [equals_annotation_base](/annotation/python-net/groupdocs.annotation.models.annotation_models/annotationbase/equals_annotation_base/) |  (inherited from [`AnnotationBase`](/annotation/python-net/groupdocs.annotation.models.annotation_models/annotationbase/)) |

### Properties
| Property | Description |
| :- | :- |
| [angle](/annotation/python-net/groupdocs.annotation.models.annotation_models/watermarkannotation/angle/) | The rotation angle of the watermark annotation. |
| [auto_scale](/annotation/python-net/groupdocs.annotation.models.annotation_models/watermarkannotation/auto_scale/) | The auto scale setting for the watermark annotation. |
| [box](/annotation/python-net/groupdocs.annotation.models.annotation_models/watermarkannotation/box/) | The watermark annotation position. |
| [font_color](/annotation/python-net/groupdocs.annotation.models.annotation_models/watermarkannotation/font_color/) | The watermark annotation text color. |
| [font_family](/annotation/python-net/groupdocs.annotation.models.annotation_models/watermarkannotation/font_family/) | The font family of the watermark annotation text. |
| [font_size](/annotation/python-net/groupdocs.annotation.models.annotation_models/watermarkannotation/font_size/) | The watermark annotation text size. |
| [horizontal_alignment](/annotation/python-net/groupdocs.annotation.models.annotation_models/watermarkannotation/horizontal_alignment/) | The watermark horizontal alignment on the document. |
| [opacity](/annotation/python-net/groupdocs.annotation.models.annotation_models/watermarkannotation/opacity/) | The opacity of the watermark annotation. |
| [text](/annotation/python-net/groupdocs.annotation.models.annotation_models/watermarkannotation/text/) | The watermark text. |
| [vertical_alignment](/annotation/python-net/groupdocs.annotation.models.annotation_models/watermarkannotation/vertical_alignment/) | The vertical alignment of the watermark on the document. |
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
from groupdocs.annotation.models import Rectangle, HorizontalAlignment, VerticalAlignment
from groupdocs.annotation.models.annotation_models import WatermarkAnnotation
from groupdocs.pydrawing import Color

def add_watermark_annotation():
    with Annotator("./sample.pdf") as annotator:
        watermark = WatermarkAnnotation()
        watermark.box = Rectangle(100, 100, 200, 100)
        watermark.text = "Watermark"
        watermark.font_family = "Arial"
        watermark.font_size = 24.0
        watermark.font_color = Color.red.to_argb()
        watermark.angle = 45.0
        watermark.auto_scale = True
        watermark.horizontal_alignment = HorizontalAlignment.CENTER
        watermark.vertical_alignment = VerticalAlignment.CENTER
        watermark.opacity = 0.5
        watermark.page_number = 0
        watermark.message = "This is a watermark annotation"
        annotator.add(watermark)
        annotator.save("./output.pdf")
```

### Guides
Task guides that use `WatermarkAnnotation`:

* [AI agents and LLM integration](/annotation/python-net/guides/agents-and-llm-integration/)
* [Add annotations](/annotation/python-net/guides/add-annotations/)

### See Also
* module [`groupdocs.annotation.models.annotation_models`](/annotation/python-net/groupdocs.annotation.models.annotation_models/)
