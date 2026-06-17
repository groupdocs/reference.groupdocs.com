---
title: User class
second_title: GroupDocs.Annotation for Python via .NET API References
description: 
type: docs
url: /python-net/groupdocs.annotation.models/user/
is_root: false
weight: 140
---


## User class

Class that represents a user.

The User type exposes the following members:

### Constructors
| Constructor | Description |
| :- | :- |
| [__init__](/annotation/python-net/groupdocs.annotation.models/user/__init__/) | Initializes a new instance of [`User`](/annotation/python-net/groupdocs.annotation.models/user/) class. |
| [__init__](/annotation/python-net/groupdocs.annotation.models/user/__init__/#id-name-role) | Initializes a new instance of [`User`](/annotation/python-net/groupdocs.annotation.models/user/). |

### Properties
| Property | Description |
| :- | :- |
| [email](/annotation/python-net/groupdocs.annotation.models/user/email/) | The user email address. |
| [id](/annotation/python-net/groupdocs.annotation.models/user/id/) | The User identifier. |
| [name](/annotation/python-net/groupdocs.annotation.models/user/name/) | The user name. |
| [role](/annotation/python-net/groupdocs.annotation.models/user/role/) | The role of the user. |

### Example

```python
from groupdocs.annotation.models import User, Role

user = User(name="Tom", role=Role.EDITOR)
```

### Guides
Task guides that use `User`:

* [AI agents and LLM integration](/annotation/python-net/guides/agents-and-llm-integration/)
* [Comments and replies](/annotation/python-net/guides/comments-and-replies/)

### See Also
* module [`groupdocs.annotation.models`](/annotation/python-net/groupdocs.annotation.models/)
