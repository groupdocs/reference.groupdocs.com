---
title: "PointAnnotation"
second_title: "GroupDocs.Annotation for Java API リファレンス"
description: "ポイント注釈プロパティを表します"
type: docs
weight: 18
url: /ja/java/com.groupdocs.annotation.models.annotationmodels/pointannotation/
---
**Inheritance:**
java.lang.Object, [com.groupdocs.annotation.models.annotationmodels.AnnotationBase](../../com.groupdocs.annotation.models.annotationmodels/annotationbase)

**All Implemented Interfaces:**
[com.groupdocs.annotation.models.annotationmodels.interfaces.annotations.IPointAnnotation](../../com.groupdocs.annotation.models.annotationmodels.interfaces.annotations/ipointannotation)
```
public class PointAnnotation extends AnnotationBase implements IPointAnnotation
```

ポイント注釈プロパティを表します
## コンストラクタ

| コンストラクタ | 説明 |
| --- | --- |
| [PointAnnotation()](#PointAnnotation--) | 新しい [PointAnnotation](../../com.groupdocs.annotation.models.annotationmodels/pointannotation) クラスのインスタンスを初期化します。 |
## メソッド

| メソッド | 説明 |
| --- | --- |
| [getBox()](#getBox--) | アノテーションの位置を取得または設定します |
| [setBox(Rectangle value)](#setBox-com.groupdocs.annotation.models.Rectangle-) | アノテーションの位置を取得または設定します |
| [equals(PointAnnotation other)](#equals-com.groupdocs.annotation.models.annotationmodels.PointAnnotation-) | IEquatable Equals メソッドを使用して Point 注釈を比較します |
| [equals(Object o)](#equals-java.lang.Object-) | 標準のオブジェクト Equals メソッドを使用して Point 注釈を比較します |
| [hashCode()](#hashCode--) | Point 注釈のハッシュコードを返します |
| [deepClone()](#deepClone--) | 同じ値を持つ新しいインスタンスを返します |
| [toString()](#toString--) |  |
| [toString(ToStringStyle toStringStyle)](#toString-org.apache.commons.lang3.builder.ToStringStyle-) |  |
### PointAnnotation() {#PointAnnotation--}
```
public PointAnnotation()
```


新しい [PointAnnotation](../../com.groupdocs.annotation.models.annotationmodels/pointannotation) クラスのインスタンスを初期化します。

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

### equals(PointAnnotation other) {#equals-com.groupdocs.annotation.models.annotationmodels.PointAnnotation-}
```
public final boolean equals(PointAnnotation other)
```


IEquatable Equals メソッドを使用して Point 注釈を比較します

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| other | [PointAnnotation](../../com.groupdocs.annotation.models.annotationmodels/pointannotation) | 現在のオブジェクトと比較するための PointAnnotation オブジェクト |

**Returns:**
boolean -
### equals(Object o) {#equals-java.lang.Object-}
```
public boolean equals(Object o)
```


標準のオブジェクト Equals メソッドを使用して Point 注釈を比較します

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


Point 注釈のハッシュコードを返します

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
