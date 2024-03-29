---
title: Editor
second_title: GroupDocs.Editor لمرجع .NET API
description: الفئة الرئيسية  والتي تلخص طرق التحويل . توفر فئة المحرر طرقًا لتحميل المستندات وتحريرها وحفظها بجميع التنسيقات التي يمكن دعمها. يمكن التخلص منه  لذا استخدم توجيه استخدام أو تخلص من موارده يدويًا عبر استدعاء الأسلوب Dispose . يتم تحميل المستند من خلال المنشئين. تحرير المستند  من خلال طريقة تحرير  والحفظ مرة أخرى إلى المستند الناتج بعد التحرير  من خلال طريقة حفظ .
type: docs
weight: 20
url: /ar/net/groupdocs.editor/editor/
---
## Editor class

الفئة الرئيسية ، والتي تلخص طرق التحويل . توفر فئة المحرر طرقًا لتحميل المستندات وتحريرها وحفظها بجميع التنسيقات التي يمكن دعمها. يمكن التخلص منه ، لذا استخدم توجيه "استخدام" أو تخلص من موارده يدويًا عبر استدعاء الأسلوب "Dispose ()". يتم تحميل المستند من خلال المنشئين. تحرير المستند - من خلال طريقة "تحرير" ، والحفظ مرة أخرى إلى المستند الناتج بعد التحرير - من خلال طريقة "حفظ" .

```csharp
public sealed class Editor : IAuxDisposable
```

## المنشئون

| اسم | وصف |
| --- | --- |
| [Editor](editor#constructor)(Func&lt;Stream&gt;) | تهيئة مثيل المحرر الجديد بمستند إدخال محدد (كتدفق) |
| [Editor](editor#constructor_2)(string) | تهيئة مثيل المحرر الجديد بمستند إدخال محدد (كمسار ملف كامل) |
| [Editor](editor#constructor_1)(Func&lt;Stream&gt;, Func&lt;ILoadOptions&gt;) | تهيئة مثيل المحرر الجديد بمستند إدخال محدد (كتدفق) بخيارات التحميل الخاصة به |
| [Editor](editor#constructor_3)(string, Func&lt;ILoadOptions&gt;) | تهيئة مثيل المحرر الجديد بمستند إدخال محدد (كمسار ملف كامل) بخيارات التحميل الخاصة به |

## الخصائص

| اسم | وصف |
| --- | --- |
| [IsDisposed](../../groupdocs.editor/editor/isdisposed) { get; } | يشير إلى ما إذا كان تم التخلص من مثيل المحرر هذا بالفعل ولا يمكن استخدامه بعد الآن (صواب) أو لم يتم التخلص منه بعد ، وبالتالي فهو نشط (خطأ) |

## طُرق

| اسم | وصف |
| --- | --- |
| [Dispose](../../groupdocs.editor/editor/dispose)() | التخلص من هذا المثيل من المحرر ، بحيث يقوم بإصدار كافة الموارد الداخلية ويصبح غير متاح للاستخدام مرة أخرى |
| [Edit](../../groupdocs.editor/editor/edit#edit)() | يفتح مستندًا تم تحميله مسبقًا للتحرير باستخدام الخيارات الافتراضية عن طريق إنشاء وإرجاع مثيل '[`EditableDocument`](../editabledocument) فئة ، والتي بدورها تحتوي على طرق لإنتاج ترميز HTML والموارد المرتبطة. |
| [Edit](../../groupdocs.editor/editor/edit#edit_1)(IEditOptions) | يفتح مستندًا تم تحميله مسبقًا للتحرير باستخدام خيارات محددة خاصة بالتنسيق عن طريق إنشاء وإرجاع مثيل '[`EditableDocument`](../editabledocument) فئة ، والتي بدورها تحتوي على طرق لإنتاج ترميز HTML والموارد المرتبطة. |
| [GetDocumentInfo](../../groupdocs.editor/editor/getdocumentinfo)(string) | إرجاع البيانات الوصفية الخاصة بالمستند الذي تم تحميله إلى مثيل "المحرر" هذا |
| [Save](../../groupdocs.editor/editor/save#save)(EditableDocument, Stream, ISaveOptions) | يحول المستند المحرر المحدد ، ويمثل مثيلاً لـ '[`EditableDocument`](../editabledocument) ، إلى المستند الناتج بتنسيق محدد ويحفظ محتواه في stream |
| [Save](../../groupdocs.editor/editor/save#save_1)(EditableDocument, string, ISaveOptions) | يحول المستند المحرر المحدد ، ويمثل مثيلاً لـ '[`EditableDocument`](../editabledocument) ، إلى المستند الناتج بالتنسيق المحدد ويحفظ محتواه في ملف بواسطة مسار الملف المحدد |

## الأحداث

| اسم | وصف |
| --- | --- |
| event [Disposed](../../groupdocs.editor/editor/disposed) | الحدث ، الذي يحدث عندما يتم التخلص من نسخة المحرر هذه بكل مواردها الداخلية |

### ملاحظات

يجب اعتبار فئة المحرر كنقطة إدخال وكائن جذر لـ GroupDocs.Editor. يتم تنفيذ جميع العمليات باستخدام هذه الفئة. الاستخدام النموذجي لفئة Editor لأداء مسار تحرير مستند كامل هو التالي:

1. قم بتحميل مستند إلى مثيل المحرر من خلال المنشئ الخاص به.
2. اختياريًا ، اكتشف نوع مستند باستخدام ملف[`GetDocumentInfo`](./getdocumentinfo) طريقة.
3. افتح مستندًا لتحريره عن طريق استدعاء ملف[`Edit`](./edit)الطريقة والحصول على مثيل[`EditableDocument`](../editabledocument) فئة منه.
4. تحرير محتوى مستند من جانب العميل باستخدام أي محرر WYSIWYG HTML.
5. إنشاء مثيل جديد من[`EditableDocument`](../editabledocument) من محتوى المستند المحرر.
6. حفظ مستند تم تحريره في بعض تنسيقات الإخراج عن طريق استدعاء ملف[`Save`](./save) طريقة.
7. التخلص من مثيل من فئة Editor عبر عامل التشغيل "using" أو يدويًا.

### أنظر أيضا

* interface [IAuxDisposable](../../groupdocs.editor.htmlcss.resources/iauxdisposable)
* مساحة الاسم [GroupDocs.Editor](../../groupdocs.editor)
* المجسم [GroupDocs.Editor](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Editor.dll -->
