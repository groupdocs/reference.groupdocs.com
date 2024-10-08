---
title: WorksheetProtection
second_title: GroupDocs.Editor for Java API Reference
description: Encapsulates worksheet protection options which allow to protect a worksheet in the output Spreadsheet document from modification of specified type with a specified password.
type: docs
weight: 47
url: /java/com.groupdocs.editor.options/worksheetprotection/
---
**Inheritance:**
java.lang.Object
```
public final class WorksheetProtection
```

Encapsulates worksheet protection options, which allow to protect a worksheet in the output Spreadsheet document from modification of specified type with a specified password.

--------------------

Most of Spreadsheet formats like XLSX allows to protect a worksheet from editing with password. This class allows to enable such protection and specify its options.
## Constructors

| Constructor | Description |
| --- | --- |
| [WorksheetProtection()](#WorksheetProtection--) | Creates new instance with default parameters. |
| [WorksheetProtection(int protectionType, String password)](#WorksheetProtection-int-java.lang.String-) | Creates new instance with specified worksheet protection type and password |
## Methods

| Method | Description |
| --- | --- |
| [getProtectionType()](#getProtectionType--) | Allows to specify a type of worksheet protection. |
| [setProtectionType(int value)](#setProtectionType-int-) | Allows to specify a type of worksheet protection. |
| [getPassword()](#getPassword--) | Password, which is used for protecting a worksheet. |
| [setPassword(String value)](#setPassword-java.lang.String-) | Password, which is used for protecting a worksheet. |
### WorksheetProtection() {#WorksheetProtection--}
```
public WorksheetProtection()
```


Creates new instance with default parameters. If not modified and passed to SpreadsheetSaveOptions, no worksheet protection will be applied

### WorksheetProtection(int protectionType, String password) {#WorksheetProtection-int-java.lang.String-}
```
public WorksheetProtection(int protectionType, String password)
```


Creates new instance with specified worksheet protection type and password

**Parameters:**
| Parameter | Type | Description |
| --- | --- | --- |
| protectionType | int | Type of worksheet protection |
| password | java.lang.String | Password, that locks the protection |

### getProtectionType() {#getProtectionType--}
```
public final int getProtectionType()
```


Allows to specify a type of worksheet protection. By default is 'None' - protection is not applied.

**Returns:**
int
### setProtectionType(int value) {#setProtectionType-int-}
```
public final void setProtectionType(int value)
```


Allows to specify a type of worksheet protection. By default is 'None' - protection is not applied.

**Parameters:**
| Parameter | Type | Description |
| --- | --- | --- |
| value | int |  |

### getPassword() {#getPassword--}
```
public final String getPassword()
```


Password, which is used for protecting a worksheet. If NULL or empty string, the protection will not be applied.

**Returns:**
java.lang.String
### setPassword(String value) {#setPassword-java.lang.String-}
```
public final void setPassword(String value)
```


Password, which is used for protecting a worksheet. If NULL or empty string, the protection will not be applied.

**Parameters:**
| Parameter | Type | Description |
| --- | --- | --- |
| value | java.lang.String |  |

