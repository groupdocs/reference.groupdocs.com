---
title: Error
second_title: GroupDocs.Viewer لمرجع .NET API
description: يكتب رسالة خطأ إلى وحدة التحكم . توفر رسائل سجل الخطأ معلومات حول الأحداث غير القابلة للاسترداد في تدفق التطبيق.
type: docs
weight: 20
url: /ar/net/groupdocs.viewer.logging/filelogger/error/
---
## FileLogger.Error method

يكتب رسالة خطأ إلى وحدة التحكم . توفر رسائل سجل الخطأ معلومات حول الأحداث غير القابلة للاسترداد في تدفق التطبيق.

```csharp
public void Error(string message, Exception exception)
```

| معامل | يكتب | وصف |
| --- | --- | --- |
| message | String | رسالة الخطأ. |
| exception | Exception | الاستثناء. |

### استثناءات

| استثناء | حالة |
| --- | --- |
| ArgumentNullException | عندما ألقيت*message* باطل. |
| ArgumentNullException | عندما ألقيت*exception* باطل. |

### أنظر أيضا

* class [FileLogger](../../filelogger)
* مساحة الاسم [GroupDocs.Viewer.Logging](../../filelogger)
* المجسم [GroupDocs.Viewer](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Viewer.dll -->
