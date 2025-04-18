---
title: PdfConvertOptions
second_title: GroupDocs.Conversion for Node.js via Java API Reference
description: Options for conversion to Pdf file type.
type: docs
weight: 25
url: /nodejs-java/com.groupdocs.conversion.options.convert/pdfconvertoptions/
---
**Inheritance:**
java.lang.Object, [com.groupdocs.conversion.contracts.ValueObject](../../com.groupdocs.conversion.contracts/valueobject), com.groupdocs.conversion.options.convert.ConvertOptions, com.groupdocs.conversion.options.convert.CommonConvertOptions

**All Implemented Interfaces:**
java.io.Serializable, [com.groupdocs.conversion.options.convert.IPageMarginConvertOptions](../../com.groupdocs.conversion.options.convert/ipagemarginconvertoptions), [com.groupdocs.conversion.options.convert.IPageSizeConvertOptions](../../com.groupdocs.conversion.options.convert/ipagesizeconvertoptions), [com.groupdocs.conversion.options.convert.IPageOrientationConvertOptions](../../com.groupdocs.conversion.options.convert/ipageorientationconvertoptions)
```
public class PdfConvertOptions extends CommonConvertOptions<PdfFileType> implements Serializable, IPageMarginConvertOptions, IPageSizeConvertOptions, IPageOrientationConvertOptions
```

Options for conversion to Pdf file type.
## Constructors

