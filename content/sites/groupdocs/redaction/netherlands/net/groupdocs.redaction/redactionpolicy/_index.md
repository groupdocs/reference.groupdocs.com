---
title: RedactionPolicy
second_title: GroupDocs.Redaction voor .NET API-referentie
description: Vertegenwoordigt een opschoningsbeleid met een reeks specifieke redacties die moeten worden toegepast.
type: docs
weight: 410
url: /nl/net/groupdocs.redaction/redactionpolicy/
---
## RedactionPolicy class

Vertegenwoordigt een opschoningsbeleid, met een reeks specifieke redacties die moeten worden toegepast.

```csharp
public class RedactionPolicy
```

## Constructeurs

| Naam | Beschrijving |
| --- | --- |
| [RedactionPolicy](redactionpolicy#constructor)() | Maakt een nieuw exemplaar van redactiebeleid. |
| [RedactionPolicy](redactionpolicy#constructor_1)(Redaction[]) | Maakt een nieuw exemplaar van het redactiebeleid met een specifieke lijst met redacties. |

## Eigenschappen

| Naam | Beschrijving |
| --- | --- |
| [Redactions](../../groupdocs.redaction/redactionpolicy/redactions) { get; } | Krijgt een reeks volledig geconfigureerde[`Redaction`](../redaction) -afgeleide klassen. |

## methoden

| Naam | Beschrijving |
| --- | --- |
| static [Load](../../groupdocs.redaction/redactionpolicy/load#load)(Stream) | Laadt een exemplaar van[`RedactionPolicy`](../redactionpolicy) uit een stream. |
| static [Load](../../groupdocs.redaction/redactionpolicy/load#load_1)(string) | Laadt een exemplaar van[`RedactionPolicy`](../redactionpolicy) vanuit een bestandspad. |
| [Save](../../groupdocs.redaction/redactionpolicy/save#save)(Stream) | Slaat het redactiebeleid op in een stream. |
| [Save](../../groupdocs.redaction/redactionpolicy/save#save_1)(string) | Slaat het redactiebeleid op in een bestand. |

### Opmerkingen

**Kom meer te weten**

* Meer informatie over beleid: [Gebruik van redactiebeleid](https://docs.groupdocs.com/redaction/net/use-redaction-policies/)
* Meer informatie over het toepassen van redacties: [Basisprincipes van redactie](https://docs.groupdocs.com/redaction/net/redaction-basics/)

### Voorbeelden

Het volgende voorbeeld laat zien hoe u een redactiebeleid toepast op alle bestanden in een bepaalde inkomende map en opslaat in een van de uitgaande mappen - voor succesvol bijgewerkte bestanden en voor mislukte bestanden.

Het volgende voorbeeld bevat een voorbeeld van een XML-beleidsbestand met voorbeeldconfiguraties voor alle typen redactie.

```csharp
RedactionPolicy policy = RedactionPolicy.Load("RedactionPolicy.xml");
foreach (var fileEntry in Directory.GetFileNames("C:\\Inbound")) 
{
     using (Redactor redactor = new Redactor(Path.Combine("C:\\Inbound\\", fileEntry)))
     {
    	     RedactorChangeLog result = redactor.Apply(policy);
    	     String resultFolder = result.Status != RedactionStatus.Failed ? "C:\\Outbound\\Done\\" : "C:\\Outbound\\Failed\\";
    	     using (Stream fileStream = File.Open(Path.Combine(resultFolder, fileEntry), FileMode.Open, FileAccess.ReadWrite))
   	     {
               redactor.Save(fileStream, new RasterizationOptions() { Enabled = false });
   	     }        
     }
}   
```

```csharp
<?xml version="1.0" encoding="utf-8"?>  
<redactionPolicy xmlns = "http://www.groupdocs.com/redaction" >
  <regexRedaction regularExpression="(dolor)" actionType="ReplaceString" replacement="foobar" />  
  <exactPhraseRedaction searchPhrase = "dolor" caseSensitive="true" actionType="DrawBox" color="Red" />   
  
  <cellColumnRedaction regularExpression = "(foo)bar1" replacement="[red1]" columnIndex="1" worksheetIndex="2" /> 
  <cellColumnRedaction regularExpression = "(foo)bar2" replacement="[red2]" wokrsheetName="Sample" /> 
  
  <eraseMetadataRedaction filter = "All" />
  <metadataSearchRedaction filter="Title, Author" replacement="foobar" valueExpression="(metasearch)" keyExpression="" />  
  
 <annotationRedaction regularExpression = "(anno1)" replacement="foobar" />  
 <deleteAnnotationRedaction regularExpression = "(anno2)" />

 <imageAreaRedaction pointX="15" pointY="17" width="200" height="10" color="#AA50FC"  />  
 <imageAreaRedaction pointX = "110" pointY="120" width="60" height="20" color="Magenta"  />  
</redactionPolicy>
```

### Zie ook

* naamruimte [GroupDocs.Redaction](../../groupdocs.redaction)
* montage [GroupDocs.Redaction](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Redaction.dll -->
