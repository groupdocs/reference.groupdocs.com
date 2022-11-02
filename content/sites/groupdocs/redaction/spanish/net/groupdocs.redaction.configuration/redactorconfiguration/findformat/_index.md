---
title: FindFormat
second_title: Referencia de API de GroupDocs.Redaction para .NET
description: Encuentra configuraciones de formato para una extensión de archivo determinada.
type: docs
weight: 30
url: /es/net/groupdocs.redaction.configuration/redactorconfiguration/findformat/
---
## RedactorConfiguration.FindFormat method

Encuentra configuraciones de formato para una extensión de archivo determinada.

```csharp
public DocumentFormatConfiguration FindFormat(string fileExtension)
```

| Parámetro | Escribe | Descripción |
| --- | --- | --- |
| fileExtension | String | Extensión de archivo, el formato es ".ext" |

### Valor_devuelto

Si se encuentra, instancia de[`DocumentFormatConfiguration`](../../documentformatconfiguration), nulo en caso contrario

### Ejemplos

El siguiente ejemplo muestra cómo obtener controladores de formato de usuario integrados o personalizados.

```csharp
var configuration = RedactorConfiguration.GetInstance();
var formatSettings = configuration.FindFormat(".psd");
```

### Ver también

* class [DocumentFormatConfiguration](../../documentformatconfiguration)
* class [RedactorConfiguration](../../redactorconfiguration)
* espacio de nombres [GroupDocs.Redaction.Configuration](../../redactorconfiguration)
* asamblea [GroupDocs.Redaction](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Redaction.dll -->