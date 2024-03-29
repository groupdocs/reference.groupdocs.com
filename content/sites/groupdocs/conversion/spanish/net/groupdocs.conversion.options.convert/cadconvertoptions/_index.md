---
title: CadConvertOptions
second_title: Referencia de API de GroupDocs.Conversion para .NET
description: Opciones de conversión a tipo Cad.
type: docs
weight: 1430
url: /es/net/groupdocs.conversion.options.convert/cadconvertoptions/
---
## CadConvertOptions class

Opciones de conversión a tipo Cad.

```csharp
public class CadConvertOptions : ConvertOptions<CadFileType>, IPagedConvertOptions
```

## Constructores

| Nombre | Descripción |
| --- | --- |
| [CadConvertOptions](cadconvertoptions)() | Inicializa una nueva instancia de[`CadConvertOptions`](../cadconvertoptions) clase. |

## Propiedades

| Nombre | Descripción |
| --- | --- |
| [Format](../../groupdocs.conversion.options.convert/convertoptions-1/format) { get; set; } | El tipo de archivo deseado al que se debe convertir el documento de entrada. |
| virtual [Format](../../groupdocs.conversion.options.convert/convertoptions/format) { get; set; } | El tipo de archivo deseado al que se debe convertir el documento de entrada. |
| [PageNumber](../../groupdocs.conversion.options.convert/cadconvertoptions/pagenumber) { get; set; } | El número de página desde el que iniciar la conversión. |
| [PagesCount](../../groupdocs.conversion.options.convert/cadconvertoptions/pagescount) { get; set; } | Número de páginas para convertir a partir de`Número de página` . |

## Métodos

| Nombre | Descripción |
| --- | --- |
| [Clone](../../groupdocs.conversion.options.convert/convertoptions/clone)() | Clona la instancia de opciones actual. |
| override [Equals](../../groupdocs.conversion.contracts/valueobject/equals)(object) | Determina si dos instancias de objeto son iguales. |
| virtual [Equals](../../groupdocs.conversion.contracts/valueobject/equals)(ValueObject) | Determina si dos instancias de objeto son iguales. |
| override [GetHashCode](../../groupdocs.conversion.contracts/valueobject/gethashcode)() | Sirve como la función hash predeterminada. |

### Ver también

* class [ConvertOptions&lt;TFileType&gt;](../convertoptions-1)
* class [CadFileType](../../groupdocs.conversion.filetypes/cadfiletype)
* interface [IPagedConvertOptions](../ipagedconvertoptions)
* espacio de nombres [GroupDocs.Conversion.Options.Convert](../../groupdocs.conversion.options.convert)
* asamblea [GroupDocs.Conversion](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Conversion.dll -->
