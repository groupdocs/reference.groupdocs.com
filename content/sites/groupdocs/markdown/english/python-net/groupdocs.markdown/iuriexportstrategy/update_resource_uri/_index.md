---
title: update_resource_uri method
second_title: GroupDocs.Markdown for Python via .NET API References
description: 
type: docs
url: /markdown/python-net/groupdocs.markdown/iuriexportstrategy/update_resource_uri/
is_root: false
weight: 1010
---


## update_resource_uri {#context}

Called for each resource URI that will be written to the Markdown output, allowing modification of properties on `context` to customize the resulting URI.

```python
def update_resource_uri(self, context):
    ...
```

| Parameter | Type | Description |
| :- | :- | :- |
| context | `UriExportContext` | The URI export context. Set `UriExportContext.resource_file_uri` to override the URI that appears in the Markdown output, or modify `UriExportContext.resource_file_name` to change the resource file name. |

### See Also
* class [`IUriExportStrategy`](/markdown/python-net/groupdocs.markdown/iuriexportstrategy/)
