---
title: generate_preview method
second_title: GroupDocs.Annotation for Python via .NET API References
description: 
type: docs
url: /python-net/groupdocs.annotation/document/generate_preview/
is_root: false
weight: 1040
---


## generate_preview {#preview_options}

Generates document pages preview (screenshots of every page).

```python
def generate_preview(self, preview_options):
    ...
```

| Parameter | Type | Description |
| :- | :- | :- |
| preview_options | `PreviewOptions` | The document preview options |

### Example

```python
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


if __name__ == "__main__":
    generate_document_preview()
```

### See Also
* class [`Document`](/annotation/python-net/groupdocs.annotation/document/)
