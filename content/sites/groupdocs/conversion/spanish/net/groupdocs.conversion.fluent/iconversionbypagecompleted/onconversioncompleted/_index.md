---
title: OnConversionCompleted
second_title: Referencia de API de GroupDocs.Conversion para .NET
description: Recibe flujo de página convertida. Se activará solo si se establece ConvertToconvertedStreamProvider.
type: docs
weight: 10
url: /es/net/groupdocs.conversion.fluent/iconversionbypagecompleted/onconversioncompleted/
---
## IConversionByPageCompleted.OnConversionCompleted method

Recibe flujo de página convertida. Se activará solo si se establece "ConvertTo(convertedStreamProvider)".

```csharp
public IConversionConvertOrCompress OnConversionCompleted(
    Action<int, Stream, string> convertedPageStream)
```

| Parámetro | Escribe | Descripción |
| --- | --- | --- |
| convertedPageStream | Action`3 | Proveedor de secuencias de páginas convertidas El nombre del archivo |

### Valor_devuelto

Interfaz para continuar construyendo conversión

### Ver también

* interface [IConversionConvertOrCompress](../../iconversionconvertorcompress)
* interface [IConversionByPageCompleted](../../iconversionbypagecompleted)
* espacio de nombres [GroupDocs.Conversion.Fluent](../../iconversionbypagecompleted)
* asamblea [GroupDocs.Conversion](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Conversion.dll -->
