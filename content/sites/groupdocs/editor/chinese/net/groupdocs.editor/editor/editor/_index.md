---
title: Editor
second_title: GroupDocs.Editor for .NET API 参考
description: 使用指定的输入文档作为流初始化新的编辑器实例
type: docs
weight: 10
url: /zh/net/groupdocs.editor/editor/editor/
---
## Editor(Func&lt;Stream&gt;) {#constructor}

使用指定的输入文档（作为流）初始化新的编辑器实例

```csharp
public Editor(Func<Stream> document)
```

| 范围 | 类型 | 描述 |
| --- | --- | --- |
| document | Func`1 | 委托，它应该返回一个包含文档内容的流。不应为 NULL。 |

### 评论

**学到更多**

* 更多关于 GroupDocs.Editor 支持的文件类型： [GroupDocs.Editor 支持的文档格式](https://docs.groupdocs.com/display/editornet/Supported+Document+Formats)
* 更多关于 GroupDocs.Editor 的 .NET 功能： [开发者指南](https://docs.groupdocs.com/display/editornet/Developer+Guide)

### 也可以看看

* class [Editor](../../editor)
* 命名空间 [GroupDocs.Editor](../../editor)
* 部件 [GroupDocs.Editor](../../../)

---

## Editor(Func&lt;Stream&gt;, Func&lt;ILoadOptions&gt;) {#constructor_1}

使用指定的输入文档（作为流）及其加载选项初始化新的编辑器实例

```csharp
public Editor(Func<Stream> document, Func<ILoadOptions> loadOptions)
```

| 范围 | 类型 | 描述 |
| --- | --- | --- |
| document | Func`1 | 委托，它应该返回一个包含文档内容的流。不应为 NULL。 |
| loadOptions | Func`1 | 委托，应该返回一个文档加载选项。可能为 NULL 并且可能返回 null - 在这种情况下将自动检测文档类型并应用该类型的默认加载选项。 |

### 评论

**学到更多**

* 更多关于 GroupDocs.Editor 支持的文件类型： [GroupDocs.Editor 支持的文档格式](https://docs.groupdocs.com/display/editornet/Supported+Document+Formats)
* 更多关于 GroupDocs.Editor 的 .NET 功能： [开发者指南](https://docs.groupdocs.com/display/editornet/Developer+Guide)
* 更多关于如何打开和编辑受密码保护的文档和来自不同存储的文档： [使用 GroupDocs.Editor 加载和编辑文档](https://docs.groupdocs.com/display/editornet/Load+document)

### 也可以看看

* interface [ILoadOptions](../../../groupdocs.editor.options/iloadoptions)
* class [Editor](../../editor)
* 命名空间 [GroupDocs.Editor](../../editor)
* 部件 [GroupDocs.Editor](../../../)

---

## Editor(string) {#constructor_2}

使用指定的输入文档（作为完整文件路径）初始化新的编辑器实例

```csharp
public Editor(string filePath)
```

| 范围 | 类型 | 描述 |
| --- | --- | --- |
| filePath | String | 文件的完整路径。不应为 NULL。应该是有效的，并且文件应该存在。 |

### 评论

**学到更多**

* 更多关于 GroupDocs.Editor 支持的文件类型： [GroupDocs.Editor 支持的文档格式](https://docs.groupdocs.com/display/editornet/Supported+Document+Formats)
* 更多关于 GroupDocs.Editor 的 .NET 功能： [开发者指南](https://docs.groupdocs.com/display/editornet/Developer+Guide)

### 也可以看看

* class [Editor](../../editor)
* 命名空间 [GroupDocs.Editor](../../editor)
* 部件 [GroupDocs.Editor](../../../)

---

## Editor(string, Func&lt;ILoadOptions&gt;) {#constructor_3}

使用指定的输入文档（作为完整文件路径）及其加载选项初始化新的编辑器实例

```csharp
public Editor(string filePath, Func<ILoadOptions> loadOptions)
```

| 范围 | 类型 | 描述 |
| --- | --- | --- |
| filePath | String | 文件的完整路径。不应为 NULL。应该是有效的，并且文件应该存在。 |
| loadOptions | Func`1 | 委托，应该返回一个文档加载选项。可能为 NULL 并且可能返回 null - 在这种情况下将自动检测文档类型并应用该类型的默认加载选项。 |

### 评论

**学到更多**

* 更多关于 GroupDocs.Editor 支持的文件类型： [GroupDocs.Editor 支持的文档格式](https://docs.groupdocs.com/display/editornet/Supported+Document+Formats)
* 更多关于 GroupDocs.Editor 的 .NET 功能： [开发者指南](https://docs.groupdocs.com/display/editornet/Developer+Guide)
* 更多关于如何打开和编辑受密码保护的文档和来自不同存储的文档： [使用 GroupDocs.Editor 加载和编辑文档](https://docs.groupdocs.com/display/editornet/Load+document)

### 也可以看看

* interface [ILoadOptions](../../../groupdocs.editor.options/iloadoptions)
* class [Editor](../../editor)
* 命名空间 [GroupDocs.Editor](../../editor)
* 部件 [GroupDocs.Editor](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Editor.dll -->