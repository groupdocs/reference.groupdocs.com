---
title: SpreadsheetPreviewOptions
second_title: Справочник по API GroupDocs.Watermark для .NET
description: Инициализирует новый экземплярSpreadsheetPreviewOptionsgroupdocs.watermark.options.spreadsheet/spreadsheetpreviewoptions класс вызывающий закрытие выходного потока.
type: docs
weight: 10
url: /ru/net/groupdocs.watermark.options.spreadsheet/spreadsheetpreviewoptions/spreadsheetpreviewoptions/
---
## SpreadsheetPreviewOptions(CreatePageStream) {#constructor}

Инициализирует новый экземпляр[`SpreadsheetPreviewOptions`](../../spreadsheetpreviewoptions) класс, вызывающий закрытие выходного потока.

```csharp
public SpreadsheetPreviewOptions(CreatePageStream createPageStream)
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| createPageStream | CreatePageStream | Создает поток для предварительного просмотра определенной страницы. |

### Смотрите также

* delegate [CreatePageStream](../../../groupdocs.watermark.options/createpagestream)
* class [SpreadsheetPreviewOptions](../../spreadsheetpreviewoptions)
* пространство имен [GroupDocs.Watermark.Options.Spreadsheet](../../spreadsheetpreviewoptions)
* сборка [GroupDocs.Watermark](../../../)

---

## SpreadsheetPreviewOptions(CreatePageStream, ReleasePageStream) {#constructor_1}

Инициализирует новый экземпляр[`SpreadsheetPreviewOptions`](../../spreadsheetpreviewoptions) класс, вызывающий возврат выходного потока клиенту для дальнейшего использования.

```csharp
public SpreadsheetPreviewOptions(CreatePageStream createPageStream, 
    ReleasePageStream releasePageStream)
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| createPageStream | CreatePageStream | Создает поток для предварительного просмотра определенной страницы. |
| releasePageStream | ReleasePageStream | Уведомляет о том, что создание предварительного просмотра страницы выполнено, и получает выходной поток. |

### Смотрите также

* delegate [CreatePageStream](../../../groupdocs.watermark.options/createpagestream)
* delegate [ReleasePageStream](../../../groupdocs.watermark.options/releasepagestream)
* class [SpreadsheetPreviewOptions](../../spreadsheetpreviewoptions)
* пространство имен [GroupDocs.Watermark.Options.Spreadsheet](../../spreadsheetpreviewoptions)
* сборка [GroupDocs.Watermark](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Watermark.dll -->
