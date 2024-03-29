---
title: OcrEventHandler
second_title: Справочник по API GroupDocs.Parser для .NET
description: Предоставляет обработчик событий OCR.
type: docs
weight: 490
url: /ru/net/groupdocs.parser.options/ocreventhandler/
---
## OcrEventHandler class

Предоставляет обработчик событий OCR.

```csharp
public class OcrEventHandler
```

## Конструкторы

| Имя | Описание |
| --- | --- |
| [OcrEventHandler](ocreventhandler)() | Инициализирует новый экземпляр[`OcrEventHandler`](../ocreventhandler) класс. |

## Характеристики

| Имя | Описание |
| --- | --- |
| [HasWarnings](../../groupdocs.parser.options/ocreventhandler/haswarnings) { get; } | Получает значение, указывающее, не является ли список предупреждений пустым. |
| [Warnings](../../groupdocs.parser.options/ocreventhandler/warnings) { get; } | Получает список предупреждающих сообщений. |

## Методы

| Имя | Описание |
| --- | --- |
| [GetWarnings](../../groupdocs.parser.options/ocreventhandler/getwarnings)(int) | Возвращает список предупреждающих сообщений для страницы с*pageIndex* . |
| virtual [OnWarnings](../../groupdocs.parser.options/ocreventhandler/onwarnings)(int, IList&lt;string&gt;) | Устанавливает предупреждающие сообщения для страницы. |

### Смотрите также

* пространство имен [GroupDocs.Parser.Options](../../groupdocs.parser.options)
* сборка [GroupDocs.Parser](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Parser.dll -->
