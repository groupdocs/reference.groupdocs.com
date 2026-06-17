---
title: get method
second_title: GroupDocs.Annotation for Python via .NET API References
description: 
type: docs
url: /python-net/groupdocs.annotation/annotator/get/
is_root: false
weight: 1080
---


## get

Gets collections of document annotations.

Learn more:

- More about how to get document annotations collection: How to get document annotations in C# (https://docs.groupdocs.com/display/annotationnet/Extract+annotations+from+document)

```python
def get(self):
    ...
```

**Returns:** The list of annotations.

### Example

```python
from groupdocs.annotation import Annotator


def get_all_annotations():
    # Open a document that already contains annotations and list them
    with Annotator("./annotated.pdf") as annotator:
        annotations = annotator.get()
        print(f"Found {len(annotations)} annotation(s):")
        for annotation in annotations:
            print(f"  [{annotation.id}] {type(annotation).__name__}: {annotation.message}")


if __name__ == "__main__":
    get_all_annotations()
```

## get {#type}

Returns a collection of document annotations filtered by the specified annotation type.

```python
def get(self, type):
    ...
```

| Parameter | Type | Description |
| :- | :- | :- |
| type | `AnnotationType` | The annotation type that must be returned. |

**Returns:** list[GroupDocs.Annotation.Annotation]: The list of annotations of the specified type.

- Learn more: More about how to get document annotations collection: https://docs.groupdocs.com/display/annotationnet/Extract+annotations+from+document

### Example

```python
from groupdocs.annotation import Annotator


def get_all_annotations():
    # Open a document that already contains annotations and list them
    with Annotator("./annotated.pdf") as annotator:
        annotations = annotator.get()
        print(f"Found {len(annotations)} annotation(s):")
        for annotation in annotations:
            print(f"  [{annotation.id}] {type(annotation).__name__}: {annotation.message}")


if __name__ == "__main__":
    get_all_annotations()
```

### See Also
* class [`Annotator`](/annotation/python-net/groupdocs.annotation/annotator/)
