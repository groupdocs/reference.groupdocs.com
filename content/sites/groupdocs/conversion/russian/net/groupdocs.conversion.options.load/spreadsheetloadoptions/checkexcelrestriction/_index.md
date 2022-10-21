---
title: CheckExcelRestriction
second_title: Справочник по API GroupDocs.Conversion для .NET
description: Проверять ли ограничение файла excel когда пользователь изменяет объекты связанные с ячейками. Например Excel не позволяет вводить строковое значение длиннее 32 КБ. Когда вы вводите значение длиннее 32 КБ если это свойство истинно вы получите исключение. Если это свойство имеет значение false мы примем введенное вами строковое значение в качестве значения ячейки чтобы позже вы могли вывести полное строковое значение для других форматов файлов таких как CSV. Однако если вы установили такое значение которое недопустимо для формата файла Excel вам не следует сохранять книгу в формате файла Excel позже. В противном случае может возникнуть непредвиденная ошибка для сгенерированного файла Excel.
type: docs
weight: 20
url: /ru/net/groupdocs.conversion.options.load/spreadsheetloadoptions/checkexcelrestriction/
---
## SpreadsheetLoadOptions.CheckExcelRestriction property

Проверять ли ограничение файла excel, когда пользователь изменяет объекты, связанные с ячейками. Например, Excel не позволяет вводить строковое значение длиннее 32 КБ. Когда вы вводите значение длиннее 32 КБ, если это свойство истинно, вы получите исключение. Если это свойство имеет значение false, мы примем введенное вами строковое значение в качестве значения ячейки, чтобы позже вы могли вывести полное строковое значение для других форматов файлов, таких как CSV. Однако, если вы установили такое значение, которое недопустимо для формата файла Excel, вам не следует сохранять книгу в формате файла Excel позже. В противном случае может возникнуть непредвиденная ошибка для сгенерированного файла Excel.

```csharp
public bool CheckExcelRestriction { get; set; }
```

### Смотрите также

* class [SpreadsheetLoadOptions](../../spreadsheetloadoptions)
* пространство имен [GroupDocs.Conversion.Options.Load](../../spreadsheetloadoptions)
* сборка [GroupDocs.Conversion](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Conversion.dll -->