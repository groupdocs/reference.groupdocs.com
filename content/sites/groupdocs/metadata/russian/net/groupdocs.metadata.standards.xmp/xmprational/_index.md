---
title: XmpRational
second_title: Справочник по API GroupDocs.Metadata для .NET
description: Представляет XMP XmpRational.
type: docs
weight: 3510
url: /ru/net/groupdocs.metadata.standards.xmp/xmprational/
---
## XmpRational class

Представляет XMP XmpRational.

```csharp
public sealed class XmpRational : XmpValueBase
```

## Конструкторы

| Имя | Описание |
| --- | --- |
| [XmpRational](xmprational#constructor_1)(string) | Инициализирует новый экземпляр[`XmpBoolean`](../xmpboolean) класс. |
| [XmpRational](xmprational#constructor)(long, long) | Инициализирует новый экземпляр[`XmpRational`](../xmprational) класс. |

## Характеристики

| Имя | Описание |
| --- | --- |
| [Denominator](../../groupdocs.metadata.standards.xmp/xmprational/denominator) { get; } | Получает знаменатель |
| [DoubleValue](../../groupdocs.metadata.standards.xmp/xmprational/doublevalue) { get; } | Получает значение рационального типа, представленное в формате double. |
| [Numerator](../../groupdocs.metadata.standards.xmp/xmprational/numerator) { get; } | Получает числитель. |
| [RawValue](../../groupdocs.metadata.common/propertyvalue/rawvalue) { get; } | Получает исходное значение. |
| [Type](../../groupdocs.metadata.common/propertyvalue/type) { get; } | Получает[`MetadataPropertyType`](../../groupdocs.metadata.common/metadatapropertytype) . |

## Методы

| Имя | Описание |
| --- | --- |
| [AcceptValue](../../groupdocs.metadata.common/propertyvalue/acceptvalue)(ValueAcceptor) | Извлекает значение свойства с помощью пользовательского[`ValueAcceptor`](../../groupdocs.metadata.common/valueacceptor) . |
| override [GetXmpRepresentation](../../groupdocs.metadata.standards.xmp/xmprational/getxmprepresentation)() | Возвращает строковое значение в формате XMP. |
| [ToArray&lt;TElement&gt;](../../groupdocs.metadata.common/propertyvalue/toarray)() | Преобразует значение свойства в массив указанного типа. |
| [ToClass&lt;T&gt;](../../groupdocs.metadata.common/propertyvalue/toclass)() | Преобразует значение свойства в ссылочный тип. |
| override [ToString](../../groupdocs.metadata.standards.xmp/xmpvaluebase/tostring)() | Возвращает строку, представляющую значение свойства. |
| [ToStruct&lt;T&gt;](../../groupdocs.metadata.common/propertyvalue/tostruct)() | Преобразует значение свойства в тип значения. |
| [ToStruct&lt;T&gt;](../../groupdocs.metadata.common/propertyvalue/tostruct)(T) | Преобразует значение свойства в тип значения. |

### Смотрите также

* class [XmpValueBase](../xmpvaluebase)
* пространство имен [GroupDocs.Metadata.Standards.Xmp](../../groupdocs.metadata.standards.xmp)
* сборка [GroupDocs.Metadata](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Metadata.dll -->
