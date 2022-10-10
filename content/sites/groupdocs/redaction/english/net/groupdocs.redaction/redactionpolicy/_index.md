---
title: RedactionPolicy
second_title: GroupDocs.Redaction for .NET API Reference
description: Represents a sanitization policy containing a set of specific redactions to apply.
type: docs
weight: 400
url: /net/groupdocs.redaction/redactionpolicy/
---
## RedactionPolicy class

Represents a sanitization policy, containing a set of specific redactions to apply.

```csharp
public class RedactionPolicy
```

## Constructors

| Name | Description |
| --- | --- |
| [RedactionPolicy](redactionpolicy#constructor)() | Creates a new instance of Redaction policy. |
| [RedactionPolicy](redactionpolicy#constructor_1)(Redaction[]) | Creates a new instance of Redaction policy with a specific list of redactions. |

## Properties

| Name | Description |
| --- | --- |
| [Redactions](../../groupdocs.redaction/redactionpolicy/redactions) { get; } | Gets an array of fully configured [`Redaction`](../redaction)-derived classes. |

## Methods

| Name | Description |
| --- | --- |
| static [Load](../../groupdocs.redaction/redactionpolicy/load#load)(Stream) | Loads an instance of [`RedactionPolicy`](../redactionpolicy) from a stream. |
| static [Load](../../groupdocs.redaction/redactionpolicy/load#load_1)(string) | Loads an instance of [`RedactionPolicy`](../redactionpolicy) from a file path. |
| [Save](../../groupdocs.redaction/redactionpolicy/save#save)(Stream) | Saves the redaction policy to a stream. |
| [Save](../../groupdocs.redaction/redactionpolicy/save#save_1)(string) | Saves the redaction policy to a file. |

### Remarks

**Learn more**

* More details about policies: [Use of redaction policies](https://docs.groupdocs.com/redaction/net/use-redaction-policies/)
* More details about applying redactions: [Redaction basics](https://docs.groupdocs.com/redaction/net/redaction-basics/)

### Examples

The following example demonstrates how to apply a redaction policy to all files within a given inbound folder, and save to one of outbound folders - for successfully updated files and for failed ones.

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

The following example contains a sample XML policy file with sample configurations for all types of redactions.

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

### See Also

* namespace [GroupDocs.Redaction](../../groupdocs.redaction)
* assembly [GroupDocs.Redaction](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.redaction.dll -->