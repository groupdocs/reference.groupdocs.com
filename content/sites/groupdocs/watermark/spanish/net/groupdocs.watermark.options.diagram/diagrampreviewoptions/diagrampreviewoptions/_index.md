---
title: DiagramPreviewOptions
second_title: Referencia de API de GroupDocs.Watermark para .NET
description: Inicializa una nueva instancia delDiagramPreviewOptionsgroupdocs.watermark.options.diagram/diagrampreviewoptions clase que hace que se cierre el flujo de salida.
type: docs
weight: 10
url: /es/net/groupdocs.watermark.options.diagram/diagrampreviewoptions/diagrampreviewoptions/
---
## DiagramPreviewOptions(CreatePageStream) {#constructor}

Inicializa una nueva instancia del[`DiagramPreviewOptions`](../../diagrampreviewoptions) clase que hace que se cierre el flujo de salida.

```csharp
public DiagramPreviewOptions(CreatePageStream createPageStream)
```

| Parámetro | Escribe | Descripción |
| --- | --- | --- |
| createPageStream | CreatePageStream | Crea una secuencia para una vista previa de página específica. |

### Ver también

* delegate [CreatePageStream](../../../groupdocs.watermark.options/createpagestream)
* class [DiagramPreviewOptions](../../diagrampreviewoptions)
* espacio de nombres [GroupDocs.Watermark.Options.Diagram](../../diagrampreviewoptions)
* asamblea [GroupDocs.Watermark](../../../)

---

## DiagramPreviewOptions(CreatePageStream, ReleasePageStream) {#constructor_1}

Inicializa una nueva instancia de[`DiagramPreviewOptions`](../../diagrampreviewoptions) clase que hace que el flujo de salida se devuelva al cliente para su uso posterior.

```csharp
public DiagramPreviewOptions(CreatePageStream createPageStream, ReleasePageStream releasePageStream)
```

| Parámetro | Escribe | Descripción |
| --- | --- | --- |
| createPageStream | CreatePageStream | Crea una secuencia para una vista previa de página específica. |
| releasePageStream | ReleasePageStream | Notifica que la generación de la vista previa de la página ha finalizado y obtiene el flujo de salida. |

### Ver también

* delegate [CreatePageStream](../../../groupdocs.watermark.options/createpagestream)
* delegate [ReleasePageStream](../../../groupdocs.watermark.options/releasepagestream)
* class [DiagramPreviewOptions](../../diagrampreviewoptions)
* espacio de nombres [GroupDocs.Watermark.Options.Diagram](../../diagrampreviewoptions)
* asamblea [GroupDocs.Watermark](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Watermark.dll -->