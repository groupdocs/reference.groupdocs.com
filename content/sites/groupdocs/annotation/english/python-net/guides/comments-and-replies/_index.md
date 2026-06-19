---
title: Comments and replies
linkTitle: "Comments & replies"
second_title: GroupDocs.Annotation for Python via .NET API References
description: 
type: docs
url: /python-net/guides/comments-and-replies/
is_root: false
weight: 100
---


Every annotation can carry a discussion thread. You build the thread as a list of [`Reply`](https://reference.groupdocs.com/annotation/python-net/groupdocs.annotation.models/reply/) objects and assign it to the annotation's `replies` property. Each reply has a `comment` and a [`User`](https://reference.groupdocs.com/annotation/python-net/groupdocs.annotation.models/user/), and each user has a `name` and a [`Role`](/annotation/python-net/groupdocs.annotation.models/role/) (`Role.EDITOR` or `Role.VIEWER`).

## Add replies to an annotation

The example below creates an area annotation and attaches a two-message conversation between two users before saving the document.

```python
from groupdocs.annotation import Annotator
from groupdocs.annotation.models import Rectangle, Reply, User, Role
from groupdocs.annotation.models.annotation_models import AreaAnnotation
from groupdocs.pydrawing import Color

def add_replies_to_annotation():
    with Annotator("./sample.pdf") as annotator:
        area = AreaAnnotation()
        area.box = Rectangle(100, 100, 100, 100)
        area.background_color = Color.yellow.to_argb()
        area.page_number = 0
        area.message = "Please review this section"

        # Attach a threaded discussion to the annotation
        first_reply = Reply()
        first_reply.comment = "Good catch, I'll take a look."
        first_reply.user = User(name="Tom", role=Role.EDITOR)

        second_reply = Reply()
        second_reply.comment = "Agreed, looks resolved now."
        second_reply.user = User(name="Jack", role=Role.VIEWER)

        area.replies = [first_reply, second_reply]

        annotator.add(area)
        annotator.save("./output.pdf")

if __name__ == "__main__":
    add_replies_to_annotation()
```

`sample.pdf` is the sample file used in this example. Click [here](https://docs.groupdocs.com/annotation/python-net/_sample_files/developer-guide/basic-usage/comments-and-replies/sample.pdf) to download it.

  
```text
Binary file (PDF, 91 KB)
```
[Download full output](https://docs.groupdocs.com/annotation/python-net/_output_files/developer-guide/basic-usage/comments-and-replies/add_replies_to_annotation/output.pdf)
