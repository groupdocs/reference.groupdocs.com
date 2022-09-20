---
title: SpreadsheetFormats
second_title: GroupDocs.Editor for Java API Reference
description: Encapsulates all binary XML and textual Spreadsheet formats excluding all textual delimiter-based formats with separator like CSV TSV semicolon-delimited etc. in which the workbook can be saved.
type: docs
weight: 14
url: /java/com.groupdocs.editor.formats/spreadsheetformats/
---
**Inheritance:**
java.lang.Object

**All Implemented Interfaces:**
[com.groupdocs.editor.formats.IDocumentFormat](../../com.groupdocs.editor.formats/idocumentformat)
```
public class SpreadsheetFormats implements IDocumentFormat
```

Encapsulates all binary, XML and textual Spreadsheet formats (excluding all textual delimiter-based formats with separator like CSV, TSV, semicolon-delimited etc.), in which the workbook can be saved. Includes the following formats: [SpreadsheetFormats\#Dif](../../com.groupdocs.editor.formats/spreadsheetformats\#Dif), [SpreadsheetFormats\#Fods](../../com.groupdocs.editor.formats/spreadsheetformats\#Fods), [SpreadsheetFormats\#Ods](../../com.groupdocs.editor.formats/spreadsheetformats\#Ods), [SpreadsheetFormats\#Sxc](../../com.groupdocs.editor.formats/spreadsheetformats\#Sxc), [SpreadsheetFormats\#Xlam](../../com.groupdocs.editor.formats/spreadsheetformats\#Xlam), [SpreadsheetFormats\#Xls](../../com.groupdocs.editor.formats/spreadsheetformats\#Xls), [SpreadsheetFormats\#Xlsb](../../com.groupdocs.editor.formats/spreadsheetformats\#Xlsb), [SpreadsheetFormats\#Xlsm](../../com.groupdocs.editor.formats/spreadsheetformats\#Xlsm), [SpreadsheetFormats\#Xlsx](../../com.groupdocs.editor.formats/spreadsheetformats\#Xlsx), [SpreadsheetFormats\#Xlt](../../com.groupdocs.editor.formats/spreadsheetformats\#Xlt), [SpreadsheetFormats\#Xltm](../../com.groupdocs.editor.formats/spreadsheetformats\#Xltm), [SpreadsheetFormats\#Xltx](../../com.groupdocs.editor.formats/spreadsheetformats\#Xltx). Learn more about Spreadsheet formats [here][].


[here]: https://wiki.fileformat.com/spreadsheet
## Constructors

| Constructor | Description |
| --- | --- |
| [SpreadsheetFormats()](#SpreadsheetFormats--) |  |
## Fields

| Field | Description |
| --- | --- |
| [Xls](#Xls) | Excel 97-2003 Binary File Format (XLS) represents files that can be created by Microsoft Excel as well as other similar spreadsheet programs such as OpenOffice Calc or Apple Numbers. |
| [Xlt](#Xlt) | Excel 97-2003 Template (XLT) represents template files created with Microsoft Excel which is a spreadsheet application which comes as part of Microsoft Office suite. |
| [Xlsx](#Xlsx) | Office Open XML Workbook Macro-Free (XLSX) represents documents that was introduced by Microsoft with the release of Microsoft Office 2007. |
| [Xlsm](#Xlsm) | Office Open XML Workbook Macro-Enabled (XLSM) is a type of Spreasheet files that support macros. |
| [Xlsb](#Xlsb) | Excel Binary Workbook (XLSB)specifies the Excel Binary File Format, which is a collection of records and structures that specify Excel workbook content. |
| [Xltx](#Xltx) | Office Open XML Template Macro-Free (XLTX) file represents Microsoft Excel Template that are based on the Office OpenXML file format specifications. |
| [Xltm](#Xltm) | Office Open XML Template Macro-Enabled (XLTM) represents files that are generated by Microsoft Excel as Macro-enabled template files. |
| [Xlam](#Xlam) | Excel Add-in (XLAM) |
| [SpreadsheetML](#SpreadsheetML) | SpreadsheetML \\u2014 Microsoft Office Excel 2002 and Excel 2003 XML Format |
| [Ods](#Ods) | OpenDocument Spreadsheet (ODS) stand for OpenDocument Spreadsheet Document format that are editable by user. |
| [Fods](#Fods) | Flat OpenDocument Spreadsheet (FODS) \\u2014 stored as a single uncompressed XML document |
| [Sxc](#Sxc) | StarOffice or OpenOffice.org Calc XML Spreadsheet (SXC) |
| [Dif](#Dif) | Data Interchange Format (DIF) |
| [Csv](#Csv) | Comma Separated Values (CSV) documents represent plain text that contain records of data with comma separated values. |
| [Tsv](#Tsv) | Tab-Separated Values (TSV) file format represents data separated with tabs in plain text format. |
| [All](#All) | Returns an internal class, that provides enumerable possibilities over all existing Spreadsheet formats |
## Methods

| Method | Description |
| --- | --- |
| [getName()](#getName--) | Returns a formal full name of this Spreadsheet format |
| [getExtension()](#getExtension--) | Returns an extension (without leading dot character) of this Spreadsheet format in lower case |
| [getMime()](#getMime--) | Returns a MIME code for this format |
| [op_Equality(SpreadsheetFormats first, SpreadsheetFormats second)](#op-Equality-com.groupdocs.editor.formats.SpreadsheetFormats-com.groupdocs.editor.formats.SpreadsheetFormats-) | Checks two given SpreadsheetFormats instances on equality |
| [op_Inequality(SpreadsheetFormats first, SpreadsheetFormats second)](#op-Inequality-com.groupdocs.editor.formats.SpreadsheetFormats-com.groupdocs.editor.formats.SpreadsheetFormats-) | Checks two given SpreadsheetFormats instances on inequality |
| [equals(SpreadsheetFormats other)](#equals-com.groupdocs.editor.formats.SpreadsheetFormats-) | Determines whether this instance is equal to the other specified SpreadsheetFormats instance |
| [equals(IDocumentFormat other)](#equals-com.groupdocs.editor.formats.IDocumentFormat-) | Determines whether this instance is equal to the other specified IDocumentFormat instance |
| [equals(Object obj)](#equals-java.lang.Object-) | Determines whether this instance is equal to the other specified object, that is presumably of boxed SpreadsheetFormats |
| [hashCode()](#hashCode--) | Returns a hash-code, that is immutable for this instance |
| [fromExtension(String extension)](#fromExtension-java.lang.String-) | Returns instance of [SpreadsheetFormats](../../com.groupdocs.editor.formats/spreadsheetformats) structure, associated to specified filename extension, or throws an exception, if extension cannot be properly parsed |
| [CloneTo(SpreadsheetFormats that)](#CloneTo-com.groupdocs.editor.formats.SpreadsheetFormats-) |  |
| [Clone()](#Clone--) |  |
| [clone()](#clone--) |  |
| [equals(SpreadsheetFormats obj1, SpreadsheetFormats obj2)](#equals-com.groupdocs.editor.formats.SpreadsheetFormats-com.groupdocs.editor.formats.SpreadsheetFormats-) |  |
### SpreadsheetFormats() {#SpreadsheetFormats--}
```
public SpreadsheetFormats()
```


### Xls {#Xls}
```
public static final SpreadsheetFormats Xls
```


Excel 97-2003 Binary File Format (XLS) represents files that can be created by Microsoft Excel as well as other similar spreadsheet programs such as OpenOffice Calc or Apple Numbers. Learn more about this file format [here][].

--------------------

https://en.wikipedia.org/wiki/Microsoft\_Excel\#File\_formats


[here]: https://wiki.fileformat.com/spreadsheet/xls

### Xlt {#Xlt}
```
public static final SpreadsheetFormats Xlt
```


Excel 97-2003 Template (XLT) represents template files created with Microsoft Excel which is a spreadsheet application which comes as part of Microsoft Office suite. Microsoft Office 97-2003 supported creating new XLT files as well as opening these. Learn more about this file format [here][].


[here]: https://wiki.fileformat.com/spreadsheet/xlt

### Xlsx {#Xlsx}
```
public static final SpreadsheetFormats Xlsx
```


Office Open XML Workbook Macro-Free (XLSX) represents documents that was introduced by Microsoft with the release of Microsoft Office 2007. Learn more about this file format [here][].


[here]: https://wiki.fileformat.com/spreadsheet/xlsx

### Xlsm {#Xlsm}
```
public static final SpreadsheetFormats Xlsm
```


Office Open XML Workbook Macro-Enabled (XLSM) is a type of Spreasheet files that support macros. Learn more about this file format [here][].


[here]: https://wiki.fileformat.com/spreadsheet/xlsm

### Xlsb {#Xlsb}
```
public static final SpreadsheetFormats Xlsb
```


Excel Binary Workbook (XLSB)specifies the Excel Binary File Format, which is a collection of records and structures that specify Excel workbook content. Learn more about this file format [here][].


[here]: https://wiki.fileformat.com/spreadsheet/xlsb

### Xltx {#Xltx}
```
public static final SpreadsheetFormats Xltx
```


Office Open XML Template Macro-Free (XLTX) file represents Microsoft Excel Template that are based on the Office OpenXML file format specifications. It is used to create a standard template file that can be utilized to generate XLSX files that exhibit the same settings as specified in the XLTX file. Learn more about this file format [here][].


[here]: https://wiki.fileformat.com/spreadsheet/xltx

### Xltm {#Xltm}
```
public static final SpreadsheetFormats Xltm
```


Office Open XML Template Macro-Enabled (XLTM) represents files that are generated by Microsoft Excel as Macro-enabled template files. XLTM files are similar to XLTX in structure other than that the later doesn't support creating template files with macros. Learn more about this file format [here][].


[here]: https://wiki.fileformat.com/spreadsheet/xltm

### Xlam {#Xlam}
```
public static final SpreadsheetFormats Xlam
```


Excel Add-in (XLAM)

--------------------

Excel add-in to add extra functionality and tools. Inherent macro support because of the file purpose.

### SpreadsheetML {#SpreadsheetML}
```
public static final SpreadsheetFormats SpreadsheetML
```


SpreadsheetML \\u2014 Microsoft Office Excel 2002 and Excel 2003 XML Format

--------------------

https://en.wikipedia.org/wiki/SpreadsheetML https://en.wikipedia.org/wiki/Microsoft\_Office\_XML\_formats

### Ods {#Ods}
```
public static final SpreadsheetFormats Ods
```


OpenDocument Spreadsheet (ODS) stand for OpenDocument Spreadsheet Document format that are editable by user. Data is stored inside ODF file into rows and columns. Learn more about this file format [here][].


[here]: https://wiki.fileformat.com/spreadsheet/ods

### Fods {#Fods}
```
public static final SpreadsheetFormats Fods
```


Flat OpenDocument Spreadsheet (FODS) \\u2014 stored as a single uncompressed XML document

--------------------

[here][]


[here]: https://en.wikipedia.org/wiki/OpenDocument_technical_specification#Document_representation

### Sxc {#Sxc}
```
public static final SpreadsheetFormats Sxc
```


StarOffice or OpenOffice.org Calc XML Spreadsheet (SXC)

--------------------

[here][]


[here]: https://en.wikipedia.org/wiki/OpenOffice.org_XML#File_formats

### Dif {#Dif}
```
public static final SpreadsheetFormats Dif
```


Data Interchange Format (DIF)

--------------------

[here][]


[here]: https://en.wikipedia.org/wiki/Data_Interchange_Format

### Csv {#Csv}
```
public static final SpreadsheetFormats Csv
```


Comma Separated Values (CSV) documents represent plain text that contain records of data with comma separated values. Each line in a CSV file is a new record from the set of records contained in the file. Learn more about this file format [here][].


[here]: https://docs.fileformat.com/spreadsheet/csv/

### Tsv {#Tsv}
```
public static final SpreadsheetFormats Tsv
```


Tab-Separated Values (TSV) file format represents data separated with tabs in plain text format. The file format, similar to CSV, is used for organization of data in a structured manner in order to import and export between different applications. Learn more about this file format [here][].


[here]: https://docs.fileformat.com/spreadsheet/tsv/

### All {#All}
```
public static final SpreadsheetFormats.AllEnumerable All
```


Returns an internal class, that provides enumerable possibilities over all existing Spreadsheet formats

### getName() {#getName--}
```
public final String getName()
```


Returns a formal full name of this Spreadsheet format

**Returns:**
java.lang.String
### getExtension() {#getExtension--}
```
public final String getExtension()
```


Returns an extension (without leading dot character) of this Spreadsheet format in lower case

**Returns:**
java.lang.String
### getMime() {#getMime--}
```
public final String getMime()
```


Returns a MIME code for this format

**Returns:**
java.lang.String
### op_Equality(SpreadsheetFormats first, SpreadsheetFormats second) {#op-Equality-com.groupdocs.editor.formats.SpreadsheetFormats-com.groupdocs.editor.formats.SpreadsheetFormats-}
```
public static boolean op_Equality(SpreadsheetFormats first, SpreadsheetFormats second)
```


Checks two given SpreadsheetFormats instances on equality

**Parameters:**
| Parameter | Type | Description |
| --- | --- | --- |
| first | [SpreadsheetFormats](../../com.groupdocs.editor.formats/spreadsheetformats) | First SpreadsheetFormats instance to check |
| second | [SpreadsheetFormats](../../com.groupdocs.editor.formats/spreadsheetformats) | Second SpreadsheetFormats instance to check |

**Returns:**
boolean - True if are equal, false if are unequal
### op_Inequality(SpreadsheetFormats first, SpreadsheetFormats second) {#op-Inequality-com.groupdocs.editor.formats.SpreadsheetFormats-com.groupdocs.editor.formats.SpreadsheetFormats-}
```
public static boolean op_Inequality(SpreadsheetFormats first, SpreadsheetFormats second)
```


Checks two given SpreadsheetFormats instances on inequality

**Parameters:**
| Parameter | Type | Description |
| --- | --- | --- |
| first | [SpreadsheetFormats](../../com.groupdocs.editor.formats/spreadsheetformats) | First SpreadsheetFormats instance to check |
| second | [SpreadsheetFormats](../../com.groupdocs.editor.formats/spreadsheetformats) | Second SpreadsheetFormats instance to check |

**Returns:**
boolean - True if are not equal, false if are equal
### equals(SpreadsheetFormats other) {#equals-com.groupdocs.editor.formats.SpreadsheetFormats-}
```
public final boolean equals(SpreadsheetFormats other)
```


Determines whether this instance is equal to the other specified SpreadsheetFormats instance

**Parameters:**
| Parameter | Type | Description |
| --- | --- | --- |
| other | [SpreadsheetFormats](../../com.groupdocs.editor.formats/spreadsheetformats) | Other SpreadsheetFormats instance, that should be checked on equality with this |

**Returns:**
boolean - True if are equal, false if are unequal
### equals(IDocumentFormat other) {#equals-com.groupdocs.editor.formats.IDocumentFormat-}
```
public final boolean equals(IDocumentFormat other)
```


Determines whether this instance is equal to the other specified IDocumentFormat instance

**Parameters:**
| Parameter | Type | Description |
| --- | --- | --- |
| other | [IDocumentFormat](../../com.groupdocs.editor.formats/idocumentformat) | Other IDocumentFormat instance. If it is not a SpreadsheetFormats, method will return 'false' |

**Returns:**
boolean - True if are equal, false if are unequal
### equals(Object obj) {#equals-java.lang.Object-}
```
public boolean equals(Object obj)
```


Determines whether this instance is equal to the other specified object, that is presumably of boxed SpreadsheetFormats

**Parameters:**
| Parameter | Type | Description |
| --- | --- | --- |
| obj | java.lang.Object | Other boxed SpreadsheetFormats instance |

**Returns:**
boolean - True if are equal, false if are unequal
### hashCode() {#hashCode--}
```
public int hashCode()
```


Returns a hash-code, that is immutable for this instance

**Returns:**
int - Signed 4-byte integer
### fromExtension(String extension) {#fromExtension-java.lang.String-}
```
public static SpreadsheetFormats fromExtension(String extension)
```


Returns instance of [SpreadsheetFormats](../../com.groupdocs.editor.formats/spreadsheetformats) structure, associated to specified filename extension, or throws an exception, if extension cannot be properly parsed

**Parameters:**
| Parameter | Type | Description |
| --- | --- | --- |
| extension | java.lang.String | Filename extension of any supportable Spreadsheet format, with or without leading dot character, case-independent. Cannot be NULL or empty, should be valid. |

**Returns:**
[SpreadsheetFormats](../../com.groupdocs.editor.formats/spreadsheetformats) - Instance of [SpreadsheetFormats](../../com.groupdocs.editor.formats/spreadsheetformats) structure on success or thrown exception on failure
### CloneTo(SpreadsheetFormats that) {#CloneTo-com.groupdocs.editor.formats.SpreadsheetFormats-}
```
public void CloneTo(SpreadsheetFormats that)
```




**Parameters:**
| Parameter | Type | Description |
| --- | --- | --- |
| that | [SpreadsheetFormats](../../com.groupdocs.editor.formats/spreadsheetformats) |  |

### Clone() {#Clone--}
```
public SpreadsheetFormats Clone()
```




**Returns:**
[SpreadsheetFormats](../../com.groupdocs.editor.formats/spreadsheetformats)
### clone() {#clone--}
```
public Object clone()
```




**Returns:**
java.lang.Object
### equals(SpreadsheetFormats obj1, SpreadsheetFormats obj2) {#equals-com.groupdocs.editor.formats.SpreadsheetFormats-com.groupdocs.editor.formats.SpreadsheetFormats-}
```
public static boolean equals(SpreadsheetFormats obj1, SpreadsheetFormats obj2)
```




**Parameters:**
| Parameter | Type | Description |
| --- | --- | --- |
| obj1 | [SpreadsheetFormats](../../com.groupdocs.editor.formats/spreadsheetformats) |  |
| obj2 | [SpreadsheetFormats](../../com.groupdocs.editor.formats/spreadsheetformats) |  |

**Returns:**
boolean