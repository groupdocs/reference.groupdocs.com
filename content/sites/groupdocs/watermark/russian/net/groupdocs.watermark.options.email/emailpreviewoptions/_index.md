---
title: EmailPreviewOptions
second_title: Справочник по API GroupDocs.Watermark для .NET
description: Предоставляет параметры для установки требований и потоковой передачи делегатов для предварительного создания документа электронной почты.
type: docs
weight: 1710
url: /ru/net/groupdocs.watermark.options.email/emailpreviewoptions/
---
## EmailPreviewOptions class

Предоставляет параметры для установки требований и потоковой передачи делегатов для предварительного создания документа электронной почты.

```csharp
public class EmailPreviewOptions : PreviewOptions
```

## Конструкторы

| Имя | Описание |
| --- | --- |
| [EmailPreviewOptions](emailpreviewoptions#constructor)(CreatePageStream) | Инициализирует новый экземпляр[`EmailPreviewOptions`](../emailpreviewoptions) класс, вызывающий закрытие выходного потока. |
| [EmailPreviewOptions](emailpreviewoptions#constructor_1)(CreatePageStream, ReleasePageStream) | Инициализирует новый экземпляр[`EmailPreviewOptions`](../emailpreviewoptions) класс, вызывающий возврат выходного потока клиенту для дальнейшего использования. |

## Характеристики

| Имя | Описание |
| --- | --- |
| [CreatePageStream](../../groupdocs.watermark.options/previewoptions/createpagestream) { get; set; } | Получает или задает экземпляр делегата создания потока страниц. |
| [Height](../../groupdocs.watermark.options/previewoptions/height) { get; set; } | Получает или задает высоту предварительного просмотра страницы. |
| [PageNumbers](../../groupdocs.watermark.options/previewoptions/pagenumbers) { get; set; } | Получает или задает массив номеров страниц для создания превью. |
| [PreviewFormat](../../groupdocs.watermark.options/previewoptions/previewformat) { get; set; } | Получает или задает формат изображения предварительного просмотра. |
| [ReleasePageStream](../../groupdocs.watermark.options/previewoptions/releasepagestream) { get; set; } | Получает или задает экземпляр делегата завершения предварительного просмотра страницы. |
| [Resolution](../../groupdocs.watermark.options.email/emailpreviewoptions/resolution) { get; set; } | Получает или задает разрешение сгенерированных изображений в точках на дюйм. |
| [Width](../../groupdocs.watermark.options/previewoptions/width) { get; set; } | Получает или задает ширину предварительного просмотра страницы. |

## Поля

| Имя | Описание |
| --- | --- |
| const [DefaultResolution](../../groupdocs.watermark.options.email/emailpreviewoptions/defaultresolution) | Разрешение по умолчанию в точках на дюйм. |

### Смотрите также

* class [PreviewOptions](../../groupdocs.watermark.options/previewoptions)
* пространство имен [GroupDocs.Watermark.Options.Email](../../groupdocs.watermark.options.email)
* сборка [GroupDocs.Watermark](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Watermark.dll -->