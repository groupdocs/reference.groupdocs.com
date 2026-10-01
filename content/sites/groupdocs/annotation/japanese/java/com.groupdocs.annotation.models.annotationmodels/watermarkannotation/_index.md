---
title: "WatermarkAnnotation"
second_title: "GroupDocs.Annotation for Java API リファレンス"
description: "透かし注釈プロパティを表します"
type: docs
weight: 28
url: /ja/java/com.groupdocs.annotation.models.annotationmodels/watermarkannotation/
---
**Inheritance:**
java.lang.Object, [com.groupdocs.annotation.models.annotationmodels.AnnotationBase](../../com.groupdocs.annotation.models.annotationmodels/annotationbase)

**All Implemented Interfaces:**
[com.groupdocs.annotation.models.annotationmodels.interfaces.annotations.IWatermarkAnnotation](../../com.groupdocs.annotation.models.annotationmodels.interfaces.annotations/iwatermarkannotation)
```
public class WatermarkAnnotation extends AnnotationBase implements IWatermarkAnnotation
```

透かし注釈プロパティを表します
## コンストラクタ

| コンストラクタ | 説明 |
| --- | --- |
| [WatermarkAnnotation()](#WatermarkAnnotation--) | 新しい [WatermarkAnnotation](../../com.groupdocs.annotation.models.annotationmodels/watermarkannotation) クラスのインスタンスを初期化します。 |
## メソッド

| メソッド | 説明 |
| --- | --- |
| [getBox()](#getBox--) | アノテーションの位置を取得または設定します |
| [setBox(Rectangle value)](#setBox-com.groupdocs.annotation.models.Rectangle-) | アノテーションの位置を取得または設定します |
| [getAutoScale()](#getAutoScale--) | watermar の自動スケールを取得または設定します |
| [setAutoScale(Boolean value)](#setAutoScale-java.lang.Boolean-) | watermar の自動スケールを取得または設定します |
| [getText()](#getText--) | 透かしテキストを取得または設定します |
| [setText(String value)](#setText-java.lang.String-) | 透かしテキストを取得または設定します |
| [getFontColor()](#getFontColor--) | 透かしテキストのフォントカラーを取得または設定します |
| [setFontColor(Integer value)](#setFontColor-java.lang.Integer-) | 透かしテキストのフォントカラーを取得または設定します |
| [getFontFamily()](#getFontFamily--) | 透かしテキストのフォントファミリーを取得または設定します |
| [setFontFamily(String value)](#setFontFamily-java.lang.String-) | 透かしテキストのフォントファミリーを取得または設定します |
| [getFontSize()](#getFontSize--) | 透かしテキストのフォントサイズを取得または設定します |
| [setFontSize(Double value)](#setFontSize-java.lang.Double-) | 透かしテキストのフォントサイズを取得または設定します |
| [getOpacity()](#getOpacity--) | アノテーションの不透明度を取得または設定します |
| [setOpacity(Double value)](#setOpacity-java.lang.Double-) | アノテーションの不透明度を取得または設定します |
| [getAngle()](#getAngle--) | 透かしの回転角度を取得または設定します |
| [setAngle(Double value)](#setAngle-java.lang.Double-) | 透かしの回転角度を取得または設定します |
| [equals(WatermarkAnnotation other)](#equals-com.groupdocs.annotation.models.annotationmodels.WatermarkAnnotation-) | IEquatable の Equals メソッドを使用して透かしアノテーションを比較します |
| [equals(Object o)](#equals-java.lang.Object-) | 標準オブジェクトの Equals メソッドを使用して透かしアノテーションを比較します |
| [hashCode()](#hashCode--) | 透かしアノテーションの HashCode を返します |
| [deepClone()](#deepClone--) | 同じ値を持つ新しいインスタンスを返します |
| [getHorizontalAlignment()](#getHorizontalAlignment--) | ドキュメント上の透かしの水平配置を取得または設定します |
| [setHorizontalAlignment(Integer value)](#setHorizontalAlignment-java.lang.Integer-) | ドキュメント上の透かしの水平配置を取得または設定します |
| [getVerticalAlignment()](#getVerticalAlignment--) | ドキュメント上の透かしの垂直配置を取得または設定します |
| [setVerticalAlignment(Integer value)](#setVerticalAlignment-java.lang.Integer-) | ドキュメント上の透かしの垂直配置を取得または設定します |
| [toString()](#toString--) |  |
| [toString(ToStringStyle toStringStyle)](#toString-org.apache.commons.lang3.builder.ToStringStyle-) |  |
### WatermarkAnnotation() {#WatermarkAnnotation--}
```
public WatermarkAnnotation()
```


新しい [WatermarkAnnotation](../../com.groupdocs.annotation.models.annotationmodels/watermarkannotation) クラスのインスタンスを初期化します。

### getBox() {#getBox--}
```
public final Rectangle getBox()
```


アノテーションの位置を取得または設定します

**Returns:**
[Rectangle](../../com.groupdocs.annotation.models/rectangle)
### setBox(Rectangle value) {#setBox-com.groupdocs.annotation.models.Rectangle-}
```
public final void setBox(Rectangle value)
```


アノテーションの位置を取得または設定します

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| value | [Rectangle](../../com.groupdocs.annotation.models/rectangle) |  |

### getAutoScale() {#getAutoScale--}
```
public final Boolean getAutoScale()
```


watermar の自動スケールを取得または設定します

**Returns:**
java.lang.Boolean -
### setAutoScale(Boolean value) {#setAutoScale-java.lang.Boolean-}
```
public final void setAutoScale(Boolean value)
```


watermar の自動スケールを取得または設定します

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| 値 | java.lang.Boolean |  |

### getText() {#getText--}
```
public final String getText()
```


透かしテキストを取得または設定します

**Returns:**
java.lang.String -
### setText(String value) {#setText-java.lang.String-}
```
public final void setText(String value)
```


透かしテキストを取得または設定します

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| 値 | java.lang.String |  |

### getFontColor() {#getFontColor--}
```
public final Integer getFontColor()
```


透かしテキストのフォントカラーを取得または設定します

**Returns:**
java.lang.Integer -
### setFontColor(Integer value) {#setFontColor-java.lang.Integer-}
```
public final void setFontColor(Integer value)
```


透かしテキストのフォントカラーを取得または設定します

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| 値 | java.lang.Integer |  |

### getFontFamily() {#getFontFamily--}
```
public final String getFontFamily()
```


透かしテキストのフォントファミリーを取得または設定します

**Returns:**
java.lang.String -
### setFontFamily(String value) {#setFontFamily-java.lang.String-}
```
public final void setFontFamily(String value)
```


透かしテキストのフォントファミリーを取得または設定します

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| 値 | java.lang.String |  |

### getFontSize() {#getFontSize--}
```
public final Double getFontSize()
```


透かしテキストのフォントサイズを取得または設定します

**Returns:**
java.lang.Double -
### setFontSize(Double value) {#setFontSize-java.lang.Double-}
```
public final void setFontSize(Double value)
```


透かしテキストのフォントサイズを取得または設定します

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| 値 | java.lang.Double |  |

### getOpacity() {#getOpacity--}
```
public final Double getOpacity()
```


アノテーションの不透明度を取得または設定します

**Returns:**
java.lang.Double -
### setOpacity(Double value) {#setOpacity-java.lang.Double-}
```
public final void setOpacity(Double value)
```


アノテーションの不透明度を取得または設定します

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| 値 | java.lang.Double |  |

### getAngle() {#getAngle--}
```
public final Double getAngle()
```


透かしの回転角度を取得または設定します

**Returns:**
java.lang.Double -
### setAngle(Double value) {#setAngle-java.lang.Double-}
```
public final void setAngle(Double value)
```


透かしの回転角度を取得または設定します

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| 値 | java.lang.Double |  |

### equals(WatermarkAnnotation other) {#equals-com.groupdocs.annotation.models.annotationmodels.WatermarkAnnotation-}
```
public final boolean equals(WatermarkAnnotation other)
```


IEquatable の Equals メソッドを使用して透かしアノテーションを比較します

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| other | [WatermarkAnnotation](../../com.groupdocs.annotation.models.annotationmodels/watermarkannotation) | 現在のオブジェクトと比較する WatermarkAnnotation オブジェクト |

**Returns:**
boolean -
### equals(Object o) {#equals-java.lang.Object-}
```
public boolean equals(Object o)
```


標準オブジェクトの Equals メソッドを使用して透かしアノテーションを比較します

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| o | java.lang.Object | 現在のオブジェクトと比較するオブジェクト |

**Returns:**
boolean
### hashCode() {#hashCode--}
```
public int hashCode()
```


透かしアノテーションの HashCode を返します

**Returns:**
int
### deepClone() {#deepClone--}
```
public Object deepClone()
```


同じ値を持つ新しいインスタンスを返します

**Returns:**
java.lang.Object -
### getHorizontalAlignment() {#getHorizontalAlignment--}
```
public final Integer getHorizontalAlignment()
```


ドキュメント上の透かしの水平配置を取得または設定します

**Returns:**
java.lang.Integer -
### setHorizontalAlignment(Integer value) {#setHorizontalAlignment-java.lang.Integer-}
```
public final void setHorizontalAlignment(Integer value)
```


ドキュメント上の透かしの水平配置を取得または設定します

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| 値 | java.lang.Integer |  |

### getVerticalAlignment() {#getVerticalAlignment--}
```
public final Integer getVerticalAlignment()
```


ドキュメント上の透かしの垂直配置を取得または設定します

**Returns:**
java.lang.Integer -
### setVerticalAlignment(Integer value) {#setVerticalAlignment-java.lang.Integer-}
```
public final void setVerticalAlignment(Integer value)
```


ドキュメント上の透かしの垂直配置を取得または設定します

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| 値 | java.lang.Integer |  |

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
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| toStringStyle | org.apache.commons.lang3.builder.ToStringStyle |  |

**Returns:**
java.lang.String
