---
title: DataConvertOptions
second_title: Справочник по API GroupDocs.Conversion для .NET
description: Параметры преобразования в тип файла данных.
type: docs
weight: 1350
url: /ru/net/groupdocs.conversion.options.convert/dataconvertoptions/
---
## DataConvertOptions class

Параметры преобразования в тип файла данных.

```csharp
public class DataConvertOptions : ConvertOptions<DataFileType>, IPagedConvertOptions
```

## Конструкторы

| Имя | Описание |
| --- | --- |
| [DataConvertOptions](dataconvertoptions)() | Инициализирует новый экземпляр[`DataConvertOptions`](../dataconvertoptions) класс. |

## Характеристики

| Имя | Описание |
| --- | --- |
| [Format](../../groupdocs.conversion.options.convert/convertoptions-1/format) { get; set; } | Желаемый тип файла, в который должен быть преобразован входной документ. |
| virtual [Format](../../groupdocs.conversion.options.convert/convertoptions/format) { get; set; } | Желаемый тип файла, в который должен быть преобразован входной документ. |
| [PageNumber](../../groupdocs.conversion.options.convert/dataconvertoptions/pagenumber) { get; set; } | Номер страницы, с которой начинается преобразование. |
| [PagesCount](../../groupdocs.conversion.options.convert/dataconvertoptions/pagescount) { get; set; } | Количество страниц для конвертации, начиная с`Номер страницы` . |

## Методы

| Имя | Описание |
| --- | --- |
| [Clone](../../groupdocs.conversion.options.convert/convertoptions/clone)() | Копирует экземпляр текущих параметров. |
| override [Equals](../../groupdocs.conversion.contracts/valueobject/equals)(object) | Определяет, равны ли два экземпляра объекта. |
| virtual [Equals](../../groupdocs.conversion.contracts/valueobject/equals)(ValueObject) | Определяет, равны ли два экземпляра объекта. |
| override [GetHashCode](../../groupdocs.conversion.contracts/valueobject/gethashcode)() | Служит хеш-функцией по умолчанию. |

### Смотрите также

* class [ConvertOptions&lt;TFileType&gt;](../convertoptions-1)
* class [DataFileType](../../groupdocs.conversion.filetypes/datafiletype)
* interface [IPagedConvertOptions](../ipagedconvertoptions)
* пространство имен [GroupDocs.Conversion.Options.Convert](../../groupdocs.conversion.options.convert)
* сборка [GroupDocs.Conversion](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Conversion.dll -->
