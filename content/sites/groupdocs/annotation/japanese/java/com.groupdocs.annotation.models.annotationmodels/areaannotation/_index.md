---
title: "AreaAnnotation"
second_title: "GroupDocs.Annotation for Java API リファレンス"
description: "エリア注釈プロパティを表します"
type: docs
weight: 11
url: /ja/java/com.groupdocs.annotation.models.annotationmodels/areaannotation/
---
**Inheritance:**
java.lang.Object, [com.groupdocs.annotation.models.annotationmodels.AnnotationBase](../../com.groupdocs.annotation.models.annotationmodels/annotationbase), com.groupdocs.annotation.models.annotationmodels.AnnotationBaseProps

**All Implemented Interfaces:**
[com.groupdocs.annotation.models.annotationmodels.interfaces.annotations.IAreaAnnotation](../../com.groupdocs.annotation.models.annotationmodels.interfaces.annotations/iareaannotation)
```
public class AreaAnnotation extends AnnotationBaseProps implements IAreaAnnotation
```

エリア注釈プロパティを表します
## コンストラクタ

| コンストラクタ | 説明 |
| --- | --- |
| [AreaAnnotation()](#AreaAnnotation--) | 新しい [AreaAnnotation](../../com.groupdocs.annotation.models.annotationmodels/areaannotation) クラスのインスタンスを初期化します。 |
## メソッド

| メソッド | 説明 |
| --- | --- |
| [getPenStyle()](#getPenStyle--) | アノテーションのペンのスタイルを取得または設定します |
| [setPenStyle(Byte value)](#setPenStyle-java.lang.Byte-) | アノテーションのペンのスタイルを取得または設定します |
| [equals(AreaAnnotation other)](#equals-com.groupdocs.annotation.models.annotationmodels.AreaAnnotation-) | IEquatable Equals メソッドを使用して Area Annotations を比較します |
| [deepClone()](#deepClone--) | 同じ値を持つ新しいインスタンスを返します |
| [equals(Object o)](#equals-java.lang.Object-) |  |
| [hashCode()](#hashCode--) |  |
| [toString()](#toString--) |  |
| [toString(ToStringStyle toStringStyle)](#toString-org.apache.commons.lang3.builder.ToStringStyle-) |  |
### AreaAnnotation() {#AreaAnnotation--}
```
public AreaAnnotation()
```


新しい [AreaAnnotation](../../com.groupdocs.annotation.models.annotationmodels/areaannotation) クラスのインスタンスを初期化します。

### getPenStyle() {#getPenStyle--}
```
public final Byte getPenStyle()
```


アノテーションのペンのスタイルを取得または設定します

**Returns:**
java.lang.Byte -
### setPenStyle(Byte value) {#setPenStyle-java.lang.Byte-}
```
public final void setPenStyle(Byte value)
```


アノテーションのペンのスタイルを取得または設定します

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| 値 | java.lang.Byte |  |

### equals(AreaAnnotation other) {#equals-com.groupdocs.annotation.models.annotationmodels.AreaAnnotation-}
```
public final boolean equals(AreaAnnotation other)
```


IEquatable Equals メソッドを使用して Area Annotations を比較します

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| other | [AreaAnnotation](../../com.groupdocs.annotation.models.annotationmodels/areaannotation) | 現在のオブジェクトと比較するための AreaAnnotation オブジェクト |

**Returns:**
boolean -
### deepClone() {#deepClone--}
```
public Object deepClone()
```


同じ値を持つ新しいインスタンスを返します

**Returns:**
java.lang.Object -
### equals(Object o) {#equals-java.lang.Object-}
```
public boolean equals(Object o)
```


標準オブジェクトの Equals メソッドを使用して Base アノテーションを比較します

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| o | java.lang.Object |  |

**Returns:**
boolean
### hashCode() {#hashCode--}
```
public int hashCode()
```


AnnotationBase の Message、PageNumber、Type プロパティの HashCode を返します

**Returns:**
int
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
