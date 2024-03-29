---
title: TextRedaction
second_title: GroupDocs.Redaction for .NET API 参考
description: 表示文档文本修订的基本抽象类
type: docs
weight: 640
url: /zh/net/groupdocs.redaction.redactions/textredaction/
---
## TextRedaction class

表示文档文本修订的基本抽象类。

```csharp
public abstract class TextRedaction : Redaction
```

## 特性

| 姓名 | 描述 |
| --- | --- |
| [ActionOptions](../../groupdocs.redaction.redactions/textredaction/actionoptions) { get; } | 获取[`ReplacementOptions`](../replacementoptions)实例，指定文本替换类型. |
| virtual [Description](../../groupdocs.redaction/redaction/description) { get; } | 返回一个字符串，描述修订及其参数。 |
| [OcrConnector](../../groupdocs.redaction.redactions/textredaction/ocrconnector) { get; set; } | 获取或设置[`IOcrConnector`](../../groupdocs.redaction.integration.ocr/iocrconnector)实现，需要从图形内容中提取文本。 |

## 方法

| 姓名 | 描述 |
| --- | --- |
| abstract [ApplyTo](../../groupdocs.redaction/redaction/applyto)(DocumentFormatInstance) | 将编辑应用到给定的格式实例。 |

### 评论

**了解更多**

* 有关应用密文的更多详细信息： [编辑基础知识](https://docs.groupdocs.com/redaction/net/redaction-basics/)
* 有关文档文本修订的更多详细信息： [文本编辑](https://docs.groupdocs.com/redaction/net/text-redactions/)

### 也可以看看

* class [Redaction](../../groupdocs.redaction/redaction)
* 命名空间 [GroupDocs.Redaction.Redactions](../../groupdocs.redaction.redactions)
* 部件 [GroupDocs.Redaction](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Redaction.dll -->
