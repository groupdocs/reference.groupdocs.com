---
title: IResult
second_title: GroupDocs.Signature för .NET API-referens
description: Gemensamt gränssnitt för signaturprocessresultat.
type: docs
weight: 530
url: /sv/net/groupdocs.signature.domain/iresult/
---
## IResult interface

Gemensamt gränssnitt för signaturprocessresultat.

```csharp
public interface IResult
```

## Egenskaper

| namn | Beskrivning |
| --- | --- |
| [DestinDocumentSize](../../groupdocs.signature.domain/iresult/destindocumentsize) { get; } | Returnerar måldokumentstorlek |
| [Failed](../../groupdocs.signature.domain/iresult/failed) { get; } | Lista över signaturer som inte bearbetades[`BaseSignature`](../basesignature) . |
| [ProcessingTime](../../groupdocs.signature.domain/iresult/processingtime) { get; } | Returnerar exekveringstiden för processen i millisekunder |
| [SourceDocumentSize](../../groupdocs.signature.domain/iresult/sourcedocumentsize) { get; } | Returnerar källdokumentets storlek |
| [Succeeded](../../groupdocs.signature.domain/iresult/succeeded) { get; } | Lista över framgångsrikt bearbetade signaturer[`BaseSignature`](../basesignature) . |
| [TotalSignatures](../../groupdocs.signature.domain/iresult/totalsignatures) { get; } | Returnerar det totala antalet behandlade signaturer |

### Se även

* namnutrymme [GroupDocs.Signature.Domain](../../groupdocs.signature.domain)
* hopsättning [GroupDocs.Signature](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Signature.dll -->
