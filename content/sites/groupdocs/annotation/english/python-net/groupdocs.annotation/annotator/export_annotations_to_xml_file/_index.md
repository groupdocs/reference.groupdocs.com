---
title: export_annotations_to_xml_file method
second_title: GroupDocs.Annotation for Python via .NET API References
description: 
type: docs
url: /python-net/groupdocs.annotation/annotator/export_annotations_to_xml_file/
is_root: false
weight: 1050
---


## export_annotations_to_xml_file {#output_path}

Exports annotations from the document to an XML file.

Learn more:

- More about how to import annotations: https://docs.groupdocs.com/display/annotationnet/Import+annotations+from+document

```python
def export_annotations_to_xml_file(self, output_path):
    ...
```

| Parameter | Type | Description |
| :- | :- | :- |
| output_path | `str` | The output file path (must be in .xml format). |

### Example

```python
from groupdocs.annotation import Annotator

def export_annotations_to_xml():
    with Annotator("./annotated.pdf") as annotator:
        annotator.export_annotations_to_xml_file(output_path="./exported_annotations.xml")
    print("Exported annotations to ./exported_annotations.xml.")
```

### See Also
* class [`Annotator`](/annotation/python-net/groupdocs.annotation/annotator/)
