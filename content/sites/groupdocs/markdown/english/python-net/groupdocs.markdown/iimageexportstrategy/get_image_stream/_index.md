---
title: get_image_stream method
second_title: GroupDocs.Markdown for Python via .NET API References
description: 
type: docs
url: /python-net/groupdocs.markdown/iimageexportstrategy/get_image_stream/
is_root: false
weight: 1010
---


## get_image_stream {#context}

Returns a writable stream for the image described by `context`.

The library writes the image bytes to this stream during conversion.

```python
def get_image_stream(self, context):
    ...
```

| Parameter | Type | Description |
| :- | :- | :- |
| context | `ImageExportContext` | The image export context containing the default image file name and other metadata. You may modify `ImageExportContext.image_file_name` before returning the stream to change the file name that appears in the Markdown output. |

**Returns:** io.RawIOBase: A writable stream where the image data will be written, or `None` to use the default behavior.

### See Also
* class [`IImageExportStrategy`](/markdown/python-net/groupdocs.markdown/iimageexportstrategy/)
