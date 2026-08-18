---
title: License
second_title: GroupDocs.Markdown for Java API Reference
description: Provides methods to license the component.
type: docs
weight: 24
url: /java/com.groupdocs.markdown/license/
---
**Inheritance:**
java.lang.Object
```
public class License
```

Provides methods to license the component.

## Constructors

| Constructor | Description |
| --- | --- |
| [License()](#License--) |  |
## Methods

| Method | Description |
| --- | --- |
| [setLicense(InputStream licenseStream)](#setLicense-java.io.InputStream-) | Licenses the component from a stream.
 |
| [setLicense(String licensePath)](#setLicense-java.lang.String-) | Licenses the component from a file path.
 |
| [set(String licensePath)](#set-java.lang.String-) | Sets the license from a file path.
 |
| [set(InputStream licenseStream)](#set-java.io.InputStream-) | Sets the license from a stream.
 |
### License() {#License--}
```
public License()
```


### setLicense(InputStream licenseStream) {#setLicense-java.io.InputStream-}
```
public void setLicense(InputStream licenseStream)
```


Licenses the component from a stream.


**Parameters:**
| Parameter | Type | Description |
| --- | --- | --- |
| licenseStream | java.io.InputStream | license stream
 |

### setLicense(String licensePath) {#setLicense-java.lang.String-}
```
public void setLicense(String licensePath)
```


Licenses the component from a file path.


**Parameters:**
| Parameter | Type | Description |
| --- | --- | --- |
| licensePath | java.lang.String | license file path
 |

### set(String licensePath) {#set-java.lang.String-}
```
public static void set(String licensePath)
```


Sets the license from a file path.


**Parameters:**
| Parameter | Type | Description |
| --- | --- | --- |
| licensePath | java.lang.String | path to license file
 |

### set(InputStream licenseStream) {#set-java.io.InputStream-}
```
public static void set(InputStream licenseStream)
```


Sets the license from a stream.


**Parameters:**
| Parameter | Type | Description |
| --- | --- | --- |
| licenseStream | java.io.InputStream | stream that contains the license
 |

