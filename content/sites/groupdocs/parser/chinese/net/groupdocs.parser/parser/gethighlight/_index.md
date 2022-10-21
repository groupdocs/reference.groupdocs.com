---
title: GetHighlight
second_title: GroupDocs.Parser for .NET API 参考
description: 从文档中提取亮点
type: docs
weight: 90
url: /zh/net/groupdocs.parser/parser/gethighlight/
---
## Parser.GetHighlight method

从文档中提取亮点。

```csharp
public HighlightItem GetHighlight(int position, bool isDirect, HighlightOptions options)
```

| 范围 | 类型 | 描述 |
| --- | --- | --- |
| position | Int32 | 高光的开始位置。 |
| isDirect | Boolean | 指示是否直接提取高光的值。 `真的`如果高光是由右边提取的*position*;否则，`错误的`. |
| options | HighlightOptions | 突出显示提取选项。 |

### 返回值

的一个实例[`HighlightItem`](../../../groupdocs.parser.data/highlightitem)表示提取的高亮的类； `无效的`如果不支持高亮提取。

### 评论

**学到更多：**

* [提取亮点](https://docs.groupdocs.com/display/parsernet/Extract+highlights)

### 例子

以下示例显示如何提取包含 3 个单词的突出显示：

```csharp
// 创建 Parser 类的实例
using (Parser parser = new Parser(filePath))
{
    // 提取一个亮点：
    HighlightItem hl = parser.GetHighlight(2, true, new HighlightOptions(3));
    
    // 检查是否支持高亮提取
    if (hl == null)
    {
        Console.WriteLine("Highlight extraction isn't supported");
        return;
    }
    
    // 打印提取的高光
    Console.WriteLine(string.Format("At {0}: {1}", hl.Position, hl.Text));
}
```

### 也可以看看

* class [HighlightItem](../../../groupdocs.parser.data/highlightitem)
* class [HighlightOptions](../../../groupdocs.parser.options/highlightoptions)
* class [Parser](../../parser)
* 命名空间 [GroupDocs.Parser](../../parser)
* 部件 [GroupDocs.Parser](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Parser.dll -->