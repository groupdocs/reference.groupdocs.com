---
title: failure method
second_title: GroupDocs.Markdown for Python via .NET API References
description: 
type: docs
url: /markdown/python-net/groupdocs.markdown/convertresult/failure/
is_root: false
weight: 1010
---


## failure {#error_message-exception}

Creates a failed result with error information.

```python
def failure(cls, error_message, exception):
    ...
```

| Parameter | Type | Description |
| :- | :- | :- |
| error_message | `str` | A human-readable description of the error. |
| exception | `Exception` | The exception that caused the failure. |

**Returns:** ConvertResult: A ConvertResult with `IsSuccess` set to `False`.

### See Also
* class [`ConvertResult`](/markdown/python-net/groupdocs.markdown/convertresult/)
