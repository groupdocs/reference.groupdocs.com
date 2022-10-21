---
title: PersonalStorageFileType
second_title: GroupDocs.Conversion for .NET API 参考
description: 定义电子邮件应用程序用来存储各种数据包括电子邮件附件文件夹地址簿等的个人存储文件格式 包括以下文件类型 Ost./personalstoragefiletype/ost  Pst./personalstoragefiletype/pst  了解有关电子邮件格式的更多信息这里https//wiki.fileformat.com/email.
type: docs
weight: 900
url: /zh/net/groupdocs.conversion.filetypes/personalstoragefiletype/
---
## PersonalStorageFileType class

定义电子邮件应用程序用来存储各种数据（包括电子邮件、附件、文件夹、地址簿等）的个人存储文件格式。 包括以下文件类型： [`Ost`](./ost) , [`Pst`](./pst) , 了解有关电子邮件格式的更多信息[这里](https://wiki.fileformat.com/email).

```csharp
public sealed class PersonalStorageFileType : FileType
```

## 构造函数

| 姓名 | 描述 |
| --- | --- |
| [PersonalStorageFileType](personalstoragefiletype)() | 序列化构造函数 |

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
| static readonly [Nsf](../../groupdocs.conversion.filetypes/personalstoragefiletype/nsf) | 扩展名为 .nsf（Notes Storage Facility）的文件是 IBM Notes 软件（以前称为 Lotus Notes）使用的数据库文件格式。它定义了存储不同类型对象的架构，例如电子邮件、约会、文档、表单和视图。 了解有关此文件格式的更多信息[这里](https://docs.fileformat.com/database/nsf) |
| static readonly [Ost](../../groupdocs.conversion.filetypes/personalstoragefiletype/ost) | OST 或脱机存储文件表示在使用 Microsoft Outlook 向 Exchange Server 注册后，在本地计算机上处于脱机模式的用户邮箱数据。 了解有关此文件格式的更多信息[这里](https://wiki.fileformat.com/email/ost) |
| static readonly [Pst](../../groupdocs.conversion.filetypes/personalstoragefiletype/pst) | 带有 .PST 扩展名的文件代表 Outlook 个人存储文件（也称为个人存储表），用于存储各种用户信息。 了解有关此文件格式的更多信息[这里](https://wiki.fileformat.com/email/pst) |

### 也可以看看

* class [FileType](../filetype)
* 命名空间 [GroupDocs.Conversion.FileTypes](../../groupdocs.conversion.filetypes)
* 部件 [GroupDocs.Conversion](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Conversion.dll -->