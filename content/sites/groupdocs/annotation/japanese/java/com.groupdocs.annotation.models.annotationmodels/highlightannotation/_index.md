---
title: "HighlightAnnotation"
second_title: "GroupDocs.Annotation for Java API リファレンス"
description: "ハイライト注釈プロパティを表します"
type: docs
weight: 15
url: /ja/java/com.groupdocs.annotation.models.annotationmodels/highlightannotation/
---
**Inheritance:**
java.lang.Object, [com.groupdocs.annotation.models.annotationmodels.AnnotationBase](../../com.groupdocs.annotation.models.annotationmodels/annotationbase)

**All Implemented Interfaces:**
[com.groupdocs.annotation.models.annotationmodels.interfaces.annotations.IHighlightAnnotation](../../com.groupdocs.annotation.models.annotationmodels.interfaces.annotations/ihighlightannotation)
```
public class HighlightAnnotation extends AnnotationBase implements IHighlightAnnotation
```

ハイライト注釈プロパティを表します
## コンストラクタ

| コンストラクタ | 説明 |
| --- | --- |
| [HighlightAnnotation()](#HighlightAnnotation--) | 新しい [HighlightAnnotation](../../com.groupdocs.annotation.models.annotationmodels/highlightannotation) クラスのインスタンスを初期化します。 |
## メソッド

| メソッド | 説明 |
| --- | --- |
| [getBackgroundColor()](#getBackgroundColor--) | 注釈の背景色を取得または設定します |
| [setBackgroundColor(Integer value)](#setBackgroundColor-java.lang.Integer-) | 注釈の背景色を取得または設定します |
| [getFontColor()](#getFontColor--) | 注釈テキストのフォント色を取得または設定します |
| [setFontColor(Integer value)](#setFontColor-java.lang.Integer-) | 注釈テキストのフォント色を取得または設定します |
| [getOpacity()](#getOpacity--) | アノテーションの不透明度を取得または設定します |
| [setOpacity(Double value)](#setOpacity-java.lang.Double-) | アノテーションの不透明度を取得または設定します |
| [getPoints()](#getPoints--) | テキスト付きの矩形を記述するポイントのコレクションを取得または設定します |
| [setPoints(List<Point> value)](#setPoints-java.util.List-com.groupdocs.annotation.models.Point--) | テキスト付きの矩形を記述するポイントのコレクションを取得または設定します |
| [equals(HighlightAnnotation other)](#equals-com.groupdocs.annotation.models.annotationmodels.HighlightAnnotation-) | IEquatable の Equals メソッドを使用して Highlight Annotations を比較します |
| [equals(Object obj)](#equals-java.lang.Object-) | 標準のオブジェクト Equals メソッドを使用して Highlight Annotations を比較します |
| [hashCode()](#hashCode--) | Highlight Annotation のハッシュコードを返します |
| [deepClone()](#deepClone--) | 同じ値を持つ新しいインスタンスを返します |
| [toString()](#toString--) |  |
| [toString(ToStringStyle toStringStyle)](#toString-org.apache.commons.lang3.builder.ToStringStyle-) |  |
### HighlightAnnotation() {#HighlightAnnotation--}
```
public HighlightAnnotation()
```


新しい [HighlightAnnotation](../../com.groupdocs.annotation.models.annotationmodels/highlightannotation) クラスのインスタンスを初期化します。

### getBackgroundColor() {#getBackgroundColor--}
```
public final Integer getBackgroundColor()
```


注釈の背景色を取得または設定します

**Returns:**
java.lang.Integer
### setBackgroundColor(Integer value) {#setBackgroundColor-java.lang.Integer-}
```
public final void setBackgroundColor(Integer value)
```


注釈の背景色を取得または設定します

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| 値 | java.lang.Integer |  |

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

### equals(HighlightAnnotation other) {#equals-com.groupdocs.annotation.models.annotationmodels.HighlightAnnotation-}
```
public final boolean equals(HighlightAnnotation other)
```


IEquatable の Equals メソッドを使用して Highlight Annotations を比較します

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| other | [HighlightAnnotation](../../com.groupdocs.annotation.models.annotationmodels/highlightannotation) | 現在のオブジェクトと比較するための HighlightAnnotation オブジェクト |

**Returns:**
boolean -
### equals(Object obj) {#equals-java.lang.Object-}
```
public boolean equals(Object obj)
```


標準のオブジェクト Equals メソッドを使用して Highlight Annotations を比較します

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| obj | java.lang.Object | 現在のオブジェクトと比較するオブジェクト |

**Returns:**
boolean
### hashCode() {#hashCode--}
```
public int hashCode()
```


Highlight Annotation のハッシュコードを返します

**Returns:**
int
### deepClone() {#deepClone--}
```
public Object deepClone()
```


同じ値を持つ新しいインスタンスを返します

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
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| toStringStyle | org.apache.commons.lang3.builder.ToStringStyle |  |

**Returns:**
java.lang.String
