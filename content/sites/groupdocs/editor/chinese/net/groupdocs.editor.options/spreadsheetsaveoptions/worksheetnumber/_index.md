---
title: WorksheetNumber
second_title: GroupDocs.Editor for .NET API 参考
description: 允许将已编辑的工作表插入到现有电子表格的副本中而不是创建新的单工作表电子表格默认行为 WorksheetNumber 是电子表格中从 1 开始的工作表编号在编辑器类中加载如果为 0默认值新的电子表格将使用单个编辑过的工作表创建 如果大于或小于零并且编辑器类中加载了有效的电子表格编辑过的工作表表示为输入 EditableDocument 实例将被插入到此电子表格中
type: docs
weight: 50
url: /zh/net/groupdocs.editor.options/spreadsheetsaveoptions/worksheetnumber/
---
## SpreadsheetSaveOptions.WorksheetNumber property

允许将已编辑的工作表插入到现有电子表格的副本中，而不是创建新的单工作表电子表格（默认行为）。 WorksheetNumber 是电子表格中从 1 开始的工作表编号，在编辑器类中加载。如果为 0（默认值），新的电子表格将使用单个编辑过的工作表创建。 如果大于或小于零，并且编辑器类中加载了有效的电子表格，编辑过的工作表，表示为输入 EditableDocument 实例，将被插入到此电子表格中。

```csharp
public int WorksheetNumber { get; set; }
```

### 评论

工作表编号整数属性，如果它不是默认状态（保留值'0'），则表示工作表编号，因此它从 1 开始，而不是从零开始，其最大值是演示文稿中所有现有幻灯片的数量。但是，如果指定的值大于所有幻灯片的数量，GroupDocs.Editor 将对其进行调整以标记最后一个工作表。也允许负值并从末尾计算工作表。例如，“-1”表示电子表格中的最后一个工作表，“-2”表示最后一个，等等。与正值一样，当负工作表数超过给定电子表格中的工作表总数时，它将调整为第一个工作表。 [`InsertAsNewWorksheet`](../insertasnewworksheet)布尔属性与此紧密耦合。

### 例子

给定电子表格有 5 个工作表： WorksheetNumber = 0; — 忽略给定的电子表格，创建一个新的电子表格并将已编辑的工作表放入其中。 WorksheetNumber = 1; — 将第一个工作表替换为edited WorksheetNumber = 2； — 将第二个工作表替换为edited WorksheetNumber = 5； — 用edited WorksheetNumber = 6 替换最后（第5 个）工作表； — 将最后（第 5 个）工作表替换为已编辑，因为 6 大于 5，因此为adjusted WorksheetNumber = -1； — 将最后（第 5 个）工作表替换为已编辑，因为“-1”表示“最后存在的” WorksheetNumber = -2； — 将第 4 个工作表替换为edited WorksheetNumber = -3； — 用edited WorksheetNumber = -4 替换第三个工作表； — 用edited WorksheetNumber = -5 替换第二个工作表； — 将第一个工作表替换为edited WorksheetNumber = -6; — 将第一个工作表替换为已编辑，因为“-6”大于 5，因此已调整

### 也可以看看

* class [SpreadsheetSaveOptions](../../spreadsheetsaveoptions)
* 命名空间 [GroupDocs.Editor.Options](../../spreadsheetsaveoptions)
* 部件 [GroupDocs.Editor](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Editor.dll -->
