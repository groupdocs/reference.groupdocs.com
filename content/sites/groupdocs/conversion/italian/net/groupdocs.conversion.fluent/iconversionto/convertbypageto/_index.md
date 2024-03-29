---
title: ConvertByPageTo
second_title: Riferimento API GroupDocs.Conversion per .NET
description: Salva la pagina convertita come stream
type: docs
weight: 10
url: /it/net/groupdocs.conversion.fluent/iconversionto/convertbypageto/
---
## ConvertByPageTo(Func&lt;int, Stream&gt;) {#convertbypageto}

Salva la pagina convertita come stream

```csharp
public IConversionConvertOptionOrPageCompletedOrConvert ConvertByPageTo(
    Func<int, Stream> convertedPageProvider)
```

| Parametro | Tipo | Descrizione |
| --- | --- | --- |
| convertedPageProvider | Func`2 | Provider flusso pagina documento convertito |

### Valore di ritorno

Interfaccia per continuare la costruzione della conversione

### Guarda anche

* interface [IConversionConvertOptionOrPageCompletedOrConvert](../../iconversionconvertoptionorpagecompletedorconvert)
* interface [IConversionTo](../../iconversionto)
* spazio dei nomi [GroupDocs.Conversion.Fluent](../../iconversionto)
* assemblea [GroupDocs.Conversion](../../../)

---

## ConvertByPageTo(Func&lt;int, FileType, Stream&gt;) {#convertbypageto_1}

Salva la pagina convertita come stream per tipo

```csharp
public IConversionConvertOptionOrPageCompletedOrConvert ConvertByPageTo(
    Func<int, FileType, Stream> convertedStreamProvider)
```

| Parametro | Tipo | Descrizione |
| --- | --- | --- |
| convertedStreamProvider | Func`3 | Provider flusso pagina documento convertito |

### Valore di ritorno

Interfaccia per continuare la costruzione della conversione

### Guarda anche

* interface [IConversionConvertOptionOrPageCompletedOrConvert](../../iconversionconvertoptionorpagecompletedorconvert)
* class [FileType](../../../groupdocs.conversion.filetypes/filetype)
* interface [IConversionTo](../../iconversionto)
* spazio dei nomi [GroupDocs.Conversion.Fluent](../../iconversionto)
* assemblea [GroupDocs.Conversion](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Conversion.dll -->
