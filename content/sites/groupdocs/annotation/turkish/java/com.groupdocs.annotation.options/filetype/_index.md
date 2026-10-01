---
title: "FileType"
second_title: "GroupDocs.Annotation Java için API Referansı"
description: "Dosya hakkında tür uzantısı vb. bilgiler"
type: docs
weight: 11
url: /tr/java/com.groupdocs.annotation.options/filetype/
---
**Inheritance:**
java.lang.Object, java.lang.Enum

**All Implemented Interfaces:**
com.aspose.ms.System.IEquatable
```
public enum FileType extends Enum<FileType> implements System.IEquatable<FileType>
```

Dosya hakkında bilgi, örneğin tür, uzantı vb.
## Alanlar

| Alan | Açıklama |
| --- | --- |
| [UNKNOWN](#UNKNOWN) | Bilinmiyor. |
| [DOC](#DOC) | Microsoft Word formatı. |
| [DOCX](#DOCX) | Microsoft Word Open XML formatı. |
| [DOCM](#DOCM) | Microsoft Word 2007 Makro dosyası. |
| [DOT](#DOT) | Microsoft Word Belge Şablonu. |
| [DOTX](#DOTX) | Microsoft Word Şablonu. |
| [DOTM](#DOTM) | Microsoft Word Makro Etkin Belge Şablonu. |
| [RTF](#RTF) | Zengin Metin Biçimi Dosyası. |
| [ODT](#ODT) | Açık Belge Metni. |
| [XLS](#XLS) | Microsoft Excel Elektronik Tablo biçimi. |
| [XLSX](#XLSX) | Microsoft Excel Açık XML Elektronik Tablosu. |
| [XLSM](#XLSM) | Microsoft Excel Elektronik Tablo Makroları biçimi |
| [XLSB](#XLSB) | Excel İkili Dosya Biçimi |
| [ODS](#ODS) | OpenDocument Elektronik Tablo Belgesi biçimi |
| [PPT](#PPT) | Microsoft PowerPoint Sunumu. |
| [PPTX](#PPTX) | Microsoft PowerPoint Açık XML Sunumu. |
| [PPS](#PPS) | Microsoft PowerPoint Slayt Gösterisi (Eski). |
| [PPSX](#PPSX) | Microsoft PowerPoint Slayt Gösterisi. |
| [ODP](#ODP) | Açık Belge Sunumu. |
| [TIF](#TIF) | Etiketli Görüntü Dosyası. |
| [TIFF](#TIFF) | Etiketli Görüntü Dosyası Biçimi |
| [JPEG](#JPEG) | Joint Photographic Experts Group. |
| [JPG](#JPG) | Joint Photographic Experts Group. |
| [PNG](#PNG) | Taşınabilir Ağ Grafiği Dosyası. |
| [BMP](#BMP) | Bitmap Görüntü Dosyası. |
| [DWG](#DWG) | AutoCAD Çizim Veritabanı Dosyası. |
| [DXF](#DXF) | Çizim Değişim Biçimi Dosyası. |
| [PDF](#PDF) | Adobe Taşınabilir Belge biçimi. |
| [HTM](#HTM) | Hipermetin İşaretleme Dili Dosyası. |
| [HTML](#HTML) | Hipermetin İşaretleme Dili Dosyası. |
| [EML](#EML) | MIME standardındaki Dosya. |
| [EMLX](#EMLX) | Apple'ın Mail.app program dosya biçimi. |
| [VSD](#VSD) | Microsoft Visio VSD ikili biçimi. |
| [VSDX](#VSDX) | Microsoft Visio 2013 VSDX dosya biçimi. |
| [VSDM](#VSDM) | Microsoft Visio Makro Etkin Çizimi. |
| [VSS](#VSS) | Microsoft Visio Şablon Dosyası. |
| [VSX](#VSX) | Microsoft Visio Şablon XML Dosyası. |
| [VSSX](#VSSX) | Microsoft Visio Şablon Dosyası. |
| [VST](#VST) | Microsoft Visio VST ikili şablon biçimi. |
| [VSTM](#VSTM) | Microsoft Visio Makro Etkin Çizim Şablonu. |
## Metotlar

| Metot | Açıklama |
| --- | --- |
| [values()](#values--) |  |
| [valueOf(String name)](#valueOf-java.lang.String-) |  |
| [fromFileNameOrExtension(String fileNameOrExtension)](#fromFileNameOrExtension-java.lang.String-) | Dosya adına veya uzantısına göre FileType döndür. |
| [getSupportedFileTypes()](#getSupportedFileTypes--) | Desteklenen dosya türleri sayımını al. |
| [fromFoundationFileType(int foundationFileType)](#fromFoundationFileType-int-) |  |
| [getFileFormat()](#getFileFormat--) | Dosya biçimi |
| [getExtension()](#getExtension--) | Dosya uzantısı |
| [typeEquals(FileType other)](#typeEquals-com.groupdocs.annotation.options.FileType-) | Dosya türü eşdeğerlik kontrolü. |
| [opEquality(FileType left, FileType right)](#opEquality-com.groupdocs.annotation.options.FileType-com.groupdocs.annotation.options.FileType-) | Operatör aşırı yükleme. |
| [opInequality(FileType left, FileType right)](#opInequality-com.groupdocs.annotation.options.FileType-com.groupdocs.annotation.options.FileType-) | Operatör aşırı yükleme. |
| [toString()](#toString--) | Dosya türünü temsil eden bir dize döndürür. |
### UNKNOWN {#UNKNOWN}
```
public static final FileType UNKNOWN
```


Bilinmiyor.

### DOC {#DOC}
```
public static final FileType DOC
```


Microsoft Word formatı.

### DOCX {#DOCX}
```
public static final FileType DOCX
```


Microsoft Word Open XML formatı.

### DOCM {#DOCM}
```
public static final FileType DOCM
```


Microsoft Word 2007 Makro dosyası.

### DOT {#DOT}
```
public static final FileType DOT
```


Microsoft Word Belge Şablonu.

### DOTX {#DOTX}
```
public static final FileType DOTX
```


Microsoft Word Şablonu.

### DOTM {#DOTM}
```
public static final FileType DOTM
```


Microsoft Word Makro Etkin Belge Şablonu.

### RTF {#RTF}
```
public static final FileType RTF
```


Zengin Metin Biçimi Dosyası.

### ODT {#ODT}
```
public static final FileType ODT
```


Açık Belge Metni.

### XLS {#XLS}
```
public static final FileType XLS
```


Microsoft Excel Elektronik Tablo biçimi.

### XLSX {#XLSX}
```
public static final FileType XLSX
```


Microsoft Excel Açık XML Elektronik Tablosu.

### XLSM {#XLSM}
```
public static final FileType XLSM
```


Microsoft Excel Elektronik Tablo Makroları biçimi

### XLSB {#XLSB}
```
public static final FileType XLSB
```


Excel İkili Dosya Biçimi

### ODS {#ODS}
```
public static final FileType ODS
```


OpenDocument Elektronik Tablo Belgesi biçimi

### PPT {#PPT}
```
public static final FileType PPT
```


Microsoft PowerPoint Sunumu.

### PPTX {#PPTX}
```
public static final FileType PPTX
```


Microsoft PowerPoint Açık XML Sunumu.

### PPS {#PPS}
```
public static final FileType PPS
```


Microsoft PowerPoint Slayt Gösterisi (Eski).

### PPSX {#PPSX}
```
public static final FileType PPSX
```


Microsoft PowerPoint Slayt Gösterisi.

### ODP {#ODP}
```
public static final FileType ODP
```


Açık Belge Sunumu.

### TIF {#TIF}
```
public static final FileType TIF
```


Etiketli Görüntü Dosyası.

### TIFF {#TIFF}
```
public static final FileType TIFF
```


Etiketli Görüntü Dosyası Biçimi

### JPEG {#JPEG}
```
public static final FileType JPEG
```


Joint Photographic Experts Group.

### JPG {#JPG}
```
public static final FileType JPG
```


Joint Photographic Experts Group.

### PNG {#PNG}
```
public static final FileType PNG
```


Taşınabilir Ağ Grafiği Dosyası.

### BMP {#BMP}
```
public static final FileType BMP
```


Bitmap Görüntü Dosyası.

### DWG {#DWG}
```
public static final FileType DWG
```


AutoCAD Çizim Veritabanı Dosyası.

### DXF {#DXF}
```
public static final FileType DXF
```


Çizim Değişim Biçimi Dosyası.

### PDF {#PDF}
```
public static final FileType PDF
```


Adobe Taşınabilir Belge biçimi.

### HTM {#HTM}
```
public static final FileType HTM
```


Hipermetin İşaretleme Dili Dosyası.

### HTML {#HTML}
```
public static final FileType HTML
```


Hipermetin İşaretleme Dili Dosyası.

### EML {#EML}
```
public static final FileType EML
```


MIME standardındaki Dosya.

### EMLX {#EMLX}
```
public static final FileType EMLX
```


Apple'ın Mail.app program dosya biçimi.

### VSD {#VSD}
```
public static final FileType VSD
```


Microsoft Visio VSD ikili biçimi.

### VSDX {#VSDX}
```
public static final FileType VSDX
```


Microsoft Visio 2013 VSDX dosya biçimi.

### VSDM {#VSDM}
```
public static final FileType VSDM
```


Microsoft Visio Makro Etkin Çizimi.

### VSS {#VSS}
```
public static final FileType VSS
```


Microsoft Visio Şablon Dosyası.

### VSX {#VSX}
```
public static final FileType VSX
```


Microsoft Visio Şablon XML Dosyası.

### VSSX {#VSSX}
```
public static final FileType VSSX
```


Microsoft Visio Şablon Dosyası.

### VST {#VST}
```
public static final FileType VST
```


Microsoft Visio VST ikili şablon biçimi.

### VSTM {#VSTM}
```
public static final FileType VSTM
```


Microsoft Visio Makro Etkin Çizim Şablonu.

### values() {#values--}
```
public static FileType[] values()
```




**Returns:**
com.groupdocs.annotation.options.FileType[]
### valueOf(String name) {#valueOf-java.lang.String-}
```
public static FileType valueOf(String name)
```




**Parameters:**
| Parametre | Tür | Açıklama |
| --- | --- | --- |
| ad | java.lang.String |  |

**Returns:**
[FileType](../../com.groupdocs.annotation.options/filetype)
### fromFileNameOrExtension(String fileNameOrExtension) {#fromFileNameOrExtension-java.lang.String-}
```
public static FileType fromFileNameOrExtension(String fileNameOrExtension)
```


Dosya adına veya uzantısına göre FileType döndür.

**Parameters:**
| Parametre | Tür | Açıklama |
| --- | --- | --- |
| dosyaAdiVeyaUzanti | java.lang.String | Dosya adı veya dosya uzantısı. |

**Returns:**
[FileType](../../com.groupdocs.annotation.options/filetype) - The file type.
### getSupportedFileTypes() {#getSupportedFileTypes--}
```
public static List<FileType> getSupportedFileTypes()
```


Desteklenen dosya türleri sayımını al.

**Returns:**
java.util.List<com.groupdocs.annotation.options.FileType> - FileType sayımı.
### fromFoundationFileType(int foundationFileType) {#fromFoundationFileType-int-}
```
public static FileType fromFoundationFileType(int foundationFileType)
```




**Parameters:**
| Parametre | Tür | Açıklama |
| --- | --- | --- |
| foundationFileType | int |  |

**Returns:**
[FileType](../../com.groupdocs.annotation.options/filetype)
### getFileFormat() {#getFileFormat--}
```
public final String getFileFormat()
```


Dosya biçimi

**Returns:**
java.lang.String -
### getExtension() {#getExtension--}
```
public final String getExtension()
```


Dosya uzantısı

**Returns:**
java.lang.String -
### typeEquals(FileType other) {#typeEquals-com.groupdocs.annotation.options.FileType-}
```
public final boolean typeEquals(FileType other)
```


Dosya türü eşdeğerlik kontrolü.

**Parameters:**
| Parametre | Tür | Açıklama |
| --- | --- | --- |
| other | [FileType](../../com.groupdocs.annotation.options/filetype) | FileType nesnesi. |

**Returns:**
boolean - Dosya türleri eşdeğer ise true, aksi takdirde false.
### opEquality(FileType left, FileType right) {#opEquality-com.groupdocs.annotation.options.FileType-com.groupdocs.annotation.options.FileType-}
```
public static boolean opEquality(FileType left, FileType right)
```


Operatör aşırı yükleme.

**Parameters:**
| Parametre | Tür | Açıklama |
| --- | --- | --- |
| left | [FileType](../../com.groupdocs.annotation.options/filetype) | Sol dosya türü. |
| right | [FileType](../../com.groupdocs.annotation.options/filetype) | Sağ dosya türü. |

**Returns:**
boolean - Dosya türleri eşdeğer ise true, aksi takdirde false.
### opInequality(FileType left, FileType right) {#opInequality-com.groupdocs.annotation.options.FileType-com.groupdocs.annotation.options.FileType-}
```
public static boolean opInequality(FileType left, FileType right)
```


Operatör aşırı yükleme.

**Parameters:**
| Parametre | Tür | Açıklama |
| --- | --- | --- |
| left | [FileType](../../com.groupdocs.annotation.options/filetype) | Sol dosya türü. |
| right | [FileType](../../com.groupdocs.annotation.options/filetype) | Sağ dosya türü. |

**Returns:**
boolean - Dosya türleri farklı ise true, aksi takdirde false.
### toString() {#toString--}
```
public String toString()
```


Dosya türünü temsil eden bir dize döndürür.

**Returns:**
java.lang.String - Dosya türünü temsil eden bir dize.
