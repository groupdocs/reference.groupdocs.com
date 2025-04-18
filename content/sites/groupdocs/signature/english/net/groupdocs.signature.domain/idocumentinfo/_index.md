---
title: IDocumentInfo
second_title: GroupDocs.Signature for .NET API Reference
description: Defines document description properties.
type: docs
weight: 680
url: /net/groupdocs.signature.domain/idocumentinfo/
---
## IDocumentInfo interface

Defines document description properties.

```csharp
public interface IDocumentInfo
```

## Properties

| Name | Description |
| --- | --- |
| [BarcodeSignatures](../../groupdocs.signature.domain/idocumentinfo/barcodesignatures) { get; } | Collection of document barcode signatures added or updated by [`Signature`](../../groupdocs.signature/signature) methods. |
| [DigitalSignatures](../../groupdocs.signature.domain/idocumentinfo/digitalsignatures) { get; } | Collection of document digital signatures added or updated by [`Signature`](../../groupdocs.signature/signature) methods. |
| [Documents](../../groupdocs.signature.domain/idocumentinfo/documents) { get; } | Collection of all existing documents within the archive files. This property is supported only for Archive document types. |
| [FileType](../../groupdocs.signature.domain/idocumentinfo/filetype) { get; set; } | File format type |
| [FormFields](../../groupdocs.signature.domain/idocumentinfo/formfields) { get; } | Collection of all existing supported Form Fields in the document. This property is supported only for Pdf and Word Processing document types. |
| [FormFieldSignatures](../../groupdocs.signature.domain/idocumentinfo/formfieldsignatures) { get; } | Collection of document Form Field signatures added or updated by [`Signature`](../../groupdocs.signature/signature) methods. |
| [ImageSignatures](../../groupdocs.signature.domain/idocumentinfo/imagesignatures) { get; } | Collection of document image signatures added or updated by [`Signature`](../../groupdocs.signature/signature) methods. |
| [MaxPageHeight](../../groupdocs.signature.domain/idocumentinfo/maxpageheight) { get; set; } | Specifies max page height. |
| [MetadataSignatures](../../groupdocs.signature.domain/idocumentinfo/metadatasignatures) { get; } | Collection of document Metadata signatures. |
| [PageCount](../../groupdocs.signature.domain/idocumentinfo/pagecount) { get; set; } | Document pages count. |
| [Pages](../../groupdocs.signature.domain/idocumentinfo/pages) { get; set; } | Collection of document pages descriptions. |
| [ProcessLogs](../../groupdocs.signature.domain/idocumentinfo/processlogs) { get; } | Collection of document history process logs. |
| [QrCodeSignatures](../../groupdocs.signature.domain/idocumentinfo/qrcodesignatures) { get; } | Collection of document QR-code signatures added or updated by [`Signature`](../../groupdocs.signature/signature) methods. |
| [Signatures](../../groupdocs.signature.domain/idocumentinfo/signatures) { get; } | Collection of document all types signatures [`BaseSignature`](../basesignature). |
| [Size](../../groupdocs.signature.domain/idocumentinfo/size) { get; set; } | Document size in bytes. |
| [TextSignatures](../../groupdocs.signature.domain/idocumentinfo/textsignatures) { get; } | Collection of document text signatures added or updated by [`Signature`](../../groupdocs.signature/signature) methods. |
| [WidthForMaxHeight](../../groupdocs.signature.domain/idocumentinfo/widthformaxheight) { get; set; } | Specifies width for max page height. |

### See Also

* namespace [GroupDocs.Signature.Domain](../../groupdocs.signature.domain)
* assembly [GroupDocs.Signature](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.signature.dll -->
