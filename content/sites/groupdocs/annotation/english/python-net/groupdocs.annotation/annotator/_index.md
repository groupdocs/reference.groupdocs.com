---
title: Annotator class
second_title: GroupDocs.Annotation for Python via .NET API References
description: 
type: docs
url: /python-net/groupdocs.annotation/annotator/
is_root: false
weight: 10
---


## Annotator class

The Annotator class is the central component of the GroupDocs.Annotation API, designed to manage and facilitate the document annotation process across various formats.

Learn more

- More about GroupDocs.Annotation features: GroupDocs.Annotation Developer Guide (https://docs.groupdocs.com/display/annotationnet/Developer+Guide)

The Annotator type exposes the following members:

### Constructors
| Constructor | Description |
| :- | :- |
| [__init__](/annotation/python-net/groupdocs.annotation/annotator/__init__/#file_path) | Initializes annotator class which accepts a document path. |
| [__init__](/annotation/python-net/groupdocs.annotation/annotator/__init__/#file_path-load_options) | Initializes annotator class which accepts document path and options. |
| [__init__](/annotation/python-net/groupdocs.annotation/annotator/__init__/#file_path-settings) | Initializes annotator class which accepts document path and settings. |
| [__init__](/annotation/python-net/groupdocs.annotation/annotator/__init__/#file_path-load_options-settings) | Initializes annotator class which accept document path, options and settings. |
| [__init__](/annotation/python-net/groupdocs.annotation/annotator/__init__/#document) | Initializes annotator class which accepts a document stream. |
| [__init__](/annotation/python-net/groupdocs.annotation/annotator/__init__/#document-load_options) | Initializes annotator class which accepts a document stream and options. |
| [__init__](/annotation/python-net/groupdocs.annotation/annotator/__init__/#document-settings) | Initializes annotator class which accepts a document stream and settings. |
| [__init__](/annotation/python-net/groupdocs.annotation/annotator/__init__/#document-load_options-settings) | Initializes annotator class which accepts a document stream, load options, and settings. |

### Methods
| Method | Description |
| :- | :- |
| [add](/annotation/python-net/groupdocs.annotation/annotator/add/#annotation) | Adds annotation to document. |
| [add](/annotation/python-net/groupdocs.annotation/annotator/add/#annotations) | Adds a collection of annotations to a document. |
| [add_annotation_base](/annotation/python-net/groupdocs.annotation/annotator/add_annotation_base/) |  |
| [add_list](/annotation/python-net/groupdocs.annotation/annotator/add_list/) |  |
| [dispose](/annotation/python-net/groupdocs.annotation/annotator/dispose/) | Dispose. |
| [export_annotations_to_xml_file](/annotation/python-net/groupdocs.annotation/annotator/export_annotations_to_xml_file/#output_path) | Exports annotations from the document to an XML file. |
| [export_annotations_to_xml_file_file](/annotation/python-net/groupdocs.annotation/annotator/export_annotations_to_xml_file_file/) |  |
| [export_annotations_to_xml_file_string](/annotation/python-net/groupdocs.annotation/annotator/export_annotations_to_xml_file_string/) |  |
| [get](/annotation/python-net/groupdocs.annotation/annotator/get/) | Gets collections of document annotations. |
| [get](/annotation/python-net/groupdocs.annotation/annotator/get/#type) | Returns a collection of document annotations filtered by the specified annotation type. |
| [get_annotation_type](/annotation/python-net/groupdocs.annotation/annotator/get_annotation_type/) |  |
| [get_version](/annotation/python-net/groupdocs.annotation/annotator/get_version/#version) | Retrieves annotations from a specific version. |
| [get_version_object](/annotation/python-net/groupdocs.annotation/annotator/get_version_object/) |  |
| [get_versions_list](/annotation/python-net/groupdocs.annotation/annotator/get_versions_list/) | Retrieves the list of versions. |
| [import_annotations_from_xml_file](/annotation/python-net/groupdocs.annotation/annotator/import_annotations_from_xml_file/#file_path) | Export annotations from XML file. |
| [import_annotations_from_xml_file_file](/annotation/python-net/groupdocs.annotation/annotator/import_annotations_from_xml_file_file/) |  |
| [import_annotations_from_xml_file_string](/annotation/python-net/groupdocs.annotation/annotator/import_annotations_from_xml_file_string/) |  |
| [remove](/annotation/python-net/groupdocs.annotation/annotator/remove/#annotation_id) | Removes an annotation from the document by its identifier. |
| [remove](/annotation/python-net/groupdocs.annotation/annotator/remove/#annotation) | Removes an annotation from the document. |
| [remove](/annotation/python-net/groupdocs.annotation/annotator/remove/#annotation_ids) | Removes a collection of annotations from the document using the provided annotation IDs. |
| [remove](/annotation/python-net/groupdocs.annotation/annotator/remove/#annotations_to_delete) | Removes collection of annotations from document. |
| [remove_annotation_base](/annotation/python-net/groupdocs.annotation/annotator/remove_annotation_base/) |  |
| [remove_int32](/annotation/python-net/groupdocs.annotation/annotator/remove_int32/) |  |
| [remove_list](/annotation/python-net/groupdocs.annotation/annotator/remove_list/) |  |
| [save](/annotation/python-net/groupdocs.annotation/annotator/save/) | Saves document after adding, updating or removing annotations. |
| [save](/annotation/python-net/groupdocs.annotation/annotator/save/#save_options) | Saves the document after adding, updating, or removing annotations. |
| [save](/annotation/python-net/groupdocs.annotation/annotator/save/#document) | Saves document after adding, updating or removing annotations. |
| [save](/annotation/python-net/groupdocs.annotation/annotator/save/#file_path) | Saves the document after adding, updating, or removing annotations. |
| [save](/annotation/python-net/groupdocs.annotation/annotator/save/#document-save_options) | Saves document after adding, updating or removing annotations. |
| [save](/annotation/python-net/groupdocs.annotation/annotator/save/#file_path-save_options) | Saves document after adding, updating or removing annotations. |
| [save_file](/annotation/python-net/groupdocs.annotation/annotator/save_file/) |  |
| [save_save_options](/annotation/python-net/groupdocs.annotation/annotator/save_save_options/) |  |
| [save_stream](/annotation/python-net/groupdocs.annotation/annotator/save_stream/) |  |
| [save_streams](/annotation/python-net/groupdocs.annotation/annotator/save_streams/) |  |
| [save_string](/annotation/python-net/groupdocs.annotation/annotator/save_string/) |  |
| [update](/annotation/python-net/groupdocs.annotation/annotator/update/#new_annotation) | Updates document annotation by id. |
| [update](/annotation/python-net/groupdocs.annotation/annotator/update/#annotations) | Updates collection of document annotations by overriding the previous list with a new one. |
| [update_annotation_base](/annotation/python-net/groupdocs.annotation/annotator/update_annotation_base/) |  |
| [update_list](/annotation/python-net/groupdocs.annotation/annotator/update_list/) |  |

### Properties
| Property | Description |
| :- | :- |
| [document](/annotation/python-net/groupdocs.annotation/annotator/document/) | The document contains various information about the uploaded document. |
| [process_pages](/annotation/python-net/groupdocs.annotation/annotator/process_pages/) | The count of processed pages. |
| [rotation](/annotation/python-net/groupdocs.annotation/annotator/rotation/) | The document rotation angle. |

### Example

```python
from groupdocs.annotation import Annotator

def export_annotations_to_xml():
    with Annotator("./annotated.pdf") as annotator:
        annotator.export_annotations_to_xml_file(output_path="./exported_annotations.xml")
    print("Exported annotations to ./exported_annotations.xml.")
```

### Guides
Task guides that use `Annotator`:

* [AI agents and LLM integration](/annotation/python-net/guides/agents-and-llm-integration/)
* [Generate document preview](/annotation/python-net/guides/generate-document-preview/)
* [Loading documents](/annotation/python-net/guides/loading-documents/)
* [Saving documents](/annotation/python-net/guides/saving-documents/)
* [Add annotations](/annotation/python-net/guides/add-annotations/)
* [Comments and replies](/annotation/python-net/guides/comments-and-replies/)
* [Import and export annotations](/annotation/python-net/guides/import-export-annotations/)
* [Manage annotations](/annotation/python-net/guides/manage-annotations/)
* [Hello, World!](/annotation/python-net/guides/hello-world/)
* [GroupDocs.Annotation for Python via .NET Overview](/annotation/python-net/guides/product-overview/)

### See Also
* module [`groupdocs.annotation`](/annotation/python-net/groupdocs.annotation/)
