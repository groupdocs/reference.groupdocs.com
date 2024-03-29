---
title: GetConsumptionCredit
second_title: GroupDocs.Parser for .NET API リファレンス
description: 消費されたクレジットの数を取得します
type: docs
weight: 30
url: /ja/net/groupdocs.parser/metered/getconsumptioncredit/
---
## Metered.GetConsumptionCredit method

消費されたクレジットの数を取得します。

```csharp
public static decimal GetConsumptionCredit()
```

### 戻り値

消費クレジットを表す 10 進数値。

### 例

次の例は、消費されたクレジットの数を取得する方法を示しています。

```csharp
string publicKey = "Public Key";
string privateKey = "Private Key";

Metered metered = new Metered();
metered.SetMeteredKey(publicKey, privateKey);

decimal creditsConsumed = Metered.GetConsumptionCredit();
```

### 関連項目

* class [Metered](../../metered)
* 名前空間 [GroupDocs.Parser](../../metered)
* 組み立て [GroupDocs.Parser](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Parser.dll -->
