---
title: AnnotationType
second_title: Справочник по API GroupDocs.Annotation для .NET
description: Перечисление описывающее типы аннотаций поддерживаемые GroupDocs.Annotation for .NET
type: docs
weight: 960
url: /ru/net/groupdocs.annotation.options/annotationtype/
---
## AnnotationType enumeration

Перечисление, описывающее типы аннотаций, поддерживаемые GroupDocs.Annotation for .NET

```csharp
[Flags]
public enum AnnotationType
```

### Ценности

| Имя | Ценность | Описание |
| --- | --- | --- |
| None | `0` | Значение по умолчанию |
| Area | `2` | Тип аннотации области, которая выделяет прямоугольную область на странице документа |
| Arrow | `4` | Тип аннотации, которая рисует стрелку на странице документа |
| Distance | `8` | Тип аннотации, который измеряет расстояние между элементами страницы документа |
| Ellipse | `10` | Аннотация эллиптической формы, обозначающая части содержимого документа |
| Link | `20` | Тип аннотации, представляющий гиперссылку на удаленный ресурс |
| Point | `40` | Точечный тип аннотации, который прикрепляет комментарий к любому месту на странице документа |
| Polyline | `80` | Тип аннотации полилинии, который позволяет добавлять на страницу документа фигуры и линии от руки |
| ResourcesRedaction | `100` | Тип аннотации, который скрывает текстовое содержимое за черным прямоугольником |
| TextField | `200` | Тип аннотации текстового поля представляет собой текстовый комментарий внутри цветной рамки |
| TextHighlight | `400` | Тип аннотации, которая выделяет и комментирует выделенный текст |
| TextRedaction | `800` | Тип аннотации, который заполняет часть выделенного текста черным прямоугольником. |
| TextReplacement | `1000` | Тип аннотации, который заменяет исходный текст другим предоставленным фрагментом текста |
| TextStrikeout | `2000` | Тип аннотации, помечающий фрагмент текста зачеркнутым стилем |
| TextUnderline | `4000` | Тип аннотации, помечающий текст подчеркиванием styling |
| Watermark | `8000` | Тип аннотации, добавляющий текстовый водяной знак поверх страницы документа |
| Image | `10000` | Тип аннотации, добавляющий изображение поверх содержимого страницы документа |
| Dropdown | `20000` | Тип компонента, добавляющий выпадающий компонент для pdf-документа**только** |
| Checkbox | `21000` | Тип аннотации, добавляющий флажок для pdf document |
| Button | `22000` | Тип аннотации, добавляющий кнопку для pdf document |
| TextSquiggly | `2500` | Тип аннотации, в которой волнистые линии и комментарии выделены text |
| SearchText | `2700` | Тип аннотации для поиска текста фрагмента в документе |
| All | `7FFFFFFF` | Все |

### Примечания

**Узнать больше**

* [Как аннотировать документы в C#](https://docs.groupdocs.com/display/annotationnet/Add+annotation+to+the+document)
* [Как добавить аннотации области в C#](https://docs.groupdocs.com/display/annotationnet/Add+area+annotation)
* [Как добавить аннотации со стрелками в C#](https://docs.groupdocs.com/display/annotationnet/Add+arrow+annotation)
* [Как добавить аннотации расстояния в C#](https://docs.groupdocs.com/display/annotationnet/Add+distance+annotation)
* [Как добавить аннотации эллипса в C#](https://docs.groupdocs.com/display/annotationnet/Add+ellipse+annotation)
* [Как добавить аннотации к ссылкам в C#](https://docs.groupdocs.com/display/annotationnet/Add+link+annotation)
* [Как добавить точечные аннотации в C#](https://docs.groupdocs.com/display/annotationnet/Add+point+annotation)
* [Как добавить полилинейные аннотации в C#](https://docs.groupdocs.com/display/annotationnet/Add+polyline+annotation)
* [Как добавить аннотации редактирования ресурсов в C#](https://docs.groupdocs.com/display/annotationnet/Add+resource+redaction+annotation)
* [Как добавить аннотации к текстовым полям в C#](https://docs.groupdocs.com/display/annotationnet/Add+text+field+annotation)
* [Как добавить аннотации выделения в C#](https://docs.groupdocs.com/display/annotationnet/Add+highlight+annotation)
* [Как добавить аннотации редактирования текста в C#](https://docs.groupdocs.com/display/annotationnet/Add+text+redaction+annotation)
* [Как добавить замещающие аннотации в C#](https://docs.groupdocs.com/display/annotationnet/Add+replacement+annotation)
* [Как добавить зачеркнутые аннотации в C#](https://docs.groupdocs.com/display/annotationnet/Add+strikeout+annotation)
* [Как добавить аннотации подчеркивания в C#](https://docs.groupdocs.com/display/annotationnet/Add+underline+annotation)
* [Как добавить аннотации водяных знаков в C#](https://docs.groupdocs.com/display/annotationnet/Add+watermark+annotation)
* [Как добавить аннотации к изображениям в C#](https://docs.groupdocs.com/display/annotationnet/Add+image+annotation)

### Смотрите также

* пространство имен [GroupDocs.Annotation.Options](../../groupdocs.annotation.options)
* сборка [GroupDocs.Annotation](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Annotation.dll -->
