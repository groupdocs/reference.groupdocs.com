---
title: FindFormat
second_title: GroupDocs.Redaction لمرجع .NET API
description: البحث عن تكوينات التنسيق لملحق ملف معين.
type: docs
weight: 30
url: /ar/net/groupdocs.redaction.configuration/redactorconfiguration/findformat/
---
## RedactorConfiguration.FindFormat method

البحث عن تكوينات التنسيق لملحق ملف معين.

```csharp
public DocumentFormatConfiguration FindFormat(string fileExtension)
```

| معامل | يكتب | وصف |
| --- | --- | --- |
| fileExtension | String | امتداد الملف ، التنسيق هو ".ext" |

### قيمة الإرجاع

إذا تم العثور على مثيل[`DocumentFormatConfiguration`](../../documentformatconfiguration)، باطل خلاف ذلك

### أمثلة

يوضح المثال التالي كيفية الحصول على معالجات تنسيق المستخدم المضمنة أو المخصصة.

```csharp
var configuration = RedactorConfiguration.GetInstance();
var formatSettings = configuration.FindFormat(".psd");
```

### أنظر أيضا

* class [DocumentFormatConfiguration](../../documentformatconfiguration)
* class [RedactorConfiguration](../../redactorconfiguration)
* مساحة الاسم [GroupDocs.Redaction.Configuration](../../redactorconfiguration)
* المجسم [GroupDocs.Redaction](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Redaction.dll -->
