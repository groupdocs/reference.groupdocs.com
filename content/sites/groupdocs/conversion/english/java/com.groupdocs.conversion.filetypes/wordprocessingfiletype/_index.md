---
title: WordProcessingFileType
second_title: GroupDocs.Conversion for Java API Reference
description: Defines Word Processing files that contain user information in plain text or rich text format.
type: docs
weight: 24
url: /java/com.groupdocs.conversion.filetypes/wordprocessingfiletype/
---
**Inheritance:**
java.lang.Object, [com.groupdocs.conversion.contracts.Enumeration](../../com.groupdocs.conversion.contracts/enumeration), [com.groupdocs.conversion.filetypes.FileType](../../com.groupdocs.conversion.filetypes/filetype)

**All Implemented Interfaces:**
java.io.Serializable
```
public final class WordProcessingFileType extends FileType implements Serializable
```

Defines Word Processing files that contain user information in plain text or rich text format. A plain text file format contains unformatted text and no font or page settings etc. can be applied. In contrast, a rich text file format allows formatting options such as setting fonts type, styles (bold, italic, underline, etc.), page margins, headings, bullets and numbers, and several other formatting features. Includes the following file types: [WordProcessingFileType\#Doc](../../com.groupdocs.conversion.filetypes/wordprocessingfiletype\#Doc), [WordProcessingFileType\#Docm](../../com.groupdocs.conversion.filetypes/wordprocessingfiletype\#Docm), [WordProcessingFileType\#Docx](../../com.groupdocs.conversion.filetypes/wordprocessingfiletype\#Docx), [WordProcessingFileType\#Dot](../../com.groupdocs.conversion.filetypes/wordprocessingfiletype\#Dot), [WordProcessingFileType\#Dotm](../../com.groupdocs.conversion.filetypes/wordprocessingfiletype\#Dotm), [WordProcessingFileType\#Dotx](../../com.groupdocs.conversion.filetypes/wordprocessingfiletype\#Dotx), [WordProcessingFileType\#Mobi](../../com.groupdocs.conversion.filetypes/wordprocessingfiletype\#Mobi), [WordProcessingFileType\#Odt](../../com.groupdocs.conversion.filetypes/wordprocessingfiletype\#Odt), [WordProcessingFileType\#Ott](../../com.groupdocs.conversion.filetypes/wordprocessingfiletype\#Ott), [WordProcessingFileType\#Rtf](../../com.groupdocs.conversion.filetypes/wordprocessingfiletype\#Rtf), [WordProcessingFileType\#Txt](../../com.groupdocs.conversion.filetypes/wordprocessingfiletype\#Txt), [WordProcessingFileType\#Md](../../com.groupdocs.conversion.filetypes/wordprocessingfiletype\#Md), [WordProcessingFileType\#Sql](../../com.groupdocs.conversion.filetypes/wordprocessingfiletype\#Sql), [WordProcessingFileType\#Log](../../com.groupdocs.conversion.filetypes/wordprocessingfiletype\#Log). Learn more about Word Processing formats [here][].


[here]: https://wiki.fileformat.com/word-processing
## Constructors

| Constructor | Description |
| --- | --- |
| [WordProcessingFileType()](#WordProcessingFileType--) | Serialization constructor |
## Fields

| Field | Description |
| --- | --- |
| [Doc](#Doc) | Files with .doc extension represent documents generated by Microsoft Word or other word processing documents in binary file format. |
| [Docm](#Docm) | DOCM files are Microsoft Word 2007 or higher generated documents with the ability to run macros. |
| [Docx](#Docx) | DOCX is a well-known format for Microsoft Word documents. |
| [Dot](#Dot) | Files with .DOT extension are template files created by Microsoft Word to have pre-formatted settings for generation of further DOC or DOCX files. |
| [Dotm](#Dotm) | A file with DOTM extension represents template file created with Microsoft Word 2007 or higher. |
| [Dotx](#Dotx) | Files with DOTX extension are template files created by Microsoft Word to have pre-formatted settings for generation of further DOCX files. |
| [Rtf](#Rtf) | Introduced and documented by Microsoft, the Rich Text Format (RTF) represents a method of encoding formatted text and graphics for use within applications. |
| [Odt](#Odt) | ODT files are type of documents created with word processing applications that are based on OpenDocument Text File format. |
| [Ott](#Ott) | Files with OTT extension represent template documents generated by applications in compliance with the OASIS' OpenDocument standard format. |
| [Mobi](#Mobi) | The MOBI file format is one of the most widely used ebook file format. |
| [Txt](#Txt) | A file with .TXT extension represents a text document that contains plain text in the form of lines. |
| [Md](#Md) | Text files created with Markdown language dialects is saved with .MD or .MARKDOWN file extension. |
| [Log](#Log) | A file with .LOG extension represents a text document that contains plain text in the form of lines. |
| [Ml](#Ml) | Ml file |
| [Sql](#Sql) | A file with .SQL extension represents a text document that contains sql. |
## Methods

| Method | Description |
| --- | --- |
| [getLoadOptions()](#getLoadOptions--) |  |
| [getConvertOptions()](#getConvertOptions--) |  |
| [getExcludedSourceTypes()](#getExcludedSourceTypes--) |  |
| [getExcludedTargetTypes()](#getExcludedTargetTypes--) |  |
### WordProcessingFileType() {#WordProcessingFileType--}
```
public WordProcessingFileType()
```


Serialization constructor

### Doc {#Doc}
```
public static final WordProcessingFileType Doc
```


Files with .doc extension represent documents generated by Microsoft Word or other word processing documents in binary file format. Learn more about this file format [here][].


[here]: https://wiki.fileformat.com/word-processing/doc

### Docm {#Docm}
```
public static final WordProcessingFileType Docm
```


DOCM files are Microsoft Word 2007 or higher generated documents with the ability to run macros. Learn more about this file format [here][].


[here]: https://wiki.fileformat.com/word-processing/docm

### Docx {#Docx}
```
public static final WordProcessingFileType Docx
```


DOCX is a well-known format for Microsoft Word documents. Introduced from 2007 with the release of Microsoft Office 2007, the structure of this new Document format was changed from plain binary to a combination of XML and binary files. Learn more about this file format [here][].


[here]: https://wiki.fileformat.com/word-processing/docx

### Dot {#Dot}
```
public static final WordProcessingFileType Dot
```


Files with .DOT extension are template files created by Microsoft Word to have pre-formatted settings for generation of further DOC or DOCX files. Learn more about this file format [here][].


[here]: https://wiki.fileformat.com/word-processing/dot

### Dotm {#Dotm}
```
public static final WordProcessingFileType Dotm
```


A file with DOTM extension represents template file created with Microsoft Word 2007 or higher. Learn more about this file format [here][].


[here]: https://wiki.fileformat.com/word-processing/dotm

### Dotx {#Dotx}
```
public static final WordProcessingFileType Dotx
```


Files with DOTX extension are template files created by Microsoft Word to have pre-formatted settings for generation of further DOCX files. Learn more about this file format [here][].


[here]: https://wiki.fileformat.com/word-processing/dotx

### Rtf {#Rtf}
```
public static final WordProcessingFileType Rtf
```


Introduced and documented by Microsoft, the Rich Text Format (RTF) represents a method of encoding formatted text and graphics for use within applications. Learn more about this file format [here][].


[here]: https://wiki.fileformat.com/word-processing/rtf

### Odt {#Odt}
```
public static final WordProcessingFileType Odt
```


ODT files are type of documents created with word processing applications that are based on OpenDocument Text File format. Learn more about this file format [here][].


[here]: https://wiki.fileformat.com/word-processing/odt

### Ott {#Ott}
```
public static final WordProcessingFileType Ott
```


Files with OTT extension represent template documents generated by applications in compliance with the OASIS' OpenDocument standard format. Learn more about this file format [here][].


[here]: https://wiki.fileformat.com/word-processing/ott

### Mobi {#Mobi}
```
public static final WordProcessingFileType Mobi
```


The MOBI file format is one of the most widely used ebook file format. The format is an enhancement to the old OEB (Open Ebook Format) format and was used as proprietary format for Mobipocket Reader. Learn more about this file format [here][].


[here]: https://wiki.fileformat.com/ebook/mobi

### Txt {#Txt}
```
public static final WordProcessingFileType Txt
```


A file with .TXT extension represents a text document that contains plain text in the form of lines. Learn more about this file format [here][].


[here]: https://wiki.fileformat.com/word-processing/txt

### Md {#Md}
```
public static final WordProcessingFileType Md
```


Text files created with Markdown language dialects is saved with .MD or .MARKDOWN file extension. MD files are saved in plain text format that uses Markdown language which also includes inline text symbols, defining how a text can be formatted such as indentations, table formatting, fonts, and headers. Learn more about this file format [here][].


[here]: https://wiki.fileformat.com/word-processing/md

### Log {#Log}
```
public static final WordProcessingFileType Log
```


A file with .LOG extension represents a text document that contains plain text in the form of lines.

### Ml {#Ml}
```
public static final WordProcessingFileType Ml
```


Ml file

### Sql {#Sql}
```
public static final WordProcessingFileType Sql
```


A file with .SQL extension represents a text document that contains sql.

### getLoadOptions() {#getLoadOptions--}
```
public LoadOptions getLoadOptions()
```


Prepared default load options for the source file type

**Returns:**
[LoadOptions](../../com.groupdocs.conversion.options.load/loadoptions)
### getConvertOptions() {#getConvertOptions--}
```
public ConvertOptions<WordProcessingFileType> getConvertOptions()
```


Prepared default convert options for the file type

**Returns:**
[ConvertOptions](../../com.groupdocs.conversion.options.convert/convertoptions)
### getExcludedSourceTypes() {#getExcludedSourceTypes--}
```
public static FileType[] getExcludedSourceTypes()
```




**Returns:**
com.groupdocs.conversion.filetypes.FileType[]
### getExcludedTargetTypes() {#getExcludedTargetTypes--}
```
public static FileType[] getExcludedTargetTypes()
```




**Returns:**
com.groupdocs.conversion.filetypes.FileType[]