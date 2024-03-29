---
title: SaveOptions
second_title: GroupDocs.Redaction voor .NET API-referentie
description: Biedt opties voor het wijzigen van een uitvoerbestandsnaam en/of het converteren van het document naar op afbeeldingen gebaseerde PDF rasterisatie.
type: docs
weight: 380
url: /nl/net/groupdocs.redaction.options/saveoptions/
---
## SaveOptions class

Biedt opties voor het wijzigen van een uitvoerbestandsnaam en/of het converteren van het document naar op afbeeldingen gebaseerde PDF (rasterisatie).

```csharp
public class SaveOptions
```

## Constructeurs

| Naam | Beschrijving |
| --- | --- |
| [SaveOptions](saveoptions#constructor)() | Initialiseert een nieuwe instantie met standaardwaarden: rasteren naar PDF - false, achtervoegsel toevoegen - false. |
| [SaveOptions](saveoptions#constructor_1)(bool, string) | Initialiseert een nieuwe instantie met opgegeven parameters. |

## Eigenschappen

| Naam | Beschrijving |
| --- | --- |
| [AddSuffix](../../groupdocs.redaction.options/saveoptions/addsuffix) { get; set; } | Haalt of stelt een waarde in die aangeeft of de bestandsnaam moet worden gewijzigd voordat deze wordt opgeslagen. Standaard onwaar. |
| [Rasterization](../../groupdocs.redaction.options/saveoptions/rasterization) { get; } | Haalt de rasterinstellingen op. |
| [RasterizeToPDF](../../groupdocs.redaction.options/saveoptions/rasterizetopdf) { get; set; } | Hiermee wordt een waarde opgehaald of ingesteld die aangeeft of alle pagina's in het document moeten worden geconverteerd naar afbeeldingen en in één PDF-bestand moeten worden geplaatst. |
| [RedactedFileSuffix](../../groupdocs.redaction.options/saveoptions/redactedfilesuffix) { get; set; } | Hiermee wordt een aangepast achtervoegsel voor de naam van het uitvoerbestand opgehaald of ingesteld. Als het niet is gespecificeerd, de[`SaveSuffix`](./savesuffix) constante zal worden gebruikt. |

## Velden

| Naam | Beschrijving |
| --- | --- |
| const [SaveSuffix](../../groupdocs.redaction.options/saveoptions/savesuffix) | Vertegenwoordigt de standaard achtervoegselwaarde, die "geredigeerd" is. |

### Opmerkingen

**Kom meer te weten**

* [Bespaar met standaardopties](https://docs.groupdocs.com/redaction/net/save-with-default-options/)
* [Opslaan in gerasterde PDF](https://docs.groupdocs.com/redaction/net/save-in-rasterized-pdf/)
* [Selecteer specifieke pagina's voor gerasterde PDF](https://docs.groupdocs.com/redaction/net/select-specific-pages-for-rasterized-pdf/)
* [Opslaan in origineel formaat](https://docs.groupdocs.com/redaction/net/save-in-original-format/)
* [Bewaar het overschrijven van het originele bestand](https://docs.groupdocs.com/redaction/net/save-overwriting-original-file/)
* [Opslaan om te streamen](https://docs.groupdocs.com/redaction/net/save-to-stream/)

### Voorbeelden

Het volgende voorbeeld laat zien hoe u een document opslaat met SaveOptions.

```csharp
    using (Redactor redactor = new Redactor(@"C:\sample.pdf"))
    {
       // Documentredactie komt hier
       // ...
    
       // Sla het document op met standaardopties (pagina's converteren naar afbeeldingen, opslaan als PDF)
       redactor.Save();
    
       // Sla het document op in het originele formaat en overschrijf het originele bestand
       redactor.Save(new SaveOptions() { AddSuffix = false, RasterizeToPDF = false });
    
       // Sla het document op in het bestand "*_Redacted.*" in de originele indeling
       redactor.Save(new SaveOptions() { AddSuffix = true, RasterizeToPDF = false });
    
       // Sla het document op in "*_AnyText.*" (bijv. tijdstempel in plaats van "AnyText") in de bestandsnaam zonder rastering
       redactor.Save(new SaveOptions(false, "AnyText"));
    }    
```

### Zie ook

* naamruimte [GroupDocs.Redaction.Options](../../groupdocs.redaction.options)
* montage [GroupDocs.Redaction](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Redaction.dll -->
