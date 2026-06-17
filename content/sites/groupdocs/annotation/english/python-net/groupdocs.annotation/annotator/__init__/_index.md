---
title: __init__ constructor
second_title: GroupDocs.Annotation for Python via .NET API References
description: 
type: docs
url: /python-net/groupdocs.annotation/annotator/__init__/
is_root: false
weight: 10
---


## __init__ {#file_path}

Initializes annotator class which accepts a document path.

- More about file types supported by GroupDocs.Annotation: https://docs.groupdocs.com/display/annotationnet/Supported+Document+Formats
- More about GroupDocs.Annotation for .NET features: https://docs.groupdocs.com/display/annotationnet/Developer+Guide

```python
def __init__(self, file_path):
    ...
```

| Parameter | Type | Description |
| :- | :- | :- |
| file_path | `str` | File path. |

### Example

```python
from groupdocs.annotation import Annotator

with Annotator("./annotated.pdf") as annotator:
    # Export annotations to an XML file
    annotator.export_annotations_to_xml_file(output_path="./exported_annotations.xml")
```

## __init__ {#file_path-load_options}

Initializes annotator class which accepts document path and options.

Learn more

- More about file types supported by GroupDocs.Annotation: https://docs.groupdocs.com/display/annotationnet/Supported+Document+Formats
- More about GroupDocs.Annotation for .NET features: https://docs.groupdocs.com/display/annotationnet/Developer+Guide
- More about how to open and annotate password-protected document: https://docs.groupdocs.com/display/annotationnet/Load+password-protected+documents
- More about how to open and annotate document from URL, FTP, Amazon S3, Azure Blob Storage and others: https://docs.groupdocs.com/display/annotationnet/Loading+documents+from+different+sources

```python
def __init__(self, file_path, load_options):
    ...
```

| Parameter | Type | Description |
| :- | :- | :- |
| file_path | `str` | File path. |
| load_options | `LoadOptions` | Load options. |

### Example

```python
from groupdocs.annotation import Annotator

def export_annotations_to_xml():
    with Annotator("./annotated.pdf") as annotator:
        annotator.export_annotations_to_xml_file(output_path="./exported_annotations.xml")
    print("Exported annotations to ./exported_annotations.xml.")
```

## __init__ {#file_path-settings}

Initializes annotator class which accepts document path and settings.

- More about file types supported by GroupDocs.Annotation: https://docs.groupdocs.com/display/annotationnet/Supported+Document+Formats
- More about GroupDocs.Annotation for .NET features: https://docs.groupdocs.com/display/annotationnet/Developer+Guide

```python
def __init__(self, file_path, settings):
    ...
```

| Parameter | Type | Description |
| :- | :- | :- |
| file_path | `str` | File path. |
| settings | `AnnotatorSettings` | Annotator settings. |

### Example

```python
from groupdocs.annotation import Annotator

with Annotator("./sample.pdf") as annotator:
    # perform annotation operations here
    annotator.save("./output.pdf")
```

## __init__ {#file_path-load_options-settings}

Initializes annotator class which accept document path, options and settings.

Learn more:

