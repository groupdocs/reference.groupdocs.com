---
title: IconImage
second_title: Справочник по API GroupDocs.Editor для .NET
description: Представляет одно изображение в формате ICON с его метаданными и дополнительными методами
type: docs
weight: 520
url: /ru/net/groupdocs.editor.htmlcss.resources.images.raster/iconimage/
---
## IconImage class

Представляет одно изображение в формате ICON с его метаданными и дополнительными методами

```csharp
public sealed class IconImage : RasterImageResourceBase
```

## Конструкторы

| Имя | Описание |
| --- | --- |
| [IconImage](iconimage#constructor)(string, Stream) | Создает новый экземпляр IconImage из содержимого, представленного в виде потока байтов, и с указанным именем |
| [IconImage](iconimage#constructor_1)(string, string) | Создает новый экземпляр IconImage из содержимого, представленного в виде строки в кодировке base64, и с указанным именем |

## Характеристики

| Имя | Описание |
| --- | --- |
| [AspectRatio](../../groupdocs.editor.htmlcss.resources.images.raster/rasterimageresourcebase/aspectratio) { get; } | Возвращает соотношение сторон этого изображения как отношение ширины к высоте |
| [ByteContent](../../groupdocs.editor.htmlcss.resources.images.raster/rasterimageresourcebase/bytecontent) { get; } | Возвращает содержимое этого растрового изображения в виде потока байтов |
| [FilenameWithExtension](../../groupdocs.editor.htmlcss.resources.images.raster/rasterimageresourcebase/filenamewithextension) { get; } | Возвращает правильное имя файла этого растрового изображения, которое состоит из имени и расширения. Теоретически может отличаться от названия. |
| [IsDisposed](../../groupdocs.editor.htmlcss.resources.images.raster/rasterimageresourcebase/isdisposed) { get; } | Определяет, удаляется это растровое изображение или нет |
| [Length](../../groupdocs.editor.htmlcss.resources.images.raster/rasterimageresourcebase/length) { get; } | Возвращает длину этого файла растрового изображения в байтах |
| [LinearDimensions](../../groupdocs.editor.htmlcss.resources.images.raster/rasterimageresourcebase/lineardimensions) { get; } | Возвращает линейные размеры этого растрового изображения (ширину и высоту) |
| [Name](../../groupdocs.editor.htmlcss.resources.images.raster/rasterimageresourcebase/name) { get; } | Возвращает имя этого растрового изображения. Обычно не содержит расширения имени файла и теоретически может отличаться от имени файла. |
| [NumberOfImages](../../groupdocs.editor.htmlcss.resources.images.raster/iconimage/numberofimages) { get; } | Возвращает количество изображений, присутствующих в этом файле ICON |
| [TextContent](../../groupdocs.editor.htmlcss.resources.images.raster/rasterimageresourcebase/textcontent) { get; } | Возвращает содержимое этого растрового изображения в виде строки в кодировке base64 |
| override [Type](../../groupdocs.editor.htmlcss.resources.images.raster/iconimage/type) { get; } | Возвращает ImageType.Icon |

## Методы

| Имя | Описание |
| --- | --- |
| [Dispose](../../groupdocs.editor.htmlcss.resources.images.raster/rasterimageresourcebase/dispose)() | Удаляет это растровое изображение, удаляя его содержимое и делая большинство методов и свойств нерабочими |
| [Equals](../../groupdocs.editor.htmlcss.resources.images.raster/rasterimageresourcebase/equals)(IHtmlResource) | Проверяет этот экземпляр на равенство, указанное в ссылке. |
| [GenerateBitmap](../../groupdocs.editor.htmlcss.resources.images.raster/rasterimageresourcebase/generatebitmap)() | Генерирует и возвращает новый экземпляр System.Drawing.Bitmap из этого растрового изображения. |
| [ReduceToNewHeight](../../groupdocs.editor.htmlcss.resources.images.raster/iconimage/reducetonewheight#reducetonewheight)(ushort) | Создает и возвращает новое уменьшенное изображение значка, но с указанной новой уменьшенной высотой и пропорционально уменьшенной шириной. (2 methods) |
| [Save](../../groupdocs.editor.htmlcss.resources.images.raster/rasterimageresourcebase/save)(string) | Сохраняет это растровое изображение в указанный файл |
| static [IsValid](../../groupdocs.editor.htmlcss.resources.images.raster/iconimage/isvalid#isvalid)(Stream) | Проверяет, является ли указанный поток действительным ICON image |
| static [IsValid](../../groupdocs.editor.htmlcss.resources.images.raster/iconimage/isvalid#isvalid_1)(string) | Проверяет, является ли указанная строка в кодировке base64 допустимым ICON image |

## События

| Имя | Описание |
| --- | --- |
| event [Disposed](../../groupdocs.editor.htmlcss.resources.images.raster/rasterimageresourcebase/disposed) | Событие, возникающее при удалении данного растрового изображения |

### Смотрите также

* class [RasterImageResourceBase](../rasterimageresourcebase)
* пространство имен [GroupDocs.Editor.HtmlCss.Resources.Images.Raster](../../groupdocs.editor.htmlcss.resources.images.raster)
* сборка [GroupDocs.Editor](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Editor.dll -->
