---
title: TiffImageContent
second_title: Справочник по API GroupDocs.Watermark для .NET
description: Представляет изображение в формате TIFF на которое можно поместить водяной знак.
type: docs
weight: 410
url: /ru/net/groupdocs.watermark.contents.image/tiffimagecontent/
---
## TiffImageContent class

Представляет изображение в формате TIFF, на которое можно поместить водяной знак.

```csharp
public class TiffImageContent : MultiframeImageContent
```

## Характеристики

| Имя | Описание |
| --- | --- |
| [Frames](../../groupdocs.watermark.contents.image/multiframeimagecontent/frames) { get; } | Получает коллекцию всех кадров изображения. |
| [Height](../../groupdocs.watermark.contents.image/imagecontent/height) { get; } | Получает высоту этого[`ImageContent`](../imagecontent) в пикселях. |
| [Width](../../groupdocs.watermark.contents.image/imagecontent/width) { get; } | Получает ширину этого[`ImageContent`](../imagecontent) в пикселях. |

## Методы

| Имя | Описание |
| --- | --- |
| [Dispose](../../groupdocs.watermark.contents/content/dispose)() | Удаляет текущий экземпляр. |
| [FindImages](../../groupdocs.watermark.contents/contentpart/findimages)() | Находит все изображения в содержании. Поиск ведется в объектах, указанных в[`SearchableObjects`](../../groupdocs.watermark/watermarker/searchableobjects) . |
| [FindImages](../../groupdocs.watermark.contents/contentpart/findimages)(ImageSearchCriteria) | Находит изображения по заданным критериям поиска. Поиск ведется в объектах, указанных в[`SearchableObjects`](../../groupdocs.watermark/watermarker/searchableobjects) . |
| [Search](../../groupdocs.watermark.contents/contentpart/search)() | Находит все возможные водяные знаки в контенте. Поиск ведется в объектах, указанных в[`SearchableObjects`](../../groupdocs.watermark/watermarker/searchableobjects) . |
| [Search](../../groupdocs.watermark.contents/contentpart/search)(SearchCriteria) | Находит возможные водяные знаки по заданным критериям поиска. Поиск ведется в объектах, указанных в[`SearchableObjects`](../../groupdocs.watermark/watermarker/searchableobjects) . |

### Смотрите также

* class [MultiframeImageContent](../multiframeimagecontent)
* пространство имен [GroupDocs.Watermark.Contents.Image](../../groupdocs.watermark.contents.image)
* сборка [GroupDocs.Watermark](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Watermark.dll -->