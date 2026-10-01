---
title: "FileType"
second_title: "GroupDocs.Annotation for Java API リファレンス"
description: "ファイルの種類や拡張子などの情報です。"
type: docs
weight: 11
url: /ja/java/com.groupdocs.annotation.options/filetype/
---
**Inheritance:**
java.lang.Object, java.lang.Enum

**All Implemented Interfaces:**
com.aspose.ms.System.IEquatable
```
public enum FileType extends Enum<FileType> implements System.IEquatable<FileType>
```

ファイルの情報（タイプ、拡張子など）です。
## フィールド

| フィールド | 説明 |
| --- | --- |
| [UNKNOWN](#UNKNOWN) | 不明です。 |
| [DOC](#DOC) | Microsoft Word 形式です。 |
| [DOCX](#DOCX) | Microsoft Word Open XML 形式です。 |
| [DOCM](#DOCM) | Microsoft Word 2007 マクロファイルです。 |
| [DOT](#DOT) | Microsoft Word ドキュメントテンプレートです。 |
| [DOTX](#DOTX) | Microsoft Word テンプレート。 |
| [DOTM](#DOTM) | Microsoft Word マクロ有効ドキュメントテンプレート。 |
| [RTF](#RTF) | リッチテキスト形式ファイル。 |
| [ODT](#ODT) | Open Document テキスト。 |
| [XLS](#XLS) | Microsoft Excel スプレッドシート形式。 |
| [XLSX](#XLSX) | Microsoft Excel Open XML スプレッドシート。 |
| [XLSM](#XLSM) | Microsoft Excel スプレッドシートマクロ形式 |
| [XLSB](#XLSB) | Excel バイナリファイル形式 |
| [ODS](#ODS) | OpenDocument スプレッドシートドキュメント形式 |
| [PPT](#PPT) | Microsoft PowerPoint プレゼンテーション。 |
| [PPTX](#PPTX) | Microsoft PowerPoint Open XML プレゼンテーション。 |
| [PPS](#PPS) | Microsoft PowerPoint スライドショー（レガシー）。 |
| [PPSX](#PPSX) | Microsoft PowerPoint スライドショー。 |
| [ODP](#ODP) | Open Document プレゼンテーション。 |
| [TIF](#TIF) | タグ付き画像ファイル。 |
| [TIFF](#TIFF) | タグ付き画像ファイル形式 |
| [JPEG](#JPEG) | Joint Photographic Experts Group。 |
| [JPG](#JPG) | Joint Photographic Experts Group。 |
| [PNG](#PNG) | ポータブルネットワークグラフィックファイル。 |
| [BMP](#BMP) | ビットマップ画像ファイル。 |
| [DWG](#DWG) | AutoCAD 図面データベースファイル。 |
| [DXF](#DXF) | Drawing Exchange フォーマットファイル。 |
| [PDF](#PDF) | Adobe ポータブルドキュメント形式。 |
| [HTM](#HTM) | ハイパーテキストマークアップ言語ファイル。 |
| [HTML](#HTML) | ハイパーテキストマークアップ言語ファイル。 |
| [EML](#EML) | MIME 標準のファイル。 |
| [EMLX](#EMLX) | Apple の Mail.app プログラムファイル形式。 |
| [VSD](#VSD) | Microsoft Visio VSD バイナリ形式。 |
| [VSDX](#VSDX) | Microsoft Visio 2013 VSDX ファイル形式。 |
| [VSDM](#VSDM) | Microsoft Visio マクロ有効図面。 |
| [VSS](#VSS) | Microsoft Visio ステンシル ファイル。 |
| [VSX](#VSX) | Microsoft Visio ステンシル XML ファイル。 |
| [VSSX](#VSSX) | Microsoft Visio ステンシル ファイル。 |
| [VST](#VST) | Microsoft Visio VST バイナリテンプレート形式。 |
| [VSTM](#VSTM) | Microsoft Visio マクロ有効図面テンプレート。 |
## メソッド

| メソッド | 説明 |
| --- | --- |
| [values()](#values--) |  |
| [valueOf(String name)](#valueOf-java.lang.String-) |  |
| [fromFileNameOrExtension(String fileNameOrExtension)](#fromFileNameOrExtension-java.lang.String-) | ファイル名または拡張子に基づいて FileType を返します。 |
| [getSupportedFileTypes()](#getSupportedFileTypes--) | サポートされているファイルタイプの列挙を取得します。 |
| [fromFoundationFileType(int foundationFileType)](#fromFoundationFileType-int-) |  |
| [getFileFormat()](#getFileFormat--) | ファイル形式 |
| [getExtension()](#getExtension--) | ファイル拡張子 |
| [typeEquals(FileType other)](#typeEquals-com.groupdocs.annotation.options.FileType-) | ファイルタイプの等価性チェック。 |
| [opEquality(FileType left, FileType right)](#opEquality-com.groupdocs.annotation.options.FileType-com.groupdocs.annotation.options.FileType-) | 演算子オーバーロード。 |
| [opInequality(FileType left, FileType right)](#opInequality-com.groupdocs.annotation.options.FileType-com.groupdocs.annotation.options.FileType-) | 演算子オーバーロード。 |
| [toString()](#toString--) | ファイルタイプを表す文字列を返します。 |
### UNKNOWN {#UNKNOWN}
```
public static final FileType UNKNOWN
```


不明です。

### DOC {#DOC}
```
public static final FileType DOC
```


Microsoft Word 形式です。

### DOCX {#DOCX}
```
public static final FileType DOCX
```


Microsoft Word Open XML 形式です。

### DOCM {#DOCM}
```
public static final FileType DOCM
```


Microsoft Word 2007 マクロファイルです。

### DOT {#DOT}
```
public static final FileType DOT
```


Microsoft Word ドキュメントテンプレートです。

### DOTX {#DOTX}
```
public static final FileType DOTX
```


Microsoft Word テンプレート。

### DOTM {#DOTM}
```
public static final FileType DOTM
```


Microsoft Word マクロ有効ドキュメントテンプレート。

### RTF {#RTF}
```
public static final FileType RTF
```


リッチテキスト形式ファイル。

### ODT {#ODT}
```
public static final FileType ODT
```


Open Document テキスト。

### XLS {#XLS}
```
public static final FileType XLS
```


Microsoft Excel スプレッドシート形式。

### XLSX {#XLSX}
```
public static final FileType XLSX
```


Microsoft Excel Open XML スプレッドシート。

### XLSM {#XLSM}
```
public static final FileType XLSM
```


Microsoft Excel スプレッドシートマクロ形式

### XLSB {#XLSB}
```
public static final FileType XLSB
```


Excel バイナリファイル形式

### ODS {#ODS}
```
public static final FileType ODS
```


OpenDocument スプレッドシートドキュメント形式

### PPT {#PPT}
```
public static final FileType PPT
```


Microsoft PowerPoint プレゼンテーション。

### PPTX {#PPTX}
```
public static final FileType PPTX
```


Microsoft PowerPoint Open XML プレゼンテーション。

### PPS {#PPS}
```
public static final FileType PPS
```


Microsoft PowerPoint スライドショー（レガシー）。

### PPSX {#PPSX}
```
public static final FileType PPSX
```


Microsoft PowerPoint スライドショー。

### ODP {#ODP}
```
public static final FileType ODP
```


Open Document プレゼンテーション。

### TIF {#TIF}
```
public static final FileType TIF
```


タグ付き画像ファイル。

### TIFF {#TIFF}
```
public static final FileType TIFF
```


タグ付き画像ファイル形式

### JPEG {#JPEG}
```
public static final FileType JPEG
```


Joint Photographic Experts Group。

### JPG {#JPG}
```
public static final FileType JPG
```


Joint Photographic Experts Group。

### PNG {#PNG}
```
public static final FileType PNG
```


ポータブルネットワークグラフィックファイル。

### BMP {#BMP}
```
public static final FileType BMP
```


ビットマップ画像ファイル。

### DWG {#DWG}
```
public static final FileType DWG
```


AutoCAD 図面データベースファイル。

### DXF {#DXF}
```
public static final FileType DXF
```


Drawing Exchange フォーマットファイル。

### PDF {#PDF}
```
public static final FileType PDF
```


Adobe ポータブルドキュメント形式。

### HTM {#HTM}
```
public static final FileType HTM
```


ハイパーテキストマークアップ言語ファイル。

### HTML {#HTML}
```
public static final FileType HTML
```


ハイパーテキストマークアップ言語ファイル。

### EML {#EML}
```
public static final FileType EML
```


MIME 標準のファイル。

### EMLX {#EMLX}
```
public static final FileType EMLX
```


Apple の Mail.app プログラムファイル形式。

### VSD {#VSD}
```
public static final FileType VSD
```


Microsoft Visio VSD バイナリ形式。

### VSDX {#VSDX}
```
public static final FileType VSDX
```


Microsoft Visio 2013 VSDX ファイル形式。

### VSDM {#VSDM}
```
public static final FileType VSDM
```


Microsoft Visio マクロ有効図面。

### VSS {#VSS}
```
public static final FileType VSS
```


Microsoft Visio ステンシル ファイル。

### VSX {#VSX}
```
public static final FileType VSX
```


Microsoft Visio ステンシル XML ファイル。

### VSSX {#VSSX}
```
public static final FileType VSSX
```


Microsoft Visio ステンシル ファイル。

### VST {#VST}
```
public static final FileType VST
```


Microsoft Visio VST バイナリテンプレート形式。

### VSTM {#VSTM}
```
public static final FileType VSTM
```


Microsoft Visio マクロ有効図面テンプレート。

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
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| 名前 | java.lang.String |  |

**Returns:**
[FileType](../../com.groupdocs.annotation.options/filetype)
### fromFileNameOrExtension(String fileNameOrExtension) {#fromFileNameOrExtension-java.lang.String-}
```
public static FileType fromFileNameOrExtension(String fileNameOrExtension)
```


ファイル名または拡張子に基づいて FileType を返します。

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| fileNameOrExtension | java.lang.String | ファイル名またはファイル拡張子です。 |

**Returns:**
[FileType](../../com.groupdocs.annotation.options/filetype) - The file type.
### getSupportedFileTypes() {#getSupportedFileTypes--}
```
public static List<FileType> getSupportedFileTypes()
```


サポートされているファイルタイプの列挙を取得します。

**Returns:**
java.util.List<com.groupdocs.annotation.options.FileType> - FileType の列挙。
### fromFoundationFileType(int foundationFileType) {#fromFoundationFileType-int-}
```
public static FileType fromFoundationFileType(int foundationFileType)
```




**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| foundationFileType | int |  |

**Returns:**
[FileType](../../com.groupdocs.annotation.options/filetype)
### getFileFormat() {#getFileFormat--}
```
public final String getFileFormat()
```


ファイル形式

**Returns:**
java.lang.String -
### getExtension() {#getExtension--}
```
public final String getExtension()
```


ファイル拡張子

**Returns:**
java.lang.String -
### typeEquals(FileType other) {#typeEquals-com.groupdocs.annotation.options.FileType-}
```
public final boolean typeEquals(FileType other)
```


ファイルタイプの等価性チェック。

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| other | [FileType](../../com.groupdocs.annotation.options/filetype) | FileType オブジェクト。 |

**Returns:**
boolean - ファイルタイプが等価であれば true、そうでなければ false。
### opEquality(FileType left, FileType right) {#opEquality-com.groupdocs.annotation.options.FileType-com.groupdocs.annotation.options.FileType-}
```
public static boolean opEquality(FileType left, FileType right)
```


演算子オーバーロード。

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| left | [FileType](../../com.groupdocs.annotation.options/filetype) | 左側のファイルタイプです。 |
| right | [FileType](../../com.groupdocs.annotation.options/filetype) | 右側のファイルタイプです。 |

**Returns:**
boolean - ファイルタイプが等価であれば true、そうでなければ false。
### opInequality(FileType left, FileType right) {#opInequality-com.groupdocs.annotation.options.FileType-com.groupdocs.annotation.options.FileType-}
```
public static boolean opInequality(FileType left, FileType right)
```


演算子オーバーロード。

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| left | [FileType](../../com.groupdocs.annotation.options/filetype) | 左側のファイルタイプです。 |
| right | [FileType](../../com.groupdocs.annotation.options/filetype) | 右側のファイルタイプです。 |

**Returns:**
boolean - ファイルタイプが異なれば true、そうでなければ false。
### toString() {#toString--}
```
public String toString()
```


ファイルタイプを表す文字列を返します。

**Returns:**
java.lang.String - ファイルタイプを表す文字列です。
