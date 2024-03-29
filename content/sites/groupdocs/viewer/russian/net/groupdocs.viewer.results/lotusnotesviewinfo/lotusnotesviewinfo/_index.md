---
title: LotusNotesViewInfo
second_title: Справочник по API GroupDocs.Viewer для .NET
description: Инициализирует новый экземплярLotusNotesViewInfogroupdocs.viewer.results/lotusnotesviewinfo класс.
type: docs
weight: 10
url: /ru/net/groupdocs.viewer.results/lotusnotesviewinfo/lotusnotesviewinfo/
---
## LotusNotesViewInfo() {#constructor}

Инициализирует новый экземпляр[`LotusNotesViewInfo`](../../lotusnotesviewinfo) класс.

```csharp
public LotusNotesViewInfo()
```

### Смотрите также

* class [LotusNotesViewInfo](../../lotusnotesviewinfo)
* пространство имен [GroupDocs.Viewer.Results](../../lotusnotesviewinfo)
* сборка [GroupDocs.Viewer](../../../)

---

## LotusNotesViewInfo(FileType, List&lt;Page&gt;, int) {#constructor_1}

Инициализирует новый экземпляр[`LotusNotesViewInfo`](../../lotusnotesviewinfo) класс.

```csharp
public LotusNotesViewInfo(FileType fileType, List<Page> pages, int notesCount)
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| fileType | FileType | Тип файла. |
| pages | List`1 | Список страниц для просмотра. |
| notesCount | Int32 | Количество заметок, содержащихся в файле хранилища базы данных Lotus. |

### Исключения

| исключение | условие |
| --- | --- |
| ArgumentNullException | Брошен, когда*fileType* нулевой. |
| ArgumentNullException | Брошен, когда*pages* нулевой. |
| ArgumentNullException | Брошен, когда*notesCount* нулевой. |

### Смотрите также

* class [FileType](../../../groupdocs.viewer/filetype)
* class [Page](../../page)
* class [LotusNotesViewInfo](../../lotusnotesviewinfo)
* пространство имен [GroupDocs.Viewer.Results](../../lotusnotesviewinfo)
* сборка [GroupDocs.Viewer](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Viewer.dll -->
