---
title: GroupDocs.Redaction.Redactions
second_title: GroupDocs.Redaction for .NET API 参考
description: 的Redactions命名空间为不同类型的编辑提供类
type: docs
weight: 70
url: /zh/net/groupdocs.redaction.redactions/
---
的Redactions命名空间为不同类型的编辑提供类。

## 课程

| 班级 | 描述 |
| --- | --- |
| [AnnotationRedaction](./annotationredaction) | 表示替换与给定正则表达式匹配的注释文本（评论等）的密文。 |
| [CellColumnRedaction](./cellcolumnredaction) | 表示替换电子表格文档（CSV、Excel 等）中的文本的文本编辑。 |
| [CellFilter](./cellfilter) | 提供一个选项来限制[`CellColumnRedaction`](../groupdocs.redaction.redactions/cellcolumnredaction)到工作表和列。 |
| [DeleteAnnotationRedaction](./deleteannotationredaction) | 表示文本编辑，如果文本与给定的正则表达式匹配，则删除注释（可选地删除所有注释）。 |
| [EraseMetadataRedaction](./erasemetadataredaction) | 表示从文档中删除所有元数据或与特定 MetadataFilters 匹配的元数据的元数据编辑。 |
| [ExactPhraseRedaction](./exactphraseredaction) | 表示替换文档文本中确切短语的文本编辑，默认情况下不区分大小写。 |
| [ImageAreaRedaction](./imagearearedaction) | 表示将彩色矩形放置在图像文档的给定区域中的编辑。 |
| [MetadataRedaction](./metadataredaction) | 表示文档元数据编辑的基本抽象类。 |
| [MetadataSearchRedaction](./metadatasearchredaction) | 表示使用正则表达式、匹配键和/或值搜索和编辑元数据的元数据编辑。 |
| [RedactionDescription](./redactiondescription) | 表示在修订过程中执行的单个更改操作信息。 |
| [RegexRedaction](./regexredaction) | 表示文本编辑，通过匹配提供的正则表达式来搜索和替换文档中的文本。 |
| [RegionReplacementOptions](./regionreplacementoptions) | 表示图像区域替换的颜色和区域参数。看[`ImageAreaRedaction`](../groupdocs.redaction.redactions/imagearearedaction). |
| [RemovePageRedaction](./removepageredaction) | 表示从文档中删除页面（幻灯片、工作表等）的编校。 |
| [ReplacementOptions](./replacementoptions) | 表示匹配文本替换的选项。 |
| [TextRedaction](./textredaction) | 表示文档文本编辑的基本抽象类。 |
| [TextReplacement](./textreplacement) | 表示文字替换信息。 |
## 接口

| 界面 | 描述 |
| --- | --- |
| [IRedactionCallback](./iredactioncallback) | 定义接收每个修订更改信息所需的方法，并可选择阻止它。 |
## 枚举

| 枚举 | 描述 |
| --- | --- |
| [MetadataFilters](./metadatafilters) | 表示最常见的文档元数据类型列表。 |
| [PageSeekOrigin](./pageseekorigin) | 提供代表文档中用于查找的参考点的字段。 |
| [RedactionActionType](./redactionactiontype) | 表示可以执行编辑的操作。 |
| [RedactionType](./redactiontype) | 表示一种文档数据，受编辑影响。 |
| [ReplacementType](./replacementtype) | 表示匹配文本的替换类型。 |

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Redaction.dll -->