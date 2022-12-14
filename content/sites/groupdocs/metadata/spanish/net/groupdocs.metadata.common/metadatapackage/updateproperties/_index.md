---
title: UpdateProperties
second_title: Referencia de API de GroupDocs.Metadata para .NET
description: Actualiza las propiedades de metadatos conocidas que satisfacen el predicado especificado. La operación es recursiva por lo que también afecta a todos los paquetes anidados.
type: docs
weight: 130
url: /es/net/groupdocs.metadata.common/metadatapackage/updateproperties/
---
## MetadataPackage.UpdateProperties method

Actualiza las propiedades de metadatos conocidas que satisfacen el predicado especificado. La operación es recursiva, por lo que también afecta a todos los paquetes anidados.

```csharp
public int UpdateProperties(Func<MetadataProperty, bool> predicate, PropertyValue value)
```

| Parámetro | Escribe | Descripción |
| --- | --- | --- |
| predicate | Func`2 | Una función para probar cada propiedad de metadatos para una condición. |
| value | PropertyValue | Un nuevo valor para las propiedades filtradas. |

### Valor_devuelto

El número de propiedades afectadas.

### Observaciones

Tenga en cuenta que GroupDocs.Metadata comprueba implícitamente el tipo de cada propiedad filtrada. Es imposible actualizar una propiedad con un valor que tiene un tipo inadecuado.

**Aprende más**

* Más ejemplos que demuestran los usos de este método: [Actualización de metadatos](https://docs.groupdocs.com/display/metadatanet/Updating+metadata)

### Ver también

* delegate [Func&lt;T,TResult&gt;](../../func-2)
* class [MetadataProperty](../../metadataproperty)
* class [PropertyValue](../../propertyvalue)
* class [MetadataPackage](../../metadatapackage)
* espacio de nombres [GroupDocs.Metadata.Common](../../metadatapackage)
* asamblea [GroupDocs.Metadata](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Metadata.dll -->
