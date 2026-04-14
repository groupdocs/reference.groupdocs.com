---
title: set_output_stream method
second_title: GroupDocs.Markdown for Python via .NET API References
description: 
type: docs
url: /python-net/groupdocs.markdown/customimagesavingargs/set_output_stream/
is_root: false
weight: 1020
---


## set_output_stream {#stream}

Redirects the image data to a custom writable stream instead of the default file output.

The library will write the image bytes to this stream during conversion.

```python
def set_output_stream(self, stream):
    ...
```

| Parameter | Type | Description |
| :- | :- | :- |
| stream | `io.RawIOBase` | A writable stream where the image data will be written. |

| Raises | Description |
| :- | :- |
| `TypeError` | When `stream` is `None`. |

### See Also
* class [`CustomImageSavingArgs`](/python-net/groupdocs.markdown/customimagesavingargs/)
