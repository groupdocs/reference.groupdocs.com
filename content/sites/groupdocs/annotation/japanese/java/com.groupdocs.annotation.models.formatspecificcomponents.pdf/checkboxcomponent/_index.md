---
title: "CheckBoxComponent"
second_title: "GroupDocs.Annotation for Java API リファレンス"
description: "チェックボックスのプロパティを表します"
type: docs
weight: 11
url: /ja/java/com.groupdocs.annotation.models.formatspecificcomponents.pdf/checkboxcomponent/
---
**Inheritance:**
java.lang.Object, [com.groupdocs.annotation.models.annotationmodels.AnnotationBase](../../com.groupdocs.annotation.models.annotationmodels/annotationbase)

**All Implemented Interfaces:**
[com.groupdocs.annotation.models.formatspecificcomponents.pdf.interfaces.ICheckBoxComponent](../../com.groupdocs.annotation.models.formatspecificcomponents.pdf.interfaces/icheckboxcomponent)
```
public class CheckBoxComponent extends AnnotationBase implements ICheckBoxComponent
```

チェックボックスのプロパティを表します

--------------------

 **Learn more** 

 *  
 *  
## コンストラクタ

| コンストラクタ | 説明 |
| --- | --- |
| [CheckBoxComponent()](#CheckBoxComponent--) | 新しい [CheckBoxComponent](../../com.groupdocs.annotation.models.formatspecificcomponents.pdf/checkboxcomponent) クラスのインスタンスを初期化します。 |
## メソッド

| メソッド | 説明 |
| --- | --- |
| [getChecked()](#getChecked--) | コンポーネントのチェック状態を取得または設定します |
| [setChecked(boolean value)](#setChecked-boolean-) | コンポーネントのチェック状態を取得または設定します |
| [getBox()](#getBox--) | コンポーネントの位置を取得または設定します |
| [setBox(Rectangle value)](#setBox-com.groupdocs.annotation.models.Rectangle-) | コンポーネントの位置を取得または設定します |
| [getPenColor()](#getPenColor--) | コンポーネントの色を取得または設定します |
| [setPenColor(Integer value)](#setPenColor-java.lang.Integer-) | コンポーネントの色を取得または設定します |
| [getStyle()](#getStyle--) | スタイルボックスを取得または設定します |
| [setStyle(Byte value)](#setStyle-java.lang.Byte-) | スタイルボックスを取得または設定します |
| [equals(CheckBoxComponent other)](#equals-com.groupdocs.annotation.models.formatspecificcomponents.pdf.CheckBoxComponent-) | IEquatable の Equals メソッドを使用して CheckBox コンポーネントを比較します |
| [equals(Object obj)](#equals-java.lang.Object-) | 標準の object Equals メソッドを使用して CheckBox コンポーネントを比較します |
| [hashCode()](#hashCode--) | CheckBox コンポーネントの HashCode を返します |
| [deepClone()](#deepClone--) | 同じ値を持つ新しいインスタンスを返します |
| [toString()](#toString--) |  |
| [toString(ToStringStyle toStringStyle)](#toString-org.apache.commons.lang3.builder.ToStringStyle-) |  |
### CheckBoxComponent() {#CheckBoxComponent--}
```
public CheckBoxComponent()
```


新しい [CheckBoxComponent](../../com.groupdocs.annotation.models.formatspecificcomponents.pdf/checkboxcomponent) クラスのインスタンスを初期化します。

### getChecked() {#getChecked--}
```
public final boolean getChecked()
```


コンポーネントのチェック状態を取得または設定します

**Returns:**
boolean -
### setChecked(boolean value) {#setChecked-boolean-}
```
public final void setChecked(boolean value)
```


コンポーネントのチェック状態を取得または設定します

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| 値 | boolean |  |

### getBox() {#getBox--}
```
public final Rectangle getBox()
```


コンポーネントの位置を取得または設定します

**Returns:**
[Rectangle](../../com.groupdocs.annotation.models/rectangle)
### setBox(Rectangle value) {#setBox-com.groupdocs.annotation.models.Rectangle-}
```
public final void setBox(Rectangle value)
```


コンポーネントの位置を取得または設定します

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| value | [Rectangle](../../com.groupdocs.annotation.models/rectangle) |  |

### getPenColor() {#getPenColor--}
```
public final Integer getPenColor()
```


コンポーネントの色を取得または設定します

**Returns:**
java.lang.Integer -
### setPenColor(Integer value) {#setPenColor-java.lang.Integer-}
```
public final void setPenColor(Integer value)
```


コンポーネントの色を取得または設定します

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| 値 | java.lang.Integer |  |

### getStyle() {#getStyle--}
```
public final Byte getStyle()
```


スタイルボックスを取得または設定します

**Returns:**
java.lang.Byte -
### setStyle(Byte value) {#setStyle-java.lang.Byte-}
```
public final void setStyle(Byte value)
```


スタイルボックスを取得または設定します

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| 値 | java.lang.Byte |  |

### equals(CheckBoxComponent other) {#equals-com.groupdocs.annotation.models.formatspecificcomponents.pdf.CheckBoxComponent-}
```
public final boolean equals(CheckBoxComponent other)
```


IEquatable の Equals メソッドを使用して CheckBox コンポーネントを比較します

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| other | [CheckBoxComponent](../../com.groupdocs.annotation.models.formatspecificcomponents.pdf/checkboxcomponent) | 現在のオブジェクトと比較するための CheckBoxComponent オブジェクト |

**Returns:**
boolean -
### equals(Object obj) {#equals-java.lang.Object-}
```
public boolean equals(Object obj)
```


標準の object Equals メソッドを使用して CheckBox コンポーネントを比較します

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


CheckBox コンポーネントの HashCode を返します

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
