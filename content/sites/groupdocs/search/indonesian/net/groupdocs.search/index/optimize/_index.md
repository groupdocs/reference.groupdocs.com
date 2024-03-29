---
title: Optimize
second_title: GroupDocs.Mencari Referensi .NET API
description: Meminimalkan jumlah segmen indeks dengan menggabungkannya satu sama lain. Operasi ini meningkatkan kinerja pencarian.
type: docs
weight: 210
url: /id/net/groupdocs.search/index/optimize/
---
## Optimize() {#optimize}

Meminimalkan jumlah segmen indeks dengan menggabungkannya satu sama lain. Operasi ini meningkatkan kinerja pencarian.

```csharp
public void Optimize()
```

### Contoh

Contoh menunjukkan cara menggabungkan segmen indeks.

```csharp
string indexFolder = @"c:\MyIndex\";
string documentsFolder1 = @"c:\MyDocuments1\";
string documentsFolder2 = @"c:\MyDocuments2\";
string documentsFolder3 = @"c:\MyDocuments3\";

Index index = new Index(indexFolder); // Membuat indeks di folder yang ditentukan

index.Add(documentsFolder1); // Pengindeksan dokumen dari folder yang ditentukan
index.Add(documentsFolder2); // Setiap panggilan ke Tambah membuat setidaknya satu segmen baru dalam indeks
index.Add(documentsFolder3);

// Menggabungkan segmen indeks
index.Optimize();
```

### Lihat juga

* class [Index](../../index)
* ruang nama [GroupDocs.Search](../../index)
* perakitan [GroupDocs.Search](../../../)

---

## Optimize(MergeOptions) {#optimize_1}

Meminimalkan jumlah segmen indeks dengan menggabungkannya satu sama lain. Operasi ini meningkatkan kinerja pencarian.

```csharp
public void Optimize(MergeOptions options)
```

| Parameter | Jenis | Keterangan |
| --- | --- | --- |
| options | MergeOptions | Opsi penggabungan. |

### Contoh

Contoh menunjukkan cara menggabungkan segmen indeks dengan opsi penggabungan tertentu.

```csharp
string indexFolder = @"c:\MyIndex\";
string documentsFolder1 = @"c:\MyDocuments1\";
string documentsFolder2 = @"c:\MyDocuments2\";
string documentsFolder3 = @"c:\MyDocuments3\";

Index index = new Index(indexFolder); // Membuat indeks di folder yang ditentukan

index.Add(documentsFolder1); // Pengindeksan dokumen dari folder yang ditentukan
index.Add(documentsFolder2); // Setiap panggilan ke Tambah membuat setidaknya satu segmen baru dalam indeks
index.Add(documentsFolder3);

MergeOptions options = new MergeOptions();
options.IsAsync = true; // Operasi asinkron
options.Cancellation = new Cancellation(); // Membuat objek pembatalan

// Menggabungkan segmen indeks
index.Optimize(options); // Metode ini akan kembali sebelum operasi selesai

options.Cancellation.CancelAfter(10000); // Mengatur durasi maksimum operasi menjadi 10 detik
```

### Lihat juga

* class [MergeOptions](../../../groupdocs.search.options/mergeoptions)
* class [Index](../../index)
* ruang nama [GroupDocs.Search](../../index)
* perakitan [GroupDocs.Search](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Search.dll -->
