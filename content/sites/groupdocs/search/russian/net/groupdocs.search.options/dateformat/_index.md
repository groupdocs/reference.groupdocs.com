---
title: DateFormat
second_title: GroupDocs.Search для справочника API .NET
description: Представляет формат даты.
type: docs
weight: 740
url: /ru/net/groupdocs.search.options/dateformat/
---
## DateFormat class

Представляет формат даты.

```csharp
public class DateFormat
```

## Конструкторы

| Имя | Описание |
| --- | --- |
| [DateFormat](dateformat#constructor)(DateFormatElement[], string) | Инициализирует новый экземпляр[`DateFormat`](../dateformat) класс. |
| [DateFormat](dateformat#constructor_1)(string, DateFormatElement[]) | Инициализирует новый экземпляр[`DateFormat`](../dateformat) класс. |

## Характеристики

| Имя | Описание |
| --- | --- |
| [DateSeparator](../../groupdocs.search.options/dateformat/dateseparator) { get; } | Получает разделитель даты. |

## Методы

| Имя | Описание |
| --- | --- |
| override [ToString](../../groupdocs.search.options/dateformat/tostring)() | ВозвращаетString который представляет текущий[`DateFormat`](../dateformat) . |

### Примечания

**Учить больше**

* [Поиск диапазона дат](https://docs.groupdocs.com/display/searchnet/Date+range+search)

### Примеры

Пример демонстрирует типичное использование класса.

```csharp
string indexFolder = @"c:\MyIndex\";
string documentsFolder = @"c:\MyDocuments\";
string query = "daterange(2017-01-01 ~~ 2019-12-31)";

Index index = new Index(indexFolder); // Создание индекса в указанной папке
index.Add(documentsFolder); // Индексация документов из указанной папки

SearchOptions options = new SearchOptions();
options.DateFormats.Clear(); // Удаление форматов даты по умолчанию
DateFormatElement[] elements = new DateFormatElement[]
{
    DateFormatElement.MonthTwoDigits,
    DateFormatElement.DateSeparator,
    DateFormatElement.DayOfMonthTwoDigits,
    DateFormatElement.DateSeparator,
    DateFormatElement.YearFourDigits,
};
// Создание шаблона формата даты 'MM/dd/yyyy'
DateFormat dateFormat = new DateFormat(elements, "/");
options.DateFormats.Add(dateFormat);

SearchResult result = index.Search(query, options); // Поиск по индексу
```

### Смотрите также

* пространство имен [GroupDocs.Search.Options](../../groupdocs.search.options)
* сборка [GroupDocs.Search](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Search.dll -->