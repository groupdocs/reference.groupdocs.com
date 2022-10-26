---
title: ReleasePageStream
second_title: Referencia de API de GroupDocs.Viewer para .NET
description: Libera el flujo que fue instanciado por el método asociado conCreatePageStream./createpagestream delegado.
type: docs
weight: 200
url: /es/net/groupdocs.viewer.interfaces/releasepagestream/
---
## ReleasePageStream delegate

Libera el flujo que fue instanciado por el método asociado con[`CreatePageStream`](../createpagestream) delegado.

```csharp
public delegate void ReleasePageStream(int pageNumber, Stream pageStream);
```

| Parámetro | Escribe | Descripción |
| --- | --- | --- |
| pageNumber | Int32 | Número de la página. |
| pageStream | Stream | El flujo creado por el método asociado con[`CreatePageStream`](../createpagestream) delegar. |

### Ver también

* espacio de nombres [GroupDocs.Viewer.Interfaces](../../groupdocs.viewer.interfaces)
* asamblea [GroupDocs.Viewer](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Viewer.dll -->