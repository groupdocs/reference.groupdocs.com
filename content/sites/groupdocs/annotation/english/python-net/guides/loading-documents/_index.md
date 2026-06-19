---
title: Loading documents
second_title: GroupDocs.Annotation for Python via .NET API References
description: 
type: docs
url: /python-net/guides/loading-documents/
is_root: false
weight: 50
---


The [`Annotator`](https://reference.groupdocs.com/annotation/python-net/groupdocs.annotation/annotator/) class can open a document from a file path or any readable binary stream, including password-protected files. The examples below show each loading scenario.

## Load from local disk

When the document is on the local disk, pass its path to the [`Annotator`](/annotation/python-net/groupdocs.annotation/annotator/) constructor.

```python
from groupdocs.annotation import Annotator
from groupdocs.annotation.models import Rectangle
from groupdocs.annotation.models.annotation_models import AreaAnnotation
from groupdocs.pydrawing import Color

def load_from_local_disk():
    # Load a document directly from a local file path
    with Annotator("./sample.pdf") as annotator:
        area = AreaAnnotation()
        area.box = Rectangle(100, 100, 100, 100)
        area.background_color = Color.yellow.to_argb()
        area.page_number = 0
        area.message = "Loaded from local disk"
        annotator.add(area)
        annotator.save("./output.pdf")

if __name__ == "__main__":
    load_from_local_disk()
```

`sample.pdf` is the sample file used in this example. Click [here](https://docs.groupdocs.com/annotation/python-net/_sample_files/developer-guide/advanced-usage/loading-documents/sample.pdf) to download it.

  
```text
Binary file (PDF, 90 KB)
```
[Download full output](https://docs.groupdocs.com/annotation/python-net/_output_files/developer-guide/advanced-usage/loading-documents/load_from_local_disk/output.pdf)

## Load from stream

As an alternative to a local file, pass an open binary stream to the `document` parameter of the [`Annotator`](/annotation/python-net/groupdocs.annotation/annotator/) constructor.

```python
from groupdocs.annotation import Annotator
from groupdocs.annotation.models import Rectangle
from groupdocs.annotation.models.annotation_models import AreaAnnotation
from groupdocs.pydrawing import Color

def load_from_stream():
    # Load a document from an open binary stream
    with open("./sample.pdf", "rb") as stream:
        with Annotator(document=stream) as annotator:
            area = AreaAnnotation()
            area.box = Rectangle(100, 100, 100, 100)
            area.background_color = Color.yellow.to_argb()
            area.page_number = 0
            area.message = "Loaded from stream"
            annotator.add(area)
            annotator.save("./output.pdf")

if __name__ == "__main__":
    load_from_stream()
```

`sample.pdf` is the sample file used in this example. Click [here](https://docs.groupdocs.com/annotation/python-net/_sample_files/developer-guide/advanced-usage/loading-documents/sample.pdf) to download it.

  
```text
Binary file (PDF, 90 KB)
```
[Download full output](https://docs.groupdocs.com/annotation/python-net/_output_files/developer-guide/advanced-usage/loading-documents/load_from_stream/output.pdf)

## Load a password-protected file

To open an encrypted document, set the `password` property of [`LoadOptions`](https://reference.groupdocs.com/annotation/python-net/groupdocs.annotation.options/loadoptions/) and pass it to the [`Annotator`](/annotation/python-net/groupdocs.annotation/annotator/) through the `load_options` parameter.

```python
from groupdocs.annotation import Annotator
from groupdocs.annotation.options import LoadOptions
from groupdocs.annotation.models import Rectangle
from groupdocs.annotation.models.annotation_models import AreaAnnotation
from groupdocs.pydrawing import Color

def load_password_protected_document():
    # Provide the password through LoadOptions
    load_options = LoadOptions()
    load_options.password = "secret"

    with Annotator("./protected.docx", load_options=load_options) as annotator:
        area = AreaAnnotation()
        area.box = Rectangle(100, 100, 100, 100)
        area.background_color = Color.yellow.to_argb()
        area.page_number = 0
        area.message = "Annotated a password-protected document"
        annotator.add(area)
        annotator.save("./output.docx")

if __name__ == "__main__":
    load_password_protected_document()
```

`protected.docx` is the sample file used in this example. Click [here](https://docs.groupdocs.com/annotation/python-net/_sample_files/developer-guide/advanced-usage/loading-documents/protected.docx) to download it.

  
```text
Binary file (DOCX, 10 KB)
```
[Download full output](https://docs.groupdocs.com/annotation/python-net/_output_files/developer-guide/advanced-usage/loading-documents/load_password_protected_document/output.docx)
