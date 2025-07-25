---
title: ConvertTo
second_title: GroupDocs.Conversion for .NET API Reference
description: Save converted document as file
type: docs
weight: 20
url: /net/groupdocs.conversion.fluent/iconversionto/convertto/
---
## ConvertTo(string) {#convertto_1}

Save converted document as file

```csharp
public IConversionOptionsOrHandlerSetup ConvertTo(string fileName)
```

| Parameter | Type | Description |
| --- | --- | --- |
| fileName | String | Converted document |

### Return Value

Options or handler setup interface to continue conversion building

### See Also

* interface [IConversionOptionsOrHandlerSetup](../../iconversionoptionsorhandlersetup)
* interface [IConversionTo](../../iconversionto)
* namespace [GroupDocs.Conversion.Fluent](../../../groupdocs.conversion.fluent)
* assembly [GroupDocs.Conversion](../../../)

---

## ConvertTo(Func&lt;SaveContext, Stream&gt;) {#convertto}

Save converted document as stream

```csharp
public IConversionOptionsOrHandlerSetup ConvertTo(Func<SaveContext, Stream> convertedStreamProvider)
```

| Parameter | Type | Description |
| --- | --- | --- |
| convertedStreamProvider | Func`2 | Converted document stream provider The save context |

### Return Value

Options or handler setup interface to continue conversion building

### See Also

* interface [IConversionOptionsOrHandlerSetup](../../iconversionoptionsorhandlersetup)
* class [SaveContext](../../../groupdocs.conversion/savecontext)
* interface [IConversionTo](../../iconversionto)
* namespace [GroupDocs.Conversion.Fluent](../../../groupdocs.conversion.fluent)
* assembly [GroupDocs.Conversion](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.conversion.dll -->
