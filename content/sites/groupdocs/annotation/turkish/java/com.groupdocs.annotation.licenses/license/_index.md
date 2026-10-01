---
title: "Lisans"
second_title: "GroupDocs.Annotation Java için API Referansı"
description: "Bileşeni lisanslamak için yöntemler sağlar."
type: docs
weight: 10
url: /tr/java/com.groupdocs.annotation.licenses/license/
---
**Inheritance:**
java.lang.Object
```
public class License
```

Bileşeni lisanslamak için yöntemler sağlar. Lisanslama hakkında daha fazla bilgi için burada.

--------------------

 **Learn more** 

 *  
 *  
## Yapıcılar

| Yapıcı | Açıklama |
| --- | --- |
| [License()](#License--) |  |
## Metotlar

| Metot | Açıklama |
| --- | --- |
| [isValidMeteredLicense()](#isValidMeteredLicense--) |  |
| [isValidLicense()](#isValidLicense--) | Bu örneğin geçerli bir lisans olup olmadığını gösteren bir değer alır. |
| [setLicense(InputStream licenseStream)](#setLicense-java.io.InputStream-) | Bileşeni lisanslar. |
| [setLicenseInternal(System.IO.Stream licenseStream)](#setLicenseInternal-com.aspose.ms.System.IO.Stream-) |  |
| [setMeteredLicense()](#setMeteredLicense--) |  |
| [setLicense(Path licensePath)](#setLicense-java.nio.file.Path-) | Bileşeni lisanslar. |
| [setLicense(String licensePath)](#setLicense-java.lang.String-) | Bileşeni lisanslar. |
| [resetLicense()](#resetLicense--) |  |
### License() {#License--}
```
public License()
```


### isValidMeteredLicense() {#isValidMeteredLicense--}
```
public static boolean isValidMeteredLicense()
```




**Returns:**
boolean
### isValidLicense() {#isValidLicense--}
```
public static boolean isValidLicense()
```


Bu örneğin geçerli bir lisans olup olmadığını gösteren bir değer alır.

Değer:  true  bu örnek geçerli bir lisans ise; aksi takdirde,  false .

**Returns:**
boolean
### setLicense(InputStream licenseStream) {#setLicense-java.io.InputStream-}
```
public final void setLicense(InputStream licenseStream)
```


Bileşeni lisanslar.

**Parameters:**
| Parametre | Tür | Açıklama |
| --- | --- | --- |
| licenseStream | java.io.InputStream | Lisans akışı. |

### setLicenseInternal(System.IO.Stream licenseStream) {#setLicenseInternal-com.aspose.ms.System.IO.Stream-}
```
public void setLicenseInternal(System.IO.Stream licenseStream)
```




**Parameters:**
| Parametre | Tür | Açıklama |
| --- | --- | --- |
| licenseStream | com.aspose.ms.System.IO.Stream |  |

### setMeteredLicense() {#setMeteredLicense--}
```
public final void setMeteredLicense()
```




### setLicense(Path licensePath) {#setLicense-java.nio.file.Path-}
```
public final void setLicense(Path licensePath)
```


Bileşeni lisanslar.

**Parameters:**
| Parametre | Tür | Açıklama |
| --- | --- | --- |
| licensePath | java.nio.file.Path | Lisans yolu. |

### setLicense(String licensePath) {#setLicense-java.lang.String-}
```
public final void setLicense(String licensePath)
```


Bileşeni lisanslar.

**Parameters:**
| Parametre | Tür | Açıklama |
| --- | --- | --- |
| licensePath | java.lang.String | Lisans yolu. |

### resetLicense() {#resetLicense--}
```
public static void resetLicense()
```




