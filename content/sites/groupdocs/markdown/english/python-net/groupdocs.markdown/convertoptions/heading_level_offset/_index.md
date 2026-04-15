---
title: heading_level_offset property
second_title: GroupDocs.Markdown for Python via .NET API References
description: 
type: docs
url: /markdown/python-net/groupdocs.markdown/convertoptions/heading_level_offset/
is_root: false
weight: 2020
---


## heading_level_offset property

The offset to apply to all heading levels in the Markdown output. Default is 0 (no change).

This is useful when you are embedding the converted Markdown inside a larger document where top-level headings are already in use. For example, setting this to 1 ensures the converted content starts at `##` instead of `#`.

### Definition:
```python
@property
def heading_level_offset(self):
    ...
@heading_level_offset.setter
def heading_level_offset(self, value):
    ...
```

### See Also
* class [`ConvertOptions`](/markdown/python-net/groupdocs.markdown/convertoptions/)
