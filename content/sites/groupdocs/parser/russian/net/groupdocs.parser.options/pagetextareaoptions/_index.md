---
title: PageTextAreaOptions
second_title: Справочник по API GroupDocs.Parser для .NET
description: Предоставляет параметры используемые для извлечения текстовых областей страницы.
type: docs
weight: 550
url: /ru/net/groupdocs.parser.options/pagetextareaoptions/
---
## PageTextAreaOptions class

Предоставляет параметры, используемые для извлечения текстовых областей страницы.

```csharp
public sealed class PageTextAreaOptions : PageAreaOptions
```

## Конструкторы

| Имя | Описание |
| --- | --- |
| [PageTextAreaOptions](pagetextareaoptions#constructor)(bool) | Инициализирует новый экземпляр[`PageTextAreaOptions`](../pagetextareaoptions) класс с опцией использования OCR. |
| [PageTextAreaOptions](pagetextareaoptions#constructor_2)(string) | Инициализирует новый экземпляр[`PageTextAreaOptions`](../pagetextareaoptions) класс с регулярным выражением. Остальные параметры установлены по умолчанию (подробности см. в примечаниях). |
| [PageTextAreaOptions](pagetextareaoptions#constructor_1)(bool, OcrOptions) | Инициализирует новый экземпляр[`PageTextAreaOptions`](../pagetextareaoptions) класс с возможностью установки опций OCR. |
| [PageTextAreaOptions](pagetextareaoptions#constructor_4)(string, Rectangle) | Инициализирует новый экземпляр[`PageTextAreaOptions`](../pagetextareaoptions) class с регулярным выражением и прямоугольной областью. Остальные параметры установлены по умолчанию (подробности см. в примечаниях). |
| [PageTextAreaOptions](pagetextareaoptions#constructor_3)(string, bool, bool, bool, Rectangle) | Инициализирует новый экземпляр[`PageTextAreaOptions`](../pagetextareaoptions) класс. |

## Характеристики

| Имя | Описание |
| --- | --- |
| [Expression](../../groupdocs.parser.options/pagetextareaoptions/expression) { get; } | Получает регулярное выражение. |
| [IgnoreFormatting](../../groupdocs.parser.options/pagetextareaoptions/ignoreformatting) { get; } | Получает значение, указывающее, игнорируется ли форматирование текста. |
| [MatchCase](../../groupdocs.parser.options/pagetextareaoptions/matchcase) { get; } | Получает значение, указывающее, не игнорируется ли текстовый регистр. |
| [OcrOptions](../../groupdocs.parser.options/pagetextareaoptions/ocroptions) { get; } | Получает дополнительные параметры для функции OCR. |
| [Rectangle](../../groupdocs.parser.options/pageareaoptions/rectangle) { get; } | Получает прямоугольную область, содержащую области страницы. |
| [UniteSegments](../../groupdocs.parser.options/pagetextareaoptions/unitesegments) { get; } | Получает значение, указывающее, объединены ли сегменты. |
| [UseOcr](../../groupdocs.parser.options/pagetextareaoptions/useocr) { get; } | Получает значение, указывающее, используются ли функции OCR для извлечения текстовых областей. |

### Примечания

Экземпляр[`PageTextAreaOptions`](../pagetextareaoptions) класс используется как параметр в[`GetTextAreas`](../../groupdocs.parser/parser/gettextareas) и[`GetTextAreas`](../../groupdocs.parser/parser/gettextareas) методы. См. примеры использования здесь. **Узнать больше:**

* [Извлечь текстовые области](https://docs.groupdocs.com/display/parsernet/Extract+text+areas)

### Смотрите также

* class [PageAreaOptions](../pageareaoptions)
* пространство имен [GroupDocs.Parser.Options](../../groupdocs.parser.options)
* сборка [GroupDocs.Parser](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Parser.dll -->
