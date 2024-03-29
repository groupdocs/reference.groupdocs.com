---
title: Name
second_title: Referencia de API de GroupDocs.Assembly para .NET
description: Obtiene o establece el nombre de esta tabla utilizada para acceder a los datos de la tabla en un documento de plantilla pasado a DocumentAssemblergroupdocs.assembly/documentassembler .
type: docs
weight: 40
url: /es/net/groupdocs.assembly.data/documenttable/name/
---
## DocumentTable.Name property

Obtiene o establece el nombre de esta tabla utilizada para acceder a los datos de la tabla en un documento de plantilla pasado a [`DocumentAssembler`](../../../groupdocs.assembly/documentassembler) .

```csharp
public string Name { get; set; }
```

### Observaciones

Si se lee el nombre de la tabla desde un documento, automáticamente se corrige el nombre para que sea válido. Sin embargo, si el nombre de la tabla se establece manualmente a través de esta propiedad y el nombre no es válido, se genera una excepción.

El nombre de la tabla se considera válido si se cumplen las siguientes condiciones:

* El nombre no está vacío.
* El primer carácter del nombre es una letra o un guión bajo.
* El resto de caracteres del nombre son letras, guiones bajos, dígitos o los siguientes caracteres: '@', '#', '$'.
* El correspondiente[`DocumentTableSet`](../../documenttableset) objeto no contiene un[`DocumentTable`](../../documenttable) instancia con el mismo nombre.

### Ver también

* class [DocumentTable](../../documenttable)
* espacio de nombres [GroupDocs.Assembly.Data](../../documenttable)
* asamblea [GroupDocs.Assembly](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Assembly.dll -->
