---
title: PdfViewOptions
second_title: Справочник по API GroupDocs.Viewer для .NET
description: Инициализирует новый экземплярPdfViewOptionsgroupdocs.viewer.options/pdfviewoptions класс.
type: docs
weight: 10
url: /ru/net/groupdocs.viewer.options/pdfviewoptions/pdfviewoptions/
---
## PdfViewOptions(CreateFileStream) {#constructor_1}

Инициализирует новый экземпляр[`PdfViewOptions`](../../pdfviewoptions) класс.

```csharp
public PdfViewOptions(CreateFileStream createFileStream)
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| createFileStream | CreateFileStream | Метод, создающий экземпляр потока, используемый для записи данных выходного файла. |

### Исключения

| исключение | условие |
| --- | --- |
| ArgumentNullException | Брошен, когда*createFileStream* нулевой. |

### Смотрите также

* delegate [CreateFileStream](../../../groupdocs.viewer.interfaces/createfilestream)
* class [PdfViewOptions](../../pdfviewoptions)
* пространство имен [GroupDocs.Viewer.Options](../../pdfviewoptions)
* сборка [GroupDocs.Viewer](../../../)

---

## PdfViewOptions(CreateFileStream, ReleaseFileStream) {#constructor_2}

Инициализирует новый экземпляр[`PdfViewOptions`](../../pdfviewoptions) класс.

```csharp
public PdfViewOptions(CreateFileStream createFileStream, ReleaseFileStream releaseFileStream)
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| createFileStream | CreateFileStream | Метод, создающий экземпляр потока, используемый для записи данных выходного файла. |
| releaseFileStream | ReleaseFileStream | Метод, который освобождает поток, созданный методом, назначенным делегату, переданному в*createFileStream* параметр. |

### Исключения

| исключение | условие |
| --- | --- |
| ArgumentNullException | Брошен, когда*createFileStream* нулевой. |
| ArgumentNullException | Брошен, когда*releaseFileStream* нулевой. |

### Смотрите также

* delegate [CreateFileStream](../../../groupdocs.viewer.interfaces/createfilestream)
* delegate [ReleaseFileStream](../../../groupdocs.viewer.interfaces/releasefilestream)
* class [PdfViewOptions](../../pdfviewoptions)
* пространство имен [GroupDocs.Viewer.Options](../../pdfviewoptions)
* сборка [GroupDocs.Viewer](../../../)

---

## PdfViewOptions(IFileStreamFactory) {#constructor_3}

Инициализирует новый экземпляр[`PdfViewOptions`](../../pdfviewoptions) класс.

```csharp
public PdfViewOptions(IFileStreamFactory fileStreamFactory)
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| fileStreamFactory | IFileStreamFactory | Фабрика, реализующая методы создания и выпуска выходного файлового потока. |

### Исключения

| исключение | условие |
| --- | --- |
| ArgumentNullException | Брошен, когда*fileStreamFactory* нулевой. |

### Смотрите также

* interface [IFileStreamFactory](../../../groupdocs.viewer.interfaces/ifilestreamfactory)
* class [PdfViewOptions](../../pdfviewoptions)
* пространство имен [GroupDocs.Viewer.Options](../../pdfviewoptions)
* сборка [GroupDocs.Viewer](../../../)

---

## PdfViewOptions() {#constructor}

Инициализирует новый экземпляр[`PdfViewOptions`](../../pdfviewoptions) класс.

```csharp
public PdfViewOptions()
```

### Примечания

Этот конструктор инициализирует новый экземпляр[`PdfViewOptions`](../../pdfviewoptions) с "output.pdf" в качестве формата пути к выходному файлу. Выходной файл будет помещен в текущий рабочий каталог приложения.

### Смотрите также

* class [PdfViewOptions](../../pdfviewoptions)
* пространство имен [GroupDocs.Viewer.Options](../../pdfviewoptions)
* сборка [GroupDocs.Viewer](../../../)

---

## PdfViewOptions(string) {#constructor_4}

Инициализирует новый экземпляр[`PdfViewOptions`](../../pdfviewoptions) класс.

```csharp
public PdfViewOptions(string outputFilePath)
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| outputFilePath | String | Путь для выходного файла PDF. |

### Исключения

| исключение | условие |
| --- | --- |
| ArgumentException | Брошен, когда*outputFilePath* является нулевым или пустым. |

### Смотрите также

* class [PdfViewOptions](../../pdfviewoptions)
* пространство имен [GroupDocs.Viewer.Options](../../pdfviewoptions)
* сборка [GroupDocs.Viewer](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Viewer.dll -->