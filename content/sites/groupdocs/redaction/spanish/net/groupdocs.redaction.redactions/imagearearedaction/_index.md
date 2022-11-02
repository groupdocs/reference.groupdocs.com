---
title: ImageAreaRedaction
second_title: Referencia de API de GroupDocs.Redaction para .NET
description: Representa una redacción que coloca un rectángulo de color en un área determinada de un documento de imagen.
type: docs
weight: 500
url: /es/net/groupdocs.redaction.redactions/imagearearedaction/
---
## ImageAreaRedaction class

Representa una redacción que coloca un rectángulo de color en un área determinada de un documento de imagen.

```csharp
public class ImageAreaRedaction : Redaction
```

## Constructores

| Nombre | Descripción |
| --- | --- |
| [ImageAreaRedaction](imagearearedaction)(Point, RegionReplacementOptions) | Inicializa una nueva instancia de la clase ImageAreaRedaction para redactar un tamaño de área específico. |

## Propiedades

| Nombre | Descripción |
| --- | --- |
| override [Description](../../groupdocs.redaction.redactions/imagearearedaction/description) { get; } | Devuelve una cadena que describe la redacción y sus parámetros. |
| [Options](../../groupdocs.redaction.redactions/imagearearedaction/options) { get; } | Obtiene el[`RegionReplacementOptions`](../regionreplacementoptions)opciones con parámetros de color y área. |
| [TopLeft](../../groupdocs.redaction.redactions/imagearearedaction/topleft) { get; } | Obtiene la posición superior izquierda del área a eliminar |

## Métodos

| Nombre | Descripción |
| --- | --- |
| override [ApplyTo](../../groupdocs.redaction.redactions/imagearearedaction/applyto)(DocumentFormatInstance) | Aplica la redacción a una instancia de formato dada. |

### Observaciones

**Aprende más**

* Más detalles sobre la aplicación de redacciones: [Conceptos básicos de redacción](https://docs.groupdocs.com/redaction/net/redaction-basics/)
* Más detalles sobre las redacciones de imágenes: [Redacciones de imágenes](https://docs.groupdocs.com/redaction/net/image-redactions/)

### Ejemplos

El siguiente ejemplo muestra cómo reemplazar un área dentro de la imagen con un rectángulo de color sólido.

```csharp
    using (Redactor redactor = new Redactor("D:\\test.jpg"))
    {
       System.Drawing.Point samplePoint = new System.Drawing.Point(516, 311);
       System.Drawing.Size sampleSize = new System.Drawing.Size(170, 35);
       RedactorChangeLog result = redactor.Apply(new ImageAreaRedaction(samplePoint,
                     new RegionReplacementOptions(System.Drawing.Color.Blue, sampleSize)));
       if (result.Status != RedactionStatus.Failed)
       {
          redactor.Save();
       };
    } 
```

### Ver también

* class [Redaction](../../groupdocs.redaction/redaction)
* espacio de nombres [GroupDocs.Redaction.Redactions](../../groupdocs.redaction.redactions)
* asamblea [GroupDocs.Redaction](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Redaction.dll -->