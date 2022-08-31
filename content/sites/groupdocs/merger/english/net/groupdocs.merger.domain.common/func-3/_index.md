---
title: FuncT1T2TResult
second_title: GroupDocs.Merger for .NET API Reference
description: Encapsulates a method that has two parameters and returns a value of the type specified by the TResult parameter.
type: docs
weight: 790
url: /net/groupdocs.merger.domain.common/func-3/
---
## Func&lt;T1,T2,TResult&gt; delegate

Encapsulates a method that has two parameters and returns a value of the type specified by the *TResult* parameter.

```csharp
public delegate TResult Func<in T1, in T2, out TResult>(T1 arg1, T2 arg2);
```

| Parameter | Description |
| --- | --- |
| T1 | The type of first parameters of the method that this delegate encapsulates. |
| T2 | The type of the second parameter of the method that this delegate encapsulates. |
| TResult | The type of the return value of the method that this delegate encapsulates. |
| arg1 | The first parameter of the method that this delegate encapsulates. |
| arg2 | The second parameter of the method that this delegate encapsulates. |

### Return Value

The return value of the method that this delegate encapsulates.

### See Also

* namespace [GroupDocs.Merger.Domain.Common](../../groupdocs.merger.domain.common)
* assembly [GroupDocs.Merger](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Merger.dll -->