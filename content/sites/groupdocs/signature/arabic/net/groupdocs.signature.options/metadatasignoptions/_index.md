---
title: MetadataSignOptions
second_title: GroupDocs.Signature لمرجع .NET API
description: يمثل خيارات توقيع البيانات الوصفية.
type: docs
weight: 1490
url: /ar/net/groupdocs.signature.options/metadatasignoptions/
---
## MetadataSignOptions class

يمثل خيارات توقيع البيانات الوصفية.

```csharp
public class MetadataSignOptions : SignOptions
```

## المنشئون

| اسم | وصف |
| --- | --- |
| [MetadataSignOptions](metadatasignoptions#constructor)() | تهيئة مثيل جديد لفئة MetadataSignOptions بالقيم الافتراضية. |
| [MetadataSignOptions](metadatasignoptions#constructor_1)(IEnumerable&lt;MetadataSignature&gt;) | تهيئة مثيل جديد لفئة MetadataSignOptions مع Metadata. |

## الخصائص

| اسم | وصف |
| --- | --- |
| virtual [AllPages](../../groupdocs.signature.options/signoptions/allpages) { get; set; } | ضع التوقيع على كل صفحات الوثيقة. |
| [Appearance](../../groupdocs.signature.options/signoptions/appearance) { get; set; } | مظهر توقيع إضافي . |
| [DataEncryption](../../groupdocs.signature.options/metadatasignoptions/dataencryption) { get; set; } | يحصل أو يحدد تنفيذ[`IDataEncryption`](../../groupdocs.signature.domain.extensions/idataencryption)واجهة لتشفير جميع تواقيع البيانات الوصفية باستخدام مجموعة الخيارات هذه. إذا تم تعيين هذه القيمة ، فستستخدم جميع التوقيعات المضافة هذا التشفير افتراضيًا أو تشفير DataEncryption الخاص بها إذا تم تعيينه. |
| [DocumentType](../../groupdocs.signature.options/signoptions/documenttype) { get; set; } | احصل على أو اضبط "نوع المستند" لخيارات التوقيع[`DocumentType`](../../groupdocs.signature.domain/documenttype) |
| [Extensions](../../groupdocs.signature.options/signoptions/extensions) { get; } | ملحقات التوقيع . |
| virtual [PageNumber](../../groupdocs.signature.options/signoptions/pagenumber) { get; set; } | الحصول على رقم صفحة المستند أو تعيينه للتوقيع. القيمة الدنيا والافتراضية هي 1. |
| virtual [PagesSetup](../../groupdocs.signature.options/signoptions/pagessetup) { get; set; } | خيارات لتحديد الصفحات المراد توقيعها. |
| [Signatures](../../groupdocs.signature.options/metadatasignoptions/signatures) { get; set; } | الحصول على البيانات الوصفية الخاصة بالتوقيع أو تعيينها. |
| [SignatureType](../../groupdocs.signature.options/signoptions/signaturetype) { get; } | احصل على نوع التوقيع[`SignatureType`](../../groupdocs.signature.domain/signaturetype) |
| [ZOrder](../../groupdocs.signature.options/signoptions/zorder) { get; set; } | الحصول على أو تحديد موضع ترتيب Z لتوقيع النص. لتحديد ترتيب عرض التواقيع المتداخلة. |

## طُرق

| اسم | وصف |
| --- | --- |
| [Add](../../groupdocs.signature.options/metadatasignoptions/add)(MetadataSignature) | إضافة نسخة MetadataSignature الموجودة إلى المجموعة. |
| [AddImageSignature](../../groupdocs.signature.options/metadatasignoptions/addimagesignature)(ushort, object) | إنشاء توقيع ImageMetadata جديد باستخدام الوسائط التي تم تمريرها وإضافتها إلى المجموعة. |
| [AddPdfSignature](../../groupdocs.signature.options/metadatasignoptions/addpdfsignature)(string, object, string) | ينشئ توقيعًا جديدًا لـ PdfMetadata مع وسيطات تم تمريرها ويضيفها إلى المجموعة. |

### ملاحظات

**يتعلم أكثر**

* الاستخدام الأساسي لإنشاء التوقيع الإلكتروني للبيانات الوصفية بواسطة GroupDocs. التوقيع: [كيفية التوقيع الإلكتروني للمستند مع توقيع البيانات الوصفية](https://docs.groupdocs.com/display/signaturenet/eSign+document+with+Metadata+signature)
* الاستخدام المتقدم لإعدادات التوقيع الإلكتروني للبيانات الوصفية باستخدام GroupDocs. التوقيع: [الاستخدام المتقدم لوثيقة eSign مع توقيع البيانات الوصفية والإعدادات الإضافية](https://docs.groupdocs.com/display/signaturenet/Sign+document+with+Metadata+signature+-+advanced)

### أنظر أيضا

* class [SignOptions](../signoptions)
* مساحة الاسم [GroupDocs.Signature.Options](../../groupdocs.signature.options)
* المجسم [GroupDocs.Signature](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Signature.dll -->
