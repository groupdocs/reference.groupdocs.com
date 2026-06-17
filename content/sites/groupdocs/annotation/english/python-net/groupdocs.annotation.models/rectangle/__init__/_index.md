---
title: __init__ constructor
second_title: GroupDocs.Annotation for Python via .NET API References
description: 
type: docs
url: /python-net/groupdocs.annotation.models/rectangle/__init__/
is_root: false
weight: 10
---


## __init__ {#x-y-width-height}

Initializes a new Rectangle.

```python
def __init__(self, x, y, width, height):
    ...
```

| Parameter | Type | Description |
| :- | :- | :- |
| x | `float` | The x coordinate (top left corner of the rectangle). |
| y | `float` | The y coordinate (top left corner of the rectangle). |
| width | `float` | The width of the rectangle. |
| height | `float` | The height of the rectangle. |

### Example

```python
from groupdocs.annotation.models import Rectangle

# Create a rectangle at position (100, 100) with width 200 and height 80
rect = Rectangle(100, 100, 200, 80)
```

### See Also
* class [`Rectangle`](/annotation/python-net/groupdocs.annotation.models/rectangle/)
