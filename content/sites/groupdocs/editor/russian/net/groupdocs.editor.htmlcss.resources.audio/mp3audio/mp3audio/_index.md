---
title: Mp3Audio
second_title: Справочник по API GroupDocs.Editor для .NET
description: Создает новый класс Mp3Audio из содержимого MP3 представленного в виде потока байтов и с указанным именем
type: docs
weight: 10
url: /ru/net/groupdocs.editor.htmlcss.resources.audio/mp3audio/mp3audio/
---
## Mp3Audio constructor

Создает новый класс Mp3Audio из содержимого MP3, представленного в виде потока байтов, и с указанным именем

```csharp
public Mp3Audio(string name, Stream binaryContent)
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| name | String | Название содержимого MP3. Не может быть нулевым, пустым или пробельным. |
| binaryContent | Stream | Контент как поток байтов. Чтение начинается с исходного положения. Не может быть нулевым. Должен быть доступен для чтения и поиска. Если этот экземпляр будет удален, этот поток тоже будет удален. |

### Исключения

| исключение | условие |
| --- | --- |
| ArgumentException |  |

### Смотрите также

* class [Mp3Audio](../../mp3audio)
* пространство имен [GroupDocs.Editor.HtmlCss.Resources.Audio](../../mp3audio)
* сборка [GroupDocs.Editor](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Editor.dll -->
