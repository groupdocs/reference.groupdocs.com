---
title: Permissions
second_title: .NET API Başvurusu için GroupDocs.Viewer
description: PDF belge izinlerini tanımlar.
type: docs
weight: 430
url: /tr/net/groupdocs.viewer.options/permissions/
---
## Permissions enumeration

PDF belge izinlerini tanımlar.

```csharp
[Flags]
public enum Permissions
```

### değerler

| İsim | Değer | Tanım |
| --- | --- | --- |
| AllowAll | `0` | Yazdırmaya, değiştirmeye ve veri çıkarmaya izin ver. |
| DenyPrinting | `1` | Yazdırmayı reddet |
| DenyModification | `2` | İçeriği değiştirmeyi, formları doldurmayı, açıklamalar eklemeyi veya değiştirmeyi reddet. |
| DenyDataExtraction | `4` | Metin ve grafik çıkartmayı reddet. |
| DenyAll | `7` | Yazdırmayı, değiştirmeyi ve veri çıkarmayı reddet. |

### Ayrıca bakınız

* ad alanı [GroupDocs.Viewer.Options](../../groupdocs.viewer.options)
* toplantı [GroupDocs.Viewer](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Viewer.dll -->
