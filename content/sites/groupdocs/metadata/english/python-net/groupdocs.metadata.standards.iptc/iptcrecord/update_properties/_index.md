﻿---
title: update_properties method
second_title: GroupDocs.Metadata for Python via .NET API References
description: 
type: docs
url: /python-net/groupdocs.metadata.standards.iptc/iptcrecord/update_properties/
is_root: false
weight: 90
---

## update_properties {#groupdocs.metadata.search.Specification-groupdocs.metadata.common.PropertyValue}

Updates known metadata properties satisfying a specification.
The operation is recursive so it affects all nested packages as well.


### Returns 


The number of affected properties.


```python
def update_properties(self, specification, value):
    ...
```


| Parameter | Type | Description |
| :- | :- | :- |
| specification | groupdocs.metadata.search.Specification | A specification to test each metadata property for a condition. |
| value | groupdocs.metadata.common.PropertyValue | A new value for the filtered properties. |



### See Also
* module [`groupdocs.metadata.standards.iptc`](../../)
* class [`IptcRecord`](/metadata/python-net/groupdocs.metadata.standards.iptc/iptcrecord)
