---
title: FileLogger
second_title: Referencia de API de GroupDocs.Signature para .NET
description: Escribe mensajes de registro en el archivo.
type: docs
weight: 1150
url: /es/net/groupdocs.signature.logging/filelogger/
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
| [Error](../../groupdocs.signature.logging/filelogger/error)(string, Exception) | Escribe un mensaje de error en la consola. Los mensajes de registro de errores brindan información sobre eventos irrecuperables en el flujo de la aplicación. |
| [Trace](../../groupdocs.signature.logging/filelogger/trace)(string) | Escribe un mensaje de seguimiento en la consola. Los mensajes de registro de seguimiento proporcionan información generalmente útil sobre el flujo de la aplicación. |
| [Warning](../../groupdocs.signature.logging/filelogger/warning)(string) | Escribe un mensaje de advertencia en la consola; Los mensajes de registro de advertencia brindan información sobre el evento inesperado y recuperable en el flujo de la aplicación. |

### Ver también

* interface [ILogger](../ilogger)
* espacio de nombres [GroupDocs.Signature.Logging](../../groupdocs.signature.logging)
* asamblea [GroupDocs.Signature](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Signature.dll -->
