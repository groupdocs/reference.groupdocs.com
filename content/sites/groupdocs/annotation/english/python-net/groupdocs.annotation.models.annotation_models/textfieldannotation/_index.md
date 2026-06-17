---
title: TextFieldAnnotation class
second_title: GroupDocs.Annotation for Python via .NET API References
description: 
type: docs
url: /python-net/groupdocs.annotation.models.annotation_models/textfieldannotation/
is_root: false
weight: 160
---


## TextFieldAnnotation class

Represents text field annotation properties.

Learn more

- More about annotation types and annotating PDF and Microsoft Word documents, Excel spreadsheets and PowerPoint Presentations: [How to annotate documents using GroupDocs.Annotation for .NET](https://docs.groupdocs.com/display/annotationnet/Add+annotation+to+the+document)
- More about adding text field annotations to documents of various types: [How to add text field annotations in C#](https://docs.groupdocs.com/display/annotationnet/Add+text+field+annotation)

The TextFieldAnnotation type exposes the following members:

### Constructors
| Constructor | Description |
| :- | :- |
| [__init__](/annotation/python-net/groupdocs.annotation.models.annotation_models/textfieldannotation/__init__/) | Initializes a new [`TextFieldAnnotation`](/annotation/python-net/groupdocs.annotation.models.annotation_models/textfieldannotation/) instance. |

### Methods
| Method | Description |
| :- | :- |
| [clone](/annotation/python-net/groupdocs.annotation.models.annotation_models/textfieldannotation/clone/) | Returns a new instance with the same values. |
| [equals](/annotation/python-net/groupdocs.annotation.models.annotation_models/textfieldannotation/equals/#other) | Compares this text field annotation with another using the IEquatable Equals method. |
| [equals](/annotation/python-net/groupdocs.annotation.models.annotation_models/textfieldannotation/equals/#obj) | Compares text field annotation using standard object Equals method. |
| [equals_object](/annotation/python-net/groupdocs.annotation.models.annotation_models/textfieldannotation/equals_object/) |  |
| [equals_text_field_annotation](/annotation/python-net/groupdocs.annotation.models.annotation_models/textfieldannotation/equals_text_field_annotation/) |  |
| [get_hash_code](/annotation/python-net/groupdocs.annotation.models.annotation_models/textfieldannotation/get_hash_code/) | Returns HashCode of the text field annotation. |
| [equals_annotation_base](/annotation/python-net/groupdocs.annotation.models.annotation_models/annotationbase/equals_annotation_base/) |  (inherited from [`AnnotationBase`](/annotation/python-net/groupdocs.annotation.models.annotation_models/annotationbase/)) |

### Properties
| Property | Description |
| :- | :- |
| [background_color](/annotation/python-net/groupdocs.annotation.models.annotation_models/textfieldannotation/background_color/) | The background color of the text field annotation. |
| [box](/annotation/python-net/groupdocs.annotation.models.annotation_models/textfieldannotation/box/) | The text field annotation position. |
| [font_color](/annotation/python-net/groupdocs.annotation.models.annotation_models/textfieldannotation/font_color/) | The font color of the text field annotation. |
| [font_family](/annotation/python-net/groupdocs.annotation.models.annotation_models/textfieldannotation/font_family/) | The font family of the text field annotation. |
| [font_size](/annotation/python-net/groupdocs.annotation.models.annotation_models/textfieldannotation/font_size/) | The font size of the text field annotation. |
| [opacity](/annotation/python-net/groupdocs.annotation.models.annotation_models/textfieldannotation/opacity/) | The opacity of the text field annotation. |
| [pen_color](/annotation/python-net/groupdocs.annotation.models.annotation_models/textfieldannotation/pen_color/) | The pen color of the text field annotation. |
| [pen_style](/annotation/python-net/groupdocs.annotation.models.annotation_models/textfieldannotation/pen_style/) | The pen style of the text field annotation. |
| [pen_width](/annotation/python-net/groupdocs.annotation.models.annotation_models/textfieldannotation/pen_width/) | The pen width of the text field annotation. |
| [text](/annotation/python-net/groupdocs.annotation.models.annotation_models/textfieldannotation/text/) | The text of the text field annotation. |
| [text_horizontal_alignment](/annotation/python-net/groupdocs.annotation.models.annotation_models/textfieldannotation/text_horizontal_alignment/) | The horizontal alignment of the text. |
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
from groupdocs.annotation.models import Rectangle, HorizontalAlignment
from groupdocs.annotation.models.annotation_models import TextFieldAnnotation
from groupdocs.pydrawing import Color


def add_text_field_annotation():
    with Annotator("./sample.pdf") as annotator:
        text_field = TextFieldAnnotation()
        text_field.box = Rectangle(100, 100, 150, 50)
        text_field.text = "Some text in a field"
        text_field.font_family = "Arial"
        text_field.font_size = 12.0
        text_field.font_color = Color.black.to_argb()
        text_field.background_color = Color.yellow.to_argb()
        text_field.text_horizontal_alignment = HorizontalAlignment.CENTER
        text_field.opacity = 0.9
        text_field.page_number = 0
        text_field.message = "This is a text field annotation"
        annotator.add(text_field)
        annotator.save("./output.pdf")


if __name__ == "__main__":
    add_text_field_annotation()
```

### Guides
Task guides that use `TextFieldAnnotation`:

* [AI agents and LLM integration](/annotation/python-net/guides/agents-and-llm-integration/)
* [Add annotations](/annotation/python-net/guides/add-annotations/)

### See Also
* module [`groupdocs.annotation.models.annotation_models`](/annotation/python-net/groupdocs.annotation.models.annotation_models/)
