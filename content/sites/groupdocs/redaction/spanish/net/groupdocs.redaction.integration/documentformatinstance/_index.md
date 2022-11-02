---
title: DocumentFormatInstance
second_title: Referencia de API de GroupDocs.Redaction para .NET
description: Representa un formato específico de un documento. Implemente esta clase para agregar sus propios tipos de documentos.
type: docs
weight: 110
url: /es/net/groupdocs.redaction.integration/documentformatinstance/
---
## DocumentFormatInstance class

Representa un formato específico de un documento. Implemente esta clase para agregar sus propios tipos de documentos.

```csharp
public abstract class DocumentFormatInstance
```

## Propiedades

| Nombre | Descripción |
| --- | --- |
| [Password](../../groupdocs.redaction.integration/documentformatinstance/password) { get; set; } | Obtiene o establece una contraseña para documentos protegidos por contraseña. |

## Métodos

| Nombre | Descripción |
| --- | --- |
| virtual [Initialize](../../groupdocs.redaction.integration/documentformatinstance/initialize)(DocumentFormatConfiguration, RedactorSettings) | Realiza la inicialización de la instancia del controlador de formato de documento. |
| [IsRedactionAccepted](../../groupdocs.redaction.integration/documentformatinstance/isredactionaccepted)(RedactionDescription) | Cheques para[`IRedactionCallback`](../../groupdocs.redaction.redactions/iredactioncallback) implementación y la invoca, si se especifica. |
| virtual [Load](../../groupdocs.redaction.integration/documentformatinstance/load)(Stream) | Carga el documento desde un stream. |
| virtual [PerformBinaryCheck](../../groupdocs.redaction.integration/documentformatinstance/performbinarycheck)(Stream) | Comprueba si la secuencia dada contiene un documento compatible con esta instancia de formato. |
| abstract [Save](../../groupdocs.redaction.integration/documentformatinstance/save)(Stream) | Guarda el documento en un flujo. |

### Observaciones

**Aprende más**

* Más detalles sobre la implementación de formatos personalizados: [Crear un controlador de formato personalizado](https://docs.groupdocs.com/redaction/net/create-custom-format-handler/)

### Ejemplos

El siguiente ejemplo muestra cómo crear un código auxiliar vacío para un controlador de formato personalizado.

El siguiente ejemplo demuestra cómo utilizar los datos de inicialización.

```csharp
public class DummyDocument : DocumentFormatInstance
{     
    public override void Load(Stream output)
    {
        // carga el contenido del archivo
    }

    public override void Save(Stream output)
    {
        // guarda los cambios en el archivo;
    }
}
```

```csharp
public class MyCustomHandler : DocumentFormatInstance
{
    private string MyProperty { get; set; }
    
    // Otro código personalizado 
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

// Conectar formato personalizado en GroupDocs.Redaction
var mySettings = new DocumentFormatConfiguration();
mySettings.ExtensionFilter = ".foo";
mySettings.DocumentType = typeof(MyCustomHandler);
mySettings.InitializationData.Add("MyProperty", "bar");
var configuration = RedactorConfiguration.GetInstance();
configuration.AvailableFormats.Add(mySettings);
```

### Ver también

* espacio de nombres [GroupDocs.Redaction.Integration](../../groupdocs.redaction.integration)
* asamblea [GroupDocs.Redaction](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Redaction.dll -->