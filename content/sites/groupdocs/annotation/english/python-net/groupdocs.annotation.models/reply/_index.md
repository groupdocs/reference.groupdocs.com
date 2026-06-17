---
title: Reply class
second_title: GroupDocs.Annotation for Python via .NET API References
description: 
type: docs
url: /python-net/groupdocs.annotation.models/reply/
is_root: false
weight: 90
---


## Reply class

Represents an annotation comment.

The Reply type exposes the following members:

### Constructors
| Constructor | Description |
| :- | :- |
| [__init__](/annotation/python-net/groupdocs.annotation.models/reply/__init__/) |  |

### Methods
| Method | Description |
| :- | :- |
| [clone](/annotation/python-net/groupdocs.annotation.models/reply/clone/) | Returns a new instance with the same values. |

### Properties
| Property | Description |
| :- | :- |
| [comment](/annotation/python-net/groupdocs.annotation.models/reply/comment/) | The comment text content. |
| [id](/annotation/python-net/groupdocs.annotation.models/reply/id/) | The comment identifier. |
| [parent_reply](/annotation/python-net/groupdocs.annotation.models/reply/parent_reply/) | The parent comment (in case current one is a reply to the original one). |
| [replied_on](/annotation/python-net/groupdocs.annotation.models/reply/replied_on/) | The comment creation date and time. |
| [user](/annotation/python-net/groupdocs.annotation.models/reply/user/) | The comment author. |

### Example

```python
from groupdocs.annotation.models import Reply

# Create a reply and set its comment
reply = Reply()
reply.comment = "Please double-check this"
```

### Guides
Task guides that use `Reply`:

* [AI agents and LLM integration](/annotation/python-net/guides/agents-and-llm-integration/)
* [Comments and replies](/annotation/python-net/guides/comments-and-replies/)
* [GroupDocs.Annotation for Python via .NET Overview](/annotation/python-net/guides/product-overview/)

### See Also
* module [`groupdocs.annotation.models`](/annotation/python-net/groupdocs.annotation.models/)
