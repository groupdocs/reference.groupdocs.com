---
title: Classify
second_title: GroupDocs.Classification for .NET API 参考
description: 文本的情感分类
type: docs
weight: 20
url: /zh/net/groupdocs.classification/sentimentclassifier/classify/
---
## SentimentClassifier.Classify method

文本的情感分类。

```csharp
public ClassificationResponse Classify(string text, int bestClassesCount = 1, 
    Taxonomy taxonomy = Taxonomy.Sentiment)
```

| 范围 | 类型 | 描述 |
| --- | --- | --- |
| text | String | 要分类的原始文本。 |
| bestClassesCount | Int32 | 返回的最佳课程的计数。 |
| taxonomy | Taxonomy | 情感分类（Sentiment 或 Sentiment3）。 |

### 返回值

[`ClassificationResponse`](../../../groupdocs.classification.dto/classificationresponse/)与分类结果。

### 例外

| 例外 | （健康）状况 |
| --- | --- |
| [ApiException](../../../groupdocs.classification.exceptions/apiexception/) | 发生 API 异常。 |

### 也可以看看

* class [ClassificationResponse](../../../groupdocs.classification.dto/classificationresponse/)
* enum [Taxonomy](../../taxonomy/)
* class [SentimentClassifier](../)
* 命名空间 [GroupDocs.Classification](../../sentimentclassifier/)
* 部件 [GroupDocs.Classification](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Classification.dll -->