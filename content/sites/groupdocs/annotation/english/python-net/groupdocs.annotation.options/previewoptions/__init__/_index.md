---
title: __init__ constructor
second_title: GroupDocs.Annotation for Python via .NET API References
description: 
type: docs
url: /python-net/groupdocs.annotation.options/previewoptions/__init__/
is_root: false
weight: 10
---


## __init__ {#create_page_stream}

Initializes a new instance of [`PreviewOptions`](/annotation/python-net/groupdocs.annotation.options/previewoptions/) class.

```python
def __init__(self, create_page_stream):
    ...
```

| Parameter | Type | Description |
| :- | :- | :- |
| create_page_stream | `CreatePageStream` | Callable that defines method to create output page preview stream. |

### Example

```python
import os
from groupdocs.annotation import Annotator
from groupdocs.annotation.options import PreviewOptions, PreviewFormats

def generate_document_preview():
    output_dir = "./preview"
    os.makedirs(output_dir, exist_ok=True)

    open_streams = {}

    def create_page_stream(page_number):
        stream = open(os.path.join(output_dir, f"page_{page_number}.png"), "wb")
        open_streams[page_number] = stream
        return stream

    def release_page_stream(page_number, page_stream):
        stream = open_streams.pop(page_number, None)
        if stream:
            stream.close()

    with Annotator("./sample.pdf") as annotator:
        preview_options = PreviewOptions(create_page_stream, release_page_stream)
        preview_options.preview_format = PreviewFormats.PNG
        preview_options.page_numbers = [1]
        annotator.document.generate_preview(preview_options)

    print(f"Generated page preview image(s) in {output_dir}.")
```

## __init__ {#create_page_stream-release_page_stream}

Initializes a new PreviewOptions instance.

```python
def __init__(self, create_page_stream, release_page_stream):
    ...
```

| Parameter | Type | Description |
| :- | :- | :- |
| create_page_stream | `CreatePageStream` | Delegate which defines method to create output page preview stream. |
| release_page_stream | `ReleasePageStream` | Delegate which defines method to release output page preview stream. |

### Example

```python
import os
from groupdocs.annotation import Annotator
from groupdocs.annotation.options import PreviewOptions, PreviewFormats

def generate_document_preview():
    output_dir = "./preview"
    os.makedirs(output_dir, exist_ok=True)

    open_streams = {}

    def create_page_stream(page_number):
        stream = open(os.path.join(output_dir, f"page_{page_number}.png"), "wb")
        open_streams[page_number] = stream
        return stream

    def release_page_stream(page_number, page_stream):
        stream = open_streams.pop(page_number, None)
        if stream:
            stream.close()

    with Annotator("./sample.pdf") as annotator:
        preview_options = PreviewOptions(create_page_stream, release_page_stream)
        preview_options.preview_format = PreviewFormats.PNG
        preview_options.page_numbers = [1]
        annotator.document.generate_preview(preview_options)

    print(f"Generated page preview image(s) in {output_dir}.")
```

### See Also
* class [`PreviewOptions`](/annotation/python-net/groupdocs.annotation.options/previewoptions/)
