---
title: XmpArray
second_title: Справочник по API GroupDocs.Metadata для .NET
description: Представляет базовую абстракцию для массива XMP.
type: docs
weight: 3250
url: /ru/net/groupdocs.metadata.standards.xmp/xmparray/
---
## XmpArray class

Представляет базовую абстракцию для массива XMP.

```csharp
public class XmpArray : XmpValueBase
```

## Конструкторы

| Имя | Описание |
| --- | --- |
| [XmpArray](xmparray#constructor)(XmpArrayType, XmpComplexType[]) | Инициализирует новый экземпляр[`XmpArray`](../xmparray) класс. |
| [XmpArray](xmparray#constructor_1)(XmpArrayType, XmpValueBase[]) | Инициализирует новый экземпляр[`XmpArray`](../xmparray) класс. |

## Характеристики

| Имя | Описание |
| --- | --- |
| [ArrayType](../../groupdocs.metadata.standards.xmp/xmparray/arraytype) { get; } | Получает тип массива XMP. |
| [RawValue](../../groupdocs.metadata.common/propertyvalue/rawvalue) { get; } | Получает исходное значение. |
| [Type](../../groupdocs.metadata.common/propertyvalue/type) { get; } | Получает[`MetadataPropertyType`](../../groupdocs.metadata.common/metadatapropertytype) . |

## Методы

| Имя | Описание |
| --- | --- |
| static [From](../../groupdocs.metadata.standards.xmp/xmparray/from#from_2)(DateTime[], XmpArrayType) | Создает[`XmpArray`](../xmparray) экземпляр формирует массив дат. |
| static [From](../../groupdocs.metadata.standards.xmp/xmparray/from#from)(double[], XmpArrayType) | Создает[`XmpArray`](../xmparray) Экземпляр образует двойной массив. |
| static [From](../../groupdocs.metadata.standards.xmp/xmparray/from#from_1)(int[], XmpArrayType) | Создает[`XmpArray`](../xmparray) Экземпляр формирует целочисленный массив. |
| static [From](../../groupdocs.metadata.standards.xmp/xmparray/from#from_3)(string[], XmpArrayType) | Создает[`XmpArray`](../xmparray) экземпляр формирует массив строк. |
| static [From&lt;T&gt;](../../groupdocs.metadata.standards.xmp/xmparray/from#from_4)(T[], XmpArrayType) | Создает[`XmpArray`](../xmparray)экземпляр образуют массив[`XmpComplexType`](../xmpcomplextype) . |
| [AcceptValue](../../groupdocs.metadata.common/propertyvalue/acceptvalue)(ValueAcceptor) | Извлекает значение свойства с помощью пользовательского[`ValueAcceptor`](../../groupdocs.metadata.common/valueacceptor) . |
| override [GetXmpRepresentation](../../groupdocs.metadata.standards.xmp/xmparray/getxmprepresentation)() | Преобразует значение XMP в представление xml. |
| [ToArray&lt;TElement&gt;](../../groupdocs.metadata.common/propertyvalue/toarray)() | Преобразует значение свойства в массив указанного типа. |
| [ToClass&lt;T&gt;](../../groupdocs.metadata.common/propertyvalue/toclass)() | Преобразует значение свойства в ссылочный тип. |
| [ToPlatformArray&lt;T&gt;](../../groupdocs.metadata.standards.xmp/xmparray/toplatformarray)() | Преобразует[`XmpArray`](../xmparray) в массив для конкретной платформы. |
| override [ToString](../../groupdocs.metadata.standards.xmp/xmpvaluebase/tostring)() | Возвращает строку, представляющую значение свойства. |
| [ToStruct&lt;T&gt;](../../groupdocs.metadata.common/propertyvalue/tostruct)() | Преобразует значение свойства в тип значения. |
| [ToStruct&lt;T&gt;](../../groupdocs.metadata.common/propertyvalue/tostruct)(T) | Преобразует значение свойства в тип значения. |

### Смотрите также

* class [XmpValueBase](../xmpvaluebase)
* пространство имен [GroupDocs.Metadata.Standards.Xmp](../../groupdocs.metadata.standards.xmp)
* сборка [GroupDocs.Metadata](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Metadata.dll -->
