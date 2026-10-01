---
title: "ReplacementAnnotation"
second_title: "GroupDocs.Annotation for Java API リファレンス"
description: "置換注釈プロパティを表します"
type: docs
weight: 20
url: /ja/java/com.groupdocs.annotation.models.annotationmodels/replacementannotation/
---
**Inheritance:**
java.lang.Object, [com.groupdocs.annotation.models.annotationmodels.AnnotationBase](../../com.groupdocs.annotation.models.annotationmodels/annotationbase)

**All Implemented Interfaces:**
[com.groupdocs.annotation.models.annotationmodels.interfaces.annotations.IReplacementAnnotation](../../com.groupdocs.annotation.models.annotationmodels.interfaces.annotations/ireplacementannotation)
```
public class ReplacementAnnotation extends AnnotationBase implements IReplacementAnnotation
```

置換注釈プロパティを表します
## コンストラクタ

| コンストラクタ | 説明 |
| --- | --- |
| [ReplacementAnnotation()](#ReplacementAnnotation--) | 新しい [ReplacementAnnotation](../../com.groupdocs.annotation.models.annotationmodels/replacementannotation) クラスのインスタンスを初期化します。 |
## メソッド

| メソッド | 説明 |
| --- | --- |
| [getFontColor()](#getFontColor--) | 注釈テキストのフォント色を取得または設定します |
| [setFontColor(Integer value)](#setFontColor-java.lang.Integer-) | 注釈テキストのフォント色を取得または設定します |
| [getBackgroundColor()](#getBackgroundColor--) | アノテーションの背景色を取得します |
| [setBackgroundColor(Integer value)](#setBackgroundColor-java.lang.Integer-) | アノテーションの背景色を設定します |
| [getFontSize()](#getFontSize--) | 注釈テキストのフォントサイズを取得または設定します |
| [setFontSize(Double value)](#setFontSize-java.lang.Double-) | 注釈テキストのフォントサイズを取得または設定します |
| [getOpacity()](#getOpacity--) | アノテーションの不透明度を取得または設定します |
| [setOpacity(Double value)](#setOpacity-java.lang.Double-) | アノテーションの不透明度を取得または設定します |
| [getPoints()](#getPoints--) | テキスト付きの矩形を記述するポイントのコレクションを取得または設定します |
| [setPoints(List<Point> value)](#setPoints-java.util.List-com.groupdocs.annotation.models.Point--) | テキスト付きの矩形を記述するポイントのコレクションを取得または設定します |
| [getTextToReplace()](#getTextToReplace--) | 置換されるテキストを取得または設定します |
| [setTextToReplace(String value)](#setTextToReplace-java.lang.String-) | 置換されるテキストを取得または設定します |
| [equals(ReplacementAnnotation other)](#equals-com.groupdocs.annotation.models.annotationmodels.ReplacementAnnotation-) | IEquatable Equals メソッドを使用して Replacement Annotations を比較します |
| [equals(Object o)](#equals-java.lang.Object-) | 標準の object Equals メソッドを使用して Replacement Annotations を比較します |
| [hashCode()](#hashCode--) | Replacement Annotation の HashCode を返します |
| [deepClone()](#deepClone--) | 同じ値を持つ新しいインスタンスを返します |
| [toString()](#toString--) |  |
| [toString(ToStringStyle toStringStyle)](#toString-org.apache.commons.lang3.builder.ToStringStyle-) |  |
### ReplacementAnnotation() {#ReplacementAnnotation--}
```
public ReplacementAnnotation()
```


新しい [ReplacementAnnotation](../../com.groupdocs.annotation.models.annotationmodels/replacementannotation) クラスのインスタンスを初期化します。

### getFontColor() {#getFontColor--}
```
public final Integer getFontColor()
```


注釈テキストのフォント色を取得または設定します

**Returns:**
java.lang.Integer -
### setFontColor(Integer value) {#setFontColor-java.lang.Integer-}
```
public final void setFontColor(Integer value)
```


注釈テキストのフォント色を取得または設定します

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| 値 | java.lang.Integer |  |

### getBackgroundColor() {#getBackgroundColor--}
```
public final Integer getBackgroundColor()
```


アノテーションの背景色を取得します

**Returns:**
java.lang.Integer -
### setBackgroundColor(Integer value) {#setBackgroundColor-java.lang.Integer-}
```
public final void setBackgroundColor(Integer value)
```


アノテーションの背景色を設定します

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| 値 | java.lang.Integer |  |

### getFontSize() {#getFontSize--}
```
public final Double getFontSize()
```


注釈テキストのフォントサイズを取得または設定します

**Returns:**
java.lang.Double -
### setFontSize(Double value) {#setFontSize-java.lang.Double-}
```
public final void setFontSize(Double value)
```


注釈テキストのフォントサイズを取得または設定します

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

### getPoints() {#getPoints--}
```
public final List<Point> getPoints()
```


テキスト付きの矩形を記述するポイントのコレクションを取得または設定します

**Returns:**
java.util.List<com.groupdocs.annotation.models.Point> -
### setPoints(List<Point> value) {#setPoints-java.util.List-com.groupdocs.annotation.models.Point--}
```
public final void setPoints(List<Point> value)
```


テキスト付きの矩形を記述するポイントのコレクションを取得または設定します

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| 値 | java.util.List<com.groupdocs.annotation.models.Point> |  |

### getTextToReplace() {#getTextToReplace--}
```
public final String getTextToReplace()
```


置換されるテキストを取得または設定します

**Returns:**
java.lang.String -
### setTextToReplace(String value) {#setTextToReplace-java.lang.String-}
```
public final void setTextToReplace(String value)
```


置換されるテキストを取得または設定します

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| 値 | java.lang.String |  |

### equals(ReplacementAnnotation other) {#equals-com.groupdocs.annotation.models.annotationmodels.ReplacementAnnotation-}
```
public final boolean equals(ReplacementAnnotation other)
```


IEquatable Equals メソッドを使用して Replacement Annotations を比較します

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| other | [ReplacementAnnotation](../../com.groupdocs.annotation.models.annotationmodels/replacementannotation) | 現在のオブジェクトと比較するための ReplacementAnnotation オブジェクト |

**Returns:**
boolean -
### equals(Object o) {#equals-java.lang.Object-}
```
public boolean equals(Object o)
```


標準の object Equals メソッドを使用して Replacement Annotations を比較します

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


Replacement Annotation の HashCode を返します

**Returns:**
int
### deepClone() {#deepClone--}
```
public Object deepClone()
```


同じ値を持つ新しいインスタンスを返します

**Returns:**
java.lang.Object
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
