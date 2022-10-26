---
title: FileLogger
second_title: Referencia de API de GroupDocs.Viewer para .NET
description: Escribe mensajes de registro en el archivo.
type: docs
weight: 240
url: /es/net/groupdocs.viewer.logging/filelogger/
---
## FileLogger class

Escribe mensajes de registro en el archivo.

```csharp
public class FileLogger : ILogger
```

## Constructores

| Nombre | Descripción |
| --- | --- |
| [FileLogger](filelogger)(string) | Crear registrador en archivo. |

## Métodos

| Nombre | Descripción |
| --- | --- |
| [Error](../../groupdocs.viewer.logging/filelogger/error)(string, Exception) | Escribe un mensaje de error en la consola. Los mensajes de registro de errores brindan información sobre eventos irrecuperables en el flujo de la aplicación. |
| [Trace](../../groupdocs.viewer.logging/filelogger/trace)(string) | Escribe un mensaje de seguimiento en la consola. Los mensajes de registro de seguimiento proporcionan información generalmente útil sobre el flujo de la aplicación. |
| [Warning](../../groupdocs.viewer.logging/filelogger/warning)(string) | Escribe un mensaje de advertencia en la consola. Los mensajes de registro de advertencia brindan información sobre eventos inesperados y recuperables en el flujo de la aplicación. |

### Ver también

* interface [ILogger](../ilogger)
* espacio de nombres [GroupDocs.Viewer.Logging](../../groupdocs.viewer.logging)
* asamblea [GroupDocs.Viewer](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Viewer.dll -->