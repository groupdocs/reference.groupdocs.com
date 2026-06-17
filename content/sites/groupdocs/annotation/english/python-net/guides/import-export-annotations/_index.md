---
title: Import and export annotations
second_title: GroupDocs.Annotation for Python via .NET API References
description: 
type: docs
url: /python-net/guides/import-export-annotations/
is_root: false
weight: 120
---


GroupDocs.Annotation can serialize a document's annotations to a standalone XML file and load them back into any document. This is useful for transferring a review between copies of a document, storing annotations separately from the source file, or applying the same set of annotations to multiple documents.

- [`export_annotations_to_xml_file(output_path)`](https://reference.groupdocs.com/annotation/python-net/groupdocs.annotation/annotator/) — write the open document's annotations to an XML file.
- [`import_annotations_from_xml_file(file_path)`](https://reference.groupdocs.com/annotation/python-net/groupdocs.annotation/annotator/) — read annotations from an XML file into the open document.

## Export annotations to XML

Open an annotated document and write its annotations to an XML file.

```python
from groupdocs.annotation import Annotator

def export_annotations_to_xml():
    with Annotator("./annotated.pdf") as annotator:
        annotator.export_annotations_to_xml_file(output_path="./exported_annotations.xml")

    print("Exported annotations to ./exported_annotations.xml.")

if __name__ == "__main__":
    export_annotations_to_xml()
```

## Import annotations from XML

Load annotations from an XML file into a document, then save the result.

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
