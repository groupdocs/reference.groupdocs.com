---
title: ReleasePageStream
second_title: GroupDocs.Comparison para la referencia de la API de .NET
description: Delegado que define el método para liberar el flujo de vista previa de la página de salida utilizado porPreviewOptions../groupdocs.comparison.options/previewoptions .
type: docs
weight: 30
url: /es/net/groupdocs.comparison.common.delegates/releasepagestream/
---
## ReleasePageStream delegate

Delegado que define el método para liberar el flujo de vista previa de la página de salida utilizado por[`PreviewOptions`](../../groupdocs.comparison.options/previewoptions) .

```csharp
public delegate void ReleasePageStream(int pageNumber, Stream pageStream);
```

| Parámetro | Escribe | Descripción |
| --- | --- | --- |
| pageNumber | Int32 | El número de página vista previa. |
| pageStream | Stream | El flujo de la página para liberar. |

### Ver también

* espacio de nombres [GroupDocs.Comparison.Common.Delegates](../../groupdocs.comparison.common.delegates)
* asamblea [GroupDocs.Comparison](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Comparison.dll -->
