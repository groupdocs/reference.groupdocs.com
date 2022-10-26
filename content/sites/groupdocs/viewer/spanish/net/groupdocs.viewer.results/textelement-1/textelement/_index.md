---
title: TextElement
second_title: Referencia de API de GroupDocs.Viewer para .NET
description: Inicializa una nueva instancia deTextElementgroupdocs.viewer.results/textelement1 clase.
type: docs
weight: 10
url: /es/net/groupdocs.viewer.results/textelement-1/textelement/
---
## TextElement&lt;T&gt; constructor

Inicializa una nueva instancia de[`TextElement`](../../textelement-1) clase.

```csharp
public TextElement(T value, double x, double y, double width, double height)
```

| Parámetro | Escribe | Descripción |
| --- | --- | --- |
| value | T | El valor del elemento de texto. |
| x | Double | La coordenada X del punto más alto a la izquierda en el diseño de página donde comienza el rectángulo que contiene el elemento. |
| y | Double | La coordenada Y del punto más alto a la izquierda en el diseño de página donde comienza el rectángulo que contiene el elemento. |
| width | Double | El ancho del rectángulo que contiene el elemento (en píxeles). |
| height | Double | La altura del rectángulo que contiene el elemento (en píxeles). |

### Excepciones

| excepción | condición |
| --- | --- |
| ArgumentNullException | arrojado cuando*value* es nulo. |
| ArgumentException | arrojado cuando*width* es menor o igual a cero. |
| ArgumentException | arrojado cuando*height* es menor o igual a cero. |

### Ver también

* class [TextElement&lt;T&gt;](../../textelement-1)
* espacio de nombres [GroupDocs.Viewer.Results](../../textelement-1)
* asamblea [GroupDocs.Viewer](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Viewer.dll -->