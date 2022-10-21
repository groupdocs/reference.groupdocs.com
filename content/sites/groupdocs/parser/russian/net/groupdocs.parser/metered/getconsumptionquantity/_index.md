---
title: GetConsumptionQuantity
second_title: Справочник по API GroupDocs.Parser для .NET
description: Получает количество обработанных МБ.
type: docs
weight: 40
url: /ru/net/groupdocs.parser/metered/getconsumptionquantity/
---
## Metered.GetConsumptionQuantity method

Получает количество обработанных МБ.

```csharp
public static decimal GetConsumptionQuantity()
```

### Возвращаемое значение

Десятичное значение, представляющее объем потребления.

### Примеры

В следующем примере показано, как получить количество обработанных МБ.

```csharp
string publicKey = "Public Key";
string privateKey = "Private Key";

Metered metered = new Metered();
metered.SetMeteredKey(publicKey, privateKey);

decimal mbProcessed = Metered.GetConsumptionQuantity();
```

### Смотрите также

* class [Metered](../../metered)
* пространство имен [GroupDocs.Parser](../../metered)
* сборка [GroupDocs.Parser](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Parser.dll -->