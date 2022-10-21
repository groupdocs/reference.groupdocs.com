---
title: FromStartPageWithCount
second_title: Справочник по API GroupDocs.Editor для .NET
description: Создает диапазон страниц который начинается с указанного номера страницы и имеет указанное количество страниц или неограниченное количество страниц до конца
type: docs
weight: 50
url: /ru/net/groupdocs.editor.options/pagerange/fromstartpagewithcount/
---
## PageRange.FromStartPageWithCount method

Создает диапазон страниц, который начинается с указанного номера страницы и имеет указанное количество страниц или неограниченное количество страниц (до конца)

```csharp
public static PageRange FromStartPageWithCount(ushort startPageNumber, ushort pageCount)
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| startPageNumber | UInt16 | Номер страницы, с которой начинается диапазон страниц включительно. Номера страниц отсчитываются от 1, поэтому они должны быть строго больше нуля. |
| pageCount | UInt16 | Количество страниц должно быть строго больше нуля. Если ноль - это означает все страницы до конца документа |

### Возвращаемое значение

Новый экземпляр PageRange

### Смотрите также

* struct [PageRange](../../pagerange)
* пространство имен [GroupDocs.Editor.Options](../../pagerange)
* сборка [GroupDocs.Editor](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Editor.dll -->