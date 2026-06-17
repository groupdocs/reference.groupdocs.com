---
title: PreviewOptions class
second_title: GroupDocs.Annotation for Python via .NET API References
description: 
type: docs
url: /python-net/groupdocs.annotation.options/previewoptions/
is_root: false
weight: 50
---


## PreviewOptions class

The class represents document preview options.

The PreviewOptions type exposes the following members:

### Constructors
| Constructor | Description |
| :- | :- |
| [__init__](/annotation/python-net/groupdocs.annotation.options/previewoptions/__init__/#create_page_stream) | Initializes a new instance of [`PreviewOptions`](/annotation/python-net/groupdocs.annotation.options/previewoptions/) class. |
| [__init__](/annotation/python-net/groupdocs.annotation.options/previewoptions/__init__/#create_page_stream-release_page_stream) | Initializes a new PreviewOptions instance. |

### Properties
| Property | Description |
| :- | :- |
| [create_page_stream](/annotation/python-net/groupdocs.annotation.options/previewoptions/create_page_stream/) | The delegate that defines a method to create an output page preview stream. |
| [height](/annotation/python-net/groupdocs.annotation.options/previewoptions/height/) | The page preview height. |
| [page_numbers](/annotation/python-net/groupdocs.annotation.options/previewoptions/page_numbers/) | The page numbers that will be previewed. |
| [preview_format](/annotation/python-net/groupdocs.annotation.options/previewoptions/preview_format/) | The preview image format. |
| [release_page_stream](/annotation/python-net/groupdocs.annotation.options/previewoptions/release_page_stream/) | The delegate which defines method to remove output page preview stream. |
| [render_annotations](/annotation/python-net/groupdocs.annotation.options/previewoptions/render_annotations/) | The property that controls whether annotations will be generated on the preview (default is True). |
| [render_comments](/annotation/python-net/groupdocs.annotation.options/previewoptions/render_comments/) | The property that controls whether comments will be generated on the preview; default is True and it is supported only in MS Word documents. |
| [resolution](/annotation/python-net/groupdocs.annotation.options/previewoptions/resolution/) | The resolution for generated images, in dots per inch. |
| [width](/annotation/python-net/groupdocs.annotation.options/previewoptions/width/) | The page preview width. |
| [worksheet_columns](/annotation/python-net/groupdocs.annotation.options/previewoptions/worksheet_columns/) | The worksheet columns to generate. Generation proceeds in the specified order. |

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

### Guides
Task guides that use `PreviewOptions`:

* [Generate document preview](/annotation/python-net/guides/generate-document-preview/)

### See Also
* module [`groupdocs.annotation.options`](/annotation/python-net/groupdocs.annotation.options/)
