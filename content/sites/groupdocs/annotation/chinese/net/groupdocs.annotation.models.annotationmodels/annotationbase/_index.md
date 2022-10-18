---
title: AnnotationBase
second_title: .NET API 参考的 GroupDocs.Annotation
description: 所有注释类型的基类
type: docs
weight: 190
url: /zh/net/groupdocs.annotation.models.annotationmodels/annotationbase/
---
## AnnotationBase class

所有注释类型的基类

```csharp
public abstract class AnnotationBase : ICloneable, IEquatable<AnnotationBase>
```

## 特性

| 姓名 | 描述 |
| --- | --- |
| [CreatedOn](../../groupdocs.annotation.models.annotationmodels/annotationbase/createdon) { get; set; } | 获取或设置注解创建日期 |
| [Id](../../groupdocs.annotation.models.annotationmodels/annotationbase/id) { get; set; } | 获取或设置注解唯一标识符 |
| [Message](../../groupdocs.annotation.models.annotationmodels/annotationbase/message) { get; set; } | 获取或设置注解消息 |
| [PageNumber](../../groupdocs.annotation.models.annotationmodels/annotationbase/pagenumber) { get; set; } | 获取或设置要标注的页码 |
| [Replies](../../groupdocs.annotation.models.annotationmodels/annotationbase/replies) { get; set; } | 表示注释回复集合 |
| [Type](../../groupdocs.annotation.models.annotationmodels/annotationbase/type) { get; set; } | 获取或设置注解类型 |
| [User](../../groupdocs.annotation.models.annotationmodels/annotationbase/user) { get; set; } | 获取或设置注解创建者 |

## 方法

| 姓名 | 描述 |
| --- | --- |
| virtual [Clone](../../groupdocs.annotation.models.annotationmodels/annotationbase/clone)() | 返回具有相同值的新实例 |
| [Equals](../../groupdocs.annotation.models.annotationmodels/annotationbase/equals#equals)(AnnotationBase) | 使用 IEquatable Equals 方法比较基本注释 |
| override [Equals](../../groupdocs.annotation.models.annotationmodels/annotationbase/equals#equals_1)(object) | 使用标准对象 Equals 方法比较基本注释 |
| override [GetHashCode](../../groupdocs.annotation.models.annotationmodels/annotationbase/gethashcode)() | 返回 AnnotationBase 消息的 HashCode、PageNumber 和类型属性 |

### 也可以看看

* 命名空间 [GroupDocs.Annotation.Models.AnnotationModels](../../groupdocs.annotation.models.annotationmodels)
* 部件 [GroupDocs.Annotation](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Annotation.dll -->