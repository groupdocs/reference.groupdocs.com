---
title: FileLogger
second_title: GroupDocs.Mencari Referensi .NET API
description: Merupakan logger yang mencatat peristiwa dan kesalahan ke file lokal.
type: docs
weight: 140
url: /id/net/groupdocs.search.common/filelogger/
---
## FileLogger class

Merupakan logger yang mencatat peristiwa dan kesalahan ke file lokal.

```csharp
public class FileLogger : ILogger
```

## Konstruktor

| Nama | Keterangan |
| --- | --- |
| [FileLogger](filelogger)(string, double) | Menginisialisasi instance baru dari[`FileLogger`](../filelogger) kelas. |

## Properti

| Nama | Keterangan |
| --- | --- |
| [FilePath](../../groupdocs.search.common/filelogger/filepath) { get; } | Mendapat jalur file log. |
| [MaxSize](../../groupdocs.search.common/filelogger/maxsize) { get; } | Mendapat ukuran maksimum file log dalam megabita. |

## Metode

| Nama | Keterangan |
| --- | --- |
| [Error](../../groupdocs.search.common/filelogger/error)(string) | Mencatat kesalahan yang terjadi di indeks. |
| [Trace](../../groupdocs.search.common/filelogger/trace)(string) | Mencatat peristiwa yang terjadi di indeks. |

### Perkataan

**Belajarlah lagi**

* [Penebangan](https://docs.groupdocs.com/display/searchnet/Logging)

### Contoh

Contoh ini menunjukkan penggunaan umum kelas.

```csharp
string indexFolder = @"c:\MyIndex\";
string documentsFolder = @"c:\MyDocuments\";
string query = "Einstein";
string logPath = @"c:\Log.txt";

IndexSettings settings = new IndexSettings();
settings.Logger = new FileLogger(logPath, 4.0); // Menentukan jalur ke file log dan panjang maksimal 4 MB

Index index = new Index(indexFolder, settings); // Membuat indeks di folder yang ditentukan

index.Add(documentsFolder); // Pengindeksan dokumen dari folder yang ditentukan

SearchResult result = index.Search(query); // Cari di index
```

### Lihat juga

* interface [ILogger](../ilogger)
* ruang nama [GroupDocs.Search.Common](../../groupdocs.search.common)
* perakitan [GroupDocs.Search](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Search.dll -->
