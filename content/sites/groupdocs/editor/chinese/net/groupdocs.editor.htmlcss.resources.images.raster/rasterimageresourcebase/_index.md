---
title: RasterImageResourceBase
second_title: GroupDocs.Editor for .NET API 参考
description: 具有固定名称尺寸纵横比类型大小和内容的任何受支持光栅图像的基类
type: docs
weight: 550
url: /zh/net/groupdocs.editor.htmlcss.resources.images.raster/rasterimageresourcebase/
---
## RasterImageResourceBase class

具有固定名称、尺寸、纵横比、类型、大小和内容的任何受支持光栅图像的基类。

```csharp
public abstract class RasterImageResourceBase : IImageResource
```

## 特性

| 姓名 | 描述 |
| --- | --- |
| [AspectRatio](../../groupdocs.editor.htmlcss.resources.images.raster/rasterimageresourcebase/aspectratio) { get; } | 返回此图像的纵横比作为宽高关系 |
| [ByteContent](../../groupdocs.editor.htmlcss.resources.images.raster/rasterimageresourcebase/bytecontent) { get; } | 将此光栅图像的内容作为字节流返回 |
| [FilenameWithExtension](../../groupdocs.editor.htmlcss.resources.images.raster/rasterimageresourcebase/filenamewithextension) { get; } | 返回此光栅图像的正确文件名，它由名称和扩展名组成。理论上可以与名称不同。 |
| [IsDisposed](../../groupdocs.editor.htmlcss.resources.images.raster/rasterimageresourcebase/isdisposed) { get; } | 确定是否处理此光栅图像 |
| [Length](../../groupdocs.editor.htmlcss.resources.images.raster/rasterimageresourcebase/length) { get; } | 以字节为单位返回此光栅图像文件的长度 |
| [LinearDimensions](../../groupdocs.editor.htmlcss.resources.images.raster/rasterimageresourcebase/lineardimensions) { get; } | 返回此光栅图像的线性尺寸（宽度和高度） |
| [Name](../../groupdocs.editor.htmlcss.resources.images.raster/rasterimageresourcebase/name) { get; } | 返回此光栅图像的名称。通常不包含文件扩展名，理论上可以不同于文件名. |
| [TextContent](../../groupdocs.editor.htmlcss.resources.images.raster/rasterimageresourcebase/textcontent) { get; } | 以 base64 编码的字符串形式返回此光栅图像的内容 |
| abstract [Type](../../groupdocs.editor.htmlcss.resources.images.raster/rasterimageresourcebase/type) { get; } | 在实现类型时应返回有关光栅图像类型的信息 |

## 方法

| 姓名 | 描述 |
| --- | --- |
| [Dispose](../../groupdocs.editor.htmlcss.resources.images.raster/rasterimageresourcebase/dispose)() | 处理此光栅图像，处理其内容并使大多数方法和属性无效 |
| [Equals](../../groupdocs.editor.htmlcss.resources.images.raster/rasterimageresourcebase/equals#equals)(IHtmlResource) | 检查此实例是否具有指定的引用相等性。 |
| [GenerateBitmap](../../groupdocs.editor.htmlcss.resources.images.raster/rasterimageresourcebase/generatebitmap)() | 从该光栅图像生成并返回“System.Drawing.Bitmap”的新实例。 |
| [ReduceToNewHeight](../../groupdocs.editor.htmlcss.resources.images.raster/rasterimageresourcebase/reducetonewheight)(ushort) | 创建并返回相同类型的新缩小图像资源，但具有指定的新缩小高度和按比例缩小的宽度。 |
| [Save](../../groupdocs.editor.htmlcss.resources.images.raster/rasterimageresourcebase/save)(string) | 将此光栅图像保存到指定文件 |

## 活动

| 姓名 | 描述 |
| --- | --- |
| event [Disposed](../../groupdocs.editor.htmlcss.resources.images.raster/rasterimageresourcebase/disposed) | 事件，当处理此光栅图像时发生 |

### 也可以看看

* interface [IImageResource](../../groupdocs.editor.htmlcss.resources.images/iimageresource)
* 命名空间 [GroupDocs.Editor.HtmlCss.Resources.Images.Raster](../../groupdocs.editor.htmlcss.resources.images.raster)
* 部件 [GroupDocs.Editor](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Editor.dll -->
