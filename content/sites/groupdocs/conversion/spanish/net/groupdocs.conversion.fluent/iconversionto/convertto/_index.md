---
title: ConvertTo
second_title: Referencia de API de GroupDocs.Conversion para .NET
description: Guardar documento convertido como archivo
type: docs
weight: 20
url: /es/net/groupdocs.conversion.fluent/iconversionto/convertto/
---
## ConvertTo(string) {#convertto_2}

Guardar documento convertido como archivo

```csharp
public IConversionConvertOptionOrCompletedOrConvert ConvertTo(string fileName)
```

| Parámetro | Escribe | Descripción |
| --- | --- | --- |
| fileName | String | Documento convertido |

### Valor_devuelto

Interfaz para continuar construyendo conversión

### Ver también

* interface [IConversionConvertOptionOrCompletedOrConvert](../../iconversionconvertoptionorcompletedorconvert)
* interface [IConversionTo](../../iconversionto)
* espacio de nombres [GroupDocs.Conversion.Fluent](../../iconversionto)
* asamblea [GroupDocs.Conversion](../../../)

---

## ConvertTo(Func&lt;Stream&gt;) {#convertto}

Guardar documento convertido como stream

```csharp
public IConversionConvertOptionOrCompletedOrConvert ConvertTo(Func<Stream> convertedStreamProvider)
```

| Parámetro | Escribe | Descripción |
| --- | --- | --- |
| convertedStreamProvider | Func`1 | Proveedor de flujo de documentos convertidos |

### Valor_devuelto

Interfaz para continuar construyendo conversión

### Ver también

* interface [IConversionConvertOptionOrCompletedOrConvert](../../iconversionconvertoptionorcompletedorconvert)
* interface [IConversionTo](../../iconversionto)
* espacio de nombres [GroupDocs.Conversion.Fluent](../../iconversionto)
* asamblea [GroupDocs.Conversion](../../../)

---

## ConvertTo(Func&lt;FileType, Stream&gt;) {#convertto_1}

Guardar documento convertido como flujo por type

```csharp
public IConversionConvertOptionOrCompletedOrConvert ConvertTo(
    Func<FileType, Stream> convertedStreamProvider)
```

| Parámetro | Escribe | Descripción |
| --- | --- | --- |
| convertedStreamProvider | Func`2 | Proveedor de flujo de documentos convertido |

### Valor_devuelto

Interfaz para continuar construyendo conversión

### Ver también

* interface [IConversionConvertOptionOrCompletedOrConvert](../../iconversionconvertoptionorcompletedorconvert)
* class [FileType](../../../groupdocs.conversion.filetypes/filetype)
* interface [IConversionTo](../../iconversionto)
* espacio de nombres [GroupDocs.Conversion.Fluent](../../iconversionto)
* asamblea [GroupDocs.Conversion](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Conversion.dll -->
