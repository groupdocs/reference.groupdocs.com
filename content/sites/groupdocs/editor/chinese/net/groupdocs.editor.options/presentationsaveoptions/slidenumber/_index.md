---
title: SlideNumber
second_title: GroupDocs.Editor for .NET API 参考
description: 允许将已编辑的幻灯片插入到现有演示文稿中而不是创建新的单张幻灯片演示文稿默认行为 幻灯片编号是演示文稿中从 1 开始的幻灯片编号加载到编辑器类中如果它是 0默认值新的演示文稿将使用单个编辑的幻灯片创建如果它大于或小于零并且在 Editor 类中加载了有效的演示文稿则存储在输入 EditableDocument 实例中的已编辑幻灯片将插入到此演示文稿中
type: docs
weight: 50
url: /zh/net/groupdocs.editor.options/presentationsaveoptions/slidenumber/
---
## PresentationSaveOptions.SlideNumber property

允许将已编辑的幻灯片插入到现有演示文稿中，而不是创建新的单张幻灯片演示文稿（默认行为）。 幻灯片编号是演示文稿中从 1 开始的幻灯片编号，加载到编辑器类中。如果它是 0（默认值），新的演示文稿将使用单个编辑的幻灯片创建。如果它大于或小于零，并且在 Editor 类中加载了有效的演示文稿，则存储在输入 EditableDocument 实例中的已编辑幻灯片将插入到此演示文稿中。

```csharp
public int SlideNumber { get; set; }
```

### 评论

幻灯片编号整数属性，如果它不是默认状态（保留值'0'），则表示幻灯片编号，因此它从 1 开始，而不是从零开始，其最大值是演示文稿中所有现有幻灯片的数量。但是，如果指定的值大于所有幻灯片的数量，GroupDocs.Editor 将调整它以标记最后一张幻灯片。也允许负值，并从末尾开始计数幻灯片。例如，“-1”表示演示文稿中的最后一张幻灯片，“-2”表示最后一张，等等。与正值一样，当负幻灯片数超过给定演示文稿中的幻灯片总数时，它将调整为第一张幻灯片. [`InsertAsNewSlide`](../insertasnewslide)布尔属性与此紧密耦合。

### 例子

给定的演示文稿有 5 张幻灯片： SlideNumber = 0; — 忽略给定的演示文稿，创建一个新的演示文稿并将编辑过的幻灯片放入其中。 SlideNumber = 1; — 将第一张幻灯片替换为edited SlideNumber = 2； — 将第二张幻灯片替换为edited SlideNumber = 5； — 用edited SlideNumber = 6 替换最后（第5）张幻灯片； — 将最后（第 5）张幻灯片替换为已编辑，因为 6 大于 5，因此为adjusted SlideNumber = -1； — 将最后（第 5）张幻灯片替换为已编辑，因为“-1”表示“最后存在的” SlideNumber = -2； —用edited SlideNumber = -3替换第4张幻灯片； — 将第三张幻灯片替换为edited SlideNumber = -4； — 将第二张幻灯片替换为edited SlideNumber = -5； — 将第一张幻灯片替换为edited SlideNumber = -6； — 将第一张幻灯片替换为已编辑，因为“-6”大于 5，因此为adjusted

### 也可以看看

* class [PresentationSaveOptions](../../presentationsaveoptions)
* 命名空间 [GroupDocs.Editor.Options](../../presentationsaveoptions)
* 部件 [GroupDocs.Editor](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Editor.dll -->