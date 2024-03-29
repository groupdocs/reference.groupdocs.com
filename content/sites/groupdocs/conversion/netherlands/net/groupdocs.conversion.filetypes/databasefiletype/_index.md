---
title: DatabaseFileType
second_title: GroupDocs.Conversion voor .NET API-referentie
description: Definieert databasedocumenten. Bevat de volgende bestandstypen Nsf./databasefiletype/nsfLog./databasefiletype/logSql./databasefiletype/sql
type: docs
weight: 890
url: /nl/net/groupdocs.conversion.filetypes/databasefiletype/
---
## DatabaseFileType class

Definieert databasedocumenten. Bevat de volgende bestandstypen: [`Nsf`](./nsf)[`Log`](./log)[`Sql`](./sql)

```csharp
public sealed class DatabaseFileType : FileType
```

## Constructeurs

| Naam | Beschrijving |
| --- | --- |
| [DatabaseFileType](databasefiletype)() | Serialisatie-constructor |

## Eigenschappen

| Naam | Beschrijving |
| --- | --- |
| [Description](../../groupdocs.conversion.filetypes/filetype/description) { get; } | Bestandstype omschrijving |
| [Extension](../../groupdocs.conversion.filetypes/filetype/extension) { get; } | De bestandsextensie |
| [Family](../../groupdocs.conversion.filetypes/filetype/family) { get; } | De bestandsfamilie |
| [FileFormat](../../groupdocs.conversion.filetypes/filetype/fileformat) { get; } | Het bestandsformaat |

## methoden

| Naam | Beschrijving |
| --- | --- |
| [CompareTo](../../groupdocs.conversion.contracts/enumeration/compareto)(object) | Vergelijkt huidige object met andere. |
| override [Equals](../../groupdocs.conversion.filetypes/filetype/equals)(Enumeration) | Bepaalt of twee objectinstanties gelijk zijn. |
| override [Equals](../../groupdocs.conversion.contracts/enumeration/equals)(object) | Bepaalt of twee objectinstanties gelijk zijn. |
| override [GetHashCode](../../groupdocs.conversion.contracts/enumeration/gethashcode)() | Dient als de standaard hash-functie. |
| override [ToString](../../groupdocs.conversion.filetypes/filetype/tostring)() | Tekenreeksweergave |

## Velden

| Naam | Beschrijving |
| --- | --- |
| static readonly [Log](../../groupdocs.conversion.filetypes/databasefiletype/log) | Een bestand met de extensie .log bevat de lijst met platte tekst met tijdstempel. Gewoonlijk worden bepaalde activiteitsdetails vastgelegd door de software of besturingssystemen om de ontwikkelaars of gebruikers te helpen bij het volgen van wat er in een bepaalde periode gebeurde. Meer informatie over dit bestandsformaat[hier](https://docs.fileformat.com/database/log) . |
| static readonly [Nsf](../../groupdocs.conversion.filetypes/databasefiletype/nsf) | Een bestand met de extensie .nsf (Notes Storage Facility) is een databasebestandsindeling die wordt gebruikt door de IBM Notes-software, voorheen bekend als Lotus Notes. Het definieert het schema om verschillende soorten objecten op te slaan, zoals e-mails, afspraken, documenten, formulieren en weergaven. Meer informatie over dit bestandsformaat[hier](https://docs.fileformat.com/database/nsf) . |
| static readonly [Sql](../../groupdocs.conversion.filetypes/databasefiletype/sql) | Een bestand met de extensie .sql is een Structured Query Language (SQL)-bestand dat code bevat om met relationele databases te werken. Het wordt gebruikt om SQL-instructies te schrijven voor CRUD-bewerkingen (Create, Read, Update en Delete) op databases. Meer informatie over dit bestandsformaat[hier](https://docs.fileformat.com/database/sql) . |

### Zie ook

* class [FileType](../filetype)
* naamruimte [GroupDocs.Conversion.FileTypes](../../groupdocs.conversion.filetypes)
* montage [GroupDocs.Conversion](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Conversion.dll -->
