---
title: RedactionResult
second_title: GroupDocs.Redaction for .NET API 参考
description: 表示编辑操作的结果
type: docs
weight: 410
url: /zh/net/groupdocs.redaction/redactionresult/
---
## RedactionResult class

表示编辑操作的结果。

```csharp
public class RedactionResult
```

## 特性

| 姓名 | 描述 |
| --- | --- |
| [ErrorMessage](../../groupdocs.redaction/redactionresult/errormessage) { get; } | 获取诊断错误消息。 |
| [Status](../../groupdocs.redaction/redactionresult/status) { get; } | 获取执行状态。 |

## 方法

| 姓名 | 描述 |
| --- | --- |
| static [Failed](../../groupdocs.redaction/redactionresult/failed)(string) | 使用失败状态初始化 RedactionResult 类的新实例。 |
| static [Partial](../../groupdocs.redaction/redactionresult/partial)(string) | 使用 PartiallyApplied 状态初始化 RedactionResult 类的新实例。 |
| static [Skipped](../../groupdocs.redaction/redactionresult/skipped)(string) | 使用已跳过状态初始化 RedactionResult 类的新实例。 |
| static [Successful](../../groupdocs.redaction/redactionresult/successful)() | 使用已应用（成功）状态初始化 RedactionResult 类的新实例。 |

### 评论

**学到更多**

* 更多关于密文结果的细节： [编辑基础知识](https://docs.groupdocs.com/redaction/net/redaction-basics/)

### 也可以看看

* 命名空间 [GroupDocs.Redaction](../../groupdocs.redaction)
* 部件 [GroupDocs.Redaction](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Redaction.dll -->