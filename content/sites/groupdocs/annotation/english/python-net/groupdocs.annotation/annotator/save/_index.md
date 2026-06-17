---
title: save method
second_title: GroupDocs.Annotation for Python via .NET API References
description: 
type: docs
url: /python-net/groupdocs.annotation/annotator/save/
is_root: false
weight: 1200
---


## save

Saves document after adding, updating or removing annotations.

Learn more about saving annotated documents

- More about how to save only annotated document pages: https://docs.groupdocs.com/display/annotationnet/Save+only+annotated+pages
- More about how to save document with specific annotation types only: https://docs.groupdocs.com/display/annotationnet/Filtering+annotation+types
- More about how to save specific pages from the whole document: https://docs.groupdocs.com/display/annotationnet/Save+specific+page+range

```python
def save(self):
    ...
```

### Example

```python
import io
from groupdocs.annotation import Annotator

with Annotator("document.pdf") as annotator:
    # add annotations here, e.g., annotator.add(area)
    buf = io.BytesIO()
    annotator.save(buf)  # BytesIO is updated after save
    data = buf.getvalue()
```

## save {#save_options}

Saves the document after adding, updating, or removing annotations.

```python
def save(self, save_options):
    ...
```

| Parameter | Type | Description |
| :- | :- | :- |
| save_options | `SaveOptions` | The save options. |

**Returns:** None.

- More about how to save only annotated document pages: Save only annotated pages (https://docs.groupdocs.com/display/annotationnet/Save+only+annotated+pages)
- More about how to save document with specific annotation types only: Filtering annotation types on save (https://docs.groupdocs.com/display/annotationnet/Filtering+annotation+types)
- More about how to save specific pages from the whole document: Save specific page range (https://docs.groupdocs.com/display/annotationnet/Save+specific+page+range)

### Example

```python
import io
from groupdocs.annotation import Annotator
from groupdocs.annotation.options import SaveOptions, AnnotationType

with Annotator("document.pdf") as annotator:
    # add annotations here, e.g., annotator.add(area)

    # Save to a memory stream
    stream = io.BytesIO()
    annotator.save(stream)
    data = stream.getvalue()

    # Save with specific options
    options = SaveOptions()
    options.annotation_types = AnnotationType.AREA
    annotator.save("filtered.pdf", save_options=options)
```

## save {#document}

Saves document after adding, updating or removing annotations.

Learn more about saving annotated documents.

- More about how to save only annotated document pages: https://docs.groupdocs.com/display/annotationnet/Save+only+annotated+pages
- More about how to save document with specific annotation types only: https://docs.groupdocs.com/display/annotationnet/Filtering+annotation+types
- More about how to save specific pages from the whole document: https://docs.groupdocs.com/display/annotationnet/Save+specific+page+range

```python
def save(self, document):
    ...
```

| Parameter | Type | Description |
| :- | :- | :- |
| document | `io.RawIOBase` | The output stream. |

### Example

```python
import io
from groupdocs.annotation import Annotator

with Annotator("document.pdf") as annotator:
    # add annotations as needed, e.g., annotator.add(area)
    buf = io.BytesIO()
    annotator.save(buf)  # BytesIO is updated after save
    data = buf.getvalue()
```

## save {#file_path}

Saves the document after adding, updating, or removing annotations.

Learn more about saving annotated documents.

- More about how to save only annotated document pages: https://docs.groupdocs.com/display/annotationnet/Save+only+annotated+pages
- More about how to save document with specific annotation types only: https://docs.groupdocs.com/display/annotationnet/Filtering+annotation+types
- More about how to save specific pages from the whole document: https://docs.groupdocs.com/display/annotationnet/Save+specific+page+range

```python
def save(self, file_path):
    ...
```

| Parameter | Type | Description |
| :- | :- | :- |
| file_path | `str` | The output file path. |

### Example

```python
import io
from groupdocs.annotation import Annotator

with Annotator("document.pdf") as annotator:
    # add annotations here, e.g., annotator.add(area)
    buf = io.BytesIO()
    annotator.save(buf)  # BytesIO is updated after save
    data = buf.getvalue()
```

## save {#document-save_options}

Saves document after adding, updating or removing annotations.

**Learn more about saving annotated documents**

- More about how to save only annotated document pages: <https://docs.groupdocs.com/display/annotationnet/Save+only+annotated+pages>
- More about how to save document with specific annotation types only: <https://docs.groupdocs.com/display/annotationnet/Filtering+annotation+types>
- More about how to save specific pages from the whole document: <https://docs.groupdocs.com/display/annotationnet/Save+specific+page+range>

```python
def save(self, document, save_options):
    ...
```

| Parameter | Type | Description |
| :- | :- | :- |
| document | `io.RawIOBase` | The output stream or file path where the annotated document will be saved. |
| save_options | `SaveOptions` | The save options that control which pages or annotation types are saved. |

### Example

```python
import io
from groupdocs.annotation import Annotator
from groupdocs.annotation.options import SaveOptions, AnnotationType

# Save to a stream
with Annotator("document.pdf") as annotator:
    # add annotations here
    buf = io.BytesIO()
    annotator.save(buf)                # BytesIO is updated after save
    data = buf.getvalue()

# Save to a file with filtering options
options = SaveOptions()
options.annotation_types = AnnotationType.AREA   # render only area annotations
options.first_page = 1                           # 1‑based page index
options.last_page = 2
with Annotator("document.pdf") as annotator:
    # add annotations here
    annotator.save("filtered.pdf", saveOptions=options)
```

## save {#file_path-save_options}

Saves document after adding, updating or removing annotations.

- More about how to save only annotated document pages: <https://docs.groupdocs.com/display/annotationnet/Save+only+annotated+pages>
- More about how to save document with specific annotation types only: <https://docs.groupdocs.com/display/annotationnet/Filtering+annotation+types>
- More about how to save specific pages from the whole document: <https://docs.groupdocs.com/display/annotationnet/Save+specific+page+range>

```python
def save(self, file_path, save_options):
    ...
```

| Parameter | Type | Description |
| :- | :- | :- |
| file_path | `str` | The output file path. |
| save_options | `SaveOptions` | The save options. |

### Example

```python
import io
from groupdocs.annotation import Annotator
from groupdocs.annotation.options import SaveOptions, AnnotationType

# Save to a stream
with Annotator("document.pdf") as annotator:
    # add annotations here
    buffer = io.BytesIO()
    annotator.save(buffer)  # buffer now contains the PDF bytes
    data = buffer.getvalue()

# Save with options (filter by type and page range)
with Annotator("document.pdf") as annotator:
    # add annotations here
    options = SaveOptions()
    options.annotation_types = AnnotationType.AREA  # render only area annotations
    options.first_page = 1  # 1‑based page numbers
    options.last_page = 2
    annotator.save("filtered.pdf", save_options=options)
```

### See Also
* class [`Annotator`](/annotation/python-net/groupdocs.annotation/annotator/)
