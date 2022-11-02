---
title: WordProcessingPreviewOptions
second_title: Referencia de API de GroupDocs.Watermark para .NET
description: Inicializa una nueva instancia delWordProcessingPreviewOptionsgroupdocs.watermark.options.wordprocessing/wordprocessingpreviewoptions clase que hace que se cierre el flujo de salida.
type: docs
weight: 10
url: /es/net/groupdocs.watermark.options.wordprocessing/wordprocessingpreviewoptions/wordprocessingpreviewoptions/
---
## WordProcessingPreviewOptions(CreatePageStream) {#constructor}

Inicializa una nueva instancia del[`WordProcessingPreviewOptions`](../../wordprocessingpreviewoptions) clase que hace que se cierre el flujo de salida.

```csharp
public WordProcessingPreviewOptions(CreatePageStream createPageStream)
```

| Parámetro | Escribe | Descripción |
| --- | --- | --- |
| createPageStream | CreatePageStream | Crea una secuencia para una vista previa de página específica. |

### Ver también

* delegate [CreatePageStream](../../../groupdocs.watermark.options/createpagestream)
* class [WordProcessingPreviewOptions](../../wordprocessingpreviewoptions)
* espacio de nombres [GroupDocs.Watermark.Options.WordProcessing](../../wordprocessingpreviewoptions)
* asamblea [GroupDocs.Watermark](../../../)

---

## WordProcessingPreviewOptions(CreatePageStream, ReleasePageStream) {#constructor_1}

Inicializa una nueva instancia de[`WordProcessingPreviewOptions`](../../wordprocessingpreviewoptions) clase que hace que el flujo de salida se devuelva al cliente para su uso posterior.

```csharp
public WordProcessingPreviewOptions(CreatePageStream createPageStream, 
    ReleasePageStream releasePageStream)
```

| Parámetro | Escribe | Descripción |
| --- | --- | --- |
| createPageStream | CreatePageStream | Crea una secuencia para una vista previa de página específica. |
| releasePageStream | ReleasePageStream | Notifica que la generación de la vista previa de la página ha finalizado y obtiene el flujo de salida. |

### Ver también

* delegate [CreatePageStream](../../../groupdocs.watermark.options/createpagestream)
* delegate [ReleasePageStream](../../../groupdocs.watermark.options/releasepagestream)
* class [WordProcessingPreviewOptions](../../wordprocessingpreviewoptions)
* espacio de nombres [GroupDocs.Watermark.Options.WordProcessing](../../wordprocessingpreviewoptions)
* asamblea [GroupDocs.Watermark](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Watermark.dll -->