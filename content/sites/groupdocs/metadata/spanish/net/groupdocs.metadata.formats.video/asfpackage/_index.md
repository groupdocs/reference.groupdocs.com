---
title: AsfPackage
second_title: Referencia de API de GroupDocs.Metadata para .NET
description: Representa metadatos nativos del contenedor de medios ASF.
type: docs
weight: 2340
url: /es/net/groupdocs.metadata.formats.video/asfpackage/
---
## AsfPackage class

Representa metadatos nativos del contenedor de medios ASF.

```csharp
public class AsfPackage : CustomPackage
```

## Propiedades

| Nombre | Descripción |
| --- | --- |
| [CodecInformation](../../groupdocs.metadata.formats.video/asfpackage/codecinformation) { get; } | Obtiene las entradas de información del códec. |
| [Count](../../groupdocs.metadata.common/metadatapackage/count) { get; } | Obtiene el número de propiedades de metadatos. |
| [CreationDate](../../groupdocs.metadata.formats.video/asfpackage/creationdate) { get; } | Obtiene la fecha y hora de la creación inicial del archivo. |
| [FileID](../../groupdocs.metadata.formats.video/asfpackage/fileid) { get; } | Obtiene el identificador único para este archivo. |
| [Flags](../../groupdocs.metadata.formats.video/asfpackage/flags) { get; } | Obtiene las banderas de encabezado. |
| [Item](../../groupdocs.metadata.common/metadatapackage/item) { get; } | Obtiene el[`MetadataProperty`](../../groupdocs.metadata.common/metadataproperty) con el nombre especificado. |
| [Keys](../../groupdocs.metadata.common/metadatapackage/keys) { get; } | Obtiene una colección de nombres de propiedades de metadatos. |
| [MetadataDescriptors](../../groupdocs.metadata.formats.video/asfpackage/metadatadescriptors) { get; } | Obtiene los descriptores de metadatos. |
| [MetadataType](../../groupdocs.metadata.common/metadatapackage/metadatatype) { get; } | Obtiene el tipo de metadato. |
| [PropertyDescriptors](../../groupdocs.metadata.common/metadatapackage/propertydescriptors) { get; } | Obtiene una colección de descriptores que contienen información sobre propiedades accesibles a través del motor de búsqueda GroupDocs.Metadata. |
| [StreamProperties](../../groupdocs.metadata.formats.video/asfpackage/streamproperties) { get; } | Obtiene las propiedades del flujo de medios digitales. |

## Métodos

| Nombre | Descripción |
| --- | --- |
| [AddProperties](../../groupdocs.metadata.common/metadatapackage/addproperties)(Func&lt;MetadataProperty, bool&gt;, PropertyValue) | Agrega propiedades de metadatos conocidas que satisfacen el predicado especificado. La operación es recursiva, por lo que también afecta a todos los paquetes anidados. |
| [Contains](../../groupdocs.metadata.common/metadatapackage/contains)(string) | Determina si el paquete contiene una propiedad de metadatos con el nombre especificado. |
| virtual [FindProperties](../../groupdocs.metadata.common/metadatapackage/findproperties)(Func&lt;MetadataProperty, bool&gt;) | Encuentra las propiedades de metadatos que satisfacen el predicado especificado. La búsqueda es recursiva, por lo que también afecta a todos los paquetes anidados. |
| [GetEnumerator](../../groupdocs.metadata.common/metadatapackage/getenumerator)() | Devuelve un enumerador que itera a través de la colección. |
| virtual [RemoveProperties](../../groupdocs.metadata.common/metadatapackage/removeproperties)(Func&lt;MetadataProperty, bool&gt;) | Elimina las propiedades de metadatos que cumplen el predicado especificado. |
| virtual [Sanitize](../../groupdocs.metadata.common/metadatapackage/sanitize)() | Elimina las propiedades de metadatos de escritura del paquete. La operación es recursiva, por lo que también afecta a todos los paquetes anidados. |
| [SetProperties](../../groupdocs.metadata.common/metadatapackage/setproperties)(Func&lt;MetadataProperty, bool&gt;, PropertyValue) | Establece propiedades de metadatos conocidas que satisfacen el predicado especificado. La operación es recursiva, por lo que también afecta a todos los paquetes anidados. Este método es una combinación de[`AddProperties`](../../groupdocs.metadata.common/metadatapackage/addproperties) y[`UpdateProperties`](../../groupdocs.metadata.common/metadatapackage/updateproperties) Si una propiedad existente satisface el predicado, su valor se actualiza. Si falta una propiedad conocida en el paquete que satisface el predicado, se agrega al paquete. |
| [UpdateProperties](../../groupdocs.metadata.common/metadatapackage/updateproperties)(Func&lt;MetadataProperty, bool&gt;, PropertyValue) | Actualiza las propiedades de metadatos conocidas que satisfacen el predicado especificado. La operación es recursiva, por lo que también afecta a todos los paquetes anidados. |

### Observaciones

**Aprende más**

* [Trabajar con metadatos en archivos ASF](https://docs.groupdocs.com/display/metadatanet/Working+with+Metadata+in+ASF+Files)

### Ver también

* class [CustomPackage](../../groupdocs.metadata.common/custompackage)
* espacio de nombres [GroupDocs.Metadata.Formats.Video](../../groupdocs.metadata.formats.video)
* asamblea [GroupDocs.Metadata](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Metadata.dll -->