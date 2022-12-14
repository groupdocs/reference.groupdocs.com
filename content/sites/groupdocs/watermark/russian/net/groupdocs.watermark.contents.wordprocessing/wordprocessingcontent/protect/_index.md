---
title: Protect
second_title: Справочник по API GroupDocs.Watermark для .NET
description: Защищает документ от изменений и устанавливает пароль защиты.
type: docs
weight: 50
url: /ru/net/groupdocs.watermark.contents.wordprocessing/wordprocessingcontent/protect/
---
## WordProcessingContent.Protect method

Защищает документ от изменений и устанавливает пароль защиты.

```csharp
public void Protect(WordProcessingProtectionType protectionType, string password)
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| protectionType | WordProcessingProtectionType | Указывает тип защиты документа. |
| password | String | Пароль для защиты документа. |

### Примечания

Чтобы содержимое документа можно было редактировать, используйте соответствующий метод добавления водяного знака с помощью AllowOnlyFormFields или ReadOnlyWithEditableContent параметр.

### Смотрите также

* enum [WordProcessingProtectionType](../../wordprocessingprotectiontype)
* class [WordProcessingContent](../../wordprocessingcontent)
* пространство имен [GroupDocs.Watermark.Contents.WordProcessing](../../wordprocessingcontent)
* сборка [GroupDocs.Watermark](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Watermark.dll -->
