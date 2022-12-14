---
title: Initialize
second_title: GroupDocs.Redaction för .NET API-referens
description: Utför initiering av instansen av dokumentformathanterare.
type: docs
weight: 20
url: /sv/net/groupdocs.redaction.integration/documentformatinstance/initialize/
---
## DocumentFormatInstance.Initialize method

Utför initiering av instansen av dokumentformathanterare.

```csharp
public virtual void Initialize(DocumentFormatConfiguration config, RedactorSettings settings)
```

| Parameter | Typ | Beskrivning |
| --- | --- | --- |
| config | DocumentFormatConfiguration | Formatkonfiguration |
| settings | RedactorSettings | Standardinställningar för redigeringsprocessen. |

### Exempel

Följande exempel visar hur man använder initialiseringsdata.

```csharp
public class MyCustomHandler : DocumentFormatInstance
{
    private string MyProperty { get; set; }
    
    // Annan anpassad kod 
    ...

    public override void Initialize(DocumentFormatConfiguration config)
    {
        base.Initialize(config);
        if (config.InitializationData.ContainsKey("MyProperty"))
        {
            MyProperty = config.InitializationData["MyProperty"];
        }
    }
}

// Ansluter anpassat format till GroupDocs.Redaction
var mySettings = new DocumentFormatConfiguration();
mySettings.ExtensionFilter = ".foo";
mySettings.DocumentType = typeof(MyCustomHandler);
mySettings.InitializationData.Add("MyProperty", "bar");
var configuration = RedactorConfiguration.GetInstance();
configuration.AvailableFormats.Add(mySettings);
```

### Se även

* class [DocumentFormatConfiguration](../../../groupdocs.redaction.configuration/documentformatconfiguration)
* class [RedactorSettings](../../../groupdocs.redaction.options/redactorsettings)
* class [DocumentFormatInstance](../../documentformatinstance)
* namnutrymme [GroupDocs.Redaction.Integration](../../documentformatinstance)
* hopsättning [GroupDocs.Redaction](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Redaction.dll -->
