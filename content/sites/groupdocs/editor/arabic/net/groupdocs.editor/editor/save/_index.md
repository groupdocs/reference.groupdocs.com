---
title: Save
second_title: GroupDocs.Editor لمرجع .NET API
description: يحول المستند المحرر المحدد  ويمثل مثيلاً لـ EditableDocumentgroupdocs.editor/editabledocument  إلى المستند الناتج بتنسيق محدد ويحفظ محتواه في stream
type: docs
weight: 70
url: /ar/net/groupdocs.editor/editor/save/
---
## Save(EditableDocument, Stream, ISaveOptions) {#save}

يحول المستند المحرر المحدد ، ويمثل مثيلاً لـ '[`EditableDocument`](../../editabledocument) ، إلى المستند الناتج بتنسيق محدد ويحفظ محتواه في stream

```csharp
public void Save(EditableDocument inputDocument, Stream outputDocument, ISaveOptions saveOptions)
```

| معامل | يكتب | وصف |
| --- | --- | --- |
| inputDocument | EditableDocument | إصدار مستند الإدخال ، الذي تم تحريره في محرر WYSIWYG HTML ويتم تخزينه كمثيل لـ '[`EditableDocument`](../../editabledocument) class ، والتي يجب تحويلها إلى مستند إخراج بتنسيق معين. يجب ألا يكون باطلاً أو تم التخلص منه. |
| outputDocument | Stream | تيار الإخراج ، حيث سيتم تسجيل محتوى المستند الناتج. يجب ألا يكون باطلاً ، ويجب أن يدعم الكتابة. |
| saveOptions | ISaveOptions | خيارات حفظ المستند ، والتي تحدد تنسيق المستند الناتج ، وكذلك خيارات الحفظ العامة والمتعلقة بالتنسيق. يجب ألا تكون فارغة. |

### ملاحظات

**يتعلم أكثر**

* المزيد حول حفظ المستند بعد التحرير باستخدام GroupDocs.Editor: [كيفية حفظ المستند المحرر باستخدام GroupDocs.Editor](https://docs.groupdocs.com/display/editornet/Save+document)

### أنظر أيضا

* class [EditableDocument](../../editabledocument)
* interface [ISaveOptions](../../../groupdocs.editor.options/isaveoptions)
* class [Editor](../../editor)
* مساحة الاسم [GroupDocs.Editor](../../editor)
* المجسم [GroupDocs.Editor](../../../)

---

## Save(EditableDocument, string, ISaveOptions) {#save_1}

يحول المستند المحرر المحدد ، ويمثل مثيلاً لـ '[`EditableDocument`](../../editabledocument) ، إلى المستند الناتج بالتنسيق المحدد ويحفظ محتواه في ملف بواسطة مسار الملف المحدد

```csharp
public void Save(EditableDocument inputDocument, string filePath, ISaveOptions saveOptions)
```

| معامل | يكتب | وصف |
| --- | --- | --- |
| inputDocument | EditableDocument | إصدار مستند الإدخال ، الذي تم تحريره في محرر WYSIWYG HTML ويتم تخزينه كمثيل لـ '[`EditableDocument`](../../editabledocument) class ، والتي يجب تحويلها إلى مستند إخراج بتنسيق معين. يجب ألا يكون باطلاً أو تم التخلص منه. |
| filePath | String | مسار الملف ، حيث سيتم حفظ المستند الناتج. يوجد ملف يحمل نفس الاسم ، وستتم إعادة كتابته بالكامل. يجب ألا تكون السلسلة ذات المسار فارغة أو فارغة أو تحتوي على مسافات بيضاء فقط. |
| saveOptions | ISaveOptions | خيارات حفظ المستند ، والتي تحدد تنسيق المستند الناتج ، وكذلك خيارات الحفظ العامة والمتعلقة بالتنسيق. يجب ألا تكون فارغة. |

### ملاحظات

**يتعلم أكثر**

* المزيد حول حفظ المستند بعد التحرير باستخدام GroupDocs.Editor: [كيفية حفظ المستند المحرر باستخدام GroupDocs.Editor](https://docs.groupdocs.com/display/editornet/Save+document)

### أنظر أيضا

* class [EditableDocument](../../editabledocument)
* interface [ISaveOptions](../../../groupdocs.editor.options/isaveoptions)
* class [Editor](../../editor)
* مساحة الاسم [GroupDocs.Editor](../../editor)
* المجسم [GroupDocs.Editor](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Editor.dll -->
