---
title: InsertAsNewSlide
second_title: Справочник по API GroupDocs.Editor для .NET
description: Булев флаг указывающий должен ли отредактированный слайд заменить существующий слайд в исходной презентации на позиции указанной параметромSlideNumbergroupdocs.editor.options/presentationsaveoptions/slidenumber свойство либо оно должно быть вставлено между существующим слайдом и предыдущим не заменяя его содержимое. По умолчанию false  существующий слайд будет заменен. Это свойство игнорируется если значениеSlideNumbergroupdocs.editor.options/presentationsaveoptions/slidenumber свойство установлено в 0.
type: docs
weight: 20
url: /ru/net/groupdocs.editor.options/presentationsaveoptions/insertasnewslide/
---
## PresentationSaveOptions.InsertAsNewSlide property

Булев флаг, указывающий, должен ли отредактированный слайд заменить существующий слайд в исходной презентации на позиции, указанной параметром[`SlideNumber`](../slidenumber) свойство, либо оно должно быть вставлено между существующим слайдом и предыдущим, не заменяя его содержимое. По умолчанию false — существующий слайд будет заменен. Это свойство игнорируется, если значение[`SlideNumber`](../slidenumber) свойство установлено в '0'.

```csharp
public bool InsertAsNewSlide { get; set; }
```

### Примечания

По умолчанию слайд заменен. Это означает, что если данная презентация состоит из 5 слайдов и[`SlideNumber`](../slidenumber) =4, то 4-й слайд будет заменен новым отредактированным слайдом, а общее количество слайдов в презентации (5) останется нетронутым. Однако, если значение этого свойства установлено равнымистинный, новый отредактированный слайд будет введен как 4-й слайд, а все последующие слайды будут сдвинуты в конец: «старый» 4-й слайд станет 5-м, а 5-й станет 6-м, а общее количество слайдов в презентации будет увеличено на один и равно 6.

### Смотрите также

* class [PresentationSaveOptions](../../presentationsaveoptions)
* пространство имен [GroupDocs.Editor.Options](../../presentationsaveoptions)
* сборка [GroupDocs.Editor](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Editor.dll -->
