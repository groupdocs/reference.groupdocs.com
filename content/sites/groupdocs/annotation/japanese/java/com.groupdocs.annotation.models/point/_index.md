---
title: "Point"
second_title: "GroupDocs.Annotation for Java API リファレンス"
description: "点を表します。"
type: docs
weight: 12
url: /ja/java/com.groupdocs.annotation.models/point/
---
**Inheritance:**
java.lang.Object
```
public class Point
```

点を表します。
## コンストラクタ

| コンストラクタ | 説明 |
| --- | --- |
| [Point()](#Point--) |  |
| [Point(float x, float y)](#Point-float-float-) | 新しいインスタンスの [Point](../../com.groupdocs.annotation.models/point) 構造体を初期化します。 |
| [Point(Point point)](#Point-com.groupdocs.annotation.models.Point-) | 新しいインスタンスの [Point](../../com.groupdocs.annotation.models/point) クラスを初期化します。 |
## メソッド

| メソッド | 説明 |
| --- | --- |
| [isPointCollectionsEqual(List<Point> points1, List<Point> points2)](#isPointCollectionsEqual-java.util.List-com.groupdocs.annotation.models.Point--java.util.List-com.groupdocs.annotation.models.Point--) |  |
| [opEquality(Point left, Point right)](#opEquality-com.groupdocs.annotation.models.Point-com.groupdocs.annotation.models.Point-) | 2つの Point オブジェクトを比較します。 |
| [opInequality(Point left, Point right)](#opInequality-com.groupdocs.annotation.models.Point-com.groupdocs.annotation.models.Point-) | 2つの Point オブジェクトを比較します。 |
| [equals(Point obj1, Point obj2)](#equals-com.groupdocs.annotation.models.Point-com.groupdocs.annotation.models.Point-) |  |
| [getX()](#getX--) | x を取得または設定します。 |
| [setX(float value)](#setX-float-) | x を取得または設定します。 |
| [getY()](#getY--) | y を取得または設定します。 |
| [setY(float value)](#setY-float-) | y を取得または設定します。 |
| [equals(Object obj)](#equals-java.lang.Object-) | 指定されたポイントが現在のポイントと等しいかどうかを判断します。 |
| [hashCode()](#hashCode--) | デフォルトのハッシュ関数として機能します。 |
| [toString()](#toString--) |  |
### Point() {#Point--}
```
public Point()
```


### Point(float x, float y) {#Point-float-float-}
```
public Point(float x, float y)
```


新しいインスタンスの [Point](../../com.groupdocs.annotation.models/point) 構造体を初期化します。

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| x | float | x. |
| y | float | y. |

### Point(Point point) {#Point-com.groupdocs.annotation.models.Point-}
```
public Point(Point point)
```


新しいインスタンスの [Point](../../com.groupdocs.annotation.models/point) クラスを初期化します。

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| point | [Point](../../com.groupdocs.annotation.models/point) | ポイントのソース。 |

### isPointCollectionsEqual(List<Point> points1, List<Point> points2) {#isPointCollectionsEqual-java.util.List-com.groupdocs.annotation.models.Point--java.util.List-com.groupdocs.annotation.models.Point--}
```
public static boolean isPointCollectionsEqual(List<Point> points1, List<Point> points2)
```




**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| points1 | java.util.List<com.groupdocs.annotation.models.Point> |  |
| points2 | java.util.List<com.groupdocs.annotation.models.Point> |  |

**Returns:**
boolean
### opEquality(Point left, Point right) {#opEquality-com.groupdocs.annotation.models.Point-com.groupdocs.annotation.models.Point-}
```
public static boolean opEquality(Point left, Point right)
```


2つの Point オブジェクトを比較します。結果は、2つの Point オブジェクトの Point.X および Point.Y プロパティの値が等しいかどうかを示します。

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| left | [Point](../../com.groupdocs.annotation.models/point) | 比較する Point。 |
| right | [Point](../../com.groupdocs.annotation.models/point) | 比較する Point。 |

**Returns:**
boolean - 左右の Point.X と Point.Y の値が等しい場合は true、そうでない場合は false。
### opInequality(Point left, Point right) {#opInequality-com.groupdocs.annotation.models.Point-com.groupdocs.annotation.models.Point-}
```
public static boolean opInequality(Point left, Point right)
```


2つの Point オブジェクトを比較します。結果は、2つの Point オブジェクトの Point.X および Point.Y プロパティの値が等しくないかどうかを示します。

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| left | [Point](../../com.groupdocs.annotation.models/point) | 比較する Point。 |
| right | [Point](../../com.groupdocs.annotation.models/point) | 比較する Point。 |

**Returns:**
boolean - 左右の Point.X と Point.Y の値が等しくない場合は true、そうでない場合は false。
### equals(Point obj1, Point obj2) {#equals-com.groupdocs.annotation.models.Point-com.groupdocs.annotation.models.Point-}
```
public static boolean equals(Point obj1, Point obj2)
```




**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| obj1 | [Point](../../com.groupdocs.annotation.models/point) |  |
| obj2 | [Point](../../com.groupdocs.annotation.models/point) |  |

**Returns:**
boolean
### getX() {#getX--}
```
public final float getX()
```


x を取得または設定します。

値: x。

**Returns:**
float -
### setX(float value) {#setX-float-}
```
public final void setX(float value)
```


x を取得または設定します。

値: x。

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| 値 | float |  |

### getY() {#getY--}
```
public final float getY()
```


y を取得または設定します。

値: y。

**Returns:**
float -
### setY(float value) {#setY-float-}
```
public final void setY(float value)
```


y を取得または設定します。

値: y。

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| 値 | float |  |

### equals(Object obj) {#equals-java.lang.Object-}
```
public boolean equals(Object obj)
```


指定されたポイントが現在のポイントと等しいかどうかを判断します。

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| obj | java.lang.Object | 現在のポイントと比較するポイント。 |

**Returns:**
boolean -   指定されたポイントが現在のポイントと等しい場合; それ以外の場合、  .
### hashCode() {#hashCode--}
```
public int hashCode()
```


デフォルトのハッシュ関数として機能します。

**Returns:**
int - 現在のポイントのハッシュコード。
### toString() {#toString--}
```
public String toString()
```




**Returns:**
java.lang.String
