---
title: WoffFont
second_title: Referencia de API de GroupDocs.Editor para .NET
description: Crea una nueva clase WoffFont a partir del contenido representada como una cadena codificada en base64 y con el nombre especificado
type: docs
weight: 10
url: /es/net/groupdocs.editor.htmlcss.resources.fonts/wofffont/wofffont/
---
## WoffFont(string, string) {#constructor_1}

Crea una nueva clase WoffFont a partir del contenido, representada como una cadena codificada en base64 y con el nombre especificado

```csharp
public WoffFont(string name, string contentInBase64)
```

| Parámetro | Escribe | Descripción |
| --- | --- | --- |
| name | String | Nombre de la fuente WOFF. No puede ser nulo, vacío o espacios en blanco. |
| contentInBase64 | String | Contenido como cadena codificada en base64. No puede ser nulo, vacío o espacios en blanco. Si no es un contenido WOFF, se lanzará una excepción. |

### Excepciones

| excepción | condición |
| --- | --- |
| ArgumentException |  |
| [InvalidImageFormatException](../../../groupdocs.editor.htmlcss.exceptions/invalidimageformatexception) |  |

### Ver también

* class [WoffFont](../../wofffont)
* espacio de nombres [GroupDocs.Editor.HtmlCss.Resources.Fonts](../../wofffont)
* asamblea [GroupDocs.Editor](../../../)

---

## WoffFont(string, Stream) {#constructor}

Crea una nueva clase WoffFont a partir del contenido, representada como flujo de bytes y con el nombre especificado

```csharp
public WoffFont(string name, Stream binaryContent)
```

| Parámetro | Escribe | Descripción |
| --- | --- | --- |
| name | String | Nombre de la fuente WOFF. No puede ser nulo, vacío o espacios en blanco. |
| binaryContent | Stream | Contenido como flujo de bytes. La lectura comienza desde la posición original. No puede ser nulo. Debe ser legible y sellable. Si se eliminará esta instancia, también se eliminará esta transmisión. |

### Excepciones

| excepción | condición |
| --- | --- |
| ArgumentException |  |
| [InvalidImageFormatException](../../../groupdocs.editor.htmlcss.exceptions/invalidimageformatexception) |  |

### Ver también

* class [WoffFont](../../wofffont)
* espacio de nombres [GroupDocs.Editor.HtmlCss.Resources.Fonts](../../wofffont)
* asamblea [GroupDocs.Editor](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Editor.dll -->
