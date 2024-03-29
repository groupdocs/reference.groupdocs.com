---
title: FromStream
second_title: Справочник по API GroupDocs.Viewer для .NET
description: Определяет тип файла читая подпись файла.
type: docs
weight: 1950
url: /ru/net/groupdocs.viewer/filetype/fromstream/
---
## FromStream(Stream) {#fromstream}

Определяет тип файла, читая подпись файла.

```csharp
public static FileType FromStream(Stream stream)
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| stream | Stream | Файловый поток. |

### Смотрите также

* class [FileType](../../filetype)
* пространство имен [GroupDocs.Viewer](../../filetype)
* сборка [GroupDocs.Viewer](../../../)

---

## FromStream(Stream, string) {#fromstream_2}

Определяет тип файла, читая подпись файла.

```csharp
public static FileType FromStream(Stream stream, string password)
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| stream | Stream | Файловый поток. |
| password | String | Пароль для открытия файла. |

### Смотрите также

* class [FileType](../../filetype)
* пространство имен [GroupDocs.Viewer](../../filetype)
* сборка [GroupDocs.Viewer](../../../)

---

## FromStream(Stream, ILogger) {#fromstream_1}

Определяет тип файла, читая подпись файла.

```csharp
public static FileType FromStream(Stream stream, ILogger logger)
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| stream | Stream | Файловый поток. |
| logger | ILogger | Регистратор. |

### Возвращаемое значение

Возвращает тип файла, если он был успешно обнаружен, в противном случае возвращает значение по умолчанию.[`Unknown`](../unknown) тип файла.

### Смотрите также

* interface [ILogger](../../../groupdocs.viewer.logging/ilogger)
* class [FileType](../../filetype)
* пространство имен [GroupDocs.Viewer](../../filetype)
* сборка [GroupDocs.Viewer](../../../)

---

## FromStream(Stream, string, ILogger) {#fromstream_3}

Определяет тип файла, читая подпись файла.

```csharp
public static FileType FromStream(Stream stream, string password, ILogger logger)
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| stream | Stream | Файловый поток. |
| password | String | Пароль для открытия файла. |
| logger | ILogger | Регистратор. |

### Возвращаемое значение

Возвращает тип файла, если он был успешно обнаружен, в противном случае возвращает значение по умолчанию.[`Unknown`](../unknown) тип файла.

### Смотрите также

* interface [ILogger](../../../groupdocs.viewer.logging/ilogger)
* class [FileType](../../filetype)
* пространство имен [GroupDocs.Viewer](../../filetype)
* сборка [GroupDocs.Viewer](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Viewer.dll -->
