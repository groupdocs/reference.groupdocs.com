---
title: PngViewOptions
second_title: Referencia de API de GroupDocs.Viewer para .NET
description: Inicializa una nueva instancia dePngViewOptionsgroupdocs.viewer.options/pngviewoptions clase.
type: docs
weight: 10
url: /es/net/groupdocs.viewer.options/pngviewoptions/pngviewoptions/
---
## PngViewOptions(CreatePageStream) {#constructor_1}

Inicializa una nueva instancia de[`PngViewOptions`](../../pngviewoptions) clase.

```csharp
public PngViewOptions(CreatePageStream createPageStream)
```

| Parámetro | Escribe | Descripción |
| --- | --- | --- |
| createPageStream | CreatePageStream | El método que instancia el flujo utilizado para escribir los datos de la página de salida. |

### Excepciones

| excepción | condición |
| --- | --- |
| ArgumentNullException | arrojado cuando*createPageStream* es nulo. |

### Ver también

* delegate [CreatePageStream](../../../groupdocs.viewer.interfaces/createpagestream)
* class [PngViewOptions](../../pngviewoptions)
* espacio de nombres [GroupDocs.Viewer.Options](../../pngviewoptions)
* asamblea [GroupDocs.Viewer](../../../)

---

## PngViewOptions(CreatePageStream, ReleasePageStream) {#constructor_2}

Inicializa una nueva instancia de[`PngViewOptions`](../../pngviewoptions) clase.

```csharp
public PngViewOptions(CreatePageStream createPageStream, ReleasePageStream releasePageStream)
```

| Parámetro | Escribe | Descripción |
| --- | --- | --- |
| createPageStream | CreatePageStream | El método que instancia el flujo utilizado para escribir los datos de la página de salida. |
| releasePageStream | ReleasePageStream | El método que libera el flujo creado por el método asignado al delegado que pasó a*createPageStream* parámetro. |

### Excepciones

| excepción | condición |
| --- | --- |
| ArgumentNullException | arrojado cuando*createPageStream* es nulo. |
| ArgumentNullException | arrojado cuando*releasePageStream* es nulo. |

### Ver también

* delegate [CreatePageStream](../../../groupdocs.viewer.interfaces/createpagestream)
* delegate [ReleasePageStream](../../../groupdocs.viewer.interfaces/releasepagestream)
* class [PngViewOptions](../../pngviewoptions)
* espacio de nombres [GroupDocs.Viewer.Options](../../pngviewoptions)
* asamblea [GroupDocs.Viewer](../../../)

---

## PngViewOptions(IPageStreamFactory) {#constructor_3}

Inicializa una nueva instancia de[`PngViewOptions`](../../pngviewoptions) clase.

```csharp
public PngViewOptions(IPageStreamFactory pageStreamFactory)
```

| Parámetro | Escribe | Descripción |
| --- | --- | --- |
| pageStreamFactory | IPageStreamFactory | La fábrica que implementa métodos para crear y publicar secuencias de páginas de salida. |

### Excepciones

| excepción | condición |
| --- | --- |
| ArgumentNullException | arrojado cuando*pageStreamFactory* es nulo. |

### Ver también

* interface [IPageStreamFactory](../../../groupdocs.viewer.interfaces/ipagestreamfactory)
* class [PngViewOptions](../../pngviewoptions)
* espacio de nombres [GroupDocs.Viewer.Options](../../pngviewoptions)
* asamblea [GroupDocs.Viewer](../../../)

---

## PngViewOptions() {#constructor}

Inicializa una nueva instancia de[`PngViewOptions`](../../pngviewoptions) clase.

```csharp
public PngViewOptions()
```

### Observaciones

Este constructor inicializa una nueva instancia de[`PngViewOptions`](../../pngviewoptions) con "p_{0}.png" como formato de ruta de archivo para los archivos de salida. Los archivos de salida se colocarán en el directorio de trabajo actual de la aplicación.

### Ver también

* class [PngViewOptions](../../pngviewoptions)
* espacio de nombres [GroupDocs.Viewer.Options](../../pngviewoptions)
* asamblea [GroupDocs.Viewer](../../../)

---

## PngViewOptions(string) {#constructor_4}

Inicializa una nueva instancia de[`PngViewOptions`](../../pngviewoptions) clase.

```csharp
public PngViewOptions(string filePathFormat)
```

| Parámetro | Escribe | Descripción |
| --- | --- | --- |
| filePathFormat | String | El formato de la ruta del archivo, por ejemplo, 'page_{0}.png'. |

### Excepciones

| excepción | condición |
| --- | --- |
| ArgumentException | arrojado cuando*filePathFormat* es nulo o vacío. |

### Ver también

* class [PngViewOptions](../../pngviewoptions)
* espacio de nombres [GroupDocs.Viewer.Options](../../pngviewoptions)
* asamblea [GroupDocs.Viewer](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Viewer.dll -->