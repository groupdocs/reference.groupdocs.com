---
title: ForEmbeddedResources
second_title: Referencia de API de GroupDocs.Viewer para .NET
description: Inicializa una nueva instancia deHtmlViewOptionsgroupdocs.viewer.options/htmlviewoptions clase para renderizar en HTML con recursos incrustados.
type: docs
weight: 10
url: /es/net/groupdocs.viewer.options/htmlviewoptions/forembeddedresources/
---
## ForEmbeddedResources(CreatePageStream) {#forembeddedresources_1}

Inicializa una nueva instancia de[`HtmlViewOptions`](../../htmlviewoptions) clase para renderizar en HTML con recursos incrustados.

```csharp
public static HtmlViewOptions ForEmbeddedResources(CreatePageStream createPageStream)
```

| Parámetro | Escribe | Descripción |
| --- | --- | --- |
| createPageStream | CreatePageStream | El método que instancia el flujo utilizado para escribir los datos de la página de salida. |

### Valor_devuelto

Nueva instancia de[`HtmlViewOptions`](../../htmlviewoptions) clase para renderizar en HTML con recursos incrustados.

### Excepciones

| excepción | condición |
| --- | --- |
| ArgumentNullException | arrojado cuando*createPageStream* es nulo. |

### Ver también

* delegate [CreatePageStream](../../../groupdocs.viewer.interfaces/createpagestream)
* class [HtmlViewOptions](../../htmlviewoptions)
* espacio de nombres [GroupDocs.Viewer.Options](../../htmlviewoptions)
* asamblea [GroupDocs.Viewer](../../../)

---

## ForEmbeddedResources(CreatePageStream, ReleasePageStream) {#forembeddedresources_2}

Inicializa una nueva instancia de[`HtmlViewOptions`](../../htmlviewoptions) clase para renderizar en HTML con recursos incrustados.

```csharp
public static HtmlViewOptions ForEmbeddedResources(CreatePageStream createPageStream, 
    ReleasePageStream releasePageStream)
```

| Parámetro | Escribe | Descripción |
| --- | --- | --- |
| createPageStream | CreatePageStream | El método que instancia el flujo utilizado para escribir los datos de la página de salida. |
| releasePageStream | ReleasePageStream | El método que libera el flujo creado por el método asignado al delegado que pasó a*createPageStream* parámetro. |

### Valor_devuelto

Nueva instancia de[`HtmlViewOptions`](../../htmlviewoptions) clase para renderizar en HTML con recursos incrustados.

### Excepciones

| excepción | condición |
| --- | --- |
| ArgumentNullException | arrojado cuando*createPageStream* es nulo. |
| ArgumentNullException | arrojado cuando*releasePageStream* es nulo. |

### Ver también

* delegate [CreatePageStream](../../../groupdocs.viewer.interfaces/createpagestream)
* delegate [ReleasePageStream](../../../groupdocs.viewer.interfaces/releasepagestream)
* class [HtmlViewOptions](../../htmlviewoptions)
* espacio de nombres [GroupDocs.Viewer.Options](../../htmlviewoptions)
* asamblea [GroupDocs.Viewer](../../../)

---

## ForEmbeddedResources(IPageStreamFactory) {#forembeddedresources_3}

Inicializa una nueva instancia de[`HtmlViewOptions`](../../htmlviewoptions) clase para renderizar en HTML con recursos incrustados.

```csharp
public static HtmlViewOptions ForEmbeddedResources(IPageStreamFactory pageStreamFactory)
```

| Parámetro | Escribe | Descripción |
| --- | --- | --- |
| pageStreamFactory | IPageStreamFactory | La fábrica que implementa métodos para crear y publicar secuencias de páginas de salida. |

### Valor_devuelto

Nueva instancia de[`HtmlViewOptions`](../../htmlviewoptions) clase para renderizar en HTML con recursos incrustados.

### Excepciones

| excepción | condición |
| --- | --- |
| ArgumentNullException | arrojado cuando*pageStreamFactory* es nulo. |

### Ver también

* interface [IPageStreamFactory](../../../groupdocs.viewer.interfaces/ipagestreamfactory)
* class [HtmlViewOptions](../../htmlviewoptions)
* espacio de nombres [GroupDocs.Viewer.Options](../../htmlviewoptions)
* asamblea [GroupDocs.Viewer](../../../)

---

## ForEmbeddedResources() {#forembeddedresources}

Inicializa una nueva instancia de[`HtmlViewOptions`](../../htmlviewoptions) clase.

```csharp
public static HtmlViewOptions ForEmbeddedResources()
```

### Ver también

* class [HtmlViewOptions](../../htmlviewoptions)
* espacio de nombres [GroupDocs.Viewer.Options](../../htmlviewoptions)
* asamblea [GroupDocs.Viewer](../../../)

---

## ForEmbeddedResources(string) {#forembeddedresources_4}

Inicializa una nueva instancia de[`HtmlViewOptions`](../../htmlviewoptions) clase.

```csharp
public static HtmlViewOptions ForEmbeddedResources(string filePathFormat)
```

| Parámetro | Escribe | Descripción |
| --- | --- | --- |
| filePathFormat | String | El formato de la ruta del archivo, por ejemplo, 'page_{0}.html'. |

### Excepciones

| excepción | condición |
| --- | --- |
| ArgumentException | arrojado cuando*filePathFormat* es nulo o vacío. |

### Ver también

* class [HtmlViewOptions](../../htmlviewoptions)
* espacio de nombres [GroupDocs.Viewer.Options](../../htmlviewoptions)
* asamblea [GroupDocs.Viewer](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Viewer.dll -->