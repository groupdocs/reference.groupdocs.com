---
title: SetLicense
second_title: GroupDocs.Conversion for .NET API 参考
description: 许可组件
type: docs
weight: 20
url: /zh/net/groupdocs.conversion/license/setlicense/
---
## SetLicense(Stream) {#setlicense}

许可组件。

```csharp
public void SetLicense(Stream licenseStream)
```

| 范围 | 类型 | 描述 |
| --- | --- | --- |
| licenseStream | Stream | 许可证流。 |

### 例子

下面的例子演示了如何设置一个license passing Stream of the license file.

```csharp
using (FileStream licenseStream = new FileStream("LicenseFile.lic", FileMode.Open))
{
    GroupDocs.Conversion.License lic = new GroupDocs.Conversion.License();
    lic.SetLicense(licenseStream);
}
```

### 也可以看看

* class [License](../../license)
* 命名空间 [GroupDocs.Conversion](../../license)
* 部件 [GroupDocs.Conversion](../../../)

---

## SetLicense(string) {#setlicense_1}

许可组件。

```csharp
public void SetLicense(string licensePath)
```

| 范围 | 类型 | 描述 |
| --- | --- | --- |
| licensePath | String | 许可证路径。 |

### 例子

以下示例演示如何设置许可证 传递许可证文件的路径。

```csharp
string licensePath = "GroupDocs.Conversion.lic";
GroupDocs.Conversion.License lic = new GroupDocs.Conversion.License();
lic.SetLicense(licensePath);
```

### 也可以看看

* class [License](../../license)
* 命名空间 [GroupDocs.Conversion](../../license)
* 部件 [GroupDocs.Conversion](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Conversion.dll -->
