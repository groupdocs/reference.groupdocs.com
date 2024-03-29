---
title: SaveOptions
second_title: Справочник по API GroupDocs.Signature для .NET
description: Позволяет указать дополнительные параметры например пароль при сохранении документа на подпись.
type: docs
weight: 1670
url: /ru/net/groupdocs.signature.options/saveoptions/
---
## SaveOptions class

Позволяет указать дополнительные параметры (например, пароль) при сохранении документа на подпись.

```csharp
public class SaveOptions
```

## Конструкторы

| Имя | Описание |
| --- | --- |
| [SaveOptions](saveoptions#constructor)() | Инициализирует новый экземпляр класса SaveOptions со значениями по умолчанию. |
| [SaveOptions](saveoptions#constructor_1)(bool) | Инициализирует новый экземпляр класса SaveOptions с указанным типом вывода и флагом перезаписи. |

## Характеристики

| Имя | Описание |
| --- | --- |
| [AddMissingExtenstion](../../groupdocs.signature.options/saveoptions/addmissingextenstion) { get; set; } | Получает или устанавливает флаг для автоматического добавления расширения, если оно отсутствовало в выходном файле. path Значение по умолчанию — false. |
| [OverwriteExistingFiles](../../groupdocs.signature.options/saveoptions/overwriteexistingfiles) { get; set; } | Получает или задает, перезаписывать ли существующий файл новым выходным файлом. В противном случае будет создан новый файл с номером в качестве суффикса. По умолчанию для этого значения установлено значение true, что означает, что файл будет перезаписан. |
| [Password](../../groupdocs.signature.options/saveoptions/password) { get; set; } | Получает или задает пароль для сохранения подписанного документа с защитой паролем. Это свойство не поддерживается для документов-изображений. |
| [UseOriginalPassword](../../groupdocs.signature.options/saveoptions/useoriginalpassword) { get; set; } | Получает или задает, следует ли использовать пароль из LoadOptions для сохранения подписанного документа как защищенного. Значение по умолчанию — true. Это свойство не поддерживается для документов-изображений. |

### Смотрите также

* пространство имен [GroupDocs.Signature.Options](../../groupdocs.signature.options)
* сборка [GroupDocs.Signature](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Signature.dll -->
