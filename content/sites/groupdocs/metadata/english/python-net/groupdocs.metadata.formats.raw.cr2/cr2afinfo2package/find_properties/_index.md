﻿---
title: find_properties method
second_title: GroupDocs.Metadata for Python via .NET API References
description: 
type: docs
url: /python-net/groupdocs.metadata.formats.raw.cr2/cr2afinfo2package/find_properties/
is_root: false
weight: 50
---

## find_properties {#groupdocs.metadata.search.Specification}

Finds the metadata properties satisfying a specification. 
The search is recursive so it affects all nested packages as well.


### Returns 


A collection that contains properties from the package that satisfy the condition.


```python
def find_properties(self, specification):
    ...
```


| Parameter | Type | Description |
| :- | :- | :- |
| specification | groupdocs.metadata.search.Specification | A function to test each metadata property for a condition. |



### See Also
* module [`groupdocs.metadata.formats.raw.cr2`](../../)
* class [`Cr2AFInfo2Package`](/metadata/python-net/groupdocs.metadata.formats.raw.cr2/cr2afinfo2package)
