---
title: GetConsumptionQuantity
second_title: GroupDocs.Parser for .NET API 参考
description: 检索已处理的 MB 数量
type: docs
weight: 40
url: /zh/net/groupdocs.parser/metered/getconsumptionquantity/
---
## Metered.GetConsumptionQuantity method

检索已处理的 MB 数量。

```csharp
public static decimal GetConsumptionQuantity()
```

### 返回值

表示消耗量的十进制值。

### 例子

以下示例演示如何检索已处理的 MB 数量。

```csharp
string publicKey = "Public Key";
string privateKey = "Private Key";

Metered metered = new Metered();
metered.SetMeteredKey(publicKey, privateKey);

decimal mbProcessed = Metered.GetConsumptionQuantity();
```

### 也可以看看

* class [Metered](../../metered)
* 命名空间 [GroupDocs.Parser](../../metered)
* 部件 [GroupDocs.Parser](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Parser.dll -->
