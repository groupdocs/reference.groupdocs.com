---
title: WatermarkableImage
second_title: Справочник по API GroupDocs.Watermark для .NET
description: Представляет изображение внутри документа.
type: docs
weight: 420
url: /ru/net/groupdocs.watermark.contents.image/watermarkableimage/
---
## WatermarkableImage class

Представляет изображение внутри документа.

```csharp
public abstract class WatermarkableImage : ContentPart
```

## Характеристики

| Имя | Описание |
| --- | --- |
| [Height](../../groupdocs.watermark.contents.image/watermarkableimage/height) { get; } | Получает высоту этого[`WatermarkableImage`](../watermarkableimage) в пикселях. |
| [Width](../../groupdocs.watermark.contents.image/watermarkableimage/width) { get; } | Получает ширину этого[`WatermarkableImage`](../watermarkableimage) в пикселях. |

## Методы

| Имя | Описание |
| --- | --- |
| [Add](../../groupdocs.watermark.contents.image/watermarkableimage/add)(Watermark) | Добавляет к этому водяной знак[`WatermarkableImage`](../watermarkableimage). Этот метод предполагает, что смещение и размер водяного знака измеряются в пикселях (если они назначены). |
| [FindImages](../../groupdocs.watermark.contents/contentpart/findimages)() | Находит все изображения в содержании. Поиск ведется в объектах, указанных в[`SearchableObjects`](../../groupdocs.watermark/watermarker/searchableobjects) . |
| [FindImages](../../groupdocs.watermark.contents/contentpart/findimages)(ImageSearchCriteria) | Находит изображения по заданным критериям поиска. Поиск ведется в объектах, указанных в[`SearchableObjects`](../../groupdocs.watermark/watermarker/searchableobjects) . |
| [GetBytes](../../groupdocs.watermark.contents.image/watermarkableimage/getbytes)() | Получает изображение в виде массива байтов. |
| [Search](../../groupdocs.watermark.contents/contentpart/search)() | Находит все возможные водяные знаки в контенте. Поиск ведется в объектах, указанных в[`SearchableObjects`](../../groupdocs.watermark/watermarker/searchableobjects) . |
| [Search](../../groupdocs.watermark.contents/contentpart/search)(SearchCriteria) | Находит возможные водяные знаки по заданным критериям поиска. Поиск ведется в объектах, указанных в[`SearchableObjects`](../../groupdocs.watermark/watermarker/searchableobjects) . |

### Примечания

**Учить больше:**

* [Добавление водяного знака к изображениям внутри документа](https://docs.groupdocs.com/display/watermarknet/Adding+watermark+to+images+inside+a+document)

### Примеры

Добавить водяной знак ко всем изображениям внутри документа любого поддерживаемого типа.

```csharp
using (Watermarker watermarker = new Watermarker(@"D:\input.doc"))
{
    // Инициализировать текстовый или графический водяной знак.
    TextWatermark watermark = new TextWatermark("DRAFT", new Font("Arial", 19));

    // Найти все изображения в содержимом.
    WatermarkableImageCollection images = watermarker.GetImages();

    // Добавить водяной знак.
    foreach (WatermarkableImage watermarkableImage in images)
    {
        watermarkableImage.Add(watermark);
    }

    // Сохранить изменения.
    watermarker.Save(@"D:\output.doc");
}
```

### Смотрите также

* class [ContentPart](../../groupdocs.watermark.contents/contentpart)
* пространство имен [GroupDocs.Watermark.Contents.Image](../../groupdocs.watermark.contents.image)
* сборка [GroupDocs.Watermark](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Watermark.dll -->