---
title: PresentationSaveOptions
second_title: Referencia de API de GroupDocs.Editor para .NET
description: Permite especificar opciones personalizadas para generar y guardar documentos de presentación compatibles con PowerPoint
type: docs
weight: 1090
url: /es/net/groupdocs.editor.options/presentationsaveoptions/
---
## PresentationSaveOptions class

Permite especificar opciones personalizadas para generar y guardar documentos de presentación (compatibles con PowerPoint)

```csharp
public sealed class PresentationSaveOptions : ISaveOptions
```

## Constructores

| Nombre | Descripción |
| --- | --- |
| [PresentationSaveOptions](presentationsaveoptions)(PresentationFormats) | Crea una nueva instancia de PresentationSaveOptions con el formato de salida de presentación obligatorio especificado, mientras que todos los demás parámetros son predeterminados |

## Propiedades

| Nombre | Descripción |
| --- | --- |
| [InsertAsNewSlide](../../groupdocs.editor.options/presentationsaveoptions/insertasnewslide) { get; set; } | Bandera booleana, que especifica si la diapositiva editada debe reemplazar la diapositiva existente en la presentación original en la posición, especificada por el[`SlideNumber`](./slidenumber) propiedad, o debe insertarse entre la diapositiva existente y la anterior, sin reemplazar su contenido. Por defecto es falso: la diapositiva existente será reemplazada. Esta propiedad se ignora si el valor de[`SlideNumber`](./slidenumber) la propiedad se establece en '0'. |
| [OutputFormat](../../groupdocs.editor.options/presentationsaveoptions/outputformat) { get; set; } | Permite especificar un formato de presentación, que se utilizará para guardar el documento |
| [Password](../../groupdocs.editor.options/presentationsaveoptions/password) { get; set; } | Permite especificar, modificar y obtener la contraseña, que se utilizará para codificar el documento de presentación resultante. Por defecto es NULL: no se establecerá la contraseña. Establézcalo en NULL o cadena vacía para eliminar la contraseña, si se configuró previamente. |
| [SlideNumber](../../groupdocs.editor.options/presentationsaveoptions/slidenumber) { get; set; } | Permite insertar una diapositiva editada en una presentación existente en lugar de crear una nueva presentación de una sola diapositiva (comportamiento predeterminado). El número de diapositiva es un número basado en 1 de una diapositiva en la presentación, cargada en la clase Editor. Si es 0 (valor predeterminado), la nueva presentación se creará con una sola diapositiva editada. Si es mayor o menor que cero, y hay una presentación válida, cargada en la clase Editor, la diapositiva editada, almacenada dentro de la instancia de EditableDocument de entrada, se insertará en esta presentación. |

### Observaciones

La instancia de esta clase debe pasarse al[`Save`](../../groupdocs.editor/editor/save)para guardar la presentación editada en el documento final de algún formato específico de la presentación. Su constructor tiene un parámetro obligatorio: formato de la presentación de salida. Todos los demás parámetros son opcionales y pueden omitirse.

### Ver también

* interface [ISaveOptions](../isaveoptions)
* espacio de nombres [GroupDocs.Editor.Options](../../groupdocs.editor.options)
* asamblea [GroupDocs.Editor](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Editor.dll -->
