---
title: RadioButtonFormFieldSignature
second_title: GroupDocs.Signature för .NET API-referens
description: Innehåller egenskaper för formulärfältsignatur för radioknappsinmatning.
type: docs
weight: 820
url: /sv/net/groupdocs.signature.domain/radiobuttonformfieldsignature/
---
## RadioButtonFormFieldSignature class

Innehåller egenskaper för formulärfältsignatur för radioknappsinmatning.

```csharp
public sealed class RadioButtonFormFieldSignature : FormFieldSignature
```

## Konstruktörer

| namn | Beskrivning |
| --- | --- |
| [RadioButtonFormFieldSignature](radiobuttonformfieldsignature#constructor)(string) | Skapar RadioButtonField-signatur med fördefinierat namn. |
| [RadioButtonFormFieldSignature](radiobuttonformfieldsignature#constructor_1)(string, List&lt;string&gt;) | Skapar RadioButtonFieldSignature med fördefinierat namn och objektlista. |
| [RadioButtonFormFieldSignature](radiobuttonformfieldsignature#constructor_2)(string, List&lt;string&gt;, object) | Skapar RadioButtonFieldSignature med fördefinierat namn, objektlista och valt värde. |

## Egenskaper

| namn | Beskrivning |
| --- | --- |
| [CreatedOn](../../groupdocs.signature.domain/basesignature/createdon) { get; set; } | Hämta eller ställ in datum för att skapa signaturen. |
| [Deleted](../../groupdocs.signature.domain/basesignature/deleted) { get; } | Hämta flaggan som indikerar om denna signatur togs bort från dokumentet. Den här egenskapen används endast för dokumenthistorikloggposter för att behålla listan över raderade signaturer. |
| [Height](../../groupdocs.signature.domain/basesignature/height) { get; set; } | Anger signaturens höjd. |
| [IsSignature](../../groupdocs.signature.domain/basesignature/issignature) { get; set; } | Hämta eller ange flagga för att indikera om denna komponent är signatur eller dokumentinnehåll. Den här egenskapen används med uppdateringsmetoden för att ställa in element som signatur (true) eller dokumentelement (false). |
| [Items](../../groupdocs.signature.domain/radiobuttonformfieldsignature/items) { get; set; } | Hämta eller ställ in alternativlista för alternativknappar. |
| [Left](../../groupdocs.signature.domain/basesignature/left) { get; set; } | Anger signaturens vänstra position. |
| [ModifiedOn](../../groupdocs.signature.domain/basesignature/modifiedon) { get; set; } | Hämta eller ställ in datum för signaturändring. |
| [Name](../../groupdocs.signature.domain/formfieldsignature/name) { get; set; } | Anger unikt formulärfältsnamn. |
| [PageNumber](../../groupdocs.signature.domain/basesignature/pagenumber) { get; } | Anger sidsignaturen som hittades på. |
| [Selected](../../groupdocs.signature.domain/radiobuttonformfieldsignature/selected) { get; set; } | Innehåller valt värde. |
| [SignatureId](../../groupdocs.signature.domain/basesignature/signatureid) { get; } | Unik signaturidentifierare för att ändra signaturen i dokumentet över Uppdatera eller Ta bort metoder. Den här egenskapen kommer att ställas in automatiskt efter att Sign- eller Sökmetoden anropas. Om den här egenskapen sparades innan den kan ställas in manuellt för att manipulera signaturen. |
| [SignatureType](../../groupdocs.signature.domain/basesignature/signaturetype) { get; } | Anger typen av signatur. |
| [Top](../../groupdocs.signature.domain/basesignature/top) { get; set; } | Anger signaturens topposition. |
| [Type](../../groupdocs.signature.domain/formfieldsignature/type) { get; } | Anger formulärfältstyp. |
| [Value](../../groupdocs.signature.domain/formfieldsignature/value) { get; set; } | Anger formulärfältdataobjekt. |
| [Width](../../groupdocs.signature.domain/basesignature/width) { get; set; } | Anger signaturens bredd. |

## Metoder

| namn | Beskrivning |
| --- | --- |
| override [Clone](../../groupdocs.signature.domain/radiobuttonformfieldsignature/clone)() | Clone FormField Signature-instans. |
| override [Equals](../../groupdocs.signature.domain/radiobuttonformfieldsignature/equals)(object) | Skriver över Equals-metoden för att jämföra signaturegenskaper |
| override [GetHashCode](../../groupdocs.signature.domain/radiobuttonformfieldsignature/gethashcode)() | Åsidosätter GetHashCode method |

### Se även

* class [FormFieldSignature](../formfieldsignature)
* namnutrymme [GroupDocs.Signature.Domain](../../groupdocs.signature.domain)
* hopsättning [GroupDocs.Signature](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Signature.dll -->
