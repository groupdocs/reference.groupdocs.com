---
title: Initialize
second_title: Riferimento API GroupDocs.Redaction per .NET
description: Esegue linizializzazione dellistanza del gestore del formato del documento.
type: docs
weight: 20
url: /it/net/groupdocs.redaction.integration/documentformatinstance/initialize/
---
## DocumentFormatInstance.Initialize method

Esegue l'inizializzazione dell'istanza del gestore del formato del documento.

```csharp
public virtual void Initialize(DocumentFormatConfiguration config, RedactorSettings settings)
```

| Parametro | Tipo | Descrizione |
| --- | --- | --- |
| config | DocumentFormatConfiguration | Configurazione del formato |
| settings | RedactorSettings | Impostazioni predefinite per il processo di redazione. |

### Esempi

Nell'esempio seguente viene illustrato come utilizzare i dati di inizializzazione.

```csharp
public class MyCustomHandler : DocumentFormatInstance
{
    private string MyProperty { get; set; }
    
    // Altro codice personalizzato 
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

// Inserimento di un formato personalizzato in GroupDocs.Redaction
var mySettings = new DocumentFormatConfiguration();
mySettings.ExtensionFilter = ".foo";
mySettings.DocumentType = typeof(MyCustomHandler);
mySettings.InitializationData.Add("MyProperty", "bar");
var configuration = RedactorConfiguration.GetInstance();
configuration.AvailableFormats.Add(mySettings);
```

### Guarda anche

* class [DocumentFormatConfiguration](../../../groupdocs.redaction.configuration/documentformatconfiguration)
* class [RedactorSettings](../../../groupdocs.redaction.options/redactorsettings)
* class [DocumentFormatInstance](../../documentformatinstance)
* spazio dei nomi [GroupDocs.Redaction.Integration](../../documentformatinstance)
* assemblea [GroupDocs.Redaction](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Redaction.dll -->