| Constructor | Description |
| --- | --- |
| [PdfConvertOptions()](#PdfConvertOptions--) | Initializes new instance of [PdfConvertOptions](../../com.groupdocs.conversion.options.convert/pdfconvertoptions) class. |
## Methods

| Method | Description |
| --- | --- |
| [getDpi()](#getDpi--) | Desired page DPI after conversion. |
| [setDpi(int value)](#setDpi-int-) | Desired page DPI after conversion. |
| [getPassword()](#getPassword--) | Set this property if you want to protect the converted document with a password. |
| [setPassword(String value)](#setPassword-java.lang.String-) | Set this property if you want to protect the converted document with a password. |
| [getMarginTop()](#getMarginTop--) | Desired page top margin in pixels after conversion. |
| [setMarginTop(int value)](#setMarginTop-int-) | Desired page top margin in pixels after conversion. |
| [getMarginBottom()](#getMarginBottom--) | Desired page bottom margin in pixels after conversion. |
| [setMarginBottom(int value)](#setMarginBottom-int-) | Desired page bottom margin in pixels after conversion. |
| [getMarginLeft()](#getMarginLeft--) | Desired page left margin in pixels after conversion. |
| [setMarginLeft(int value)](#setMarginLeft-int-) | Desired page left margin in pixels after conversion. |
| [getMarginRight()](#getMarginRight--) | Desired page right margin in pixels after conversion. |
| [setMarginRight(int value)](#setMarginRight-int-) | Desired page right margin in pixels after conversion. |
| [getPdfOptions()](#getPdfOptions--) | Pdf specific convert options |
| [setPdfOptions(PdfOptions value)](#setPdfOptions-com.groupdocs.conversion.options.convert.PdfOptions-) | Pdf specific convert options |
| [getRotate()](#getRotate--) | Page rotation |
| [setRotate(Rotation value)](#setRotate-com.groupdocs.conversion.options.convert.Rotation-) | Page rotation |
| [getPageOrientation()](#getPageOrientation--) |  |
| [setPageOrientation(PageOrientation pageOrientation)](#setPageOrientation-com.groupdocs.conversion.options.convert.PageOrientation-) |  |
| [getPageSize()](#getPageSize--) |  |
| [setPageSize(PageSize pageSize)](#setPageSize-com.groupdocs.conversion.options.convert.PageSize-) |  |
| [getPageWidth()](#getPageWidth--) |  |
| [setPageWidth(float pageWidth)](#setPageWidth-float-) |  |
| [getPageHeight()](#getPageHeight--) |  |
| [setPageHeight(float pageHeight)](#setPageHeight-float-) |  |
### PdfConvertOptions() {#PdfConvertOptions--}
```
public PdfConvertOptions()
```


Initializes new instance of [PdfConvertOptions](../../com.groupdocs.conversion.options.convert/pdfconvertoptions) class.

### getDpi() {#getDpi--}
```
public final int getDpi()
```


Desired page DPI after conversion. The default resolution is: 96 dpi.

**Returns:**
int
### setDpi(int value) {#setDpi-int-}
```
public final void setDpi(int value)
```


Desired page DPI after conversion. The default resolution is: 96 dpi.

**Parameters:**
| Parameter | Type | Description |
| --- | --- | --- |
| value | int |  |

### getPassword() {#getPassword--}
```
public final String getPassword()
```


Set this property if you want to protect the converted document with a password.

**Returns:**
java.lang.String
### setPassword(String value) {#setPassword-java.lang.String-}
```
public final void setPassword(String value)
```


Set this property if you want to protect the converted document with a password.

**Parameters:**
| Parameter | Type | Description |
| --- | --- | --- |
| value | java.lang.String |  |

### getMarginTop() {#getMarginTop--}
```
public final int getMarginTop()
```


Desired page top margin in pixels after conversion.

**Returns:**
int
### setMarginTop(int value) {#setMarginTop-int-}
```
public final void setMarginTop(int value)
```


Desired page top margin in pixels after conversion.

**Parameters:**
| Parameter | Type | Description |
| --- | --- | --- |
| value | int |  |

### getMarginBottom() {#getMarginBottom--}
```
public final int getMarginBottom()
```


Desired page bottom margin in pixels after conversion.

**Returns:**
int
### setMarginBottom(int value) {#setMarginBottom-int-}
```
public final void setMarginBottom(int value)
```


Desired page bottom margin in pixels after conversion.

**Parameters:**
| Parameter | Type | Description |
| --- | --- | --- |
| value | int |  |

### getMarginLeft() {#getMarginLeft--}
```
public final int getMarginLeft()
```


Desired page left margin in pixels after conversion.

**Returns:**
int
### setMarginLeft(int value) {#setMarginLeft-int-}
```
public final void setMarginLeft(int value)
```


Desired page left margin in pixels after conversion.

**Parameters:**
| Parameter | Type | Description |
| --- | --- | --- |
| value | int |  |

### getMarginRight() {#getMarginRight--}
```
public final int getMarginRight()
```


Desired page right margin in pixels after conversion.

**Returns:**
int
### setMarginRight(int value) {#setMarginRight-int-}
```
public final void setMarginRight(int value)
```


Desired page right margin in pixels after conversion.

**Parameters:**
| Parameter | Type | Description |
| --- | --- | --- |
| value | int |  |

### getPdfOptions() {#getPdfOptions--}
```
public final PdfOptions getPdfOptions()
```


Pdf specific convert options

**Returns:**
[PdfOptions](../../com.groupdocs.conversion.options.convert/pdfoptions)
### setPdfOptions(PdfOptions value) {#setPdfOptions-com.groupdocs.conversion.options.convert.PdfOptions-}
```
public final void setPdfOptions(PdfOptions value)
```


Pdf specific convert options

**Parameters:**
| Parameter | Type | Description |
| --- | --- | --- |
| value | [PdfOptions](../../com.groupdocs.conversion.options.convert/pdfoptions) |  |

### getRotate() {#getRotate--}
```
public final Rotation getRotate()
```


Page rotation

**Returns:**
[Rotation](../../com.groupdocs.conversion.options.convert/rotation)
### setRotate(Rotation value) {#setRotate-com.groupdocs.conversion.options.convert.Rotation-}
```
public final void setRotate(Rotation value)
```


Page rotation

**Parameters:**
| Parameter | Type | Description |
| --- | --- | --- |
| value | [Rotation](../../com.groupdocs.conversion.options.convert/rotation) |  |

### getPageOrientation() {#getPageOrientation--}
```
public PageOrientation getPageOrientation()
```


Gets page orientation after conversion

**Returns:**
[PageOrientation](../../com.groupdocs.conversion.options.convert/pageorientation)
### setPageOrientation(PageOrientation pageOrientation) {#setPageOrientation-com.groupdocs.conversion.options.convert.PageOrientation-}
```
public void setPageOrientation(PageOrientation pageOrientation)
```


Sets desired page orientation after conversion

**Parameters:**
| Parameter | Type | Description |
| --- | --- | --- |
| pageOrientation | [PageOrientation](../../com.groupdocs.conversion.options.convert/pageorientation) |  |

### getPageSize() {#getPageSize--}
```
public PageSize getPageSize()
```


Gets desired page size after conversion

**Returns:**
[PageSize](../../com.groupdocs.conversion.options.convert/pagesize)
### setPageSize(PageSize pageSize) {#setPageSize-com.groupdocs.conversion.options.convert.PageSize-}
```
public void setPageSize(PageSize pageSize)
```


Set desired page size after conversion

**Parameters:**
| Parameter | Type | Description |
| --- | --- | --- |
| pageSize | [PageSize](../../com.groupdocs.conversion.options.convert/pagesize) |  |

### getPageWidth() {#getPageWidth--}
```
public float getPageWidth()
```


Specified page width in points if  is set to PageSize.Custom

**Returns:**
float
### setPageWidth(float pageWidth) {#setPageWidth-float-}
```
public void setPageWidth(float pageWidth)
```


Set desired page width

**Parameters:**
| Parameter | Type | Description |
| --- | --- | --- |
| pageWidth | float |  |

### getPageHeight() {#getPageHeight--}
```
public float getPageHeight()
```


Specified page height in points if  is set to PageSize.Custom

**Returns:**
float
### setPageHeight(float pageHeight) {#setPageHeight-float-}
```
public void setPageHeight(float pageHeight)
```


Set desired page height

**Parameters:**
| Parameter | Type | Description |
| --- | --- | --- |
| pageHeight | float |  |

