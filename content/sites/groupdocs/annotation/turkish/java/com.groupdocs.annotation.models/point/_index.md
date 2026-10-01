---
title: "Point"
second_title: "GroupDocs.Annotation Java için API Referansı"
description: "Noktayı temsil eder."
type: docs
weight: 12
url: /tr/java/com.groupdocs.annotation.models/point/
---
**Inheritance:**
java.lang.Object
```
public class Point
```

Noktayı temsil eder.
## Yapıcılar

| Yapıcı | Açıklama |
| --- | --- |
| [Point()](#Point--) |  |
| [Point(float x, float y)](#Point-float-float-) | Yeni bir [Point](../../com.groupdocs.annotation.models/point) struct örneği başlatır. |
| [Point(Point point)](#Point-com.groupdocs.annotation.models.Point-) | Yeni bir [Point](../../com.groupdocs.annotation.models/point) sınıf örneği başlatır. |
## Metotlar

| Metot | Açıklama |
| --- | --- |
| [isPointCollectionsEqual(List<Point> points1, List<Point> points2)](#isPointCollectionsEqual-java.util.List-com.groupdocs.annotation.models.Point--java.util.List-com.groupdocs.annotation.models.Point--) |  |
| [opEquality(Point left, Point right)](#opEquality-com.groupdocs.annotation.models.Point-com.groupdocs.annotation.models.Point-) | İki Point nesnesini karşılaştırır. |
| [opInequality(Point left, Point right)](#opInequality-com.groupdocs.annotation.models.Point-com.groupdocs.annotation.models.Point-) | İki Point nesnesini karşılaştırır. |
| [equals(Point obj1, Point obj2)](#equals-com.groupdocs.annotation.models.Point-com.groupdocs.annotation.models.Point-) |  |
| [getX()](#getX--) | x değerini alır veya ayarlar. |
| [setX(float value)](#setX-float-) | x değerini alır veya ayarlar. |
| [getY()](#getY--) | y değerini alır veya ayarlar. |
| [setY(float value)](#setY-float-) | y değerini alır veya ayarlar. |
| [equals(Object obj)](#equals-java.lang.Object-) | Belirtilen noktanın geçerli nokta ile eşit olup olmadığını belirler. |
| [hashCode()](#hashCode--) | Varsayılan hash işlevi olarak hizmet verir. |
| [toString()](#toString--) |  |
### Point() {#Point--}
```
public Point()
```


### Point(float x, float y) {#Point-float-float-}
```
public Point(float x, float y)
```


Yeni bir [Point](../../com.groupdocs.annotation.models/point) struct örneği başlatır.

**Parameters:**
| Parametre | Tür | Açıklama |
| --- | --- | --- |
| x | float | x. |
| y | float | y. |

### Point(Point point) {#Point-com.groupdocs.annotation.models.Point-}
```
public Point(Point point)
```


Yeni bir [Point](../../com.groupdocs.annotation.models/point) sınıf örneği başlatır.

**Parameters:**
| Parametre | Tür | Açıklama |
| --- | --- | --- |
| point | [Point](../../com.groupdocs.annotation.models/point) | Nokta kaynağı. |

### isPointCollectionsEqual(List<Point> points1, List<Point> points2) {#isPointCollectionsEqual-java.util.List-com.groupdocs.annotation.models.Point--java.util.List-com.groupdocs.annotation.models.Point--}
```
public static boolean isPointCollectionsEqual(List<Point> points1, List<Point> points2)
```




**Parameters:**
| Parametre | Tür | Açıklama |
| --- | --- | --- |
| points1 | java.util.List<com.groupdocs.annotation.models.Point> |  |
| points2 | java.util.List<com.groupdocs.annotation.models.Point> |  |

**Returns:**
boolean
### opEquality(Point left, Point right) {#opEquality-com.groupdocs.annotation.models.Point-com.groupdocs.annotation.models.Point-}
```
public static boolean opEquality(Point left, Point right)
```


İki Point nesnesini karşılaştırır. Sonuç, iki Point nesnesinin Point.X ve Point.Y özellik değerlerinin eşit olup olmadığını belirtir.

**Parameters:**
| Parametre | Tür | Açıklama |
| --- | --- | --- |
| left | [Point](../../com.groupdocs.annotation.models/point) | Karşılaştırılacak bir Point. |
| right | [Point](../../com.groupdocs.annotation.models/point) | Karşılaştırılacak bir Point. |

**Returns:**
boolean - sol ve sağın Point.X ve Point.Y değerleri eşitse true; aksi takdirde false.
### opInequality(Point left, Point right) {#opInequality-com.groupdocs.annotation.models.Point-com.groupdocs.annotation.models.Point-}
```
public static boolean opInequality(Point left, Point right)
```


İki Point nesnesini karşılaştırır. Sonuç, iki Point nesnesinin Point.X ve Point.Y özellik değerlerinin eşit olmaması durumunu belirtir.

**Parameters:**
| Parametre | Tür | Açıklama |
| --- | --- | --- |
| left | [Point](../../com.groupdocs.annotation.models/point) | Karşılaştırılacak bir Point. |
| right | [Point](../../com.groupdocs.annotation.models/point) | Karşılaştırılacak bir Point. |

**Returns:**
boolean - sol ve sağın Point.X ve Point.Y değerleri eşit değilse true; aksi takdirde false.
### equals(Point obj1, Point obj2) {#equals-com.groupdocs.annotation.models.Point-com.groupdocs.annotation.models.Point-}
```
public static boolean equals(Point obj1, Point obj2)
```




**Parameters:**
| Parametre | Tür | Açıklama |
| --- | --- | --- |
| obj1 | [Point](../../com.groupdocs.annotation.models/point) |  |
| obj2 | [Point](../../com.groupdocs.annotation.models/point) |  |

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

### equals(Object obj) {#equals-java.lang.Object-}
```
public boolean equals(Object obj)
```


Belirtilen noktanın geçerli nokta ile eşit olup olmadığını belirler.

**Parameters:**
| Parametre | Tür | Açıklama |
| --- | --- | --- |
| obj | java.lang.Object | Geçerli nokta ile karşılaştırılacak nokta. |

**Returns:**
boolean -   belirtilen nokta geçerli noktaya eşitse; aksi takdirde,  .
### hashCode() {#hashCode--}
```
public int hashCode()
```


Varsayılan hash işlevi olarak hizmet verir.

**Returns:**
int - Geçerli nokta için bir karma kodu.
### toString() {#toString--}
```
public String toString()
```




**Returns:**
java.lang.String
