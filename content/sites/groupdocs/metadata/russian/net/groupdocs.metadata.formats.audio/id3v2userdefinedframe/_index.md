---
title: ID3V2UserDefinedFrame
second_title: Справочник по API GroupDocs.Metadata для .NET
description: Представляет кадр TXXX вID3V2Tag./id3v2tag .
type: docs
weight: 540
url: /ru/net/groupdocs.metadata.formats.audio/id3v2userdefinedframe/
---
## ID3V2UserDefinedFrame class

Представляет кадр TXXX в[`ID3V2Tag`](../id3v2tag) .

```csharp
public sealed class ID3V2UserDefinedFrame : ID3V2TagFrame
```

## Конструкторы

| Имя | Описание |
| --- | --- |
| [ID3V2UserDefinedFrame](id3v2userdefinedframe#constructor_1)(string, string) | Инициализирует новый экземпляр[`ID3V2UserDefinedFrame`](../id3v2userdefinedframe) класс. |
| [ID3V2UserDefinedFrame](id3v2userdefinedframe#constructor)(ID3V2EncodingType, string, string) | Инициализирует новый экземпляр[`ID3V2UserDefinedFrame`](../id3v2userdefinedframe) класс. |

## Характеристики

| Имя | Описание |
| --- | --- |
| [Count](../../groupdocs.metadata.common/metadatapackage/count) { get; } | Получает количество свойств метаданных. |
| [Data](../../groupdocs.metadata.formats.audio/id3v2tagframe/data) { get; } | Получает данные кадра. |
| [Description](../../groupdocs.metadata.formats.audio/id3v2userdefinedframe/description) { get; } | Получает описание. |
| [Encoding](../../groupdocs.metadata.formats.audio/id3v2userdefinedframe/encoding) { get; } | Получает кодировку кадра. |
| [Flags](../../groupdocs.metadata.formats.audio/id3v2tagframe/flags) { get; } | Получает флаги кадра. |
| [Id](../../groupdocs.metadata.formats.audio/id3v2tagframe/id) { get; } | Получает идентификатор фрейма (четыре символа, соответствующие шаблону [A-Z0-9]). |
| [Item](../../groupdocs.metadata.common/metadatapackage/item) { get; } | Получает[`MetadataProperty`](../../groupdocs.metadata.common/metadataproperty) с указанным именем. |
| [Keys](../../groupdocs.metadata.common/metadatapackage/keys) { get; } | Получает коллекцию имен свойств метаданных. |
| [MetadataType](../../groupdocs.metadata.common/metadatapackage/metadatatype) { get; } | Получает тип метаданных. |
| [PropertyDescriptors](../../groupdocs.metadata.common/metadatapackage/propertydescriptors) { get; } | Получает набор дескрипторов, содержащих информацию о свойствах, доступных через поисковую систему GroupDocs.Metadata. |
| [Value](../../groupdocs.metadata.formats.audio/id3v2userdefinedframe/value) { get; } | Получает значение. |

## Методы

| Имя | Описание |
| --- | --- |
| [AddProperties](../../groupdocs.metadata.common/metadatapackage/addproperties)(Func&lt;MetadataProperty, bool&gt;, PropertyValue) | Добавляет известные свойства метаданных, удовлетворяющие указанному предикату. Операция является рекурсивной, поэтому она также влияет на все вложенные пакеты. |
| [Contains](../../groupdocs.metadata.common/metadatapackage/contains)(string) | Определяет, содержит ли пакет свойство метаданных с указанным именем. |
| virtual [FindProperties](../../groupdocs.metadata.common/metadatapackage/findproperties)(Func&lt;MetadataProperty, bool&gt;) | Находит свойства метаданных, удовлетворяющие указанному предикату. Поиск является рекурсивным, поэтому он затрагивает также все вложенные пакеты. |
| [GetEnumerator](../../groupdocs.metadata.common/metadatapackage/getenumerator)() | Возвращает перечислитель, который выполняет итерацию по коллекции. |
| virtual [RemoveProperties](../../groupdocs.metadata.common/metadatapackage/removeproperties)(Func&lt;MetadataProperty, bool&gt;) | Удаляет свойства метаданных, удовлетворяющие указанному предикату. |
| virtual [Sanitize](../../groupdocs.metadata.common/metadatapackage/sanitize)() | Удаляет доступные для записи свойства метаданных из пакета. Операция является рекурсивной, поэтому она также влияет на все вложенные пакеты. |
| [SetProperties](../../groupdocs.metadata.common/metadatapackage/setproperties)(Func&lt;MetadataProperty, bool&gt;, PropertyValue) | Устанавливает известные свойства метаданных, удовлетворяющие указанному предикату. Операция является рекурсивной, поэтому она влияет также на все вложенные пакеты. Этот метод представляет собой комбинацию[`AddProperties`](../../groupdocs.metadata.common/metadatapackage/addproperties) и[`UpdateProperties`](../../groupdocs.metadata.common/metadatapackage/updateproperties) Если существующее свойство удовлетворяет предикату, его значение обновляется. Если в пакете отсутствует известное свойство, удовлетворяющее предикату, оно добавляется в пакет. |
| [UpdateProperties](../../groupdocs.metadata.common/metadatapackage/updateproperties)(Func&lt;MetadataProperty, bool&gt;, PropertyValue) | Обновляет известные свойства метаданных, удовлетворяющие указанному предикату. Операция является рекурсивной, поэтому она также влияет на все вложенные пакеты. |

### Примечания

**Узнать больше**

* [Обработка тега ID3v2](https://docs.groupdocs.com/display/metadatanet/Handling+the+ID3v2+tag)

### Смотрите также

* class [ID3V2TagFrame](../id3v2tagframe)
* пространство имен [GroupDocs.Metadata.Formats.Audio](../../groupdocs.metadata.formats.audio)
* сборка [GroupDocs.Metadata](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Metadata.dll -->
