---
title: LoadOptions class
second_title: GroupDocs.Annotation for Python via .NET API References
description: 
type: docs
url: /python-net/groupdocs.annotation.options/loadoptions/
is_root: false
weight: 30
---


## LoadOptions class

Allows to specify additional options (such as password) when opening a document to annotate.

The LoadOptions type exposes the following members:

### Constructors
| Constructor | Description |
| :- | :- |
| [__init__](/annotation/python-net/groupdocs.annotation.options/loadoptions/__init__/) |  |

### Properties
| Property | Description |
| :- | :- |
| [font_directories](/annotation/python-net/groupdocs.annotation.options/loadoptions/font_directories/) | The list of font directories to load custom fonts from. |
| [password](/annotation/python-net/groupdocs.annotation.options/loadoptions/password/) | The document password. |
| [version](/annotation/python-net/groupdocs.annotation.options/loadoptions/version/) | The version of the document to load. Default is the latest version. |

### Example

```python
from groupdocs.annotation import Annotator
from groupdocs.annotation.options import LoadOptions
from groupdocs.annotation.models import Rectangle
from groupdocs.annotation.models.annotation_models import AreaAnnotation
from groupdocs.pydrawing import Color


def load_password_protected_document():
    # Provide the password through LoadOptions
    load_options = LoadOptions()
    load_options.password = "secret"

    with Annotator("./protected.docx", load_options=load_options) as annotator:
        area = AreaAnnotation()
        area.box = Rectangle(100, 100, 100, 100)
        area.background_color = Color.yellow.to_argb()
        area.page_number = 0
        area.message = "Annotated a password-protected document"
        annotator.add(area)
        annotator.save("./output.docx")
```

### Guides
Task guides that use `LoadOptions`:

* [AI agents and LLM integration](/annotation/python-net/guides/agents-and-llm-integration/)
* [Loading documents](/annotation/python-net/guides/loading-documents/)

### See Also
* module [`groupdocs.annotation.options`](/annotation/python-net/groupdocs.annotation.options/)
