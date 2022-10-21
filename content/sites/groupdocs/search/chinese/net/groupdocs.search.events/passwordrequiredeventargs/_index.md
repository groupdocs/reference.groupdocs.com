---
title: PasswordRequiredEventArgs
second_title: GroupDocs.Search for .NET API 参考
description: 表示当受密码保护的文档正在编入索引时发生的事件的参数
type: docs
weight: 570
url: /zh/net/groupdocs.search.events/passwordrequiredeventargs/
---
## PasswordRequiredEventArgs class

表示当受密码保护的文档正在编入索引时发生的事件的参数。

```csharp
public class PasswordRequiredEventArgs : BaseIndexEventArgs
```

## 特性

| 姓名 | 描述 |
| --- | --- |
| [DocumentFullPath](../../groupdocs.search.events/passwordrequiredeventargs/documentfullpath) { get; } | 获取文档完整路径。 |
| [IndexFolder](../../groupdocs.search.events/baseindexeventargs/indexfolder) { get; } | 获取索引文件夹。 |
| [IndexId](../../groupdocs.search.events/baseindexeventargs/indexid) { get; } | 获取索引 ID。 |
| [Password](../../groupdocs.search.events/passwordrequiredeventargs/password) { get; set; } | 获取或设置打开文档的密码 |
| [Status](../../groupdocs.search.events/baseindexeventargs/status) { get; } | 获取索引状态。 |
| [Time](../../groupdocs.search.events/baseindexeventargs/time) { get; } | 获取事件的时间。 |

### 评论

**学到更多**

* [搜索索引事件](https://docs.groupdocs.com/display/searchnet/Search+index+events)

### 也可以看看

* class [BaseIndexEventArgs](../baseindexeventargs)
* 命名空间 [GroupDocs.Search.Events](../../groupdocs.search.events)
* 部件 [GroupDocs.Search](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Search.dll -->