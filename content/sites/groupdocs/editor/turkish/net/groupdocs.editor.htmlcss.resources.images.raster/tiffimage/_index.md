---
title: TiffImage
second_title: .NET API Başvurusu için GroupDocs.Editor
description: Meta verileri ve ek yöntemleriyle TIFF Etiketli Görüntü Dosyası Biçimi biçimindeki bir görüntüyü temsil eder
type: docs
weight: 560
url: /tr/net/groupdocs.editor.htmlcss.resources.images.raster/tiffimage/
---
## TiffImage class

Meta verileri ve ek yöntemleriyle TIFF (Etiketli Görüntü Dosyası Biçimi) biçimindeki bir görüntüyü temsil eder

```csharp
public sealed class TiffImage : RasterImageResourceBase
```

## yapıcılar

| İsim | Tanım |
| --- | --- |
| [TiffImage](tiffimage#constructor)(string, Stream) | İçerikten, bayt akışı olarak temsil edilen ve belirtilen ad ile yeni GifImage örneği oluşturur |
| [TiffImage](tiffimage#constructor_1)(string, string) | İçerikten, base64 kodlu dize olarak temsil edilen ve belirtilen name ile yeni TiffImage örneği oluşturur |

## Özellikleri

| İsim | Tanım |
| --- | --- |
| [AspectRatio](../../groupdocs.editor.htmlcss.resources.images.raster/rasterimageresourcebase/aspectratio) { get; } | Genişlik-yükseklik ilişkisi olarak bu görüntünün en boy oranını döndürür |
| [ByteContent](../../groupdocs.editor.htmlcss.resources.images.raster/rasterimageresourcebase/bytecontent) { get; } | Bu raster görüntünün içeriğini bayt akışı olarak döndürür |
| [FilenameWithExtension](../../groupdocs.editor.htmlcss.resources.images.raster/rasterimageresourcebase/filenamewithextension) { get; } | Bu raster görüntünün, ad ve uzantıdan oluşan doğru dosya adını döndürür. Teorik olarak isimden farklı olabilir. |
| [FramesCount](../../groupdocs.editor.htmlcss.resources.images.raster/tiffimage/framescount) { get; } | Bu TIFF görüntüsünün içinde bir dizi kare (görüntü) döndürür. 1. 'den küçük olamaz |
| [IsDisposed](../../groupdocs.editor.htmlcss.resources.images.raster/rasterimageresourcebase/isdisposed) { get; } | Bu raster görüntünün atılıp atılmayacağını belirler |
| [Length](../../groupdocs.editor.htmlcss.resources.images.raster/rasterimageresourcebase/length) { get; } | Bu raster görüntü dosyasının uzunluğunu bytes cinsinden döndürür |
| [LinearDimensions](../../groupdocs.editor.htmlcss.resources.images.raster/rasterimageresourcebase/lineardimensions) { get; } | Bu raster görüntünün doğrusal boyutlarını verir (genişlik ve yükseklik) |
| [Name](../../groupdocs.editor.htmlcss.resources.images.raster/rasterimageresourcebase/name) { get; } | Bu raster görüntünün adını döndürür. Genellikle dosya adı uzantısı içermez ve teorik olarak dosya adından farklı olabilir. |
| [TextContent](../../groupdocs.editor.htmlcss.resources.images.raster/rasterimageresourcebase/textcontent) { get; } | Bu raster görüntünün içeriğini base64 kodlu string olarak döndürür |
| override [Type](../../groupdocs.editor.htmlcss.resources.images.raster/tiffimage/type) { get; } | ImageType.Tiff döndürür |

## yöntemler

| İsim | Tanım |
| --- | --- |
| [Dispose](../../groupdocs.editor.htmlcss.resources.images.raster/rasterimageresourcebase/dispose)() | İçeriğini düzenleyerek ve çoğu yöntem ve özelliği çalışmaz hale getirerek bu raster görüntüyü kaldırır |
| [Equals](../../groupdocs.editor.htmlcss.resources.images.raster/rasterimageresourcebase/equals)(IHtmlResource) | Belirtilen referans eşitliği ile bu örneği kontrol eder. |
| [GenerateBitmap](../../groupdocs.editor.htmlcss.resources.images.raster/rasterimageresourcebase/generatebitmap)() | Bu raster görüntüden 'System.Drawing.Bitmap'in yeni bir örneğini oluşturur ve döndürür. |
| [ReduceToNewHeight](../../groupdocs.editor.htmlcss.resources.images.raster/rasterimageresourcebase/reducetonewheight)(ushort) | Aynı türde, ancak belirtilen yeni azaltılmış yükseklik ve orantılı olarak azaltılmış genişliğe sahip yeni bir azaltılmış görüntü kaynağı oluşturur ve döndürür. |
| [Save](../../groupdocs.editor.htmlcss.resources.images.raster/rasterimageresourcebase/save)(string) | Bu raster görüntüyü belirtilen dosyaya kaydeder |
| static [IsValid](../../groupdocs.editor.htmlcss.resources.images.raster/tiffimage/isvalid#isvalid)(Stream) | Belirtilen akışın geçerli bir TIFF image olup olmadığını kontrol eder |
| static [IsValid](../../groupdocs.editor.htmlcss.resources.images.raster/tiffimage/isvalid#isvalid_1)(string) | Belirtilen base64 kodlu dizenin geçerli bir TIFF image olup olmadığını kontrol eder |

## Olaylar

| İsim | Tanım |
| --- | --- |
| event [Disposed](../../groupdocs.editor.htmlcss.resources.images.raster/rasterimageresourcebase/disposed) | Bu raster görüntü atıldığında meydana gelen olay |

### Notlar

Ayrıntılar için https://en.wikipedia.org/wiki/TIFF adresine bakın. Çok nadir durumlarda, WordProcessing belgelerinin içinde TIFF bulunur.

### Ayrıca bakınız

* class [RasterImageResourceBase](../rasterimageresourcebase)
* ad alanı [GroupDocs.Editor.HtmlCss.Resources.Images.Raster](../../groupdocs.editor.htmlcss.resources.images.raster)
* toplantı [GroupDocs.Editor](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Editor.dll -->
