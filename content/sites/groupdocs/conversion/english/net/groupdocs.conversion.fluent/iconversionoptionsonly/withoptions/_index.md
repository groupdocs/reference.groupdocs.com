---
title: WithOptions
second_title: GroupDocs.Conversion for .NET API Reference
description: Sets conversion options for the conversion process.
type: docs
weight: 10
url: /net/groupdocs.conversion.fluent/iconversionoptionsonly/withoptions/
---
## WithOptions(ConvertOptions) {#withoptions}

Sets conversion options for the conversion process.

```csharp
public IConversionHandlerSetup WithOptions(ConvertOptions options)
```

| Parameter | Type | Description |
| --- | --- | --- |
| options | ConvertOptions | Conversion options. |

### Return Value

Handler setup interface to continue conversion building.

### See Also

* interface [IConversionHandlerSetup](../../iconversionhandlersetup)
* class [ConvertOptions](../../../groupdocs.conversion.options.convert/convertoptions)
* interface [IConversionOptionsOnly](../../iconversionoptionsonly)
* namespace [GroupDocs.Conversion.Fluent](../../../groupdocs.conversion.fluent)
* assembly [GroupDocs.Conversion](../../../)

---

## WithOptions(Func&lt;ConvertContext, ConvertOptions&gt;) {#withoptions_1}

Sets conversion options using a provider function.

```csharp
public IConversionHandlerSetup WithOptions(Func<ConvertContext, ConvertOptions> optionsProvider)
```

| Parameter | Type | Description |
| --- | --- | --- |
| optionsProvider | Func`2 | A function that provides conversion options based on the conversion context. |

### Return Value

Handler setup interface to continue conversion building.

### See Also

* interface [IConversionHandlerSetup](../../iconversionhandlersetup)
* class [ConvertContext](../../../groupdocs.conversion/convertcontext)
* class [ConvertOptions](../../../groupdocs.conversion.options.convert/convertoptions)
* interface [IConversionOptionsOnly](../../iconversionoptionsonly)
* namespace [GroupDocs.Conversion.Fluent](../../../groupdocs.conversion.fluent)
* assembly [GroupDocs.Conversion](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.conversion.dll -->
