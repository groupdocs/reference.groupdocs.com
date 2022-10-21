---
title: PdfAnnotationWatermarkOptions
second_title: Справочник по API GroupDocs.Watermark для .NET
description: Представляет параметры добавления водяного знака при добавлении водяного знака аннотации в документ PDF.
type: docs
weight: 1860
url: /ru/net/groupdocs.watermark.options.pdf/pdfannotationwatermarkoptions/
---
## PdfAnnotationWatermarkOptions class

Представляет параметры добавления водяного знака при добавлении водяного знака аннотации в документ PDF.

```csharp
public sealed class PdfAnnotationWatermarkOptions : PdfWatermarkOptions
```

## Конструкторы

| Имя | Описание |
| --- | --- |
| [PdfAnnotationWatermarkOptions](pdfannotationwatermarkoptions)() | Инициализирует новый экземпляр[`PdfAnnotationWatermarkOptions`](../pdfannotationwatermarkoptions) класс. |

## Характеристики

| Имя | Описание |
| --- | --- |
| [PageIndex](../../groupdocs.watermark.options.pdf/pdfannotationwatermarkoptions/pageindex) { get; set; } | Получает или задает индекс страницы для добавления водяного знака. |
| [PrintOnly](../../groupdocs.watermark.options.pdf/pdfannotationwatermarkoptions/printonly) { get; set; } | Получить или установить значение, указывающее, будет ли аннотация распечатываться, но не отображаться в приложении для просмотра pdf. |

### Примечания

**Учить больше:**

* [Добавляйте водяные знаки в документы PDF](https://docs.groupdocs.com/display/watermarknet/Add+watermarks+to+PDF+documents)

### Примеры

Добавить водяной знак аннотации изображения в документ PDF.

```csharp
PdfLoadOptions loadOptions = new PdfLoadOptions();
using (Watermarker watermarker = new Watermarker(@"D:\test.pdf", loadOptions))
{
    using (ImageWatermark watermark = new ImageWatermark(@"D:\icon.png"))
    {
        PdfAnnotationWatermarkOptions options = new PdfAnnotationWatermarkOptions();
        options.PageIndex = -1; // по умолчанию - все страницы

        watermarker.Add(watermark, options);
    }

    watermarker.Save();
}
```

### Смотрите также

* class [PdfWatermarkOptions](../pdfwatermarkoptions)
* пространство имен [GroupDocs.Watermark.Options.Pdf](../../groupdocs.watermark.options.pdf)
* сборка [GroupDocs.Watermark](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Watermark.dll -->