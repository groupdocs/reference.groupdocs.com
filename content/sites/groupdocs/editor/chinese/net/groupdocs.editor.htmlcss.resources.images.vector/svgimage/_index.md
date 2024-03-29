---
title: SvgImage
second_title: GroupDocs.Editor for .NET API 参考
description: 表示一张 SVG可缩放矢量图形格式的矢量图像及其元数据和其他方法
type: docs
weight: 590
url: /zh/net/groupdocs.editor.htmlcss.resources.images.vector/svgimage/
---
## SvgImage class

表示一张 SVG（可缩放矢量图形）格式的矢量图像及其元数据和其他方法

```csharp
public sealed class SvgImage : VectorImageResourceBase
```

## 构造函数

| 姓名 | 描述 |
| --- | --- |
| [SvgImage](svgimage#constructor)(string, Stream) | 从内容创建新的 SvgImage 实例，表示为字节流，并具有指定的名称 |
| [SvgImage](svgimage#constructor_1)(string, string) | 从内容创建新的 SvgImage 实例，表示为通常的字符串，并具有指定的名称 |

## 特性

| 姓名 | 描述 |
| --- | --- |
| [AspectRatio](../../groupdocs.editor.htmlcss.resources.images.vector/vectorimageresourcebase/aspectratio) { get; } | 返回此矢量图像的纵横比 |
| override [ByteContent](../../groupdocs.editor.htmlcss.resources.images.vector/svgimage/bytecontent) { get; } | 将此 SVG 图像的内容作为二进制流返回 |
| [FilenameWithExtension](../../groupdocs.editor.htmlcss.resources.images.vector/vectorimageresourcebase/filenamewithextension) { get; } | 返回此矢量图像的正确文件名，由名称和扩展名组成。理论上可以与名称不同。 |
| [IsDisposed](../../groupdocs.editor.htmlcss.resources.images.vector/vectorimageresourcebase/isdisposed) { get; } | 确定是否处理此光栅图像（`真的`） 或不 （`错误的` ) |
| [LinearDimensions](../../groupdocs.editor.htmlcss.resources.images.vector/vectorimageresourcebase/lineardimensions) { get; } | 返回此矢量图像的线性尺寸（宽度和高度） |
| [Name](../../groupdocs.editor.htmlcss.resources.images.vector/vectorimageresourcebase/name) { get; } | 返回此矢量图像的名称。通常不包含文件扩展名，理论上可以不同于文件名. |
| override [TextContent](../../groupdocs.editor.htmlcss.resources.images.vector/svgimage/textcontent) { get; } | 返回此 SVG 图像的内容作为 base64 编码的二进制内容（而不是 XML 格式的原始文本） |
| override [Type](../../groupdocs.editor.htmlcss.resources.images.vector/svgimage/type) { get; } | 返回 ImageType.Svg |
| [XmlContent](../../groupdocs.editor.htmlcss.resources.images.vector/svgimage/xmlcontent) { get; } | 以其原始的符合 XML 的文本形式返回此 SVG 图像的内容 |

## 方法

| 姓名 | 描述 |
| --- | --- |
| override [Dispose](../../groupdocs.editor.htmlcss.resources.images.vector/svgimage/dispose)() | 处理此光栅图像，处理其内容并使大多数方法和属性无效 |
| [Equals](../../groupdocs.editor.htmlcss.resources.images.vector/vectorimageresourcebase/equals)(IHtmlResource) | 检查此实例是否具有指定的引用相等性。 |
| override [Save](../../groupdocs.editor.htmlcss.resources.images.vector/svgimage/save)(string) | 将此 SVG 图像保存到文件 |
| override [SaveToPng](../../groupdocs.editor.htmlcss.resources.images.vector/svgimage/savetopng)(Stream) | 将此矢量 SVG 图像保存为光栅 PNG image |
| static [IsValid](../../groupdocs.editor.htmlcss.resources.images.vector/svgimage/isvalid)(string) | 执行表面检查指定的文本 XML 兼容内容是否表示 SVG 图像 |

## 活动

| 姓名 | 描述 |
| --- | --- |
| event [Disposed](../../groupdocs.editor.htmlcss.resources.images.vector/vectorimageresourcebase/disposed) | 事件，当处理此光栅图像时发生 |

### 也可以看看

* class [VectorImageResourceBase](../vectorimageresourcebase)
* 命名空间 [GroupDocs.Editor.HtmlCss.Resources.Images.Vector](../../groupdocs.editor.htmlcss.resources.images.vector)
* 部件 [GroupDocs.Editor](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Editor.dll -->
