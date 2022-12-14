---
title: SetLicense
second_title: GroupDocs.Conversion لمرجع .NET API
description: تراخيص المكون .
type: docs
weight: 20
url: /ar/net/groupdocs.conversion/license/setlicense/
---
## SetLicense(Stream) {#setlicense}

تراخيص المكون .

```csharp
public void SetLicense(Stream licenseStream)
```

| معامل | يكتب | وصف |
| --- | --- | --- |
| licenseStream | Stream | تيار الترخيص. |

### أمثلة

يوضح المثال التالي كيفية تعيين License تمرير دفق ملف الترخيص.

```csharp
using (FileStream licenseStream = new FileStream("LicenseFile.lic", FileMode.Open))
{
    GroupDocs.Conversion.License lic = new GroupDocs.Conversion.License();
    lic.SetLicense(licenseStream);
}
```

### أنظر أيضا

* class [License](../../license)
* مساحة الاسم [GroupDocs.Conversion](../../license)
* المجسم [GroupDocs.Conversion](../../../)

---

## SetLicense(string) {#setlicense_1}

تراخيص المكون .

```csharp
public void SetLicense(string licensePath)
```

| معامل | يكتب | وصف |
| --- | --- | --- |
| licensePath | String | مسار الترخيص. |

### أمثلة

يوضح المثال التالي كيفية تعيين ترخيص تمرير مسار إلى ملف الترخيص.

```csharp
string licensePath = "GroupDocs.Conversion.lic";
GroupDocs.Conversion.License lic = new GroupDocs.Conversion.License();
lic.SetLicense(licensePath);
```

### أنظر أيضا

* class [License](../../license)
* مساحة الاسم [GroupDocs.Conversion](../../license)
* المجسم [GroupDocs.Conversion](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Conversion.dll -->
