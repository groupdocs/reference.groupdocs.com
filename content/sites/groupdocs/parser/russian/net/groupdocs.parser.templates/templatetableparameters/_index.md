---
title: TemplateTableParameters
second_title: Справочник по API GroupDocs.Parser для .NET
description: Предоставляет параметры для алгоритмов обнаружения таблиц.
type: docs
weight: 710
url: /ru/net/groupdocs.parser.templates/templatetableparameters/
---
## TemplateTableParameters class

Предоставляет параметры для алгоритмов обнаружения таблиц.

```csharp
public sealed class TemplateTableParameters
```

## Конструкторы

| Имя | Описание |
| --- | --- |
| [TemplateTableParameters](templatetableparameters#constructor)(Rectangle, IEnumerable&lt;double&gt;) | Инициализирует новый экземпляр[`TemplateTableParameters`](../templatetableparameters) класс. |
| [TemplateTableParameters](templatetableparameters#constructor_1)(Rectangle, IEnumerable&lt;double&gt;, bool?, int?, int?, int?) | Инициализирует новый экземпляр[`TemplateTableParameters`](../templatetableparameters) класс. |

## Характеристики

| Имя | Описание |
| --- | --- |
| [HasMergedCells](../../groupdocs.parser.templates/templatetableparameters/hasmergedcells) { get; } | Получает значение, указывающее, есть ли в таблице объединенные ячейки. |
| [MinColumnCount](../../groupdocs.parser.templates/templatetableparameters/mincolumncount) { get; } | Получает минимальное количество столбцов таблицы. |
| [MinRowCount](../../groupdocs.parser.templates/templatetableparameters/minrowcount) { get; } | Получает минимальное количество строк таблицы. |
| [MinVerticalSpace](../../groupdocs.parser.templates/templatetableparameters/minverticalspace) { get; } | Получает минимальное расстояние между столбцами таблицы. |
| [Rectangle](../../groupdocs.parser.templates/templatetableparameters/rectangle) { get; } | Получает прямоугольную область, содержащую таблицу. |
| [VerticalSeparators](../../groupdocs.parser.templates/templatetableparameters/verticalseparators) { get; } | Получает разделители столбцов таблицы. |

### Примечания

Существует два алгоритма обнаружения таблицы:

* Позволяет обнаружить таблицу в прямоугольной области с заданными столбцами. Этот алгоритм полезен для простых таблиц (без объединенных столбцов) и обеспечивает более точное обнаружение.
* Позволяет обнаружить таблицу в любом месте страницы. Это более сложный алгоритм. Он может обнаруживать таблицы в любом месте на странице. Дополнительные параметры помогают определить таблицу более корректно.

В некоторых случаях, когда алгоритмы не могут обнаружить таблицу или делают это неточно [`TemplateTableLayout`](../templatetablelayout) используется класс.

### Смотрите также

* пространство имен [GroupDocs.Parser.Templates](../../groupdocs.parser.templates)
* сборка [GroupDocs.Parser](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Parser.dll -->