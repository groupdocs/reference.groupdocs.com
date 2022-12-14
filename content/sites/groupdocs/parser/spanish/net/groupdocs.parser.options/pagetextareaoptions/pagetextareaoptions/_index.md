---
title: PageTextAreaOptions
second_title: Referencia de API de GroupDocs.Parser para .NET
description: Inicializa una nueva instancia delPageTextAreaOptionsgroupdocs.parser.options/pagetextareaoptions clase con la expresión regular. Otras opciones están configuradas de forma predeterminada ver comentarios para más detalles.
type: docs
weight: 10
url: /es/net/groupdocs.parser.options/pagetextareaoptions/pagetextareaoptions/
---
## PageTextAreaOptions(string) {#constructor}

Inicializa una nueva instancia del[`PageTextAreaOptions`](../../pagetextareaoptions) clase con la expresión regular. Otras opciones están configuradas de forma predeterminada (ver comentarios para más detalles).

```csharp
public PageTextAreaOptions(string expression)
```

| Parámetro | Escribe | Descripción |
| --- | --- | --- |
| expression | String | La expresión regular. |

### Observaciones

Las siguientes propiedades tienen valores predeterminados:

**[`MatchCase`](../matchcase)**

`falso`

**[`UniteSegments`](../unitesegments)**

`falso`

**[`IgnoreFormatting`](../ignoreformatting)**

`falso`

**[`Rectangle`](../../pageareaoptions/rectangle)**

`nulo`

### Ver también

* class [PageTextAreaOptions](../../pagetextareaoptions)
* espacio de nombres [GroupDocs.Parser.Options](../../pagetextareaoptions)
* asamblea [GroupDocs.Parser](../../../)

---

## PageTextAreaOptions(string, Rectangle) {#constructor_2}

Inicializa una nueva instancia del[`PageTextAreaOptions`](../../pagetextareaoptions) class con la expresión regular y el área rectangular. Otras opciones están configuradas de forma predeterminada (ver comentarios para más detalles).

```csharp
public PageTextAreaOptions(string expression, Rectangle rectangle)
```

| Parámetro | Escribe | Descripción |
| --- | --- | --- |
| expression | String | La expresión regular. |
| rectangle | Rectangle | El área rectangular que contiene áreas de página. |

### Observaciones

Las siguientes propiedades tienen valores predeterminados:

**[`MatchCase`](../matchcase)**

`falso`

**[`UniteSegments`](../unitesegments)**

`falso`

**[`IgnoreFormatting`](../ignoreformatting)**

`falso`

### Ver también

* class [Rectangle](../../../groupdocs.parser.data/rectangle)
* class [PageTextAreaOptions](../../pagetextareaoptions)
* espacio de nombres [GroupDocs.Parser.Options](../../pagetextareaoptions)
* asamblea [GroupDocs.Parser](../../../)

---

## PageTextAreaOptions(string, bool, bool, bool, Rectangle) {#constructor_1}

Inicializa una nueva instancia del[`PageTextAreaOptions`](../../pagetextareaoptions) clase.

```csharp
public PageTextAreaOptions(string expression, bool matchCase, bool uniteSegments, 
    bool ignoreFormatting, Rectangle rectangle)
```

| Parámetro | Escribe | Descripción |
| --- | --- | --- |
| expression | String | La expresión regular. |
| matchCase | Boolean | El valor que indica si un caso de texto no se ignora. |
| uniteSegments | Boolean | El valor que indica si los segmentos están unidos. |
| ignoreFormatting | Boolean | El valor que indica si se ignora el formato de texto. |
| rectangle | Rectangle | El área rectangular que contiene áreas de página. |

### Ver también

* class [Rectangle](../../../groupdocs.parser.data/rectangle)
* class [PageTextAreaOptions](../../pagetextareaoptions)
* espacio de nombres [GroupDocs.Parser.Options](../../pagetextareaoptions)
* asamblea [GroupDocs.Parser](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Parser.dll -->
