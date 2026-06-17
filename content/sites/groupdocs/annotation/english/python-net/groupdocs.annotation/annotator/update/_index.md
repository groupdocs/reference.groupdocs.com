---
title: update method
second_title: GroupDocs.Annotation for Python via .NET API References
description: 
type: docs
url: /python-net/groupdocs.annotation/annotator/update/
is_root: false
weight: 1260
---


## update {#new_annotation}

Updates document annotation by id.

Learn more

- More about how to update document annotations: https://docs.groupdocs.com/display/annotationnet/Update+annotations

```python
def update(self, new_annotation):
    ...
```

| Parameter | Type | Description |
| :- | :- | :- |
| new_annotation | `AnnotationBase` | The annotation to update (Id should be provided). |

### Example

```python
from groupdocs.annotation import Annotator

with Annotator("annotated.pdf") as annotator:
    annotations = annotator.get()
    annotator.update(annotations[0])
```

## update {#annotations}

Updates collection of document annotations by overriding the previous list with a new one.

- More about how to update document annotations: https://docs.groupdocs.com/display/annotationnet/Update+annotations

```python
def update(self, annotations):
    ...
```

| Parameter | Type | Description |
| :- | :- | :- |
| annotations | `List[AnnotationBase]` | The annotations list that will be set. |

### Example

```python
from groupdocs.annotation import Annotator

with Annotator("annotated.pdf") as annotator:
    all_annotations = annotator.get()
    # modify an annotation as needed
    annotator.update([all_annotations[0]])  # replace the current list with the modified annotation
    annotator.save("edited.pdf")
```

### See Also
* class [`Annotator`](/annotation/python-net/groupdocs.annotation/annotator/)
