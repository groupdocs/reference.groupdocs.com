---
title: Saving documents
linkTitle: "Save documents"
second_title: GroupDocs.Annotation for Python via .NET API References
description: 
type: docs
url: /python-net/guides/saving-documents/
is_root: false
weight: 80
---


By default `save()` writes every annotation back into the document. With [`SaveOptions`](https://reference.groupdocs.com/annotation/python-net/groupdocs.annotation.options/saveoptions/) you can persist only certain annotation types or limit the output to a range of pages. Pass the configured [`SaveOptions`](/annotation/python-net/groupdocs.annotation.options/saveoptions/) to `save()` through the `save_options` parameter.

## Save specific annotation types

Set `annotation_types` to an [`AnnotationType`](https://reference.groupdocs.com/annotation/python-net/groupdocs.annotation.options/annotationtype/) value to write only annotations of that type, even if the document contains others.

```python
from groupdocs.annotation import Annotator
from groupdocs.annotation.models import Rectangle
from groupdocs.annotation.models.annotation_models import AreaAnnotation, EllipseAnnotation
from groupdocs.annotation.options import SaveOptions, AnnotationType
from groupdocs.pydrawing import Color

def save_specific_annotation_types():
    with Annotator("./sample.pdf") as annotator:
        area = AreaAnnotation()
        area.box = Rectangle(100, 100, 100, 100)
        area.background_color = Color.yellow.to_argb()
        area.page_number = 0
        area.message = "Area"

        ellipse = EllipseAnnotation()
        ellipse.box = Rectangle(100, 250, 150, 80)
        ellipse.background_color = Color.from_argb(255, 144, 238, 144).to_argb()
        ellipse.page_number = 0
        ellipse.message = "Ellipse"

        annotator.add(area)
        annotator.add(ellipse)

        # Persist only the area annotations
        save_options = SaveOptions()
        save_options.annotation_types = AnnotationType.AREA
        annotator.save("./output.pdf", save_options=save_options)

if __name__ == "__main__":
    save_specific_annotation_types()
```

`sample.pdf` is the sample file used in this example. Click [here](https://docs.groupdocs.com/annotation/python-net/_sample_files/developer-guide/advanced-usage/saving-documents/sample.pdf) to download it.

  
```text
Binary file (PDF, 90 KB)
```
[Download full output](https://docs.groupdocs.com/annotation/python-net/_output_files/developer-guide/advanced-usage/saving-documents/save_specific_annotation_types/output.pdf)

## Save a page range

Set `first_page` and `last_page` to write only a range of pages. These values are **1-based** — page `1` is the first page.

```python
from groupdocs.annotation import Annotator
from groupdocs.annotation.models import Rectangle
from groupdocs.annotation.models.annotation_models import AreaAnnotation
from groupdocs.annotation.options import SaveOptions
from groupdocs.pydrawing import Color

def save_specific_pages():
    with Annotator("./multipage_sample.pdf") as annotator:
        area = AreaAnnotation()
        area.box = Rectangle(100, 100, 100, 100)
        area.background_color = Color.yellow.to_argb()
        area.page_number = 0
        area.message = "Page 1 annotation"
        annotator.add(area)

        # first_page / last_page are 1-based for SaveOptions
        save_options = SaveOptions()
        save_options.first_page = 1
        save_options.last_page = 2
        annotator.save("./output.pdf", save_options=save_options)

if __name__ == "__main__":
    save_specific_pages()
```

`multipage_sample.pdf` is the sample file used in this example. Click [here](https://docs.groupdocs.com/annotation/python-net/_sample_files/developer-guide/advanced-usage/saving-documents/multipage_sample.pdf) to download it.

  
```text
Binary file (PDF, 92 KB)
```
[Download full output](https://docs.groupdocs.com/annotation/python-net/_output_files/developer-guide/advanced-usage/saving-documents/save_specific_pages/output.pdf)
