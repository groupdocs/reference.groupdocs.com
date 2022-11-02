---
title: JpegImage
second_title: Referencia de API de GroupDocs.Editor para .NET
description: Crea una nueva instancia de JpegImage a partir del contenido representada como una cadena codificada en base64 y con el nombre especificado
type: docs
weight: 10
url: /es/net/groupdocs.editor.htmlcss.resources.images.raster/jpegimage/jpegimage/
---
## JpegImage(string, string) {#constructor_1}

Crea una nueva instancia de JpegImage a partir del contenido, representada como una cadena codificada en base64 y con el nombre especificado

```csharp
public JpegImage(string name, string contentInBase64)
```

| Parámetro | Escribe | Descripción |
| --- | --- | --- |
| name | String | Nombre de la imagen JPEG. No puede ser nulo, vacío o espacios en blanco. |
| contentInBase64 | String | Contenido como cadena codificada en base64. No puede ser nulo, vacío o espacios en blanco. Si no es un contenido JPEG, se lanzará una excepción. |

### Excepciones

| excepción | condición |
| --- | --- |
| ArgumentException |  |
| [InvalidImageFormatException](../../../groupdocs.editor.htmlcss.exceptions/invalidimageformatexception) |  |

### Ver también

* class [JpegImage](../../jpegimage)
* espacio de nombres [GroupDocs.Editor.HtmlCss.Resources.Images.Raster](../../jpegimage)
* asamblea [GroupDocs.Editor](../../../)

---

## JpegImage(string, Stream) {#constructor}

Crea una nueva instancia de JpegImage a partir del contenido, representada como flujo de bytes y con el nombre especificado

```csharp
public JpegImage(string name, Stream binaryContent)
```

| Parámetro | Escribe | Descripción |
| --- | --- | --- |
| name | String | Nombre de la imagen JPEG. No puede ser nulo, vacío o espacios en blanco. |
| binaryContent | Stream | Contenido como flujo de bytes. La lectura comienza desde la posición original. No puede ser nulo. Debe ser legible y buscable. Si se eliminará esta instancia, también se eliminará esta transmisión. |

### Excepciones

| excepción | condición |
| --- | --- |
| ArgumentException |  |
| [InvalidImageFormatException](../../../groupdocs.editor.htmlcss.exceptions/invalidimageformatexception) |  |

### Ver también

* class [JpegImage](../../jpegimage)
* espacio de nombres [GroupDocs.Editor.HtmlCss.Resources.Images.Raster](../../jpegimage)
* asamblea [GroupDocs.Editor](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Editor.dll -->