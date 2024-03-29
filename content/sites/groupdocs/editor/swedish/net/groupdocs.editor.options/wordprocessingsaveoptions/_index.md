---
title: WordProcessingSaveOptions
second_title: GroupDocs.Editor för .NET API-referens
description: Gör det möjligt att ange anpassade alternativ för att generera och spara WordProcessingkompatibla dokument efter att de har redigerats
type: docs
weight: 1240
url: /sv/net/groupdocs.editor.options/wordprocessingsaveoptions/
---
## WordProcessingSaveOptions class

Gör det möjligt att ange anpassade alternativ för att generera och spara WordProcessing-kompatibla dokument efter att de har redigerats

```csharp
public sealed class WordProcessingSaveOptions : ICloneable, ISaveOptions
```

## Konstruktörer

| namn | Beskrivning |
| --- | --- |
| [WordProcessingSaveOptions](wordprocessingsaveoptions)(WordProcessingFormats) | Skapar en ny instans av WordProcessingSaveOptions med specificerat obligatoriskt WordProcessing-utdataformat, medan alla andra parametrar är default |

## Egenskaper

| namn | Beskrivning |
| --- | --- |
| [EnablePagination](../../groupdocs.editor.options/wordprocessingsaveoptions/enablepagination) { get; set; } | Tillåter att aktivera eller inaktivera paginering som kommer att användas för att spara WordProcessing-dokumentet. Om originaldokumentet öppnades och redigerades i pagineringsläge, bör detta alternativ också vara aktiverat. Som standard är inaktiverad. |
| [FontEmbedding](../../groupdocs.editor.options/wordprocessingsaveoptions/fontembedding) { get; set; } | Ansvarig för att bädda in teckensnittsresurser i utgående WordProcessing-dokument. Som standard bäddar inte in några teckensnitt (NotEmbed). |
| [Locale](../../groupdocs.editor.options/wordprocessingsaveoptions/locale) { get; set; } | Tillåter att ställa in åsidosättande standardspråk (språk) för WordProcessing-dokumentet, som kommer att tillämpas under dess skapande. När inte anges (standardvärde), kommer MS Word (eller annat program) att upptäcka (eller välja) dokumentets locale enligt till sina egna inställningar eller andra faktorer. |
| [LocaleBi](../../groupdocs.editor.options/wordprocessingsaveoptions/localebi) { get; set; } | Tillåter att ställa in åsidosättningsspråk (språk) för WordProcessing-dokumentet för RTL-texten (höger till vänster), som kommer att tillämpas under skapandet. När inte anges (standardvärde), MS Word (eller annat program) kommer att upptäcka (eller välja) dokumentet RTL locale enligt sina egna inställningar eller andra faktorer. |
| [LocaleFarEast](../../groupdocs.editor.options/wordprocessingsaveoptions/localefareast) { get; set; } | Tillåter att åsidosätta språket (språket) för WordProcessing-dokumentet för den östasiatiska texten, som kommer att tillämpas under dess skapelse. När inte anges (standardvärde), kommer MS Word (eller annat program) att upptäcka (eller välja ) dokumentet East-Asian locale enligt dess egna inställningar eller andra faktorer. |
| [OptimizeMemoryUsage](../../groupdocs.editor.options/wordprocessingsaveoptions/optimizememoryusage) { get; set; } | Aktiverar minnesoptimeringsmekanismer under dokumentgenerering från HTML, vilket försämrar prestandan som en kostnad för att minska minnesanvändningen. Om du ställer in detta alternativ till sant kan det minska minnesförbrukningen avsevärt samtidigt som stora dokument genereras till priset av långsammare spartid. Standard är falskt (minnesoptimering är inaktiverad för bättre prestanda). |
| [OutputFormat](../../groupdocs.editor.options/wordprocessingsaveoptions/outputformat) { get; set; } | Tillåter att ange ett WordProcessing-format som kommer att användas för att spara document |
| [Password](../../groupdocs.editor.options/wordprocessingsaveoptions/password) { get; set; } | Tillåter att ange, ändra, erhålla eller ta bort ett lösenord, som kommer att användas för att koda det genererade WordProcessing-dokumentet. Ange NULL eller tom sträng för att ta bort (rensa) lösenordet. |
| [Protection](../../groupdocs.editor.options/wordprocessingsaveoptions/protection) { get; set; } | Tillåter att styra och tillämpa dokumentskyddsalternativen för WordProcessing-dokumentet i alla format, som stöder dokumentskydd. Som standard är NULL - dokumentskydd kommer inte att användas. |

## Metoder

| namn | Beskrivning |
| --- | --- |
| [Clone](../../groupdocs.editor.options/wordprocessingsaveoptions/clone)() | Skapar och returnerar en fullständig kopia av denna instans av WordProcessingSaveOptions class |

### Anmärkningar

WordProcessingSaveOptions tillämpas i situationer när det finns en instans av EditableDocument-klassen, som innehåller ett redigerat dokumentinnehåll, och det krävs för att spara detta innehåll i det nya dokumentet i WordProcessing-format.

### Se även

* interface [ISaveOptions](../isaveoptions)
* namnutrymme [GroupDocs.Editor.Options](../../groupdocs.editor.options)
* hopsättning [GroupDocs.Editor](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Editor.dll -->
