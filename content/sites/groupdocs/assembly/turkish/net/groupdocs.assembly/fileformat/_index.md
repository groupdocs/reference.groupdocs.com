---
title: FileFormat
second_title: .NET API Başvurusu için GroupDocs.Assembly
description: Bir dosyanın formatını belirtir.
type: docs
weight: 220
url: /tr/net/groupdocs.assembly/fileformat/
---
## FileFormat enumeration

Bir dosyanın formatını belirtir.

```csharp
public enum FileFormat
```

### değerler

| İsim | Değer | Tanım |
| --- | --- | --- |
| Unspecified | `0` | Ayarlanmamış bir değer belirtir. varsayılan. |
| Doc | `1` | Microsoft Word 97 - 2007 İkili Belge formatını belirtir. |
| Dot | `2` | Microsoft Word 97 - 2007 İkili Şablon biçimini belirtir. |
| Docx | `3` | Office Açık XML WordprocessingML Belgesi (makrosuz) biçimini belirtir. |
| Docm | `4` | Office Açık XML WordprocessingML Makro Etkinleştirilmiş Belge biçimini belirtir. |
| Dotx | `5` | Office Açık XML WordprocessingML Şablonu (makrosuz) biçimini belirtir. |
| Dotm | `6` | Office Açık XML WordprocessingML Makro Etkin Şablon biçimini belirtir. |
| FlatOpc | `7` | ZIP paketi yerine düz bir XML dosyasında saklanan Office Açık XML Kelime İşleme ML biçimini belirtir. |
| FlatOpcMacroEnabled | `8` | ZIP paketi yerine düz bir XML dosyasında depolanan Office Açık XML Kelime İşlemeML Makro Etkin Belge biçimini belirtir. |
| FlatOpcTemplate | `9` | ZIP paketi yerine düz bir XML dosyasında saklanan Office Açık XML WordprocessingML Şablonu (makrosuz) biçimini belirtir. |
| FlatOpcTemplateMacroEnabled | `10` | ZIP paketi yerine düz bir XML dosyasında depolanan Office Açık XML Kelime İşlemeML Makro Etkinleştirilmiş Şablon biçimini belirtir. |
| WordML | `11` | Microsoft Word 2003 WordprocessingML biçimini belirtir. |
| Odt | `12` | ODF Metin Belgesi formatını belirtir. |
| Ott | `13` | ODF Metin Belgesi Şablonu formatını belirtir. |
| Xls | `14` | Microsoft Excel 97 - 2007 İkili Çalışma Kitabı formatını belirtir. |
| Xlsx | `15` | Office Açık XML Elektronik Tablo ML Çalışma Kitabı (makrosuz) biçimini belirtir. |
| Xlsm | `16` | Office Açık XML Elektronik TablosuML Makro Etkin Çalışma Kitabı biçimini belirtir. |
| Xltx | `17` | Office Açık XML Elektronik TabloML Şablonu (makrosuz) biçimini belirtir. |
| Xltm | `18` | Office Açık XML Elektronik TabloML Makro Etkin Şablon biçimini belirtir. |
| Xlam | `19` | Office Açık XML Elektronik TablosuML Makro Etkin Eklenti biçimini belirtir. |
| Xlsb | `20` | Microsoft Excel 2007 Makro Etkin İkili Dosya formatını belirtir. |
| SpreadsheetML | `21` | Microsoft Excel 2003 SpreadsheetML biçimini belirtir. |
| Ods | `22` | ODF Elektronik Tablo formatını belirtir. |
| Ppt | `23` | Microsoft PowerPoint 97 - 2007 İkili Sunum biçimini belirtir. |
| Pps | `24` | Microsoft PowerPoint 97 - 2007 İkili Slayt Gösterisi formatını belirtir. |
| Pptx | `25` | Office Open XML PresentationML Presentation (makrosuz) biçimini belirtir. |
| Pptm | `26` | Office Açık XML PresentationML Makro Etkinleştirilmiş Sunum formatını belirtir. |
| Ppsx | `27` | Office Açık XML PresentationML Slayt Gösterisi (makrosuz) biçimini belirtir. |
| Ppsm | `28` | Office Açık XML PresentationML Makro Etkin Slayt Gösterisi biçimini belirtir. |
| Potx | `29` | Office Açık XML PresentationML Şablonu (makrosuz) biçimini belirtir. |
| Potm | `30` | Office Açık XML PresentationML Makro Etkinleştirilmiş Şablon biçimini belirtir. |
| Odp | `31` | ODF Sunum formatını belirtir. |
| MsgAscii | `32` | ASCII karakter kodlamasını kullanarak Microsoft Outlook Mesajı (MSG) formatını belirtir. |
| MsgUnicode | `33` | Unicode karakter kodlamasını kullanarak Microsoft Outlook Mesajı (MSG) formatını belirtir. |
| Eml | `34` | MIME standart biçimini belirtir. |
| Emlx | `35` | Apple Mail.app program dosyası biçimini belirtir. |
| Rtf | `36` | RTF biçimini belirtir. |
| Text | `37` | Düz metin biçimini belirtir. |
| Xml | `38` | Genel bir formun XML biçimini belirtir. |
| Xaml | `39` | Genişletilebilir Uygulama İşaretleme Dili (XAML) formatını belirtir. |
| XamlPackage | `40` | Genişletilebilir Uygulama İşaretleme Dili (XAML) paket biçimini belirtir. |
| Html | `41` | HTML biçimini belirtir. |
| Mhtml | `42` | MHTML (Web arşivi) biçimini belirtir. |
| Xps | `43` | XPS (XML Kağıt Spesifikasyonu) formatını belirtir. |
| OpenXps | `44` | OpenXPS (Ecma-388) biçimini belirtir. |
| Pdf | `45` | PDF (Adobe Portable Document) formatını belirtir. |
| Epub | `46` | IDPF EPUB formatını belirtir. |
| Ps | `47` | PS (PostScript) biçimini belirtir. |
| Pcl | `48` | PCL (Yazıcı Kontrol Dili) formatını belirtir. |
| Svg | `49` | SVG (Ölçeklenebilir Vektör Grafikleri) biçimini belirtir. |
| Tiff | `50` | TIFF biçimini belirtir. |
| Markdown | `51` | İşaretleme formatını belirtir. |
| Pot | `52` | Microsoft PowerPoint 97 - 2007 İkili Şablon biçimini belirtir. |
| Otp | `53` | ODF Sunum Şablonu biçimini belirtir. |
| Xlt | `54` | Microsoft Excel 97 - 2007 İkili Şablon biçimini belirtir. |

### Ayrıca bakınız

* ad alanı [GroupDocs.Assembly](../../groupdocs.assembly)
* toplantı [GroupDocs.Assembly](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Assembly.dll -->
