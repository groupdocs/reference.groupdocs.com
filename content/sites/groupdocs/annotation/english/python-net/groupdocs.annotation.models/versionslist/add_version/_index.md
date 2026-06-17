---
title: add_version method
second_title: GroupDocs.Annotation for Python via .NET API References
description: 
type: docs
url: /python-net/groupdocs.annotation.models/versionslist/add_version/
is_root: false
weight: 1010
---


## add_version {#annotations}

Add list of the annotations.

```python
def add_version(self, annotations):
    ...
```

| Parameter | Type | Description |
| :- | :- | :- |
| annotations | `List[AnnotationBase]` | List of the annotations to add. |

## add_version {#new_version_key-annotations}

Adds a list of annotations for a version key.

```python
def add_version(self, new_version_key, annotations):
    ...
```

| Parameter | Type | Description |
| :- | :- | :- |
| new_version_key | `Any` | Key of the version. |
| annotations | `List[AnnotationBase]` | List of the annotations. |

| Raises | Description |
| :- | :- |
| `Exception` | If the version key already exists. |

### See Also
* class [`VersionsList`](/annotation/python-net/groupdocs.annotation.models/versionslist/)
