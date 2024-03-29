---
title: DocumentAssemblyOptions
second_title: GroupDocs.Assembly för .NET API-referens
description: Anger alternativ som styr beteendet förDocumentAssembler./documentassembler när du sätter ihop ett dokument.
type: docs
weight: 210
url: /sv/net/groupdocs.assembly/documentassemblyoptions/
---
## DocumentAssemblyOptions enumeration

Anger alternativ som styr beteendet för[`DocumentAssembler`](../documentassembler) när du sätter ihop ett dokument.

```csharp
[Flags]
public enum DocumentAssemblyOptions
```

### Värderingar

| namn | Värde | Beskrivning |
| --- | --- | --- |
| None | `0` | Anger standardalternativ. |
| AllowMissingMembers | `1` | Anger att saknade objektmedlemmar ska behandlas som noll-literaler av assemblern. Det här alternativet påverkar endast åtkomst till instanser (det vill säga icke-statiska) objektmedlemmar och tilläggsmetoder. Om det här alternativet inte är inställt, skapar assemblern ett undantag när den stöter på en saknad objektmedlem. |
| UpdateFieldsAndFormulas | `2` | Anger att fält för resultatordbehandlingsdokument och formler för resultatkalkylarksdokument ska uppdateras av assemblern. |
| RemoveEmptyParagraphs | `4` | Anger att assemblern ska ta bort stycken som blir tomma efter att mallsyntaxtaggar har tagits bort eller ersatts med tomma värden. |
| InlineErrorMessages | `8` | Anger att assemblern ska infoga mallsyntaxfelmeddelanden i utdatadokument. Om det här alternativet inte är inställt, skapar assemblern ett undantag när ett syntaxfel stöter på. |
| UseSpreadsheetDataTypes | `10` | Avser endast kalkylarksdokument. Anger att utvärderade uttrycksresultat ska mappas till motsvarande kalkylbladsdatatyper, vilket också påverkar deras standardformatering inom celler. Om det här alternativet inte är inställt, skrivs uttrycksresultat alltid som strängar av assemblern. Det här alternativet har ingen effekt när uttrycksresultat formateras med mallsyntax - uttrycksresultat skrivs alltid som strängar då också. |

### Se även

* namnutrymme [GroupDocs.Assembly](../../groupdocs.assembly)
* hopsättning [GroupDocs.Assembly](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Assembly.dll -->
