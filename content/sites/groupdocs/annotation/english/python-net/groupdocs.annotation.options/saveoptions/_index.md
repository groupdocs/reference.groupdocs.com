---
title: SaveOptions class
second_title: GroupDocs.Annotation for Python via .NET API References
description: 
type: docs
url: /python-net/groupdocs.annotation.options/saveoptions/
is_root: false
weight: 70
---


## SaveOptions class

Allows to specify additional options (such as password) when saving an annotated document.

The SaveOptions type exposes the following members:

### Constructors
| Constructor | Description |
| :- | :- |
| [__init__](/annotation/python-net/groupdocs.annotation.options/saveoptions/__init__/) |  |

### Properties
| Property | Description |
| :- | :- |
| [annotation_types](/annotation/python-net/groupdocs.annotation.options/saveoptions/annotation_types/) | The annotations that will be in the resultant document. |
| [first_page](/annotation/python-net/groupdocs.annotation.options/saveoptions/first_page/) | The first page number when saving a page range. |
| [last_page](/annotation/python-net/groupdocs.annotation.options/saveoptions/last_page/) | The last page number when saving a page range. |
| [only_annotated_pages](/annotation/python-net/groupdocs.annotation.options/saveoptions/only_annotated_pages/) | The property indicates whether to save only annotated pages. |
| [version](/annotation/python-net/groupdocs.annotation.options/saveoptions/version/) | The version key that will be used to access the current version. |

### Example

```python
from groupdocs.annotation import Annotator
from groupdocs.annotation.options import SaveOptions, AnnotationType

with Annotator("document.pdf") as annotator:
    options = SaveOptions()
    options.annotation_types = AnnotationType.AREA
    options.first_page = 1
    options.last_page = 2
    annotator.save("filtered.pdf", save_options=options)
```

### Guides
Task guides that use `SaveOptions`:

* [AI agents and LLM integration](/annotation/python-net/guides/agents-and-llm-integration/)
* [Saving documents](/annotation/python-net/guides/saving-documents/)
* [GroupDocs.Annotation for Python via .NET Overview](/annotation/python-net/guides/product-overview/)

### See Also
* module [`groupdocs.annotation.options`](/annotation/python-net/groupdocs.annotation.options/)