- More about file types supported by GroupDocs.Annotation: Document formats supported by GroupDocs.Annotation (https://docs.groupdocs.com/display/annotationnet/Supported+Document+Formats)
- More about GroupDocs.Annotation for .NET features: Developer Guide (https://docs.groupdocs.com/display/annotationnet/Developer+Guide)
- More about how to open and annotate password-protected document: Open and annotate password-protected document (https://docs.groupdocs.com/display/annotationnet/Load+password-protected+documents)
- More about how to open and annotate document from URL, FTP, Amazon S3, Azure Blob Storage and others: Open and annotate documents from third-party storages (https://docs.groupdocs.com/display/annotationnet/Loading+documents+from+different+sources)

```python
def __init__(self, file_path, load_options, settings):
    ...
```

| Parameter | Type | Description |
| :- | :- | :- |
| file_path | `str` | File path. |
| load_options | `LoadOptions` | Load options. |
| settings | `AnnotatorSettings` | Annotator settings. |

### Example

```python
from groupdocs.annotation import Annotator

def export_annotations_to_xml():
    with Annotator("./annotated.pdf") as annotator:
        annotator.export_annotations_to_xml_file(output_path="./exported_annotations.xml")
    print("Exported annotations to ./exported_annotations.xml.")
```

## __init__ {#document}

Initializes annotator class which accepts a document stream.

Learn more

- More about file types supported by GroupDocs.Annotation: https://docs.groupdocs.com/display/annotationnet/Supported+Document+Formats
- More about GroupDocs.Annotation for .NET features: https://docs.groupdocs.com/display/annotationnet/Developer+Guide

```python
def __init__(self, document):
    ...
```

| Parameter | Type | Description |
| :- | :- | :- |
| document | `io.RawIOBase` | Document stream. |

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

## __init__ {#document-load_options}

Initializes annotator class which accepts a document stream and options.

```python
def __init__(self, document, load_options):
    ...
```

| Parameter | Type | Description |
| :- | :- | :- |
| document | `io.RawIOBase` | Document stream. |
| load_options | `LoadOptions` | Load options. - More about file types supported by GroupDocs.Annotation: https://docs.groupdocs.com/display/annotationnet/Supported+Document+Formats - More about GroupDocs.Annotation for .NET features: https://docs.groupdocs.com/display/annotationnet/Developer+Guide - More about how to open and annotate password-protected document: https://docs.groupdocs.com/display/annotationnet/Load+password-protected+documents - More about how to open and annotate document from URL, FTP, Amazon S3, Azure Blob Storage and others: https://docs.groupdocs.com/display/annotationnet/Loading+documents+from+different+sources |

### Example

```python
from groupdocs.annotation import Annotator

def export_annotations_to_xml():
    with Annotator("./annotated.pdf") as annotator:
        annotator.export_annotations_to_xml_file(output_path="./exported_annotations.xml")
    print("Exported annotations to ./exported_annotations.xml.")
```

## __init__ {#document-settings}

Initializes annotator class which accepts a document stream and settings.

- More about file types supported by GroupDocs.Annotation: [Document formats supported by GroupDocs.Annotation](https://docs.groupdocs.com/display/annotationnet/Supported+Document+Formats)
- More about GroupDocs.Annotation for .NET features: [Developer Guide](https://docs.groupdocs.com/display/annotationnet/Developer+Guide)

```python
def __init__(self, document, settings):
    ...
```

| Parameter | Type | Description |
| :- | :- | :- |
| document | `io.RawIOBase` | Document stream. |
| settings | `AnnotatorSettings` | Annotator settings. |

### Example

```python
from groupdocs.annotation import Annotator

def export_annotations_to_xml():
    with Annotator("./annotated.pdf") as annotator:
        annotator.export_annotations_to_xml_file(output_path="./exported_annotations.xml")
    print("Exported annotations to ./exported_annotations.xml.")
```

## __init__ {#document-load_options-settings}

Initializes annotator class which accepts a document stream, load options, and settings.

Learn more.

- More about file types supported by GroupDocs.Annotation: https://docs.groupdocs.com/display/annotationnet/Supported+Document+Formats
- More about GroupDocs.Annotation for .NET features: https://docs.groupdocs.com/display/annotationnet/Developer+Guide
- More about how to open and annotate password-protected document: https://docs.groupdocs.com/display/annotationnet/Load+password-protected+documents
- More about how to open and annotate document from URL, FTP, Amazon S3, Azure Blob Storage and others: https://docs.groupdocs.com/display/annotationnet/Loading+documents+from+different+sources

```python
def __init__(self, document, load_options, settings):
    ...
```

| Parameter | Type | Description |
| :- | :- | :- |
| document | `io.RawIOBase` | Document stream. |
| load_options | `LoadOptions` | Load options. |
| settings | `AnnotatorSettings` | Annotator settings. |

### See Also
* class [`Annotator`](/annotation/python-net/groupdocs.annotation/annotator/)
