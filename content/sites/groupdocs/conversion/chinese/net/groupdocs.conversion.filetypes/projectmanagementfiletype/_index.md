---
title: ProjectManagementFileType
second_title: GroupDocs.Conversion for .NET API 参考
description: 定义由项目管理软件如 Microsoft ProjectPrimavera P6 等创建的项目文件格式项目文件是任务资源及其调度的集合以在表单或产品或服务中获得可衡量的输出 项目管理文件包括以下文件类型 Mpp./projectmanagementfiletype/mpp  Mpt./projectmanagementfiletype/mpt  Mpx./projectmanagementfiletype/mpx . 了解有关项目管理格式的更多信息这里https//wiki.fileformat.com/projectmanagement.
type: docs
weight: 920
url: /zh/net/groupdocs.conversion.filetypes/projectmanagementfiletype/
---
## ProjectManagementFileType class

定义由项目管理软件（如 Microsoft Project、Primavera P6 等）创建的项目文件格式。项目文件是任务、资源及其调度的集合，以在表单或产品或服务中获得可衡量的输出。 项目管理文件。包括以下文件类型： [`Mpp`](./mpp) , [`Mpt`](./mpt) , [`Mpx`](./mpx) . 了解有关项目管理格式的更多信息[这里](https://wiki.fileformat.com/project-management).

```csharp
public sealed class ProjectManagementFileType : FileType
```

## 构造函数

| 姓名 | 描述 |
| --- | --- |
| [ProjectManagementFileType](projectmanagementfiletype)() | 序列化构造函数 |

## 特性

| 姓名 | 描述 |
| --- | --- |
| [Description](../../groupdocs.conversion.filetypes/filetype/description) { get; } | 文件类型描述 |
| [Extension](../../groupdocs.conversion.filetypes/filetype/extension) { get; } | 文件扩展名 |
| [Family](../../groupdocs.conversion.filetypes/filetype/family) { get; } | 档案族 |
| [FileFormat](../../groupdocs.conversion.filetypes/filetype/fileformat) { get; } | 文件格式 |

## 方法

| 姓名 | 描述 |
| --- | --- |
| [CompareTo](../../groupdocs.conversion.contracts/enumeration/compareto)(object) | 将当前对象与其他对象进行比较。 |
| virtual [Equals](../../groupdocs.conversion.contracts/enumeration/equals)(Enumeration) | 确定两个对象实例是否相等。 |
| override [Equals](../../groupdocs.conversion.contracts/enumeration/equals)(object) | 确定两个对象实例是否相等。 |
| override [GetHashCode](../../groupdocs.conversion.contracts/enumeration/gethashcode)() | 用作默认哈希函数。 |
| override [ToString](../../groupdocs.conversion.filetypes/filetype/tostring)() | 字符串表示 |

## 字段

| 姓名 | 描述 |
| --- | --- |
| static readonly [Mpp](../../groupdocs.conversion.filetypes/projectmanagementfiletype/mpp) | MPP 是 Microsoft Project 数据文件，它以集成方式存储与项目管理相关的信息。 了解有关此文件格式的更多信息[这里](https://wiki.fileformat.com/project-management/mpp) |
| static readonly [Mpt](../../groupdocs.conversion.filetypes/projectmanagementfiletype/mpt) | Microsoft Project 模板文件，包含基本信息和结构以及用于创建 .MPP 文件的文档设置。 了解有关此文件格式的更多信息[这里](https://wiki.fileformat.com/project-management/mpt) |
| static readonly [Mpx](../../groupdocs.conversion.filetypes/projectmanagementfiletype/mpx) | Microsoft Exchange 文件格式，是一种 ASCII 文件格式，用于在 Microsoft Project (MSP) 和其他支持 MPX 文件格式的应用程序（如 Primavera Project Planner、Sciforma 和 Timerline Precision Estimating）之间传输项目信息。 了解有关此文件格式的更多信息[这里](https://wiki.fileformat.com/project-management/mpx) |
| static readonly [Xer](../../groupdocs.conversion.filetypes/projectmanagementfiletype/xer) | XER 文件格式是 Primavera P6 项目规划和管理应用程序使用的专有项目文件格式。 了解有关此文件格式的更多信息[这里](https://docs.fileformat.com/project-management/xer) |

### 也可以看看

* class [FileType](../filetype)
* 命名空间 [GroupDocs.Conversion.FileTypes](../../groupdocs.conversion.filetypes)
* 部件 [GroupDocs.Conversion](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Conversion.dll -->