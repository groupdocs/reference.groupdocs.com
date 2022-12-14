---
title: ReleasePageStream
second_title: Referencia de API de GroupDocs.Watermark para .NET
description: Representa un método que libera el flujo creado por elCreatePageStream./createpagestream delegado.
type: docs
weight: 2090
url: /es/net/groupdocs.watermark.options/releasepagestream/
---
## ReleasePageStream delegate

Representa un método que libera el flujo creado por el[`CreatePageStream`](../createpagestream) delegado.

```csharp
public delegate void ReleasePageStream(int pageNumber, Stream pageStream);
```

| Parámetro | Escribe | Descripción |
| --- | --- | --- |
| pageNumber | Int32 | El número de página de una vista previa de página generada. |
| pageStream | Stream | El flujo que contiene la vista previa de la página generada. |

### Ver también

* espacio de nombres [GroupDocs.Watermark.Options](../../groupdocs.watermark.options)
* asamblea [GroupDocs.Watermark](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Watermark.dll -->
