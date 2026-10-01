---
title: "Rectangle"
second_title: "GroupDocs.Annotation Java için API Referansı"
description: "Dikdörtgeni temsil eder."
type: docs
weight: 13
url: /tr/java/com.groupdocs.annotation.models/rectangle/
---
**Inheritance:**
java.lang.Object
```
public class Rectangle
```

Dikdörtgeni temsil eder.
## Yapıcılar

| Yapıcı | Açıklama |
| --- | --- |
| [Rectangle()](#Rectangle--) |  |
| [Rectangle(float x, float y, float width, float height)](#Rectangle-float-float-float-float-) | Yeni bir [Rectangle](../../com.groupdocs.annotation.models/rectangle) sınıfının örneğini başlatır. |
| [Rectangle(Rectangle rectangle)](#Rectangle-com.groupdocs.annotation.models.Rectangle-) | Yeni bir [Rectangle](../../com.groupdocs.annotation.models/rectangle) sınıfının örneğini başlatır. |
## Metotlar

| Metot | Açıklama |
| --- | --- |
| [opEquality(Rectangle left, Rectangle right)](#opEquality-com.groupdocs.annotation.models.Rectangle-com.groupdocs.annotation.models.Rectangle-) | İki Rectangle nesnesini karşılaştırır. |
| [opInequality(Rectangle left, Rectangle right)](#opInequality-com.groupdocs.annotation.models.Rectangle-com.groupdocs.annotation.models.Rectangle-) | İki Rectangle nesnesini karşılaştırır. |
| [equals(Rectangle obj1, Rectangle obj2)](#equals-com.groupdocs.annotation.models.Rectangle-com.groupdocs.annotation.models.Rectangle-) |  |
| [getX()](#getX--) | x değerini alır veya ayarlar. |
| [setX(float value)](#setX-float-) | x değerini alır veya ayarlar. |
| [getY()](#getY--) | y değerini alır veya ayarlar. |
| [setY(float value)](#setY-float-) | y değerini alır veya ayarlar. |
| [getWidth()](#getWidth--) | genişlik değerini alır veya ayarlar. |
| [setWidth(float value)](#setWidth-float-) | genişlik değerini alır veya ayarlar. |
| [getHeight()](#getHeight--) | yükseklik değerini alır veya ayarlar. |
| [setHeight(float value)](#setHeight-float-) | yükseklik değerini alır veya ayarlar. |
| [equals(Object obj)](#equals-java.lang.Object-) | Belirtilen dikdörtgenin mevcut dikdörtgenle eşit olup olmadığını belirler. |
| [hashCode()](#hashCode--) | Varsayılan hash işlevi olarak hizmet verir. |
| [toString()](#toString--) |  |
### Rectangle() {#Rectangle--}
```
public Rectangle()
```


### Rectangle(float x, float y, float width, float height) {#Rectangle-float-float-float-float-}
```
public Rectangle(float x, float y, float width, float height)
```


Yeni bir [Rectangle](../../com.groupdocs.annotation.models/rectangle) sınıfının örneğini başlatır.

**Parameters:**
| Parametre | Tür | Açıklama |
| --- | --- | --- |
| x | float | x. |
| y | float | y. |
| genişlik | float | genişlik. |
| yükseklik | float | yükseklik. |

### Rectangle(Rectangle rectangle) {#Rectangle-com.groupdocs.annotation.models.Rectangle-}
```
public Rectangle(Rectangle rectangle)
```


Yeni bir [Rectangle](../../com.groupdocs.annotation.models/rectangle) sınıfının örneğini başlatır.

**Parameters:**
| Parametre | Tür | Açıklama |
| --- | --- | --- |
| rectangle | [Rectangle](../../com.groupdocs.annotation.models/rectangle) | dikdörtgen. |

### opEquality(Rectangle left, Rectangle right) {#opEquality-com.groupdocs.annotation.models.Rectangle-com.groupdocs.annotation.models.Rectangle-}
```
public static boolean opEquality(Rectangle left, Rectangle right)
```


İki Rectangle nesnesini karşılaştırır. Sonuç, iki Rectangle nesnesinin Rectangle.X, Rectangle.Y, Rectangle.Width ve Rectangle.Height özelliklerinin değerlerinin eşit olup olmadığını belirtir.

**Parameters:**
| Parametre | Tür | Açıklama |
| --- | --- | --- |
| left | [Rectangle](../../com.groupdocs.annotation.models/rectangle) | Karşılaştırılacak bir Rectangle. |
| right | [Rectangle](../../com.groupdocs.annotation.models/rectangle) | Karşılaştırılacak bir Rectangle. |

**Returns:**
boolean - sol ve sağ Rectangle.X, Rectangle.Y, Rectangle.Width ve Rectangle.Height değerleri eşitse true; aksi takdirde false.
### opInequality(Rectangle left, Rectangle right) {#opInequality-com.groupdocs.annotation.models.Rectangle-com.groupdocs.annotation.models.Rectangle-}
```
public static boolean opInequality(Rectangle left, Rectangle right)
```


İki Rectangle nesnesini karşılaştırır. Sonuç, iki Rectangle nesnesinin Rectangle.X, Rectangle.Y, Rectangle.Width ve Rectangle.Height özelliklerinin değerlerinin eşit olmaması durumunu belirtir.

**Parameters:**
| Parametre | Tür | Açıklama |
| --- | --- | --- |
| left | [Rectangle](../../com.groupdocs.annotation.models/rectangle) | Karşılaştırılacak bir Rectangle. |
| right | [Rectangle](../../com.groupdocs.annotation.models/rectangle) | Karşılaştırılacak bir Rectangle. |

**Returns:**
boolean - sol ve sağ Rectangle.X, Rectangle.Y, Rectangle.Width ve Rectangle.Height değerleri eşit değilse true; aksi takdirde false.
### equals(Rectangle obj1, Rectangle obj2) {#equals-com.groupdocs.annotation.models.Rectangle-com.groupdocs.annotation.models.Rectangle-}
```
public static boolean equals(Rectangle obj1, Rectangle obj2)
```




**Parameters:**
| Parametre | Tür | Açıklama |
| --- | --- | --- |
| obj1 | [Rectangle](../../com.groupdocs.annotation.models/rectangle) |  |
| obj2 | [Rectangle](../../com.groupdocs.annotation.models/rectangle) |  |

**Returns:**
boolean
### getX() {#getX--}
```
public final float getX()
```


x değerini alır veya ayarlar.

Değer: x.

**Returns:**
float -
### setX(float value) {#setX-float-}
```
public final void setX(float value)
```


x değerini alır veya ayarlar.

Değer: x.

**Parameters:**
| Parametre | Tür | Açıklama |
| --- | --- | --- |
| değer | float |  |

### getY() {#getY--}
```
public final float getY()
```


y değerini alır veya ayarlar.

Değer: y.

**Returns:**
float -
### setY(float value) {#setY-float-}
```
public final void setY(float value)
```


y değerini alır veya ayarlar.

Değer: y.

**Parameters:**
| Parametre | Tür | Açıklama |
| --- | --- | --- |
| değer | float |  |

### getWidth() {#getWidth--}
```
public final float getWidth()
```


genişlik değerini alır veya ayarlar.

Değer: genişlik.

**Returns:**
float -
### setWidth(float value) {#setWidth-float-}
```
public final void setWidth(float value)
```


genişlik değerini alır veya ayarlar.

Değer: genişlik.

**Parameters:**
| Parametre | Tür | Açıklama |
| --- | --- | --- |
| değer | float |  |

### getHeight() {#getHeight--}
```
public final float getHeight()
```


yükseklik değerini alır veya ayarlar.

Değer: yükseklik.

**Returns:**
float -
### setHeight(float value) {#setHeight-float-}
```
public final void setHeight(float value)
```


yükseklik değerini alır veya ayarlar.

Değer: yükseklik.

**Parameters:**
| Parametre | Tür | Açıklama |
| --- | --- | --- |
| değer | float |  |

### equals(Object obj) {#equals-java.lang.Object-}
```
public boolean equals(Object obj)
```


Belirtilen dikdörtgenin mevcut dikdörtgenle eşit olup olmadığını belirler.

**Parameters:**
| Parametre | Tür | Açıklama |
| --- | --- | --- |
| obj | java.lang.Object | Mevcut dikdörtgen ile karşılaştırılacak dikdörtgen. |

**Returns:**
boolean - belirtilen dikdörtgen mevcut dikdörtgenle eşitse; aksi takdirde .
### hashCode() {#hashCode--}
```
public int hashCode()
```


Varsayılan hash işlevi olarak hizmet verir.

**Returns:**
int - Mevcut dikdörtgen için bir hash kodu.
### toString() {#toString--}
```
public String toString()
```




**Returns:**
java.lang.String
