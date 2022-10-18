---
title: CadOptions
second_title: Справочник по API GroupDocs.Viewer для .NET
description: Предоставляет параметры для визуализации чертежей САПР.
type: docs
weight: 290
url: /ru/net/groupdocs.viewer.options/cadoptions/
---
## CadOptions class

Предоставляет параметры для визуализации чертежей САПР.

```csharp
public class CadOptions
```

## Характеристики

| Имя | Описание |
| --- | --- |
| [BackgroundColor](../../groupdocs.viewer.options/cadoptions/backgroundcolor) { get; set; } | Цвет фона изображения |
| [Height](../../groupdocs.viewer.options/cadoptions/height) { get; } | Высота выходного результата в пикселях. |
| [Layers](../../groupdocs.viewer.options/cadoptions/layers) { get; set; } | Слои чертежа САПР для визуализации. |
| [LayoutName](../../groupdocs.viewer.options/cadoptions/layoutname) { get; set; } | Имя конкретного макета для рендеринга. Имя макета чувствительно к регистру. |
| [Pc3File](../../groupdocs.viewer.options/cadoptions/pc3file) { get; set; } | PC3 - файл конфигурации плоттера |
| [RenderLayouts](../../groupdocs.viewer.options/cadoptions/renderlayouts) { get; set; } | Указывает, следует ли визуализировать макеты из документа САПР. |
| [ScaleFactor](../../groupdocs.viewer.options/cadoptions/scalefactor) { get; } | Значения выше 1 увеличивают результат вывода; значения от 0 до 1 уменьшат результат вывода. |
| [Tiles](../../groupdocs.viewer.options/cadoptions/tiles) { get; set; } | Области рисования для визуализации. |
| [Width](../../groupdocs.viewer.options/cadoptions/width) { get; } | Ширина выходного результата в пикселях. |

## Методы

| Имя | Описание |
| --- | --- |
| static [ForRenderingByHeight](../../groupdocs.viewer.options/cadoptions/forrenderingbyheight)(int) | Инициализирует новый экземпляр[`CadOptions`](../cadoptions) класс для рендеринга по высоте. |
| static [ForRenderingByScaleFactor](../../groupdocs.viewer.options/cadoptions/forrenderingbyscalefactor)(float) | Инициализирует новый экземпляр[`CadOptions`](../cadoptions) класс для рендеринга по масштабному коэффициенту. |
| static [ForRenderingByWidth](../../groupdocs.viewer.options/cadoptions/forrenderingbywidth)(int) | Инициализирует новый экземпляр[`CadOptions`](../cadoptions) класс для рендеринга по ширине. |
| static [ForRenderingByWidthAndHeight](../../groupdocs.viewer.options/cadoptions/forrenderingbywidthandheight)(int, int) | Инициализирует новый экземпляр[`CadOptions`](../cadoptions) класс для рендеринга по ширине и высоте. |

### Смотрите также

* пространство имен [GroupDocs.Viewer.Options](../../groupdocs.viewer.options)
* сборка [GroupDocs.Viewer](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Viewer.dll -->