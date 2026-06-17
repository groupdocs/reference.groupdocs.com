---
title: get_document_info method
second_title: GroupDocs.Annotation for Python via .NET API References
description: 
type: docs
url: /python-net/groupdocs.annotation/document/get_document_info/
is_root: false
weight: 1060
---


## get_document_info

Retrieves information about the document, including its type, size, page count, and detailed page data.

```python
def get_document_info(self):
    ...
```

### Example

```python
with Annotator("document.pdf") as annotator:
    info = annotator.document.get_document_info()
    print(info.file_type.file_format, info.page_count, info.size)
```

### See Also
* class [`Document`](/annotation/python-net/groupdocs.annotation/document/)
