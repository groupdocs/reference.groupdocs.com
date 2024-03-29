---
title: VerificationResult
second_title: GroupDocs.Signature för .NET API-referens
description: Instans för att behålla resultaten av verifieringsprocessen.
type: docs
weight: 1050
url: /sv/net/groupdocs.signature.domain/verificationresult/
---
## VerificationResult class

Instans för att behålla resultaten av verifieringsprocessen.

```csharp
public class VerificationResult : IResult
```

## Egenskaper

| namn | Beskrivning |
| --- | --- |
| [DestinDocumentSize](../../groupdocs.signature.domain/verificationresult/destindocumentsize) { get; } | Returnerar måldokumentets storlek. För verifiering innehåller denna variabel alltid noll. |
| [IsValid](../../groupdocs.signature.domain/verificationresult/isvalid) { get; } | Returnerar sant om verifieringsprocessen lyckades annars false. |
| [ProcessingTime](../../groupdocs.signature.domain/verificationresult/processingtime) { get; } | Returnerar exekveringstiden för processen i millisekunder. |
| [SourceDocumentSize](../../groupdocs.signature.domain/verificationresult/sourcedocumentsize) { get; } | Returnerar källdokumentets storlek i bytes |
| [Succeeded](../../groupdocs.signature.domain/verificationresult/succeeded) { get; } | Lista över framgångsrika verifierade signaturer[`BaseSignature`](../basesignature) . |
| [TotalSignatures](../../groupdocs.signature.domain/verificationresult/totalsignatures) { get; } | Returnerar det totala antalet behandlade signaturer |

### Se även

* interface [IResult](../iresult)
* namnutrymme [GroupDocs.Signature.Domain](../../groupdocs.signature.domain)
* hopsättning [GroupDocs.Signature](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Signature.dll -->
