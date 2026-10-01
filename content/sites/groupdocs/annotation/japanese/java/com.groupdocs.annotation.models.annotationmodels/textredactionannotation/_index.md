---
title: "TextRedactionAnnotation"
second_title: "GroupDocs.Annotation for Java API リファレンス"
description: "テキスト削除注釈プロパティを表します"
type: docs
weight: 26
url: /ja/java/com.groupdocs.annotation.models.annotationmodels/textredactionannotation/
---
**Inheritance:**
java.lang.Object, [com.groupdocs.annotation.models.annotationmodels.AnnotationBase](../../com.groupdocs.annotation.models.annotationmodels/annotationbase)

**All Implemented Interfaces:**
[com.groupdocs.annotation.models.annotationmodels.interfaces.annotations.ITextRedactionAnnotation](../../com.groupdocs.annotation.models.annotationmodels.interfaces.annotations/itextredactionannotation)
```
public class TextRedactionAnnotation extends AnnotationBase implements ITextRedactionAnnotation
```

テキスト削除注釈プロパティを表します
## コンストラクタ

| コンストラクタ | 説明 |
| --- | --- |
| [TextRedactionAnnotation()](#TextRedactionAnnotation--) | 新しい [TextRedactionAnnotation](../../com.groupdocs.annotation.models.annotationmodels/textredactionannotation) クラスのインスタンスを初期化します。 |
## メソッド

| メソッド | 説明 |
| --- | --- |
| [getFontColor()](#getFontColor--) | 注釈テキストのフォント色を取得または設定します |
| [setFontColor(Integer value)](#setFontColor-java.lang.Integer-) | 注釈テキストのフォント色を取得または設定します |
| [getPoints()](#getPoints--) | テキスト付きの矩形を記述するポイントのコレクションを取得または設定します |
| [setPoints(List<Point> value)](#setPoints-java.util.List-com.groupdocs.annotation.models.Point--) | テキスト付きの矩形を記述するポイントのコレクションを取得または設定します |
| [equals(TextRedactionAnnotation other)](#equals-com.groupdocs.annotation.models.annotationmodels.TextRedactionAnnotation-) | IEquatable Equals メソッドを使用して Text Redaction Annotations を比較します |
| [equals(Object o)](#equals-java.lang.Object-) | 標準の object Equals メソッドを使用して Text Redaction Annotations を比較します |
| [hashCode()](#hashCode--) | Text Redaction Annotation の HashCode を返します |
| [deepClone()](#deepClone--) | 同じ値を持つ新しいインスタンスを返します |
| [toString()](#toString--) |  |
| [toString(ToStringStyle toStringStyle)](#toString-org.apache.commons.lang3.builder.ToStringStyle-) |  |
### TextRedactionAnnotation() {#TextRedactionAnnotation--}
```
public TextRedactionAnnotation()
```


新しい [TextRedactionAnnotation](../../com.groupdocs.annotation.models.annotationmodels/textredactionannotation) クラスのインスタンスを初期化します。

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

### equals(TextRedactionAnnotation other) {#equals-com.groupdocs.annotation.models.annotationmodels.TextRedactionAnnotation-}
```
public final boolean equals(TextRedactionAnnotation other)
```


IEquatable Equals メソッドを使用して Text Redaction Annotations を比較します

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| other | [TextRedactionAnnotation](../../com.groupdocs.annotation.models.annotationmodels/textredactionannotation) | 現在のオブジェクトと比較するための TextRedactionAnnotation オブジェクト |

**Returns:**
boolean
### equals(Object o) {#equals-java.lang.Object-}
```
public boolean equals(Object o)
```


標準の object Equals メソッドを使用して Text Redaction Annotations を比較します

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


Text Redaction Annotation の HashCode を返します

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
