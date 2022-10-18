---
title: PdfViewInfo
second_title: Справочник по API GroupDocs.Viewer для .NET
description: Инициализирует новый экземплярPdfViewInfogroupdocs.viewer.results/pdfviewinfo класс.
type: docs
weight: 10
url: /ru/net/groupdocs.viewer.results/pdfviewinfo/pdfviewinfo/
---
## PdfViewInfo constructor

Инициализирует новый экземпляр[`PdfViewInfo`](../../pdfviewinfo) класс.

```csharp
public PdfViewInfo(FileType fileType, IList<Page> pages, bool printingAllowed)
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| fileType | FileType | Тип файла. |
| pages | IList`1 | Список страниц для просмотра. |
| printingAllowed | Boolean | Индикатор разрешения печати. |

### Исключения

| исключение | условие |
| --- | --- |
| ArgumentNullException | Брошен, когда*pages* нулевой. |

### Смотрите также

* class [FileType](../../../groupdocs.viewer/filetype)
* class [Page](../../page)
* class [PdfViewInfo](../../pdfviewinfo)
* пространство имен [GroupDocs.Viewer.Results](../../pdfviewinfo)
* сборка [GroupDocs.Viewer](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Viewer.dll -->