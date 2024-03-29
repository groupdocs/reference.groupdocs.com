---
title: FontSize
second_title: GroupDocs.Editor for .NET API 参考
description: 表示字体大小为特殊单位或长度值它指定字体的大小历史上是大写M的宽度
type: docs
weight: 290
url: /zh/net/groupdocs.editor.htmlcss.css.properties/fontsize/
---
## FontSize structure

表示字体大小为特殊单位或长度值，它指定字体的大小（历史上是大写“M”的宽度）。

```csharp
public struct FontSize : IEquatable<FontSize>
```

## 特性

| 姓名 | 描述 |
| --- | --- |
| [IsAbsoluteSize](../../groupdocs.editor.htmlcss.css.properties/fontsize/isabsolutesize) { get; } | 表示这个font-size是否以绝对大小为关键字定义，基于用户的默认字体大小（即medium） |
| [IsInitial](../../groupdocs.editor.htmlcss.css.properties/fontsize/isinitial) { get; } | 表示这个font-size是否有初始值(Medium) |
| [IsLengthDefined](../../groupdocs.editor.htmlcss.css.properties/fontsize/islengthdefined) { get; } | 指示此字体大小是否定义为[`Length`](../../groupdocs.editor.htmlcss.css.datatypes/length)值 |
| [IsRelativeSize](../../groupdocs.editor.htmlcss.css.properties/fontsize/isrelativesize) { get; } | 指示此字体大小是否以相对大小作为关键字定义。字体将相对于父元素的字体大小变大或变小，大致按照用于分隔绝对大小关键字的比例。 |
| [Length](../../groupdocs.editor.htmlcss.css.properties/fontsize/length) { get; } | 一个长度值，如果这个字体大小是用它定义的，否则抛出异常 |
| [Value](../../groupdocs.editor.htmlcss.css.properties/fontsize/value) { get; } | 返回此字体大小的值作为字符串 |

## 方法

| 姓名 | 描述 |
| --- | --- |
| static [FromLength](../../groupdocs.editor.htmlcss.css.properties/fontsize/fromlength)(Length) | 从指定长度创建字体大小 |
| [Equals](../../groupdocs.editor.htmlcss.css.properties/fontsize/equals#equals)(FontSize) | 确定此字体大小实例是否等于指定的 |
| override [Equals](../../groupdocs.editor.htmlcss.css.properties/fontsize/equals#equals_1)(object) | 确定此字体大小实例是否等于指定的 uncasted |
| override [GetHashCode](../../groupdocs.editor.htmlcss.css.properties/fontsize/gethashcode)() | 返回此实例的哈希码 |
| static [TryParse](../../groupdocs.editor.htmlcss.css.properties/fontsize/tryparse)(string, out FontSize) | 尝试将指定关键字识别为“font-size”的正确关键字值，并在成功时返回它或在失败时返回 NULL。 |
| [operator ==](../../groupdocs.editor.htmlcss.css.properties/fontsize/op_equality) | 检查两个“FontSize”值是否相等 |
| [operator !=](../../groupdocs.editor.htmlcss.css.properties/fontsize/op_inequality) | 检查两个“FontSize”值是否不相等 |

## 字段

| 姓名 | 描述 |
| --- | --- |
| static readonly [Large](../../groupdocs.editor.htmlcss.css.properties/fontsize/large) | 通常较大的绝对大小 |
| static readonly [Larger](../../groupdocs.editor.htmlcss.css.properties/fontsize/larger) | Larger relative-size - 字体相对于父元素的字体大小会更大，大致按照用于分隔上面的绝对大小关键字的比例。 |
| static readonly [Medium](../../groupdocs.editor.htmlcss.css.properties/fontsize/medium) | 中号。初始值. |
| static readonly [Small](../../groupdocs.editor.htmlcss.css.properties/fontsize/small) | 通常较小的 absolute-size |
| static readonly [Smaller](../../groupdocs.editor.htmlcss.css.properties/fontsize/smaller) | Smaller relative-size - 字体相对于父元素的字体大小会更小，大致按照用于分隔上面的绝对大小关键字的比例。 |
| static readonly [XLarge](../../groupdocs.editor.htmlcss.css.properties/fontsize/xlarge) | 平庸的大 absolute-size |
| static readonly [XSmall](../../groupdocs.editor.htmlcss.css.properties/fontsize/xsmall) | 平庸的小绝对尺寸 |
| static readonly [XxLarge](../../groupdocs.editor.htmlcss.css.properties/fontsize/xxlarge) | 非常大的绝对大小 |
| static readonly [XxSmall](../../groupdocs.editor.htmlcss.css.properties/fontsize/xxsmall) | 非常小的绝对尺寸 |

### 也可以看看

* 命名空间 [GroupDocs.Editor.HtmlCss.Css.Properties](../../groupdocs.editor.htmlcss.css.properties)
* 部件 [GroupDocs.Editor](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Editor.dll -->
