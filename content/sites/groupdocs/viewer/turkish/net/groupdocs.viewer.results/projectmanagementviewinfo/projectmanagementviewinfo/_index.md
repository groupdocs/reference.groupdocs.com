---
title: ProjectManagementViewInfo
second_title: .NET API Başvurusu için GroupDocs.Viewer
description: Yeni örneğini başlatırProjectManagementViewInfogroupdocs.viewer.results/projectmanagementviewinfo sınıf.
type: docs
weight: 10
url: /tr/net/groupdocs.viewer.results/projectmanagementviewinfo/projectmanagementviewinfo/
---
## ProjectManagementViewInfo constructor

Yeni örneğini başlatır[`ProjectManagementViewInfo`](../../projectmanagementviewinfo) sınıf.

```csharp
public ProjectManagementViewInfo(FileType fileType, IList<Page> pages, DateTime startDate, 
    DateTime endDate)
```

| Parametre | Tip | Tanım |
| --- | --- | --- |
| fileType | FileType | Dosyanın türü. |
| pages | IList`1 | Görüntülenecek sayfaların listesi. |
| startDate | DateTime | Projenin başladığı tarih saat. |
| endDate | DateTime | Projenin tamamlanacağı tarih saat. |

### istisnalar

| istisna | şart |
| --- | --- |
| ArgumentNullException | ne zaman atıldı*fileType* boş. |
| ArgumentNullException | ne zaman atıldı*pages* boş. |

### Ayrıca bakınız

* class [FileType](../../../groupdocs.viewer/filetype)
* class [Page](../../page)
* class [ProjectManagementViewInfo](../../projectmanagementviewinfo)
* ad alanı [GroupDocs.Viewer.Results](../../projectmanagementviewinfo)
* toplantı [GroupDocs.Viewer](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Viewer.dll -->
