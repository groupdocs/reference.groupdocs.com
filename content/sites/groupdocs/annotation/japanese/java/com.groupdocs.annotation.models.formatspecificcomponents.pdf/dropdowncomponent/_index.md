---
title: "DropdownComponent"
second_title: "GroupDocs.Annotation for Java API リファレンス"
description: "ドロップダウンコンポーネントのプロパティを表します"
type: docs
weight: 12
url: /ja/java/com.groupdocs.annotation.models.formatspecificcomponents.pdf/dropdowncomponent/
---
**Inheritance:**
java.lang.Object, [com.groupdocs.annotation.models.annotationmodels.AnnotationBase](../../com.groupdocs.annotation.models.annotationmodels/annotationbase)

**All Implemented Interfaces:**
[com.groupdocs.annotation.models.formatspecificcomponents.pdf.interfaces.IDropdownComponent](../../com.groupdocs.annotation.models.formatspecificcomponents.pdf.interfaces/idropdowncomponent)
```
public class DropdownComponent extends AnnotationBase implements IDropdownComponent
```

ドロップダウンコンポーネントのプロパティを表します

--------------------

 **Learn more** 

 *  
 *  
## コンストラクタ

| コンストラクタ | 説明 |
| --- | --- |
| [DropdownComponent()](#DropdownComponent--) | 新しい [CheckBoxComponent](../../com.groupdocs.annotation.models.formatspecificcomponents.pdf/checkboxcomponent) クラスのインスタンスを初期化します。 |
## メソッド

| メソッド | 説明 |
| --- | --- |
| [getOptions()](#getOptions--) | コンポーネントがクリックされたときに表示されるオプション（ドロップダウン項目）のリスト |
| [setOptions(List<String> value)](#setOptions-java.util.List-java.lang.String--) | コンポーネントがクリックされたときに表示されるオプション（ドロップダウン項目）のリスト |
| [getSelectedOption()](#getSelectedOption--) | デフォルトで選択されるオプションの番号 |
| [setSelectedOption(Integer value)](#setSelectedOption-java.lang.Integer-) | デフォルトで選択されるオプションの番号 |
| [getPlaceholder()](#getPlaceholder--) | まだオプションが選択されていないときに表示されるテキスト |
| [setPlaceholder(String value)](#setPlaceholder-java.lang.String-) | まだオプションが選択されていないときに表示されるテキスト |
| [getBox()](#getBox--) | コンポーネントの位置を取得または設定します |
| [setBox(Rectangle value)](#setBox-com.groupdocs.annotation.models.Rectangle-) | コンポーネントの位置を取得または設定します |
| [getPenColor()](#getPenColor--) | コンポーネントのペンの色を取得または設定します |
| [setPenColor(Integer value)](#setPenColor-java.lang.Integer-) | コンポーネントのペンの色を取得または設定します |
| [getPenStyle()](#getPenStyle--) | コンポーネントのペンスタイルを取得または設定します |
| [setPenStyle(Byte value)](#setPenStyle-java.lang.Byte-) | コンポーネントのペンスタイルを取得または設定します |
| [getPenWidth()](#getPenWidth--) | コンポーネントのペン幅を取得または設定します |
| [setPenWidth(Byte value)](#setPenWidth-java.lang.Byte-) | コンポーネントのペン幅を取得または設定します |
| [equals(DropdownComponent other)](#equals-com.groupdocs.annotation.models.formatspecificcomponents.pdf.DropdownComponent-) | IEquatable の Equals メソッドを使用して Dropdown コンポーネントを比較します |
| [equals(Object obj)](#equals-java.lang.Object-) | 標準の object Equals メソッドを使用して Dropdown コンポーネントを比較します |
| [hashCode()](#hashCode--) | Dropdown コンポーネントのハッシュコードを返します |
| [deepClone()](#deepClone--) | 同じ値を持つ新しいインスタンスを返します |
| [toString()](#toString--) |  |
| [toString(ToStringStyle toStringStyle)](#toString-org.apache.commons.lang3.builder.ToStringStyle-) |  |
### DropdownComponent() {#DropdownComponent--}
```
public DropdownComponent()
```


新しい [CheckBoxComponent](../../com.groupdocs.annotation.models.formatspecificcomponents.pdf/checkboxcomponent) クラスのインスタンスを初期化します。

### getOptions() {#getOptions--}
```
public final List<String> getOptions()
```


コンポーネントがクリックされたときに表示されるオプション（ドロップダウン項目）のリスト

**Returns:**
java.util.List<java.lang.String> -
### setOptions(List<String> value) {#setOptions-java.util.List-java.lang.String--}
```
public final void setOptions(List<String> value)
```


コンポーネントがクリックされたときに表示されるオプション（ドロップダウン項目）のリスト

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| 値 | java.util.List<java.lang.String> |  |

### getSelectedOption() {#getSelectedOption--}
```
public final Integer getSelectedOption()
```


デフォルトで選択されるオプションの番号

**Returns:**
java.lang.Integer
### setSelectedOption(Integer value) {#setSelectedOption-java.lang.Integer-}
```
public final void setSelectedOption(Integer value)
```


デフォルトで選択されるオプションの番号

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| 値 | java.lang.Integer |  |

### getPlaceholder() {#getPlaceholder--}
```
public final String getPlaceholder()
```


まだオプションが選択されていないときに表示されるテキスト

**Returns:**
java.lang.String
### setPlaceholder(String value) {#setPlaceholder-java.lang.String-}
```
public final void setPlaceholder(String value)
```


まだオプションが選択されていないときに表示されるテキスト

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| 値 | java.lang.String |  |

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


コンポーネントのペンの色を取得または設定します

**Returns:**
java.lang.Integer
### setPenColor(Integer value) {#setPenColor-java.lang.Integer-}
```
public final void setPenColor(Integer value)
```


コンポーネントのペンの色を取得または設定します

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| 値 | java.lang.Integer |  |

### getPenStyle() {#getPenStyle--}
```
public final Byte getPenStyle()
```


コンポーネントのペンスタイルを取得または設定します

**Returns:**
java.lang.Byte
### setPenStyle(Byte value) {#setPenStyle-java.lang.Byte-}
```
public final void setPenStyle(Byte value)
```


コンポーネントのペンスタイルを取得または設定します

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| 値 | java.lang.Byte |  |

### getPenWidth() {#getPenWidth--}
```
public final Byte getPenWidth()
```


コンポーネントのペン幅を取得または設定します

**Returns:**
java.lang.Byte
### setPenWidth(Byte value) {#setPenWidth-java.lang.Byte-}
```
public final void setPenWidth(Byte value)
```


コンポーネントのペン幅を取得または設定します

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| 値 | java.lang.Byte |  |

### equals(DropdownComponent other) {#equals-com.groupdocs.annotation.models.formatspecificcomponents.pdf.DropdownComponent-}
```
public final boolean equals(DropdownComponent other)
```


IEquatable の Equals メソッドを使用して Dropdown コンポーネントを比較します

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| other | [DropdownComponent](../../com.groupdocs.annotation.models.formatspecificcomponents.pdf/dropdowncomponent) | 現在のオブジェクトと比較するための DropdownComponent オブジェクト |

**Returns:**
boolean -
### equals(Object obj) {#equals-java.lang.Object-}
```
public boolean equals(Object obj)
```


標準の object Equals メソッドを使用して Dropdown コンポーネントを比較します

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


Dropdown コンポーネントのハッシュコードを返します

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
