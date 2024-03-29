---
title: TemplateFixedPosition
second_title: Referencia de API de GroupDocs.Parser para .NET
description: Proporciona una posición de campo de plantilla definida por el área rectangular.
type: docs
weight: 680
url: /es/net/groupdocs.parser.templates/templatefixedposition/
---
## TemplateFixedPosition class

Proporciona una posición de campo de plantilla definida por el área rectangular.

```csharp
public sealed class TemplateFixedPosition : TemplatePosition
```

## Constructores

| Nombre | Descripción |
| --- | --- |
| [TemplateFixedPosition](templatefixedposition)(Rectangle) | Inicializa una nueva instancia del[`TemplateFixedPosition`](../templatefixedposition) clase. |

## Propiedades

| Nombre | Descripción |
| --- | --- |
| [Rectangle](../../groupdocs.parser.templates/templatefixedposition/rectangle) { get; } | Obtiene el área rectangular que contiene el campo de plantilla. |

### Ejemplos

Esta es la forma más sencilla de definir la posición del campo. Requiere establecer un área rectangular en la página que limite el valor del campo. Todo el texto contenido (incluso parcialmente) en el área rectangular se extraerá como un valor:

```csharp
// Crea un campo de plantilla fijo con el nombre "Dirección" que está delimitado por un rectángulo en la posición (35, 160) y con el tamaño (110, 20)
TemplateField templateField = new TemplateField(
    new TemplateFixedPosition(new Rectangle(new Point(35, 160), new Size(110, 20))),
    "Address");
```

### Ver también

* class [TemplatePosition](../templateposition)
* espacio de nombres [GroupDocs.Parser.Templates](../../groupdocs.parser.templates)
* asamblea [GroupDocs.Parser](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Parser.dll -->
