---
title: JsonDataLoadOptions
second_title: Справочник по API GroupDocs.Assembly для .NET
description: Представляет параметры анализа данных JSON.
type: docs
weight: 140
url: /ru/net/groupdocs.assembly.data/jsondataloadoptions/
---
## JsonDataLoadOptions class

Представляет параметры анализа данных JSON.

```csharp
public class JsonDataLoadOptions
```

## Конструкторы

| Имя | Описание |
| --- | --- |
| [JsonDataLoadOptions](jsondataloadoptions)() | Инициализирует новый экземпляр этого класса с параметрами по умолчанию. |

## Характеристики

| Имя | Описание |
| --- | --- |
| [AlwaysGenerateRootObject](../../groupdocs.assembly.data/jsondataloadoptions/alwaysgeneraterootobject) { get; set; } | Получает или задает флаг, указывающий, всегда ли сгенерированный источник данных будет содержать объект для элемента JSON root . Если корневой элемент JSON содержит одно сложное свойство, такой объект по умолчанию не создается. |
| [ExactDateTimeParseFormats](../../groupdocs.assembly.data/jsondataloadoptions/exactdatetimeparseformats) { get; set; } | Получает или задает точные форматы для анализа значений даты и времени JSON при загрузке JSON. По умолчанию**нулевой** . |
| [SimpleValueParseMode](../../groupdocs.assembly.data/jsondataloadoptions/simplevalueparsemode) { get; set; } | Получает или задает режим анализа простых значений JSON (пустых, логических, числовых, целых и строковых) при загрузке JSON. Такой режим не влияет на синтаксический анализ значений даты и времени. По умолчанию Loose . |

### Примечания

Экземпляр этого класса может быть передан в конструкторы[`JsonDataSource`](../jsondatasource) .

### Смотрите также

* пространство имен [GroupDocs.Assembly.Data](../../groupdocs.assembly.data)
* сборка [GroupDocs.Assembly](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Assembly.dll -->
