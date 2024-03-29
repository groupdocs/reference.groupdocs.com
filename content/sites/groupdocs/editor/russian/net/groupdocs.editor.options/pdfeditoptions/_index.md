---
title: PdfEditOptions
second_title: Справочник по API GroupDocs.Editor для .NET
description: Позволяет указать пользовательские параметры редактирования PDFдокументов
type: docs
weight: 1040
url: /ru/net/groupdocs.editor.options/pdfeditoptions/
---
## PdfEditOptions class

Позволяет указать пользовательские параметры редактирования PDF-документов

```csharp
public sealed class PdfEditOptions : FixedLayoutEditOptionsBase
```

## Конструкторы

| Имя | Описание |
| --- | --- |
| [PdfEditOptions](pdfeditoptions#constructor)() | Создает и возвращает новый экземпляр класса PdfEditOptions, где для всех параметров установлены значения по умолчанию |
| [PdfEditOptions](pdfeditoptions#constructor_1)(bool) | Создает и возвращает новый экземпляр класса PdfEditOptions с указанным разбиением на страницы и всеми остальными опциями по умолчанию |

## Характеристики

| Имя | Описание |
| --- | --- |
| [EnablePagination](../../groupdocs.editor.options/fixedlayouteditoptionsbase/enablepagination) { get; set; } | Позволяет включить (true) или отключить (false) нумерацию страниц в результирующем HTML-документе. По умолчанию отключено (false). |
| [Pages](../../groupdocs.editor.options/fixedlayouteditoptionsbase/pages) { get; set; } | Позволяет установить диапазон страниц для обработки. По умолчанию обрабатываются все страницы документа с фиксированным макетом. |
| [SkipImages](../../groupdocs.editor.options/fixedlayouteditoptionsbase/skipimages) { get; set; } | Получает или задает флаг, указывающий, следует ли пропускать изображения при преобразовании входного документа с фиксированным макетом в результирующий HTML. По умолчанию false — изображения сохраняются. |

### Смотрите также

* class [FixedLayoutEditOptionsBase](../fixedlayouteditoptionsbase)
* пространство имен [GroupDocs.Editor.Options](../../groupdocs.editor.options)
* сборка [GroupDocs.Editor](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Editor.dll -->
