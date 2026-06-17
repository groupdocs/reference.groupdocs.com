---
title: import_annotations_from_xml_file method
second_title: GroupDocs.Annotation for Python via .NET API References
description: 
type: docs
url: /python-net/groupdocs.annotation/annotator/import_annotations_from_xml_file/
is_root: false
weight: 1130
---


## import_annotations_from_xml_file {#file_path}

Export annotations from XML file.

Learn more
- More about how to export annotations: https://docs.groupdocs.com/display/annotationnet/Export+annotations+from+document

```python
def import_annotations_from_xml_file(self, file_path):
    ...
```

| Parameter | Type | Description |
| :- | :- | :- |
| file_path | `str` | The path to XML file. |

### Example

```python
from groupdocs.annotation import Annotator

def import_annotations_from_xml():
    with Annotator("./sample.pdf") as annotator:
        annotator.import_annotations_from_xml_file(file_path="./annotations.xml")
        annotator.save("./output.pdf")

    print("Imported annotations from ./annotations.xml. Output saved to ./output.pdf.")

if __name__ == "__main__":
    import_annotations_from_xml()
```

### See Also
* class [`Annotator`](/annotation/python-net/groupdocs.annotation/annotator/)
