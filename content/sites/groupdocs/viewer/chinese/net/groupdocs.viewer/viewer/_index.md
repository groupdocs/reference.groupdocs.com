---
title: Viewer
second_title: GroupDocs.Viewer for .NET API 参考
description: 表示控制文档渲染过程的主类
type: docs
weight: 800
url: /zh/net/groupdocs.viewer/viewer/
---
## Viewer class

表示控制文档渲染过程的主类。

```csharp
public class Viewer : IDisposable
```

## 构造函数

| 姓名 | 描述 |
| --- | --- |
| [Viewer](viewer#constructor)(Func&lt;Stream&gt;) | 初始化的新实例[`Viewer`](../viewer)类. |
| [Viewer](viewer#constructor_4)(Stream) | 初始化的新实例[`Viewer`](../viewer)类. |
| [Viewer](viewer#constructor_12)(string) | 初始化的新实例[`Viewer`](../viewer)类. |
| [Viewer](viewer#constructor_2)(Func&lt;Stream&gt;, Func&lt;LoadOptions&gt;) | 初始化的新实例[`Viewer`](../viewer)类. |
| [Viewer](viewer#constructor_1)(Func&lt;Stream&gt;, ViewerSettings) | 初始化的新实例[`Viewer`](../viewer)类. |
| [Viewer](viewer#constructor_5)(Stream, bool) | 初始化的新实例[`Viewer`](../viewer)类. |
| [Viewer](viewer#constructor_6)(Stream, LoadOptions) | 初始化的新实例[`Viewer`](../viewer)类. |
| [Viewer](viewer#constructor_10)(Stream, ViewerSettings) | 初始化的新实例[`Viewer`](../viewer)类. |
| [Viewer](viewer#constructor_13)(string, LoadOptions) | 初始化的新实例[`Viewer`](../viewer)类. |
| [Viewer](viewer#constructor_15)(string, ViewerSettings) | 初始化的新实例[`Viewer`](../viewer)类. |
| [Viewer](viewer#constructor_3)(Func&lt;Stream&gt;, Func&lt;LoadOptions&gt;, ViewerSettings) | 初始化的新实例[`Viewer`](../viewer)类. |
| [Viewer](viewer#constructor_7)(Stream, LoadOptions, bool) | 初始化的新实例[`Viewer`](../viewer)类. |
| [Viewer](viewer#constructor_8)(Stream, LoadOptions, ViewerSettings) | 初始化的新实例[`Viewer`](../viewer)类. |
| [Viewer](viewer#constructor_11)(Stream, ViewerSettings, bool) | 初始化的新实例[`Viewer`](../viewer)类. |
| [Viewer](viewer#constructor_14)(string, LoadOptions, ViewerSettings) | 初始化的新实例[`Viewer`](../viewer)类. |
| [Viewer](viewer#constructor_9)(Stream, LoadOptions, ViewerSettings, bool) | 初始化的新实例[`Viewer`](../viewer)类. |

## 方法

| 姓名 | 描述 |
| --- | --- |
| [Dispose](../../groupdocs.viewer/viewer/dispose)() | 释放文件流和管理的内部资源。 |
| [GetAttachments](../../groupdocs.viewer/viewer/getattachments#getattachments)() | 返回文档包含的附件。 |
| [GetAttachments](../../groupdocs.viewer/viewer/getattachments#getattachments_1)(CancellationToken) | 返回文档包含的附件。 |
| [GetFileInfo](../../groupdocs.viewer/viewer/getfileinfo)() | 返回有关文件的信息，例如指示文件是否已加密的文件类型和标志。 |
| [GetViewInfo](../../groupdocs.viewer/viewer/getviewinfo#getviewinfo)(ViewInfoOptions) | 返回有关视图和文档特定信息的信息。 |
| [GetViewInfo](../../groupdocs.viewer/viewer/getviewinfo#getviewinfo_1)(ViewInfoOptions, CancellationToken) | 返回有关视图和文档特定信息的信息。 |
| [SaveAttachment](../../groupdocs.viewer/viewer/saveattachment#saveattachment)(Attachment, Stream) | 将附件文件保存到*destination*流. |
| [SaveAttachment](../../groupdocs.viewer/viewer/saveattachment#saveattachment_1)(Attachment, Stream, CancellationToken) | 将附件文件保存到*destination*流. |
| [View](../../groupdocs.viewer/viewer/view#view)(ViewOptions) | 创建所有文档页面的视图。 |
| [View](../../groupdocs.viewer/viewer/view#view_2)(ViewOptions, CancellationToken) | 创建所有文档页面的视图。 |
| [View](../../groupdocs.viewer/viewer/view#view_1)(ViewOptions, params int[]) | 创建特定文档页面的视图。 |
| [View](../../groupdocs.viewer/viewer/view#view_3)(ViewOptions, CancellationToken, params int[]) | 创建特定文档页面的视图。 |

### 也可以看看

* 命名空间 [GroupDocs.Viewer](../../groupdocs.viewer)
* 部件 [GroupDocs.Viewer](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Viewer.dll -->