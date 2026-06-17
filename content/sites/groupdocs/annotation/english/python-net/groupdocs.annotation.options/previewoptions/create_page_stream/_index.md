---
title: create_page_stream property
second_title: GroupDocs.Annotation for Python via .NET API References
description: 
type: docs
url: /python-net/groupdocs.annotation.options/previewoptions/create_page_stream/
is_root: false
weight: 2010
---


## create_page_stream property

The delegate that defines a method to create an output page preview stream.

The callable should accept a page number (`int`) and return a writable stream (`io.RawIOBase`).

### Definition:
```python
@property
def create_page_stream(self):
    ...
@create_page_stream.setter
def create_page_stream(self, value):
    ...
```

### See Also
* class [`PreviewOptions`](/annotation/python-net/groupdocs.annotation.options/previewoptions/)
