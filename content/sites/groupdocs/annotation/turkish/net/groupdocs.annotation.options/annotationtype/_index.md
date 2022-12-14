---
title: AnnotationType
second_title: .NET API Başvurusu için GroupDocs.Annotation
description: GroupDocs tarafından desteklenen ek açıklama türlerini açıklayan numaralandırma. .NET için Annotation
type: docs
weight: 950
url: /tr/net/groupdocs.annotation.options/annotationtype/
---
## AnnotationType enumeration

GroupDocs tarafından desteklenen ek açıklama türlerini açıklayan numaralandırma. .NET için Annotation

```csharp
[Flags]
public enum AnnotationType
```

### değerler

| İsim | Değer | Tanım |
| --- | --- | --- |
| None | `0` | Varsayılan değer |
| Area | `2` | Belge page içindeki dikdörtgen alanı vurgulayan alan açıklama türü |
| Arrow | `4` | Belgeye ok çizen ek açıklama türü page |
| Distance | `8` | Bir belgenin öğeleri arasındaki mesafeyi ölçen ek açıklama türü page |
| Ellipse | `10` | Belge içeriğinin bölümlerini işaretleyen eliptik formun notu |
| Link | `20` | Uzak bir kaynağa bir köprüyü temsil eden açıklama türü |
| Point | `40` | Bir yorumu belge page içindeki herhangi bir yere yapıştıran nokta açıklama türü |
| Polyline | `80` | Bir belgeye çizim şekilleri ve serbest çizgiler eklemeye izin veren çoklu çizgi ek açıklama türü page |
| ResourcesRedaction | `100` | Metin içeriğini siyah dikdörtgenin arkasına gizleyen ek açıklama türü |
| TextField | `200` | Metin alanı açıklama türü, renkli çerçeve içindeki metinsel yorumu temsil eder |
| TextHighlight | `400` | Seçilenleri vurgulayan ve yorumlayan ek açıklama türü text |
| TextRedaction | `800` | Seçili metnin bir bölümünü siyah dikdörtgenle dolduran ek açıklama türü. |
| TextReplacement | `1000` | Orijinal metni sağlanan diğer metin parçasıyla değiştiren ek açıklama türü |
| TextStrikeout | `2000` | Metin parçasını üstü çizili stil ile işaretleyen ek açıklama türü |
| TextUnderline | `4000` | Metni altı çizili stille işaretleyen ek açıklama türü |
| Watermark | `8000` | Belge sayfası üzerine metinsel filigran ekleyen ek açıklama türü |
| Image | `10000` | Belge sayfası üzerine görüntü kaplaması ekleyen ek açıklama türü content |
| Dropdown | `20000` | pdf belgesi için açılır bileşen ekleyen bileşen türü**sadece** |
| Checkbox | `21000` |  |
| Button | `22000` |  |
| TextSquiggly | `2500` | Seçili dalgalı ve yorum yapan ek açıklama türü text |
| SearchText | `2700` | Document içindeki parça metnini arayan ek açıklama türü |
| All | `7FFFFFFF` | Hepsi |

### Notlar

**Daha fazla bilgi edin**

* [C# belgelerine açıklama ekleme](https://docs.groupdocs.com/display/annotationnet/Add+annotation+to+the+document)
* [C#'da alan açıklamaları nasıl eklenir](https://docs.groupdocs.com/display/annotationnet/Add+area+annotation)
* [C#'ta ok ek açıklamaları nasıl eklenir?](https://docs.groupdocs.com/display/annotationnet/Add+arrow+annotation)
* [C#'ta mesafe ek açıklamaları nasıl eklenir?](https://docs.groupdocs.com/display/annotationnet/Add+distance+annotation)
* [C#'da elips ek açıklamaları nasıl eklenir](https://docs.groupdocs.com/display/annotationnet/Add+ellipse+annotation)
* [C#'ta bağlantı ek açıklamaları nasıl eklenir?](https://docs.groupdocs.com/display/annotationnet/Add+link+annotation)
* [C#'ta nokta ek açıklamaları nasıl eklenir?](https://docs.groupdocs.com/display/annotationnet/Add+point+annotation)
* [C#'da çoklu çizgi ek açıklamaları nasıl eklenir](https://docs.groupdocs.com/display/annotationnet/Add+polyline+annotation)
* [C#'ta kaynak redaksiyon ek açıklamaları nasıl eklenir?](https://docs.groupdocs.com/display/annotationnet/Add+resource+redaction+annotation)
* [C# metin alanı ek açıklamaları nasıl eklenir](https://docs.groupdocs.com/display/annotationnet/Add+text+field+annotation)
* [C#'da vurgu açıklamaları nasıl eklenir](https://docs.groupdocs.com/display/annotationnet/Add+highlight+annotation)
* [C# metin redaksiyon ek açıklamaları nasıl eklenir](https://docs.groupdocs.com/display/annotationnet/Add+text+redaction+annotation)
* [C#'da değiştirme açıklamaları nasıl eklenir](https://docs.groupdocs.com/display/annotationnet/Add+replacement+annotation)
* [C#'ta üstü çizili notlar nasıl eklenir?](https://docs.groupdocs.com/display/annotationnet/Add+strikeout+annotation)
* [C#'ta altı çizili açıklamalar nasıl eklenir?](https://docs.groupdocs.com/display/annotationnet/Add+underline+annotation)
* [C#'ta filigran ek açıklamaları nasıl eklenir?](https://docs.groupdocs.com/display/annotationnet/Add+watermark+annotation)
* [C#'ta görüntü ek açıklamaları nasıl eklenir?](https://docs.groupdocs.com/display/annotationnet/Add+image+annotation)

### Ayrıca bakınız

* ad alanı [GroupDocs.Annotation.Options](../../groupdocs.annotation.options)
* toplantı [GroupDocs.Annotation](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Annotation.dll -->
