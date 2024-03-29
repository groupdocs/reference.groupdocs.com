---
title: ReplaceInColumn
second_title: GroupDocs.Redaction untuk Referensi .NET API
description: Menggantikan semua kecocokan dengan pengganti yang diberikan di kolom dan lembar kerja yang ditentukan.
type: docs
weight: 20
url: /id/net/groupdocs.redaction.integration/icellularformatinstance/replaceincolumn/
---
## ReplaceInColumn(Regex, string, int, int) {#replaceincolumn_1}

Menggantikan semua kecocokan dengan pengganti yang diberikan di kolom dan lembar kerja yang ditentukan.

```csharp
public RedactionResult ReplaceInColumn(Regex regularExpression, string replacement, int column, 
    int sheet)
```

| Parameter | Jenis | Keterangan |
| --- | --- | --- |
| regularExpression | Regex | Ekspresi reguler untuk mencari dan mengganti |
| replacement | String | Penggantian tekstual |
| column | Int32 | Indeks kolom berbasis nol |
| sheet | Int32 | Indeks lembar kerja berbasis nol |

### Nilai Pengembalian

Hasil penggantian

### Lihat juga

* class [RedactionResult](../../../groupdocs.redaction/redactionresult)
* interface [ICellularFormatInstance](../../icellularformatinstance)
* ruang nama [GroupDocs.Redaction.Integration](../../icellularformatinstance)
* perakitan [GroupDocs.Redaction](../../../)

---

## ReplaceInColumn(Regex, string, int) {#replaceincolumn}

Menggantikan semua kecocokan dengan pengganti yang diberikan pada kolom yang ditentukan pada semua lembar kerja.

```csharp
public RedactionResult ReplaceInColumn(Regex regularExpression, string replacement, int column)
```

| Parameter | Jenis | Keterangan |
| --- | --- | --- |
| regularExpression | Regex | Ekspresi reguler untuk mencari dan mengganti |
| replacement | String | Penggantian tekstual |
| column | Int32 | Indeks kolom berbasis nol |

### Nilai Pengembalian

Hasil penggantian

### Lihat juga

* class [RedactionResult](../../../groupdocs.redaction/redactionresult)
* interface [ICellularFormatInstance](../../icellularformatinstance)
* ruang nama [GroupDocs.Redaction.Integration](../../icellularformatinstance)
* perakitan [GroupDocs.Redaction](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Redaction.dll -->
