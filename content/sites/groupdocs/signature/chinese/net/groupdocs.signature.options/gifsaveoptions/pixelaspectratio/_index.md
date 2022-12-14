---
title: PixelAspectRatio
second_title: GroupDocs.Signature for .NET API 参考
description: 获取或设置 GIF 像素纵横比
type: docs
weight: 80
url: /zh/net/groupdocs.signature.options/gifsaveoptions/pixelaspectratio/
---
## GifSaveOptions.PixelAspectRatio property

获取或设置 GIF 像素纵横比。

```csharp
public byte PixelAspectRatio { get; set; }
```

### 评论

Pixel Aspect Ratio - 用于计算原始图像中像素的 aspect 比率的近似值的因子。如果该字段的值不是 0，则该纵横比的近似值根据以下公式计算： 纵横比=（像素纵横比+ 15）/64像素纵横比定义为 为像素宽度的商超过它的高度。此字段中的值 range 允许以 1/64 的增量指定 4:1 的最宽像素到 1:4 的最高 像素。值：0 - 没有给出纵横比信息 。 1..255 - 计算中使用的值。

### 也可以看看

* class [GifSaveOptions](../../gifsaveoptions)
* 命名空间 [GroupDocs.Signature.Options](../../gifsaveoptions)
* 部件 [GroupDocs.Signature](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Signature.dll -->
