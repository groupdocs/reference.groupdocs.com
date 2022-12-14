---
title: PageImageArea
second_title: Справочник по API GroupDocs.Parser для .NET
description: Представляет область изображения страницы которая используется для представления изображения на странице при синтаксическом анализе с помощью функции шаблона или вложения изображения если изображения извлекаются из электронных писем или Zipархивов.
type: docs
weight: 110
url: /ru/net/groupdocs.parser.data/pageimagearea/
---
## PageImageArea class

Представляет область изображения страницы, которая используется для представления изображения на странице при синтаксическом анализе с помощью функции шаблона или вложения изображения, если изображения извлекаются из электронных писем или Zip-архивов.

```csharp
public sealed class PageImageArea : PageArea
```

## Конструкторы

| Имя | Описание |
| --- | --- |
| [PageImageArea](pageimagearea#constructor)(Stream, FileType, double) | Инициализирует новый экземпляр[`PageImageArea`](../pageimagearea) класс. |
| [PageImageArea](pageimagearea#constructor_1)(Stream, FileType, double, Page, Rectangle) | Инициализирует новый экземпляр[`PageImageArea`](../pageimagearea) класс. |

## Характеристики

| Имя | Описание |
| --- | --- |
| [FileType](../../groupdocs.parser.data/pageimagearea/filetype) { get; } | Получает формат изображения. |
| [Page](../../groupdocs.parser.data/pagearea/page) { get; } | Получает информацию о странице документа, такую как индекс страницы и размер страницы. |
| [Rectangle](../../groupdocs.parser.data/pagearea/rectangle) { get; } | Получает прямоугольную область. |
| [Rotation](../../groupdocs.parser.data/pageimagearea/rotation) { get; } | Получает угол поворота изображения. |

## Методы

| Имя | Описание |
| --- | --- |
| [GetImageStream](../../groupdocs.parser.data/pageimagearea/getimagestream#getimagestream)() | Возвращает поток изображения. |
| [GetImageStream](../../groupdocs.parser.data/pageimagearea/getimagestream#getimagestream_1)(ImageOptions) | Возвращает поток изображения в другом формате. |
| [Save](../../groupdocs.parser.data/pageimagearea/save#save)(string) | Сохраняет изображение в файл. |
| [Save](../../groupdocs.parser.data/pageimagearea/save#save_1)(string, ImageOptions) | Сохраняет изображение в файл в другом формате. |

### Примечания

Экземпляр[`PageImageArea`](../pageimagearea) class используется как возвращаемое значение следующих методов:

* [`GetImages`](../../groupdocs.parser/parser/getimages)
* [`GetImages`](../../groupdocs.parser/parser/getimages)
* [`GetImages`](../../groupdocs.parser/parser/getimages)
* [`GetImages`](../../groupdocs.parser/parser/getimages)

См. примеры использования там.

### Смотрите также

* class [PageArea](../pagearea)
* пространство имен [GroupDocs.Parser.Data](../../groupdocs.parser.data)
* сборка [GroupDocs.Parser](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Parser.dll -->
