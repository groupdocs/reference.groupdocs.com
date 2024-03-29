---
title: CreateRenameNotification
second_title: GroupDocs.Mencari Referensi .NET API
description: Membuat objek pemberitahuan untuk mengubah nama dokumen yang diindeks yang telah diubah namanya dan tidak perlu diindeks ulang. Dokumen yang diubah namanya tidak akan diindeks ulang selama operasi pembaruan berikutnya bahkan jika isinya telah diubah.
type: docs
weight: 10
url: /id/net/groupdocs.search.common/notification/createrenamenotification/
---
## Notification.CreateRenameNotification method

Membuat objek pemberitahuan untuk mengubah nama dokumen yang diindeks yang telah diubah namanya dan tidak perlu diindeks ulang. Dokumen yang diubah namanya tidak akan diindeks ulang selama operasi pembaruan berikutnya, bahkan jika isinya telah diubah.

```csharp
public static Notification CreateRenameNotification(string oldPath, string newPath)
```

| Parameter | Jenis | Keterangan |
| --- | --- | --- |
| oldPath | String | Jalur lama ke dokumen yang diindeks. |
| newPath | String | Jalur baru ke dokumen yang diindeks. |

### Nilai Pengembalian

Objek pemberitahuan ganti nama baru.

### Lihat juga

* class [Notification](../../notification)
* ruang nama [GroupDocs.Search.Common](../../notification)
* perakitan [GroupDocs.Search](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Search.dll -->
