---
title: GroupDocs.Redaction.Integration
second_title: GroupDocs.Redaction for .NET API Reference
description: The Integration namespace provides interfaces and classes used to integrate documents of different formats with GroupDocs.Redaction.
type: docs
weight: 40
url: /net/groupdocs.redaction.integration/
---
The Integration namespace provides interfaces and classes, used to integrate documents of different formats with GroupDocs.Redaction.

## Classes

| Class | Description |
| --- | --- |
| [DocumentFormatInstance](./documentformatinstance) | Represents a specific format of a document. Implement this class to add your own document types. |
| [MetadataCollection](./metadatacollection) | Represents a dictionary of [`MetadataItem`](../groupdocs.redaction.integration/metadataitem) with its title as a key. |
| [MetadataItem](./metadataitem) | Represents an item of metadata, common for all supported formats and used in metadata redactions. |
## Interfaces

| Interface | Description |
| --- | --- |
| [IAnnotatedDocument](./iannotateddocument) | Defines methods that are required for access to annotations, such as comments. Needs to be implemented by [`DocumentFormatInstance`](../groupdocs.redaction.integration/documentformatinstance)-derived class to perform annotation redactions. |
| [ICellularFormatInstance](./icellularformatinstance) | Defines methods that are required for access to spreadsheet formats, having one or many worksheets. |
| [IFixedFormatDocument](./ifixedformatdocument) | Defines methods that are required for access formats of fixed structure, such as PDF or presentations. |
| [IImageFormatInstance](./iimageformatinstance) | Defines methods that are required for raster image format redactions. |
| [IMetadataAccess](./imetadataaccess) | Defines methods that are required for access to metadata of a document, if format supports it. |
| [IPaginatedDocument](./ipaginateddocument) | Defines methods that are required to manipulate a document's pages. Needs to be implemented by [`DocumentFormatInstance`](../groupdocs.redaction.integration/documentformatinstance)-derived class to perform page redactions. |
| [IPreviewable](./ipreviewable) | Defines methods to create preview of the document. |
| [IRasterizableDocument](./irasterizabledocument) | Defines methods that are required for saving document in any binary form. Built-in types save a document as a PDF with images of its pages. |
| [ITextualFormatInstance](./itextualformatinstance) | Defines methods that are required for redacting textual data in any document, containing text. |

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.redaction.dll -->
