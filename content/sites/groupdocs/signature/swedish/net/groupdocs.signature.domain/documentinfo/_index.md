---
title: DocumentInfo
second_title: GroupDocs.Signature för .NET API-referens
description: Definierar dokumentbeskrivningsegenskaper.
type: docs
weight: 160
url: /sv/net/groupdocs.signature.domain/documentinfo/
---
## DocumentInfo class

Definierar dokumentbeskrivningsegenskaper.

```csharp
public class DocumentInfo : IDocumentInfo
```

## Konstruktörer

| namn | Beskrivning |
| --- | --- |
| [DocumentInfo](documentinfo)() | Initierar en ny instans av[`DocumentInfo`](../documentinfo)class. |

## Egenskaper

| namn | Beskrivning |
| --- | --- |
| [BarcodeSignatures](../../groupdocs.signature.domain/documentinfo/barcodesignatures) { get; } | Samling av dokumentstreckkodsignaturer tillagda eller uppdaterade av[`Signature`](../../groupdocs.signature/signature) metoder. |
| [DigitalSignatures](../../groupdocs.signature.domain/documentinfo/digitalsignatures) { get; } | Samling av digitala dokumentsignaturer tillagda eller uppdaterade av[`Signature`](../../groupdocs.signature/signature) metoder. |
| [FileType](../../groupdocs.signature.domain/documentinfo/filetype) { get; set; } | Filformatstyp. |
| [FormFields](../../groupdocs.signature.domain/documentinfo/formfields) { get; } | Samling av alla befintliga formulärfält som stöds i dokumentet. Den här egenskapen stöds endast för dokumenttyperna PDF och ordbehandling. |
| [FormFieldSignatures](../../groupdocs.signature.domain/documentinfo/formfieldsignatures) { get; } | Samling av dokument Form Fältsignaturer tillagda eller uppdaterade av[`Signature`](../../groupdocs.signature/signature) metoder. |
| [ImageSignatures](../../groupdocs.signature.domain/documentinfo/imagesignatures) { get; } | Samling av dokumentbildsignaturer tillagda eller uppdaterade av[`Signature`](../../groupdocs.signature/signature) metoder. |
| [MaxPageHeight](../../groupdocs.signature.domain/documentinfo/maxpageheight) { get; set; } | Anger max sidhöjd. |
| [MetadataSignatures](../../groupdocs.signature.domain/documentinfo/metadatasignatures) { get; } | Samling av dokumentmetadatasignaturer. |
| [PageCount](../../groupdocs.signature.domain/documentinfo/pagecount) { get; set; } | Dokumentsidor räknas. |
| [Pages](../../groupdocs.signature.domain/documentinfo/pages) { get; set; } | Samling av beskrivningar av dokumentsidor. |
| [ProcessLogs](../../groupdocs.signature.domain/documentinfo/processlogs) { get; } | Samling av dokumenthistorikprocesser som Sign, Update, Delete. |
| [QrCodeSignatures](../../groupdocs.signature.domain/documentinfo/qrcodesignatures) { get; } | Samling av dokument QR-kodsignaturer tillagda eller uppdaterade av[`Signature`](../../groupdocs.signature/signature) metoder. |
| [Signatures](../../groupdocs.signature.domain/documentinfo/signatures) { get; } | Samling av dokument av alla typer signaturer[`BaseSignature`](../basesignature) . |
| [Size](../../groupdocs.signature.domain/documentinfo/size) { get; set; } | Dokumentstorlek i byte. |
| [TextSignatures](../../groupdocs.signature.domain/documentinfo/textsignatures) { get; } | Samling av dokumenttextsignaturer. |
| [WidthForMaxHeight](../../groupdocs.signature.domain/documentinfo/widthformaxheight) { get; set; } | Anger bredd för max sidhöjd. |

### Se även

* interface [IDocumentInfo](../idocumentinfo)
* namnutrymme [GroupDocs.Signature.Domain](../../groupdocs.signature.domain)
* hopsättning [GroupDocs.Signature](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Signature.dll -->
