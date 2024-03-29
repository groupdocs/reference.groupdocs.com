---
title: SetProperties
second_title: Справочник по API GroupDocs.Metadata для .NET
description: Устанавливает известные свойства метаданных удовлетворяющие указанному предикату. Операция является рекурсивной поэтому она влияет также на все вложенные пакеты. Этот метод представляет собой комбинациюAddPropertiesgroupdocs.metadata/metadata/addproperties иUpdatePropertiesgroupdocs.metadata/metadata/updateproperties . Если существующее свойство удовлетворяет предикату его значение обновляется. Если в пакете отсутствует известное свойство удовлетворяющее предикату оно добавляется в пакет.
type: docs
weight: 120
url: /ru/net/groupdocs.metadata/metadata/setproperties/
---
## Metadata.SetProperties method

Устанавливает известные свойства метаданных, удовлетворяющие указанному предикату. Операция является рекурсивной, поэтому она влияет также на все вложенные пакеты. Этот метод представляет собой комбинацию[`AddProperties`](../addproperties) и[`UpdateProperties`](../updateproperties) . Если существующее свойство удовлетворяет предикату, его значение обновляется. Если в пакете отсутствует известное свойство, удовлетворяющее предикату, оно добавляется в пакет.

```csharp
public int SetProperties(Func<MetadataProperty, bool> predicate, PropertyValue value)
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| predicate | Func`2 | Функция для проверки каждого свойства метаданных на наличие условия. |
| value | PropertyValue | Новое значение отфильтрованных свойств. |

### Возвращаемое значение

Количество затронутых свойств.

### Примечания

Обратите внимание, что GroupDocs.Metadata неявно проверяет тип каждого отфильтрованного свойства. Невозможно установить свойство со значением неподходящего типа.

**Узнать больше**

* [Установить свойства метаданных](https://docs.groupdocs.com/display/metadatanet/Set+metadata+properties)

### Примеры

В этом примере показано, как установить определенные свойства метаданных с использованием различных критериев.

```csharp
using (Metadata metadata = new Metadata(Constants.InputVsdx))
{
    // Установить значение каждого свойства, которое удовлетворяет предикату:
    // свойство содержит дату/время создания или изменения документа
    var affected = metadata.SetProperties(
    p => p.Tags.Contains(Tags.Time.Created) || p.Tags.Contains(Tags.Time.Modified),
    new PropertyValue(DateTime.Now));

    Console.WriteLine("Properties set: {0}", affected);

    metadata.Save(Constants.OutputVsdx);
}
```

### Смотрите также

* delegate [Func&lt;T,TResult&gt;](../../../groupdocs.metadata.common/func-2)
* class [MetadataProperty](../../../groupdocs.metadata.common/metadataproperty)
* class [PropertyValue](../../../groupdocs.metadata.common/propertyvalue)
* class [Metadata](../../metadata)
* пространство имен [GroupDocs.Metadata](../../metadata)
* сборка [GroupDocs.Metadata](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Metadata.dll -->
