---
title: FirstRowContainsColumnNames
second_title: Справочник по API GroupDocs.Assembly для .NET
description: Получает или задает значение указывающее следует ли получать имена столбцов из извлеченной строки first таблицы документа. Значение по умолчанию  false.
type: docs
weight: 20
url: /ru/net/groupdocs.assembly.data/documenttableoptions/firstrowcontainscolumnnames/
---
## DocumentTableOptions.FirstRowContainsColumnNames property

Получает или задает значение, указывающее, следует ли получать имена столбцов из извлеченной строки first таблицы документа. Значение по умолчанию — false.

```csharp
public bool FirstRowContainsColumnNames { get; set; }
```

### Примечания

Если не задано получение имен столбцов из первой извлеченной строки таблицы документа, вместо них используются имена столбцов по умолчанию . Для документов форматов файлов электронных таблиц имена столбцов по умолчанию определяются как A, B, C, ... Z, AA, AB и т. д. Для документов других форматов файлов имена столбцов по умолчанию определяются как Column1, Column2, Column3 и т. д.

### Смотрите также

* class [DocumentTableOptions](../../documenttableoptions)
* пространство имен [GroupDocs.Assembly.Data](../../documenttableoptions)
* сборка [GroupDocs.Assembly](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Assembly.dll -->