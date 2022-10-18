---
title: Attachment
second_title: Справочник по API GroupDocs.Viewer для .NET
description: Инициализирует новый экземплярAttachmentgroupdocs.viewer.results/attachment класс.
type: docs
weight: 10
url: /ru/net/groupdocs.viewer.results/attachment/attachment/
---
## Attachment(string, string) {#constructor}

Инициализирует новый экземпляр[`Attachment`](../../attachment) класс.

```csharp
public Attachment(string fileName, string filePath)
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| fileName | String | Имя файла вложения. |
| filePath | String | Относительный путь вложения, напримерпапка/файл.docxили имя файла, если файл находится в корне архива, в сообщении электронной почты или в файле данных. |

### Исключения

| исключение | условие |
| --- | --- |
| ArgumentException | Брошен, когда*fileName* является нулевым или пустым. |
| ArgumentException | Брошен, когда*filePath* является нулевым или пустым. |

### Смотрите также

* class [Attachment](../../attachment)
* пространство имен [GroupDocs.Viewer.Results](../../attachment)
* сборка [GroupDocs.Viewer](../../../)

---

## Attachment(string, string, string, long) {#constructor_2}

Инициализирует новый экземпляр[`Attachment`](../../attachment) класс.

```csharp
public Attachment(string id, string fileName, string filePath, long size)
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| id | String | Уникальный (в контексте одного файла) идентификатор вложения. |
| fileName | String | Имя файла вложения. |
| filePath | String | Относительный путь вложения, напримерпапка/файл.docxили имя файла, если файл находится в корне архива, в сообщении электронной почты или в файле данных. |
| size | Int64 | Размер вложенного файла в байтах. |

### Исключения

| исключение | условие |
| --- | --- |
| ArgumentException | Брошен, когда*id* является нулевым или пустым. |
| ArgumentException | Брошен, когда*fileName* является нулевым или пустым. |
| ArgumentException | Брошен, когда*filePath* является нулевым или пустым. |

### Смотрите также

* class [Attachment](../../attachment)
* пространство имен [GroupDocs.Viewer.Results](../../attachment)
* сборка [GroupDocs.Viewer](../../../)

---

## Attachment(string, string, string, FileType, long) {#constructor_1}

Инициализирует новый экземпляр[`Attachment`](../../attachment) класс.

```csharp
public Attachment(string id, string fileName, string filePath, FileType fileType, long size)
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| id | String | Уникальный (в контексте одного файла) идентификатор вложения. |
| fileName | String | Имя файла вложения. |
| filePath | String | Относительный путь вложения, напримерпапка/файл.docxили имя файла, если файл находится в корне архива, в сообщении электронной почты или в файле данных. |
| fileType | FileType | Тип файла вложения. |
| size | Int64 | Размер вложенного файла в байтах. |

### Исключения

| исключение | условие |
| --- | --- |
| ArgumentException | Брошен, когда*id* является нулевым или пустым. |
| ArgumentException | Брошен, когда*fileName* является нулевым или пустым. |
| ArgumentException | Брошен, когда*filePath* является нулевым или пустым. |
| ArgumentNullException | Брошен, когда*fileType* нулевой. |

### Смотрите также

* class [FileType](../../../groupdocs.viewer/filetype)
* class [Attachment](../../attachment)
* пространство имен [GroupDocs.Viewer.Results](../../attachment)
* сборка [GroupDocs.Viewer](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Viewer.dll -->