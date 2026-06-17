---
title: __init__ constructor
second_title: GroupDocs.Annotation for Python via .NET API References
description: 
type: docs
url: /python-net/groupdocs.annotation.models/user/__init__/
is_root: false
weight: 10
---


## __init__

Initializes a new instance of [`User`](/annotation/python-net/groupdocs.annotation.models/user/) class.

```python
def __init__(self):
    ...
```

## __init__ {#id-name-role}

Initializes a new instance of [`User`](/annotation/python-net/groupdocs.annotation.models/user/).

```python
def __init__(self, id, name, role):
    ...
```

| Parameter | Type | Description |
| :- | :- | :- |
| id | `int` | The user id. |
| name | `str` | The user name. |
| role | `Role` | The user role. |

### Example

```python
from groupdocs.annotation.models import User, Role

# Create a user with a name and role
user = User(name="Tom", role=Role.EDITOR)

# Create a user with an explicit id
user_with_id = User(id=123, name="Jack", role=Role.VIEWER)
```

### See Also
* class [`User`](/annotation/python-net/groupdocs.annotation.models/user/)
