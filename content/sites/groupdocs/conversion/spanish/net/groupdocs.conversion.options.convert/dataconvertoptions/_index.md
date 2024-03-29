---
title: DataConvertOptions
second_title: Referencia de API de GroupDocs.Conversion para .NET
description: Opciones para la conversión a tipo de archivo de datos.
type: docs
weight: 1480
url: /es/net/groupdocs.conversion.options.convert/dataconvertoptions/
---
## DataConvertOptions class

Opciones para la conversión a tipo de archivo de datos.

```csharp
[Obsolete("This class will be removed in Conversion.NET 23.3. Please use WebConvertOptions instead.")]
public class DataConvertOptions : ConvertOptions<DataFileType>, IPagedConvertOptions
```

## Propiedades

| Nombre | Descripción |
| --- | --- |
| [Format](../../groupdocs.conversion.options.convert/convertoptions-1/format) { get; set; } | El tipo de archivo deseado al que se debe convertir el documento de entrada. |
| virtual [Format](../../groupdocs.conversion.options.convert/convertoptions/format) { get; set; } | El tipo de archivo deseado al que se debe convertir el documento de entrada. |

## Métodos

| Nombre | Descripción |
| --- | --- |
| [Clone](../../groupdocs.conversion.options.convert/convertoptions/clone)() | Clona la instancia de opciones actual. |
| override [Equals](../../groupdocs.conversion.contracts/valueobject/equals)(object) | Determina si dos instancias de objeto son iguales. |
| virtual [Equals](../../groupdocs.conversion.contracts/valueobject/equals)(ValueObject) | Determina si dos instancias de objeto son iguales. |
| override [GetHashCode](../../groupdocs.conversion.contracts/valueobject/gethashcode)() | Sirve como la función hash predeterminada. |

### Ver también

* class [ConvertOptions&lt;TFileType&gt;](../convertoptions-1)
* class [DataFileType](../../groupdocs.conversion.filetypes/datafiletype)
* interface [IPagedConvertOptions](../ipagedconvertoptions)
* espacio de nombres [GroupDocs.Conversion.Options.Convert](../../groupdocs.conversion.options.convert)
* asamblea [GroupDocs.Conversion](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Conversion.dll -->
