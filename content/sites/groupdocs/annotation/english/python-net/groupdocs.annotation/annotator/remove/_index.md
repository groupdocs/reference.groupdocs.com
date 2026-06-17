---
title: remove method
second_title: GroupDocs.Annotation for Python via .NET API References
description: 
type: docs
url: /python-net/groupdocs.annotation/annotator/remove/
is_root: false
weight: 1160
---


## remove {#annotation_id}

Removes an annotation from the document by its identifier.

- More about how to remove document annotations: https://docs.groupdocs.com/display/annotationnet/Remove+annotation+from+document

```python
def remove(self, annotation_id):
    ...
```

| Parameter | Type | Description |
| :- | :- | :- |
| annotation_id | `int` | The annotation's id that must be removed. |

### Example

```python
from groupdocs.annotation import Annotator

def remove_annotation_by_id():
    # Open an annotated document and remove a single annotation by its id
    with Annotator("./annotated.pdf") as annotator:
        annotations = annotator.get()
        if annotations:
            annotator.remove(annotation_id=annotations[0].id)
        annotator.save("./output.pdf")
```

## remove {#annotation}

Removes an annotation from the document.

- More about how to remove document annotations: How to remove document annotations in C# (https://docs.groupdocs.com/display/annotationnet/Remove+annotation+from+document)

```python
def remove(self, annotation):
    ...
```

| Parameter | Type | Description |
| :- | :- | :- |
| annotation | `AnnotationBase` | Annotation that must be removed. |

**Returns:** None.

### Example

```python
from groupdocs.annotation import Annotator

def remove_annotation_by_object():
    # Open an annotated document and remove a single annotation by its object
    with Annotator("./annotated.pdf") as annotator:
        annotations = annotator.get()
        if annotations:
            annotator.remove(annotation=annotations[0])
        annotator.save("./output.pdf")
```

## remove {#annotation_ids}

Removes a collection of annotations from the document using the provided annotation IDs.

More about how to remove document annotations:
- https://docs.groupdocs.com/display/annotationnet/Remove+annotation+from+document

```python
def remove(self, annotation_ids):
    ...
```

| Parameter | Type | Description |
| :- | :- | :- |
| annotation_ids | `List[int]` | Iterable of annotation IDs (e.g., list of str) that should be removed. |

### Example

```python
from groupdocs.annotation import Annotator

def remove_annotation_by_id():
    # Open an annotated document and remove a single annotation by its id
    with Annotator("./annotated.pdf") as annotator:
        annotations = annotator.get()
        if annotations:
            annotator.remove(annotation_id=annotations[0].id)
        annotator.save("./output.pdf")
```

## remove {#annotations_to_delete}

Removes collection of annotations from document.

- More about how to remove document annotations: https://docs.groupdocs.com/display/annotationnet/Remove+annotation+from+document

```python
def remove(self, annotations_to_delete):
    ...
```

| Parameter | Type | Description |
| :- | :- | :- |
| annotations_to_delete | `List[AnnotationBase]` | The annotations that must be removed. |

### Example

```python
from groupdocs.annotation import Annotator

def remove_all_annotations():
    with Annotator("./annotated.pdf") as annotator:
        annotations = annotator.get()
        if annotations:
            annotator.remove(annotations_to_delete=annotations)
        annotator.save("./output.pdf")
```

### See Also
* class [`Annotator`](/annotation/python-net/groupdocs.annotation/annotator/)
