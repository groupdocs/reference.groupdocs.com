---
title: ForSplitSheetIntoPages
second_title: Справочник по API GroupDocs.Viewer для .NET
description: Инициализирует новый экземплярSpreadsheetOptionsgroupdocs.viewer.options/spreadsheetoptions для преобразования листа в страницы.
type: docs
weight: 40
url: /ru/net/groupdocs.viewer.options/spreadsheetoptions/forsplitsheetintopages/
---
## ForSplitSheetIntoPages(int) {#forsplitsheetintopages}

Инициализирует новый экземпляр[`SpreadsheetOptions`](../../spreadsheetoptions) для преобразования листа в страницы.

```csharp
public static SpreadsheetOptions ForSplitSheetIntoPages(int countRowsPerPage)
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| countRowsPerPage | Int32 | Количество строк для включения в каждую страницу. |

### Возвращаемое значение

Новый экземпляр[`SpreadsheetOptions`](../../spreadsheetoptions) для преобразования листа в страницы.

### Исключения

| исключение | условие |
| --- | --- |
| ArgumentException | Брошен, когда*countRowsPerPage* равен или меньше нуля. |

### Смотрите также

* class [SpreadsheetOptions](../../spreadsheetoptions)
* пространство имен [GroupDocs.Viewer.Options](../../spreadsheetoptions)
* сборка [GroupDocs.Viewer](../../../)

---

## ForSplitSheetIntoPages(int, int) {#forsplitsheetintopages_1}

Инициализирует новый экземпляр[`SpreadsheetOptions`](../../spreadsheetoptions) для преобразования листа в страницы.

```csharp
public static SpreadsheetOptions ForSplitSheetIntoPages(int countRowsPerPage, 
    int countColumnsPerPage)
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| countRowsPerPage | Int32 | Количество строк для включения в каждую страницу. |
| countColumnsPerPage | Int32 | Количество столбцов для включения в каждую страницу. |

### Возвращаемое значение

Новый экземпляр[`SpreadsheetOptions`](../../spreadsheetoptions) для преобразования листа в страницы.

### Исключения

| исключение | условие |
| --- | --- |
| ArgumentException | Брошен, когда*countRowsPerPage* равен или меньше нуля. |
| ArgumentException | Брошен, когда*countColumnsPerPage* равен или меньше нуля. |

### Смотрите также

* class [SpreadsheetOptions](../../spreadsheetoptions)
* пространство имен [GroupDocs.Viewer.Options](../../spreadsheetoptions)
* сборка [GroupDocs.Viewer](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Viewer.dll -->