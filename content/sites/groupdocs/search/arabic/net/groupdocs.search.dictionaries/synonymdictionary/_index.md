---
title: SynonymDictionary
second_title: GroupDocs. ابحث عن مرجع .NET API
description: يمثل قاموس المرادفات.
type: docs
weight: 490
url: /ar/net/groupdocs.search.dictionaries/synonymdictionary/
---
## SynonymDictionary class

يمثل قاموس المرادفات.

```csharp
public class SynonymDictionary : DictionaryBase, IEnumerable<string>
```

## الخصائص

| اسم | وصف |
| --- | --- |
| [Count](../../groupdocs.search.dictionaries/synonymdictionary/count) { get; } | الحصول على عدد الكلمات الموجودة في هذا[`SynonymDictionary`](../synonymdictionary) . |

## طُرق

| اسم | وصف |
| --- | --- |
| [AddRange](../../groupdocs.search.dictionaries/synonymdictionary/addrange#addrange)(IEnumerable&lt;string[]&gt;) | إضافة المجموعة المحددة من مجموعات المرادفات إلى نسخة ملف[`SynonymDictionary`](../synonymdictionary) . |
| [AddRange](../../groupdocs.search.dictionaries/synonymdictionary/addrange#addrange_1)(string[][]) | إضافة المجموعة المحددة من مجموعات المرادفات إلى نسخة ملف[`SynonymDictionary`](../synonymdictionary) . |
| [Clear](../../groupdocs.search.dictionaries/synonymdictionary/clear)() | يزيل كل الكلمات من هذا[`SynonymDictionary`](../synonymdictionary) الكائن . |
| [ExportDictionary](../../groupdocs.search.dictionaries/dictionarybase/exportdictionary)(string) | يصدر القاموس إلى ملف بالاسم المحدد. |
| [GetAllSynonymGroups](../../groupdocs.search.dictionaries/synonymdictionary/getallsynonymgroups)() | يحصل على كافة مجموعات المرادفات الموجودة في هذا القاموس. |
| [GetEnumerator](../../groupdocs.search.dictionaries/synonymdictionary/getenumerator)() | إرجاع عداد يتكرر خلال المجموعة. |
| [GetSynonymGroups](../../groupdocs.search.dictionaries/synonymdictionary/getsynonymgroups)(string) | يحصل على كافة مجموعات المرادفات التي تنتمي إليها الكلمة المحددة. |
| [GetSynonyms](../../groupdocs.search.dictionaries/synonymdictionary/getsynonyms)(string) | يحصل على مرادفات الكلمة المحددة. المصفوفة الناتجة لا تحتوي على الكلمة الأصلية. |
| [ImportDictionary](../../groupdocs.search.dictionaries/dictionarybase/importdictionary)(string) | لاستيراد قاموس من الملف المحدد. |

### ملاحظات

**يتعلم أكثر**

* [البحث عن المرادفات](https://docs.groupdocs.com/display/searchnet/Synonym+search)
* [إدارة قاموس المرادفات](https://docs.groupdocs.com/display/searchnet/Synonym+dictionary)

### أنظر أيضا

* class [DictionaryBase](../dictionarybase)
* مساحة الاسم [GroupDocs.Search.Dictionaries](../../groupdocs.search.dictionaries)
* المجسم [GroupDocs.Search](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Search.dll -->
