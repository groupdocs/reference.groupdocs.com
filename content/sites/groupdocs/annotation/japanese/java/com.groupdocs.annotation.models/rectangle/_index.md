---
title: "Rectangle"
second_title: "GroupDocs.Annotation for Java API リファレンス"
description: "矩形を表します。"
type: docs
weight: 13
url: /ja/java/com.groupdocs.annotation.models/rectangle/
---
**Inheritance:**
java.lang.Object
```
public class Rectangle
```

矩形を表します。
## コンストラクタ

| コンストラクタ | 説明 |
| --- | --- |
| [Rectangle()](#Rectangle--) |  |
| [Rectangle(float x, float y, float width, float height)](#Rectangle-float-float-float-float-) | 新しい [Rectangle](../../com.groupdocs.annotation.models/rectangle) クラスのインスタンスを初期化します。 |
| [Rectangle(Rectangle rectangle)](#Rectangle-com.groupdocs.annotation.models.Rectangle-) | 新しい [Rectangle](../../com.groupdocs.annotation.models/rectangle) クラスのインスタンスを初期化します。 |
## メソッド

| メソッド | 説明 |
| --- | --- |
| [opEquality(Rectangle left, Rectangle right)](#opEquality-com.groupdocs.annotation.models.Rectangle-com.groupdocs.annotation.models.Rectangle-) | 2つの Rectangle オブジェクトを比較します。 |
| [opInequality(Rectangle left, Rectangle right)](#opInequality-com.groupdocs.annotation.models.Rectangle-com.groupdocs.annotation.models.Rectangle-) | 2つの Rectangle オブジェクトを比較します。 |
| [equals(Rectangle obj1, Rectangle obj2)](#equals-com.groupdocs.annotation.models.Rectangle-com.groupdocs.annotation.models.Rectangle-) |  |
| [getX()](#getX--) | x を取得または設定します。 |
| [setX(float value)](#setX-float-) | x を取得または設定します。 |
| [getY()](#getY--) | y を取得または設定します。 |
| [setY(float value)](#setY-float-) | y を取得または設定します。 |
| [getWidth()](#getWidth--) | 幅を取得または設定します。 |
| [setWidth(float value)](#setWidth-float-) | 幅を取得または設定します。 |
| [getHeight()](#getHeight--) | 高さを取得または設定します。 |
| [setHeight(float value)](#setHeight-float-) | 高さを取得または設定します。 |
| [equals(Object obj)](#equals-java.lang.Object-) | 指定された矩形が現在の矩形と等しいかどうかを判断します。 |
| [hashCode()](#hashCode--) | デフォルトのハッシュ関数として機能します。 |
| [toString()](#toString--) |  |
### Rectangle() {#Rectangle--}
```
public Rectangle()
```


### Rectangle(float x, float y, float width, float height) {#Rectangle-float-float-float-float-}
```
public Rectangle(float x, float y, float width, float height)
```


新しい [Rectangle](../../com.groupdocs.annotation.models/rectangle) クラスのインスタンスを初期化します。

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| x | float | x. |
| y | float | y. |
| 幅 | float | 幅. |
| 高さ | float | 高さ. |

### Rectangle(Rectangle rectangle) {#Rectangle-com.groupdocs.annotation.models.Rectangle-}
```
public Rectangle(Rectangle rectangle)
```


新しい [Rectangle](../../com.groupdocs.annotation.models/rectangle) クラスのインスタンスを初期化します。

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| rectangle | [Rectangle](../../com.groupdocs.annotation.models/rectangle) | 矩形. |

### opEquality(Rectangle left, Rectangle right) {#opEquality-com.groupdocs.annotation.models.Rectangle-com.groupdocs.annotation.models.Rectangle-}
```
public static boolean opEquality(Rectangle left, Rectangle right)
```


2つの Rectangle オブジェクトを比較します。結果は、2つの Rectangle オブジェクトの Rectangle.X、Rectangle.Y、Rectangle.Width、Rectangle.Height プロパティの値が等しいかどうかを示します。

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| left | [Rectangle](../../com.groupdocs.annotation.models/rectangle) | 比較用の Rectangle。 |
| right | [Rectangle](../../com.groupdocs.annotation.models/rectangle) | 比較用の Rectangle。 |

**Returns:**
boolean - 左右の Rectangle.X、Rectangle.Y、Rectangle.Width、Rectangle.Height の値が等しい場合は true、そうでない場合は false。
### opInequality(Rectangle left, Rectangle right) {#opInequality-com.groupdocs.annotation.models.Rectangle-com.groupdocs.annotation.models.Rectangle-}
```
public static boolean opInequality(Rectangle left, Rectangle right)
```


2つの Rectangle オブジェクトを比較します。結果は、2つの Rectangle オブジェクトの Rectangle.X、Rectangle.Y、Rectangle.Width、Rectangle.Height プロパティの値が等しくないかどうかを示します。

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| left | [Rectangle](../../com.groupdocs.annotation.models/rectangle) | 比較用の Rectangle。 |
| right | [Rectangle](../../com.groupdocs.annotation.models/rectangle) | 比較用の Rectangle。 |

**Returns:**
boolean - 左右の Rectangle.X、Rectangle.Y、Rectangle.Width、Rectangle.Height の値が等しくない場合は true、そうでない場合は false。
### equals(Rectangle obj1, Rectangle obj2) {#equals-com.groupdocs.annotation.models.Rectangle-com.groupdocs.annotation.models.Rectangle-}
```
public static boolean equals(Rectangle obj1, Rectangle obj2)
```




**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| obj1 | [Rectangle](../../com.groupdocs.annotation.models/rectangle) |  |
| obj2 | [Rectangle](../../com.groupdocs.annotation.models/rectangle) |  |

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

### getWidth() {#getWidth--}
```
public final float getWidth()
```


幅を取得または設定します。

値: 幅。

**Returns:**
float -
### setWidth(float value) {#setWidth-float-}
```
public final void setWidth(float value)
```


幅を取得または設定します。

値: 幅。

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| 値 | float |  |

### getHeight() {#getHeight--}
```
public final float getHeight()
```


高さを取得または設定します。

値: 高さ。

**Returns:**
float -
### setHeight(float value) {#setHeight-float-}
```
public final void setHeight(float value)
```


高さを取得または設定します。

値: 高さ。

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| 値 | float |  |

### equals(Object obj) {#equals-java.lang.Object-}
```
public boolean equals(Object obj)
```


指定された矩形が現在の矩形と等しいかどうかを判断します。

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| obj | java.lang.Object | 現在の矩形と比較する矩形。 |

**Returns:**
boolean - 指定された矩形が現在の矩形と等しい場合は true、そうでない場合は false。
### hashCode() {#hashCode--}
```
public int hashCode()
```


デフォルトのハッシュ関数として機能します。

**Returns:**
int - 現在の矩形のハッシュコード。
### toString() {#toString--}
```
public String toString()
```




**Returns:**
java.lang.String
