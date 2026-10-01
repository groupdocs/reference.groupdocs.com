---
title: "LinkAnnotation"
second_title: "GroupDocs.Annotation for Java API リファレンス"
description: "リンク注釈プロパティを表します"
type: docs
weight: 17
url: /ja/java/com.groupdocs.annotation.models.annotationmodels/linkannotation/
---
**Inheritance:**
java.lang.Object, [com.groupdocs.annotation.models.annotationmodels.AnnotationBase](../../com.groupdocs.annotation.models.annotationmodels/annotationbase)

**All Implemented Interfaces:**
[com.groupdocs.annotation.models.annotationmodels.interfaces.annotations.ILinkAnnotation](../../com.groupdocs.annotation.models.annotationmodels.interfaces.annotations/ilinkannotation)
```
public class LinkAnnotation extends AnnotationBase implements ILinkAnnotation
```

リンク注釈プロパティを表します
## コンストラクタ

| コンストラクタ | 説明 |
| --- | --- |
| [LinkAnnotation()](#LinkAnnotation--) | 新しい [LinkAnnotation](../../com.groupdocs.annotation.models.annotationmodels/linkannotation) クラスのインスタンスを初期化します。 |
## メソッド

| メソッド | 説明 |
| --- | --- |
| [getFontColor()](#getFontColor--) | 注釈テキストのフォント色を取得または設定します |
| [setFontColor(Integer value)](#setFontColor-java.lang.Integer-) | 注釈テキストのフォント色を取得または設定します |
| [getBackgroundColor()](#getBackgroundColor--) | 注釈テキストのフォント色を取得または設定します |
| [setBackgroundColor(Integer value)](#setBackgroundColor-java.lang.Integer-) | 注釈テキストのフォント色を取得または設定します |
| [getOpacity()](#getOpacity--) | アノテーションの不透明度を取得または設定します |
| [setOpacity(Double value)](#setOpacity-java.lang.Double-) | アノテーションの不透明度を取得または設定します |
| [getPoints()](#getPoints--) | 座標 |
| [setPoints(List<Point> value)](#setPoints-java.util.List-com.groupdocs.annotation.models.Point--) | 座標 |
| [getUrl()](#getUrl--) | アノテーションリンクの URL を取得または設定します |
| [setUrl(String value)](#setUrl-java.lang.String-) | アノテーションリンクの URL を取得または設定します |
| [equals(LinkAnnotation other)](#equals-com.groupdocs.annotation.models.annotationmodels.LinkAnnotation-) | IEquatable Equals メソッドを使用して Link Annotations を比較します |
| [equals(Object o)](#equals-java.lang.Object-) | 標準オブジェクトの Equals メソッドを使用して Link Annotations を比較します |
| [hashCode()](#hashCode--) | Link Annotation の HashCode を返します |
| [deepClone()](#deepClone--) | 同じ値を持つ新しいインスタンスを返します |
| [toString()](#toString--) |  |
| [toString(ToStringStyle toStringStyle)](#toString-org.apache.commons.lang3.builder.ToStringStyle-) |  |
### LinkAnnotation() {#LinkAnnotation--}
```
public LinkAnnotation()
```


新しい [LinkAnnotation](../../com.groupdocs.annotation.models.annotationmodels/linkannotation) クラスのインスタンスを初期化します。

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


注釈テキストのフォント色を取得または設定します

**Returns:**
java.lang.Integer -
### setBackgroundColor(Integer value) {#setBackgroundColor-java.lang.Integer-}
```
public final void setBackgroundColor(Integer value)
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


座標

**Returns:**
java.util.List<com.groupdocs.annotation.models.Point> -
### setPoints(List<Point> value) {#setPoints-java.util.List-com.groupdocs.annotation.models.Point--}
```
public final void setPoints(List<Point> value)
```


座標

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| 値 | java.util.List<com.groupdocs.annotation.models.Point> |  |

### getUrl() {#getUrl--}
```
public final String getUrl()
```


アノテーションリンクの URL を取得または設定します

**Returns:**
java.lang.String -
### setUrl(String value) {#setUrl-java.lang.String-}
```
public final void setUrl(String value)
```


アノテーションリンクの URL を取得または設定します

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| 値 | java.lang.String |  |

### equals(LinkAnnotation other) {#equals-com.groupdocs.annotation.models.annotationmodels.LinkAnnotation-}
```
public final boolean equals(LinkAnnotation other)
```


IEquatable Equals メソッドを使用して Link Annotations を比較します

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| other | [LinkAnnotation](../../com.groupdocs.annotation.models.annotationmodels/linkannotation) | 現在のオブジェクトと比較するための LinkAnnotation オブジェクト |

**Returns:**
boolean -
### equals(Object o) {#equals-java.lang.Object-}
```
public boolean equals(Object o)
```


標準オブジェクトの Equals メソッドを使用して Link Annotations を比較します

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


Link Annotation の HashCode を返します

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
