---
title: OtfFont
second_title: Справочник по API GroupDocs.Editor для .NET
description: Создает новый класс OtfFont из содержимого представленного в виде строки в кодировке base64 и с указанным именем
type: docs
weight: 10
url: /ru/net/groupdocs.editor.htmlcss.resources.fonts/otffont/otffont/
---
## OtfFont(string, string) {#constructor_1}

Создает новый класс OtfFont из содержимого, представленного в виде строки в кодировке base64, и с указанным именем

```csharp
public OtfFont(string name, string contentInBase64)
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| name | String | Имя шрифта OTF. Не может быть нулевым, пустым или пробельным. |
| contentInBase64 | String | Содержимое в виде строки в кодировке base64. Не может быть нулевым, пустым или пробельным. Если это не содержимое OTF, будет выдано исключение. |

### Исключения

| исключение | условие |
| --- | --- |
| ArgumentException |  |
| [InvalidImageFormatException](../../../groupdocs.editor.htmlcss.exceptions/invalidimageformatexception) |  |

### Смотрите также

* class [OtfFont](../../otffont)
* пространство имен [GroupDocs.Editor.HtmlCss.Resources.Fonts](../../otffont)
* сборка [GroupDocs.Editor](../../../)

---

## OtfFont(string, Stream) {#constructor}

Создает новый класс OtfFont из содержимого, представленного в виде потока байтов, и с указанным именем

```csharp
public OtfFont(string name, Stream binaryContent)
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| name | String | Имя шрифта OTF. Не может быть нулевым, пустым или пробельным. |
| binaryContent | Stream | Контент как поток байтов. Чтение начинается с исходного положения. Не может быть нулевым. Должен быть доступен для чтения и поиска. Если этот экземпляр будет удален, этот поток тоже будет удален. |

### Исключения

| исключение | условие |
| --- | --- |
| ArgumentException |  |
| [InvalidImageFormatException](../../../groupdocs.editor.htmlcss.exceptions/invalidimageformatexception) |  |

### Смотрите также

* class [OtfFont](../../otffont)
* пространство имен [GroupDocs.Editor.HtmlCss.Resources.Fonts](../../otffont)
* сборка [GroupDocs.Editor](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Editor.dll -->