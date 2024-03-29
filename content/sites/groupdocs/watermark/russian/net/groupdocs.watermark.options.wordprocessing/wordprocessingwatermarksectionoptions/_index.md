---
title: WordProcessingWatermarkSectionOptions
second_title: Справочник по API GroupDocs.Watermark для .NET
description: Представляет параметры при добавлении водяного знака формы в раздел документа Word.
type: docs
weight: 2380
url: /ru/net/groupdocs.watermark.options.wordprocessing/wordprocessingwatermarksectionoptions/
---
## WordProcessingWatermarkSectionOptions class

Представляет параметры при добавлении водяного знака формы в раздел документа Word.

```csharp
public sealed class WordProcessingWatermarkSectionOptions : WordProcessingWatermarkBaseOptions
```

## Конструкторы

| Имя | Описание |
| --- | --- |
| [WordProcessingWatermarkSectionOptions](wordprocessingwatermarksectionoptions)() | Инициализирует новый экземпляр[`WordProcessingWatermarkSectionOptions`](../wordprocessingwatermarksectionoptions) класс. |

## Характеристики

| Имя | Описание |
| --- | --- |
| [AlternativeText](../../groupdocs.watermark.options.wordprocessing/wordprocessingwatermarkbaseoptions/alternativetext) { get; set; } | Получает или задает описательный (альтернативный) текст, который будет связан с фигурой. |
| [Effects](../../groupdocs.watermark.options.wordprocessing/wordprocessingwatermarkbaseoptions/effects) { get; set; } | Получает или задает значение[`WordProcessingImageEffects`](../wordprocessingimageeffects) или [`WordProcessingTextEffects`](../wordprocessingtexteffects) для эффектов, которые должны быть применены к водяному знаку. |
| [IsLocked](../../groupdocs.watermark.options.wordprocessing/wordprocessingwatermarkbaseoptions/islocked) { get; set; } | Получает или задает значение, указывающее, запрещено ли редактирование фигуры в Word. |
| [LockType](../../groupdocs.watermark.options.wordprocessing/wordprocessingwatermarkbaseoptions/locktype) { get; set; } | Получает или задает тип блокировки водяного знака. |
| [Name](../../groupdocs.watermark.options.wordprocessing/wordprocessingwatermarkbaseoptions/name) { get; set; } | Получает или задает имя фигуры. |
| [Password](../../groupdocs.watermark.options.wordprocessing/wordprocessingwatermarkbaseoptions/password) { get; set; } | Получает или задает пароль, используемый для блокировки водяного знака. |
| [SectionIndex](../../groupdocs.watermark.options.wordprocessing/wordprocessingwatermarksectionoptions/sectionindex) { get; set; } | Получает или задает индекс раздела для добавления водяного знака. |

### Примечания

**Узнать больше:**

* [Добавляйте водяные знаки в текстовые документы](https://docs.groupdocs.com/display/watermarknet/Add+watermarks+to+word+processing+documents)

### Примеры

Добавить водяной знак в определенный раздел документа Word.

```csharp
WordProcessingLoadOptions loadOptions = new WordProcessingLoadOptions();
using (Watermarker watermarker = new Watermarker(@"C:\Documents\test.doc", loadOptions))
{
    TextWatermark watermark = new TextWatermark("Test watermark", new Font("Arial", 36, FontStyle.Bold | FontStyle.Italic));
    watermark.HorizontalAlignment = HorizontalAlignment.Center;
    watermark.VerticalAlignment = VerticalAlignment.Center;
    watermark.ForegroundColor = Color.Red;

    WordProcessingWatermarkSectionOptions options = new WordProcessingWatermarkSectionOptions();
    options.SectionIndex = 0;

    watermarker.Add(watermark, options);
    watermarker.Save();
}
```

### Смотрите также

* class [WordProcessingWatermarkBaseOptions](../wordprocessingwatermarkbaseoptions)
* пространство имен [GroupDocs.Watermark.Options.WordProcessing](../../groupdocs.watermark.options.wordprocessing)
* сборка [GroupDocs.Watermark](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Watermark.dll -->
