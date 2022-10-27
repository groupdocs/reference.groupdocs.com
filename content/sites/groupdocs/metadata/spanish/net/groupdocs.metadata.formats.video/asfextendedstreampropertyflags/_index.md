---
title: AsfExtendedStreamPropertyFlags
second_title: Referencia de API de GroupDocs.Metadata para .NET
description: Define los indicadores de propiedad de secuencia extendida de ASF.
type: docs
weight: 2300
url: /es/net/groupdocs.metadata.formats.video/asfextendedstreampropertyflags/
---
## AsfExtendedStreamPropertyFlags enumeration

Define los indicadores de propiedad de secuencia extendida de ASF.

```csharp
[Flags]
public enum AsfExtendedStreamPropertyFlags : uint
```

### Valores

| Nombre | Valor | Descripción |
| --- | --- | --- |
| Reliable | `1` | Este flujo de medios digitales, si se envía a través de una red, debe transportarse a través de un mecanismo de transporte de comunicaciones de datos confiable. |
| Seekable | `2` | Este indicador debe establecerse solo si se puede buscar la secuencia. |
| NoCleanpoints | `2` | La secuencia no contiene ningún punto limpio. |
| ResendLiveCleanpoints | `2` | Se une a una transmisión en medio de la transmisión, toda la información desde el punto limpio más reciente hasta la hora actual debe enviarse antes de que comience la transmisión normal en la hora actual. |

### Ver también

* espacio de nombres [GroupDocs.Metadata.Formats.Video](../../groupdocs.metadata.formats.video)
* asamblea [GroupDocs.Metadata](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Metadata.dll -->