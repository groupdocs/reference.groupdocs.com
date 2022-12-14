---
title: MultiframeImageWatermarkOptions
second_title: Referencia de API de GroupDocs.Watermark para .NET
description: Representa las opciones de adición de marca de agua al agregar una marca de agua a una imagen de varios fotogramas.
type: docs
weight: 1800
url: /es/net/groupdocs.watermark.options.image/multiframeimagewatermarkoptions/
---
## MultiframeImageWatermarkOptions class

Representa las opciones de adición de marca de agua al agregar una marca de agua a una imagen de varios fotogramas.

```csharp
public class MultiframeImageWatermarkOptions : WatermarkOptions
```

## Constructores

| Nombre | Descripción |
| --- | --- |
| [MultiframeImageWatermarkOptions](multiframeimagewatermarkoptions#constructor)() | Inicializa una nueva instancia del[`MultiframeImageWatermarkOptions`](../multiframeimagewatermarkoptions) clase. |
| [MultiframeImageWatermarkOptions](multiframeimagewatermarkoptions#constructor_1)(int) | Inicializa una nueva instancia del[`MultiframeImageWatermarkOptions`](../multiframeimagewatermarkoptions) class con un índice especificado del marco. |

## Propiedades

| Nombre | Descripción |
| --- | --- |
| [FrameIndex](../../groupdocs.watermark.options.image/multiframeimagewatermarkoptions/frameindex) { get; set; } | Obtiene o establece el índice del marco para agregar la marca de agua. |

### Observaciones

**Aprende más:**

* [Agregar marcas de agua a las imágenes](https://docs.groupdocs.com/display/watermarknet/Add+watermarks+to+images)

### Ejemplos

Agregue una marca de agua a un cuadro particular de una imagen de varios cuadros.

```csharp
ImageLoadOptions loadOptions = new ImageLoadOptions();
using (Watermarker watermarker = new Watermarker(@"C:\test.gif", loadOptions))
{
    TextWatermark watermark = new TextWatermark("Test", new Font("Arial", 12));

    MultiframeImageWatermarkOptions options = new MultiframeImageWatermarkOptions();
    options.FrameIndex = 0;

    watermarker.Add(watermark, options);
    watermarker.Save();
}
```

### Ver también

* class [WatermarkOptions](../../groupdocs.watermark.options/watermarkoptions)
* espacio de nombres [GroupDocs.Watermark.Options.Image](../../groupdocs.watermark.options.image)
* asamblea [GroupDocs.Watermark](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Watermark.dll -->
