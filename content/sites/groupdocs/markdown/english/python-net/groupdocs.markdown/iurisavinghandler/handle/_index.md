---
title: handle method
second_title: GroupDocs.Markdown for Python via .NET API References
description: 
type: docs
url: /python-net/groupdocs.markdown/iurisavinghandler/handle/
is_root: false
weight: 1010
---


## handle {#args}

Called once for each resource URI that will be written to the Markdown output.

```python
def handle(self, args):
    ...
```

| Parameter | Type | Description |
| :- | :- | :- |
| args | `UriSavingArgs` | Provides the default resource file name and URI, and allows you to override the URI via `UriSavingArgs.set_resource_file_uri`. |

### See Also
* class [`IUriSavingHandler`](/markdown/python-net/groupdocs.markdown/iurisavinghandler/)
