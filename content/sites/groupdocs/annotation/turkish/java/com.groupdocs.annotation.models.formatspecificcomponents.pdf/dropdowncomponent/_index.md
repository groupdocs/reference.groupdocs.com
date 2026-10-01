---
title: "DropdownComponent"
second_title: "GroupDocs.Annotation Java için API Referansı"
description: "Açılır menü bileşeni özelliklerini temsil eder"
type: docs
weight: 12
url: /tr/java/com.groupdocs.annotation.models.formatspecificcomponents.pdf/dropdowncomponent/
---
**Inheritance:**
java.lang.Object, [com.groupdocs.annotation.models.annotationmodels.AnnotationBase](../../com.groupdocs.annotation.models.annotationmodels/annotationbase)

**All Implemented Interfaces:**
[com.groupdocs.annotation.models.formatspecificcomponents.pdf.interfaces.IDropdownComponent](../../com.groupdocs.annotation.models.formatspecificcomponents.pdf.interfaces/idropdowncomponent)
```
public class DropdownComponent extends AnnotationBase implements IDropdownComponent
```

Açılır menü bileşeni özelliklerini temsil eder

--------------------

 **Learn more** 

 *  
 *  
## Yapıcılar

| Yapıcı | Açıklama |
| --- | --- |
| [DropdownComponent()](#DropdownComponent--) | Yeni bir [CheckBoxComponent](../../com.groupdocs.annotation.models.formatspecificcomponents.pdf/checkboxcomponent) sınıfı örneğini başlatır. |
## Metotlar

| Metot | Açıklama |
| --- | --- |
| [getOptions()](#getOptions--) | Bileşen tıklandığında gösterilecek seçeneklerin (açılır öğeler) listesi |
| [setOptions(List<String> value)](#setOptions-java.util.List-java.lang.String--) | Bileşen tıklandığında gösterilecek seçeneklerin (açılır öğeler) listesi |
| [getSelectedOption()](#getSelectedOption--) | Varsayılan olarak seçilecek seçenek sayısı |
| [setSelectedOption(Integer value)](#setSelectedOption-java.lang.Integer-) | Varsayılan olarak seçilecek seçenek sayısı |
| [getPlaceholder()](#getPlaceholder--) | Henüz seçenek seçilmediğinde gösterilecek metin |
| [setPlaceholder(String value)](#setPlaceholder-java.lang.String-) | Henüz seçenek seçilmediğinde gösterilecek metin |
| [getBox()](#getBox--) | Bileşen konumunu alır veya ayarlar |
| [setBox(Rectangle value)](#setBox-com.groupdocs.annotation.models.Rectangle-) | Bileşen konumunu alır veya ayarlar |
| [getPenColor()](#getPenColor--) | Bileşen kalem rengini alır veya ayarlar |
| [setPenColor(Integer value)](#setPenColor-java.lang.Integer-) | Bileşen kalem rengini alır veya ayarlar |
| [getPenStyle()](#getPenStyle--) | Bileşen kalem stilini alır veya ayarlar |
| [setPenStyle(Byte value)](#setPenStyle-java.lang.Byte-) | Bileşen kalem stilini alır veya ayarlar |
| [getPenWidth()](#getPenWidth--) | Bileşen kalem genişliğini alır veya ayarlar |
| [setPenWidth(Byte value)](#setPenWidth-java.lang.Byte-) | Bileşen kalem genişliğini alır veya ayarlar |
| [equals(DropdownComponent other)](#equals-com.groupdocs.annotation.models.formatspecificcomponents.pdf.DropdownComponent-) | Dropdown bileşenini IEquatable Equals yöntemiyle karşılaştırır |
| [equals(Object obj)](#equals-java.lang.Object-) | Dropdown Bileşenlerini standart nesne Equals yöntemiyle karşılaştırır |
| [hashCode()](#hashCode--) | Dropdown Bileşeninin HashCode değerini döndürür |
| [deepClone()](#deepClone--) | Aynı değerlerle yeni bir örnek döndürür |
| [toString()](#toString--) |  |
| [toString(ToStringStyle toStringStyle)](#toString-org.apache.commons.lang3.builder.ToStringStyle-) |  |
### DropdownComponent() {#DropdownComponent--}
```
public DropdownComponent()
```


Yeni bir [CheckBoxComponent](../../com.groupdocs.annotation.models.formatspecificcomponents.pdf/checkboxcomponent) sınıfı örneğini başlatır.

### getOptions() {#getOptions--}
```
public final List<String> getOptions()
```


Bileşen tıklandığında gösterilecek seçeneklerin (açılır öğeler) listesi

**Returns:**
java.util.List<java.lang.String> -
### setOptions(List<String> value) {#setOptions-java.util.List-java.lang.String--}
```
public final void setOptions(List<String> value)
```


Bileşen tıklandığında gösterilecek seçeneklerin (açılır öğeler) listesi

**Parameters:**
| Parametre | Tür | Açıklama |
| --- | --- | --- |
| değer | java.util.List<java.lang.String> |  |

### getSelectedOption() {#getSelectedOption--}
```
public final Integer getSelectedOption()
```


Varsayılan olarak seçilecek seçenek sayısı

**Returns:**
java.lang.Integer
### setSelectedOption(Integer value) {#setSelectedOption-java.lang.Integer-}
```
public final void setSelectedOption(Integer value)
```


Varsayılan olarak seçilecek seçenek sayısı

**Parameters:**
| Parametre | Tür | Açıklama |
| --- | --- | --- |
| değer | java.lang.Integer |  |

### getPlaceholder() {#getPlaceholder--}
```
public final String getPlaceholder()
```


Henüz seçenek seçilmediğinde gösterilecek metin

**Returns:**
java.lang.String
### setPlaceholder(String value) {#setPlaceholder-java.lang.String-}
```
public final void setPlaceholder(String value)
```


Henüz seçenek seçilmediğinde gösterilecek metin

**Parameters:**
| Parametre | Tür | Açıklama |
| --- | --- | --- |
| değer | java.lang.String |  |

### getBox() {#getBox--}
```
public final Rectangle getBox()
```


Bileşen konumunu alır veya ayarlar

**Returns:**
[Rectangle](../../com.groupdocs.annotation.models/rectangle)
### setBox(Rectangle value) {#setBox-com.groupdocs.annotation.models.Rectangle-}
```
public final void setBox(Rectangle value)
```


Bileşen konumunu alır veya ayarlar

**Parameters:**
| Parametre | Tür | Açıklama |
| --- | --- | --- |
| value | [Rectangle](../../com.groupdocs.annotation.models/rectangle) |  |

### getPenColor() {#getPenColor--}
```
public final Integer getPenColor()
```


Bileşen kalem rengini alır veya ayarlar

**Returns:**
java.lang.Integer
### setPenColor(Integer value) {#setPenColor-java.lang.Integer-}
```
public final void setPenColor(Integer value)
```


Bileşen kalem rengini alır veya ayarlar

**Parameters:**
| Parametre | Tür | Açıklama |
| --- | --- | --- |
| değer | java.lang.Integer |  |

### getPenStyle() {#getPenStyle--}
```
public final Byte getPenStyle()
```


Bileşen kalem stilini alır veya ayarlar

**Returns:**
java.lang.Byte
### setPenStyle(Byte value) {#setPenStyle-java.lang.Byte-}
```
public final void setPenStyle(Byte value)
```


Bileşen kalem stilini alır veya ayarlar

**Parameters:**
| Parametre | Tür | Açıklama |
| --- | --- | --- |
| değer | java.lang.Byte |  |

### getPenWidth() {#getPenWidth--}
```
public final Byte getPenWidth()
```


Bileşen kalem genişliğini alır veya ayarlar

**Returns:**
java.lang.Byte
### setPenWidth(Byte value) {#setPenWidth-java.lang.Byte-}
```
public final void setPenWidth(Byte value)
```


Bileşen kalem genişliğini alır veya ayarlar

**Parameters:**
| Parametre | Tür | Açıklama |
| --- | --- | --- |
| değer | java.lang.Byte |  |

### equals(DropdownComponent other) {#equals-com.groupdocs.annotation.models.formatspecificcomponents.pdf.DropdownComponent-}
```
public final boolean equals(DropdownComponent other)
```


Dropdown bileşenini IEquatable Equals yöntemiyle karşılaştırır

**Parameters:**
| Parametre | Tür | Açıklama |
| --- | --- | --- |
| other | [DropdownComponent](../../com.groupdocs.annotation.models.formatspecificcomponents.pdf/dropdowncomponent) | Mevcut nesneyle karşılaştırmak için DropdownComponent nesnesi |

**Returns:**
boolean -
### equals(Object obj) {#equals-java.lang.Object-}
```
public boolean equals(Object obj)
```


Dropdown Bileşenlerini standart nesne Equals yöntemiyle karşılaştırır

**Parameters:**
| Parametre | Tür | Açıklama |
| --- | --- | --- |
| obj | java.lang.Object | Mevcut nesneyle karşılaştırılacak nesne |

**Returns:**
boolean
### hashCode() {#hashCode--}
```
public int hashCode()
```


Dropdown Bileşeninin HashCode değerini döndürür

**Returns:**
int
### deepClone() {#deepClone--}
```
public Object deepClone()
```


Aynı değerlerle yeni bir örnek döndürür

**Returns:**
java.lang.Object -
### toString() {#toString--}
```
public String toString()
```




**Returns:**
java.lang.String
### toString(ToStringStyle toStringStyle) {#toString-org.apache.commons.lang3.builder.ToStringStyle-}
```
public String toString(ToStringStyle toStringStyle)
```




**Parameters:**
| Parametre | Tür | Açıklama |
| --- | --- | --- |
| toStringStyle | org.apache.commons.lang3.builder.ToStringStyle |  |

**Returns:**
java.lang.String
