---
title: Merger
second_title: GroupDocs.Merger for .NET API 参考
description: 表示控制文档合并过程的主类
type: docs
weight: 790
url: /zh/net/groupdocs.merger/merger/
---
## Merger class

表示控制文档合并过程的主类。

```csharp
public class Merger : IDisposable
```

## 构造函数

| 姓名 | 描述 |
| --- | --- |
| [Merger](merger#constructor)(Func&lt;Stream&gt;) | 初始化新实例[`Merger`](../merger)类. |
| [Merger](merger#constructor_4)(Stream) | 初始化新实例[`Merger`](../merger)类. |
| [Merger](merger#constructor_8)(string) | 初始化新实例[`Merger`](../merger)类. |
| [Merger](merger#constructor_1)(Func&lt;Stream&gt;, ILoadOptions) | 初始化新实例[`Merger`](../merger)类. |
| [Merger](merger#constructor_3)(Func&lt;Stream&gt;, MergerSettings) | 初始化新实例[`Merger`](../merger)类. |
| [Merger](merger#constructor_5)(Stream, ILoadOptions) | 初始化新实例[`Merger`](../merger)类. |
| [Merger](merger#constructor_7)(Stream, MergerSettings) | 初始化新实例[`Merger`](../merger)类. |
| [Merger](merger#constructor_9)(string, ILoadOptions) | 初始化新实例[`Merger`](../merger)类. |
| [Merger](merger#constructor_11)(string, MergerSettings) | 初始化新实例[`Merger`](../merger)类. |
| [Merger](merger#constructor_2)(Func&lt;Stream&gt;, ILoadOptions, MergerSettings) | 初始化新实例[`Merger`](../merger)类. |
| [Merger](merger#constructor_6)(Stream, ILoadOptions, MergerSettings) | 初始化新实例[`Merger`](../merger)类. |
| [Merger](merger#constructor_10)(string, ILoadOptions, MergerSettings) | 初始化新实例[`Merger`](../merger)类. |

## 方法

| 姓名 | 描述 |
| --- | --- |
| [AddPassword](../../groupdocs.merger/merger/addpassword)(IAddPasswordOptions) | 使用密码保护文档。 |
| [ChangeOrientation](../../groupdocs.merger/merger/changeorientation)(IOrientationOptions) | 为指定页面应用新的方向模式。 |
| [Dispose](../../groupdocs.merger/merger/dispose)() | 处置资源。 |
| [ExtractPages](../../groupdocs.merger/merger/extractpages)(IExtractOptions) | 使用源文档中的一些页面创建一个新文档。 |
| [GeneratePreview](../../groupdocs.merger/merger/generatepreview)(IPreviewOptions) | 生成文档页面预览。 |
| [GetDocumentInfo](../../groupdocs.merger/merger/getdocumentinfo)() | 获取有关文档页面的信息：它们的大小、最大页面高度、具有最大高度的页面的宽度。 |
| [ImportDocument](../../groupdocs.merger/merger/importdocument)(IImportDocumentOptions) | 将文档作为附件导入或通过 Ole 嵌入。 |
| [IsPasswordSet](../../groupdocs.merger/merger/ispasswordset)() | 检查文档是否受密码保护。 |
| [Join](../../groupdocs.merger/merger/join#join)(Stream) | 将文档合并为一个文档。 |
| [Join](../../groupdocs.merger/merger/join#join_3)(string) | 将文档合并为一个文档。 |
| [Join](../../groupdocs.merger/merger/join#join_1)(Stream, IImageJoinOptions) | 将文档合并为一个文档。 |
| [Join](../../groupdocs.merger/merger/join#join_2)(Stream, IJoinOptions) | 将文档合并为一个文档。 |
| [Join](../../groupdocs.merger/merger/join#join_4)(string, IImageJoinOptions) | 将文档合并为一个文档。 |
| [Join](../../groupdocs.merger/merger/join#join_5)(string, IJoinOptions) | 将文档合并为一个文档。 |
| [MovePage](../../groupdocs.merger/merger/movepage)(IMoveOptions) | 将页面移动到已知格式文档中的新位置。 |
| [RemovePages](../../groupdocs.merger/merger/removepages)(IRemoveOptions) | 从已知格式的文档中删除页面。 |
| [RemovePassword](../../groupdocs.merger/merger/removepassword)() | 从文档中删除密码。 |
| [RotatePages](../../groupdocs.merger/merger/rotatepages)(IRotateOptions) | 旋转文档的页面。 |
| [Save](../../groupdocs.merger/merger/save#save)(Stream) | 将结果文档保存到流中*document*. |
| [Save](../../groupdocs.merger/merger/save#save_1)(string) | 将结果文档文件保存到*filePath*. |
| [Save](../../groupdocs.merger/merger/save#save_2)(string, bool) | 将结果文档文件保存到*filePath*. |
| [Split](../../groupdocs.merger/merger/split#split)(ISplitOptions) | 将单个文档拆分为多个文档。 |
| [Split](../../groupdocs.merger/merger/split#split_1)(ITextSplitOptions) | 将单个文档拆分为多个文档。 |
| [SwapPages](../../groupdocs.merger/merger/swappages)(ISwapOptions) | 在已知格式的文档中交换两页。 |
| [UpdatePassword](../../groupdocs.merger/merger/updatepassword)(IUpdatePasswordOptions) | 更新文档的现有密码。 |

### 也可以看看

* 命名空间 [GroupDocs.Merger](../../groupdocs.merger)
* 部件 [GroupDocs.Merger](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Merger.dll -->
