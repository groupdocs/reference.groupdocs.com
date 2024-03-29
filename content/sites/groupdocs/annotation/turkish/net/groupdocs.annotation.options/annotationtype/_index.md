---
title: AnnotationType
second_title: .NET API Başvurusu için GroupDocs.Annotation
description: GroupDocs tarafından desteklenen ek açıklama türlerini açıklayan numaralandırma. .NET için Annotation
type: docs
weight: 960
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
| Link | `20` | Uzak bir kaynağa köprüyü temsil eden ek açıklama türü |
| Point | `40` | Belgede herhangi bir yere yorum yapıştıran nokta açıklama türü page |
| Polyline | `80` | Bir belgeye çizim şekilleri ve serbest çizgiler eklenmesine izin veren çoklu çizgi açıklama türü page |
| ResourcesRedaction | `100` | Metin içeriğini siyah dikdörtgenin arkasına gizleyen ek açıklama türü |
| TextField | `200` | Metin alanı açıklama tipi, renkli çerçeve içindeki metinsel yorumu temsil eder |
| TextHighlight | `400` | Seçilen metni vurgulayan ve yorumlayan ek açıklama türü |
| TextRedaction | `800` | Seçili metnin bir bölümünü siyah dikdörtgenle dolduran ek açıklama türü. |
| TextReplacement | `1000` | Orijinal metni sağlanan diğer metinle değiştiren ek açıklama türü fragment |
| TextStrikeout | `2000` | Metin parçasını üstü çizili stil ile işaretleyen ek açıklama türü |
| TextUnderline | `4000` | Metni altı çizili stille işaretleyen ek açıklama türü |
| Watermark | `8000` | Belge sayfası üzerine metinsel filigran ekleyen ek açıklama türü |
| Image | `10000` | Belge sayfası üzerine görüntü kaplaması ekleyen ek açıklama türü content |
| Dropdown | `20000` | pdf belgesi için açılır bileşen ekleyen bileşen türü**sadece** |
| Checkbox | `21000` | pdf belgesi için onay kutusu ekleyen ek açıklama türü |
| Button | `22000` | pdf belgesi için düğme ekleyen ek açıklama türü |
| TextSquiggly | `2500` | Seçili dalgalı ve yorum yapan ek açıklama türü text |
| SearchText | `2700` | Document içindeki parça metnini arayan ek açıklama türü |
| All | `7FFFFFFF` | Hepsi |

### Notlar

**Daha fazla bilgi edin**

* [C# belgelerine açıklama ekleme](https://docs.groupdocs.com/display/annotationnet/Add+annotation+to+the+document)
* [C#'ta alan ek açıklamaları nasıl eklenir?](https://docs.groupdocs.com/display/annotationnet/Add+area+annotation)
* [C#'ta ok ek açıklamaları nasıl eklenir?](https://docs.groupdocs.com/display/annotationnet/Add+arrow+annotation)
* [C#'ta mesafe ek açıklamaları nasıl eklenir?](https://docs.groupdocs.com/display/annotationnet/Add+distance+annotation)
* [C#'ta elips ek açıklamaları nasıl eklenir](https://docs.groupdocs.com/display/annotationnet/Add+ellipse+annotation)
* [C#'ta bağlantı ek açıklamaları nasıl eklenir?](https://docs.groupdocs.com/display/annotationnet/Add+link+annotation)
* [C#'ta nokta ek açıklamaları nasıl eklenir?](https://docs.groupdocs.com/display/annotationnet/Add+point+annotation)
* [C#'ta çoklu çizgi ek açıklamaları nasıl eklenir?](https://docs.groupdocs.com/display/annotationnet/Add+polyline+annotation)
* [C#'ta kaynak redaksiyon ek açıklamaları nasıl eklenir?](https://docs.groupdocs.com/display/annotationnet/Add+resource+redaction+annotation)
* [C# metin alanı ek açıklamaları nasıl eklenir](https://docs.groupdocs.com/display/annotationnet/Add+text+field+annotation)
* [C#'ta vurgu ek açıklamaları nasıl eklenir?](https://docs.groupdocs.com/display/annotationnet/Add+highlight+annotation)
* [C# metin redaksiyon ek açıklamaları nasıl eklenir](https://docs.groupdocs.com/display/annotationnet/Add+text+redaction+annotation)
* [C#'ta değiştirme ek açıklamaları nasıl eklenir?](https://docs.groupdocs.com/display/annotationnet/Add+replacement+annotation)
* [C#'ta üstü çizili notlar nasıl eklenir?](https://docs.groupdocs.com/display/annotationnet/Add+strikeout+annotation)
* [C#'ta altı çizili açıklamalar nasıl eklenir?](https://docs.groupdocs.com/display/annotationnet/Add+underline+annotation)
* [C#'ta filigran ek açıklamaları nasıl eklenir?](https://docs.groupdocs.com/display/annotationnet/Add+watermark+annotation)
* [C#'ta görüntü ek açıklamaları nasıl eklenir?](https://docs.groupdocs.com/display/annotationnet/Add+image+annotation)

### Ayrıca bakınız

* ad alanı [GroupDocs.Annotation.Options](../../groupdocs.annotation.options)
* toplantı [GroupDocs.Annotation](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Annotation.dll -->
