---
title: SetLicense
second_title: Справочник по API GroupDocs.Merge для .NET
description: Лицензирует компонент.
type: docs
weight: 20
url: /ru/net/groupdocs.merger/license/setlicense/
---
## SetLicense(Stream) {#setlicense}

Лицензирует компонент.

```csharp
public void SetLicense(Stream licenseStream)
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| licenseStream | Stream | Лицензионный поток. |

### Примеры

В следующем примере показано, как установить лицензию , передавая поток файла лицензии.

```csharp
using (FileStream licenseStream = new FileStream("LicenseFile.lic", FileMode.Open))
{
    GroupDocs.Merger.License lic = new GroupDocs.Merger.License();
    lic.SetLicense(licenseStream);
}
```

### Смотрите также

* class [License](../../license)
* пространство имен [GroupDocs.Merger](../../license)
* сборка [GroupDocs.Merger](../../../)

---

## SetLicense(string) {#setlicense_1}

Лицензирует компонент.

```csharp
public void SetLicense(string licensePath)
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| licensePath | String | Лицензионный путь. |

### Примеры

В следующем примере показано, как установить лицензию , передав путь к файлу лицензии.

```csharp
string licensePath = "GroupDocs.Merger.lic";
GroupDocs.Merger.License lic = new GroupDocs.Merger.License();
lic.SetLicense(licensePath);
```

### Смотрите также

* class [License](../../license)
* пространство имен [GroupDocs.Merger](../../license)
* сборка [GroupDocs.Merger](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Merger.dll -->
