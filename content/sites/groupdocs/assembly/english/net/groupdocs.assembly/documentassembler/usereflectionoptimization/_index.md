---
title: UseReflectionOptimization
second_title: GroupDocs.Assembly for .NET API Reference
description: Gets or sets a value indicating whether invocations of custom type members performed via reflection API are optimized using dynamic class generation or not. The default value is true.
type: docs
weight: 60
url: /net/groupdocs.assembly/documentassembler/usereflectionoptimization/
---
## DocumentAssembler.UseReflectionOptimization property

Gets or sets a value indicating whether invocations of custom type members performed via reflection API are optimized using dynamic class generation or not. The default value is true.

```csharp
public static bool UseReflectionOptimization { get; set; }
```

### Remarks

There are some scenarios where it is preferrable to disable this optimization. For example, if you are dealing with small collections of data items all the time, then an overhead of dynamic class generation can be more noticeable than an overhead of direct reflection API calls.

### See Also

* class [DocumentAssembler](../../documentassembler)
* namespace [GroupDocs.Assembly](../../documentassembler)
* assembly [GroupDocs.Assembly](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Assembly.dll -->
