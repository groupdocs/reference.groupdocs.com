---
title: ReleaseSplitStream
second_title: GroupDocs.Merger untuk Referensi .NET API
description: Delegasi yang menentukan metode untuk merilis aliran pemisahan output.
type: docs
weight: 90
url: /id/net/groupdocs.merger.domain.common/releasesplitstream/
---
## ReleaseSplitStream delegate

Delegasi yang menentukan metode untuk merilis aliran pemisahan output.

```csharp
public delegate void ReleaseSplitStream(int number, Stream createSplitStream);
```

| Parameter | Jenis | Keterangan |
| --- | --- | --- |
| number | Int32 | Nomor halaman atau baris yang digunakan untuk pemisahan dokumen. |
| createSplitStream | Stream | Aliran yang dibuat oleh*createSplitStream* metode. |

### Lihat juga

* ruang nama [GroupDocs.Merger.Domain.Common](../../groupdocs.merger.domain.common)
* perakitan [GroupDocs.Merger](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Merger.dll -->
