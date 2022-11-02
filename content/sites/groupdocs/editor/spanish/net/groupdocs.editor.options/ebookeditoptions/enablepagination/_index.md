---
title: EnablePagination
second_title: Referencia de API de GroupDocs.Editor para .NET
description: Permite habilitar o deshabilitar la paginación en el documento HTML resultante. Por defecto está deshabilitado falso .
type: docs
weight: 30
url: /es/net/groupdocs.editor.options/ebookeditoptions/enablepagination/
---
## EbookEditOptions.EnablePagination property

Permite habilitar o deshabilitar la paginación en el documento HTML resultante. Por defecto está deshabilitado (`falso` ).

```csharp
public bool EnablePagination { get; set; }
```

### Observaciones

En esencia, la mayoría de los formatos de libros electrónicos internamente son un formato de flujo como Office Open XML, donde el contenido es sólido y se divide en capítulos pero no en páginas. Sin embargo, contiene información específica de la página, como los números de página, notas al pie, encabezados/pies de página, etc. Algunos lectores de libros electrónicos dividen el contenido del libro electrónico en páginas, mientras que otros (especialmente los móviles) no lo hacen. Esta opción permite controlar cómo se debe representar el contenido del libro electrónico en HTML/CSS durante la edición, en el flotante (`falso`) o paginado (`verdadero`) vista.

### Ver también

* class [EbookEditOptions](../../ebookeditoptions)
* espacio de nombres [GroupDocs.Editor.Options](../../ebookeditoptions)
* asamblea [GroupDocs.Editor](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Editor.dll -->