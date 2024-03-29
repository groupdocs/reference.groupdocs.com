---
title: OperationProgressEventArgs
second_title: GroupDocs.Search for .NET API 参考
description: 表示索引操作进度更新事件的参数
type: docs
weight: 560
url: /zh/net/groupdocs.search.events/operationprogresseventargs/
---
## OperationProgressEventArgs class

表示索引操作进度更新事件的参数。

```csharp
public class OperationProgressEventArgs : BaseIndexEventArgs
```

## 特性

| 姓名 | 描述 |
| --- | --- |
| [IndexFolder](../../groupdocs.search.events/baseindexeventargs/indexfolder) { get; } | 获取索引文件夹。 |
| [IndexId](../../groupdocs.search.events/baseindexeventargs/indexid) { get; } | 获取索引 ID. |
| [LastDocumentKey](../../groupdocs.search.events/operationprogresseventargs/lastdocumentkey) { get; } | 获取最后处理的文档的key。 |
| [LastDocumentPath](../../groupdocs.search.events/operationprogresseventargs/lastdocumentpath) { get; } | 获取上次处理文档的路径。 |
| [LastDocumentStatus](../../groupdocs.search.events/operationprogresseventargs/lastdocumentstatus) { get; } | 获取最后处理的文档的状态。 |
| [ProcessedDocuments](../../groupdocs.search.events/operationprogresseventargs/processeddocuments) { get; } | 获取成功处理的文档数。 |
| [ProgressPercentage](../../groupdocs.search.events/operationprogresseventargs/progresspercentage) { get; } | 获取进度的百分比。 |
| [SkippedDocuments](../../groupdocs.search.events/operationprogresseventargs/skippeddocuments) { get; } | 获取跳过的文档数。 |
| [Status](../../groupdocs.search.events/baseindexeventargs/status) { get; } | 获取索引状态。 |
| [Time](../../groupdocs.search.events/baseindexeventargs/time) { get; } | 获取事件的时间。 |
| [TotalDocuments](../../groupdocs.search.events/operationprogresseventargs/totaldocuments) { get; } | 获取处理文档的总数。 |

### 评论

**了解更多**

* [搜索索引事件](https://docs.groupdocs.com/display/searchnet/Search+index+events)

### 也可以看看

* class [BaseIndexEventArgs](../baseindexeventargs)
* 命名空间 [GroupDocs.Search.Events](../../groupdocs.search.events)
* 部件 [GroupDocs.Search](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Search.dll -->
