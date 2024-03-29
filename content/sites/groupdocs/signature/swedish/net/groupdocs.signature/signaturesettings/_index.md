---
title: SignatureSettings
second_title: GroupDocs.Signature för .NET API-referens
description: Definierar inställningar för anpassningSignature./signature beteende.
type: docs
weight: 1890
url: /sv/net/groupdocs.signature/signaturesettings/
---
## SignatureSettings class

Definierar inställningar för anpassning[`Signature`](../signature) beteende.

```csharp
public class SignatureSettings
```

## Konstruktörer

| namn | Beskrivning |
| --- | --- |
| [SignatureSettings](signaturesettings#constructor)() | Skapar standard SignatureSettings-instans med standardvärden. |
| [SignatureSettings](signaturesettings#constructor_1)(ILogger) | Skapar standard SignatureSettings-instans med Logger-implementeringen. |

## Egenskaper

| namn | Beskrivning |
| --- | --- |
| [DefaultCulture](../../groupdocs.signature/signaturesettings/defaultculture) { get; set; } | Hämtar eller ställer in standardkultur som ska användas under dokumentbehandling. Standardvärdet är "en-US". |
| [IncludeStandardMetadataSignatures](../../groupdocs.signature/signaturesettings/includestandardmetadatasignatures) { get; set; } | Hämtar eller ställer in flaggan för att inkludera i metadatalistan de inbäddade standarddokumentmetadatasignaturerna som författare, ägare, dokumentets skapandedatum, ändringsdatum, etc. Om denna flagga är inställd på false (som standard) kommer GetDocumentInfo inte att inkludera dessa metadata signaturer. När denna flagga är inställd på sant kommer dokumentinformationen att inkludera dessa standardmetadatasignaturer. |
| [Logger](../../groupdocs.signature/signaturesettings/logger) { get; } | Loggerimplementationen som används för loggning (fel, varningar, spår).[`ILogger`](../../groupdocs.signature.logging/ilogger) . |
| [LogLevel](../../groupdocs.signature/signaturesettings/loglevel) { get; set; } | Nivån på loggningen för att begränsa meddelanden (Alla, Spår, Varningar, Fel).[`LogLevel`](./loglevel) . Som standard är typen Alla nivåer inställd. |
| [SaveDocumentOnEmptyDelete](../../groupdocs.signature/signaturesettings/savedocumentonemptydelete) { get; set; } | Hämtar eller ställer in flaggan för att återspara källdokument när raderingsmetoden inte har några påverkade signaturer att ta bort. Om denna flagga är inställd på sant (som standard) kommer dokumentet att sparas med motsvarande historikprocesslogg (datum och operationstyp) även om Raderingsmetoden har inga signaturer att ta bort. När denna lägenhet är inställd på falskt källdokument kommer inte att ändras alls. |
| [SaveDocumentOnEmptyUpdate](../../groupdocs.signature/signaturesettings/savedocumentonemptyupdate) { get; set; } | Hämtar eller ställer in flaggan för att återspara källdokument när uppdateringsmetoden inte har några signaturer att uppdatera. Om denna flagga är inställd på sant (som standard) kommer dokumentet att sparas med motsvarande historikprocesslogg (datum och operationstyp) även om Uppdatering metod har inga signaturer att uppdatera. När denna lägenhet är inställd på falskt källdokument kommer inte att ändras alls. |
| [ShowDeletedSignaturesInfo](../../groupdocs.signature/signaturesettings/showdeletedsignaturesinfo) { get; set; } | Hämtar eller ställer in flagga som inkluderar borttagna signaturer i dokumentinforesultat. Varje signatur[`BaseSignature`](../../groupdocs.signature.domain/basesignature) har raderad flagga[`Deleted`](../../groupdocs.signature.domain/basesignature/deleted) för att upptäcka om den har tagits bort. |

### Se även

* namnutrymme [GroupDocs.Signature](../../groupdocs.signature)
* hopsättning [GroupDocs.Signature](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Signature.dll -->
