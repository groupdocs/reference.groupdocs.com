---
title: ImageWatermark
second_title: Справочник по API GroupDocs.Watermark для .NET
description: Представляет водяной знак изображения.
type: docs
weight: 3110
url: /ru/net/groupdocs.watermark.watermarks/imagewatermark/
---
## ImageWatermark class

Представляет водяной знак изображения.

```csharp
public sealed class ImageWatermark : Watermark, IDisposable
```

## Конструкторы

| Имя | Описание |
| --- | --- |
| [ImageWatermark](imagewatermark#constructor)(Stream) | Инициализирует новый экземпляр[`ImageWatermark`](../imagewatermark) класс с указанным потоком. |
| [ImageWatermark](imagewatermark#constructor_1)(string) | Инициализирует новый экземпляр[`ImageWatermark`](../imagewatermark) класс с указанным путем к файлу. |

## Характеристики

| Имя | Описание |
| --- | --- |
| [ConsiderParentMargins](../../groupdocs.watermark/watermark/considerparentmargins) { get; set; } | Получает или задает значение, указывающее, вычисляются ли размер и координаты водяного знака с учетом родительских полей. |
| [Height](../../groupdocs.watermark/watermark/height) { get; set; } | Получает или задает желаемую высоту этого[`Watermark`](../../groupdocs.watermark/watermark) . |
| [HorizontalAlignment](../../groupdocs.watermark/watermark/horizontalalignment) { get; set; } | Получает или задает горизонтальное выравнивание этого[`Watermark`](../../groupdocs.watermark/watermark) . |
| [IsBackground](../../groupdocs.watermark/watermark/isbackground) { get; set; } | Получает или задает значение, указывающее, следует ли размещать водяной знак на фоне. |
| [Margins](../../groupdocs.watermark/watermark/margins) { get; set; } | Получает или задает параметры полей этого[`Watermark`](../../groupdocs.watermark/watermark) . |
| [Opacity](../../groupdocs.watermark/watermark/opacity) { get; set; } | Получает или задает непрозрачность этого[`Watermark`](../../groupdocs.watermark/watermark) . |
| [RotateAngle](../../groupdocs.watermark/watermark/rotateangle) { get; set; } | Получает или задает угол поворота этого[`Watermark`](../../groupdocs.watermark/watermark) в градусах. |
| [ScaleFactor](../../groupdocs.watermark/watermark/scalefactor) { get; set; } | Получает или задает значение, определяющее зависимость размера водяного знака от размера родительского элемента. |
| [SizingType](../../groupdocs.watermark/watermark/sizingtype) { get; set; } | Получает или задает значение, определяющее размер водяного знака. |
| [VerticalAlignment](../../groupdocs.watermark/watermark/verticalalignment) { get; set; } | Получает или задает вертикальное выравнивание этого[`Watermark`](../../groupdocs.watermark/watermark) . |
| [Width](../../groupdocs.watermark/watermark/width) { get; set; } | Получает или задает желаемую ширину этого[`Watermark`](../../groupdocs.watermark/watermark) . |
| [X](../../groupdocs.watermark/watermark/x) { get; set; } | Получает или задает координату x этого[`Watermark`](../../groupdocs.watermark/watermark) . |
| [Y](../../groupdocs.watermark/watermark/y) { get; set; } | Получает или задает координату y этого[`Watermark`](../../groupdocs.watermark/watermark) . |

## Методы

| Имя | Описание |
| --- | --- |
| [Dispose](../../groupdocs.watermark.watermarks/imagewatermark/dispose)() | Удаляет текущий экземпляр. |

### Примечания

**Учить больше:**

* [Добавление водяных знаков изображения](https://docs.groupdocs.com/display/watermarknet/Adding+image+watermarks)

### Примеры

Добавить изображение водяного знака в документ любого поддерживаемого типа.

```csharp
foreach (string filePath in Directory.GetFiles(@"C:\Documents"))
{
    using (Watermarker watermarker = new Watermarker(filePath))
    {
        using (ImageWatermark watermark = new ImageWatermark(@"C:\watermark.png"))
        {
            watermark.HorizontalAlignment = HorizontalAlignment.Center;
            watermark.VerticalAlignment = VerticalAlignment.Center;
            watermarker.Add(watermark);
        }

        watermarker.Save();
    }
}
```

### Смотрите также

* class [Watermark](../../groupdocs.watermark/watermark)
* пространство имен [GroupDocs.Watermark.Watermarks](../../groupdocs.watermark.watermarks)
* сборка [GroupDocs.Watermark](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Watermark.dll -->