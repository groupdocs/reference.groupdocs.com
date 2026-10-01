---
title: "ImageAnnotation"
second_title: "GroupDocs.Annotation for Java API リファレンス"
description: "画像注釈プロパティを表します"
type: docs
weight: 16
url: /ja/java/com.groupdocs.annotation.models.annotationmodels/imageannotation/
---
**Inheritance:**
java.lang.Object, [com.groupdocs.annotation.models.annotationmodels.AnnotationBase](../../com.groupdocs.annotation.models.annotationmodels/annotationbase)

**All Implemented Interfaces:**
[com.groupdocs.annotation.models.annotationmodels.interfaces.annotations.IImageAnnotation](../../com.groupdocs.annotation.models.annotationmodels.interfaces.annotations/iimageannotation)
```
public class ImageAnnotation extends AnnotationBase implements IImageAnnotation
```

画像注釈プロパティを表します

--------------------

 **Learn more** 

 *  
 *  
## コンストラクタ

| コンストラクタ | 説明 |
| --- | --- |
| [ImageAnnotation()](#ImageAnnotation--) | 新しい [ImageAnnotation](../../com.groupdocs.annotation.models.annotationmodels/imageannotation) クラスのインスタンスを初期化します。 |
## メソッド

| メソッド | 説明 |
| --- | --- |
| [getBox()](#getBox--) | アノテーションの位置を取得または設定します |
| [setBox(Rectangle value)](#setBox-com.groupdocs.annotation.models.Rectangle-) | アノテーションの位置を取得または設定します |
| [getImagePath()](#getImagePath--) | 画像パスを取得または設定します |
| [setImagePath(String value)](#setImagePath-java.lang.String-) | 画像パスを取得または設定します |
| [getImageData()](#getImageData--) | 画像データを取得または設定します |
| [setImageData(String value)](#setImageData-java.lang.String-) | 画像データを取得または設定します |
| [getImageExtension()](#getImageExtension--) | 画像データを取得または設定します |
| [setImageExtension(String value)](#setImageExtension-java.lang.String-) |  |
| [getOpacity()](#getOpacity--) | アノテーションの不透明度を取得または設定します |
| [setOpacity(Double value)](#setOpacity-java.lang.Double-) | アノテーションの不透明度を取得または設定します |
| [getAngle()](#getAngle--) | 注釈の回転角度を取得または設定します |
| [setAngle(Double value)](#setAngle-java.lang.Double-) | 注釈の回転角度を取得または設定します |
| [getZIndex()](#getZIndex--) | z-index を取得または設定します。 |
| [setZIndex(Integer value)](#setZIndex-java.lang.Integer-) | アノテーションのペンの色を取得または設定します |
| [getImage()](#getImage--) | 画像オブジェクトを取得します |
| [equals(ImageAnnotation other)](#equals-com.groupdocs.annotation.models.annotationmodels.ImageAnnotation-) | IEquatable の Equals メソッドを使用して Image Annotations を比較します |
| [equals(Object o)](#equals-java.lang.Object-) | 標準のオブジェクト Equals メソッドを使用して Image Annotations を比較します |
| [hashCode()](#hashCode--) | Image Annotation のハッシュコードを返します |
| [deepClone()](#deepClone--) | 同じ値を持つ新しいインスタンスを返します |
| [toString()](#toString--) |  |
| [toString(ToStringStyle toStringStyle)](#toString-org.apache.commons.lang3.builder.ToStringStyle-) |  |
### ImageAnnotation() {#ImageAnnotation--}
```
public ImageAnnotation()
```


新しい [ImageAnnotation](../../com.groupdocs.annotation.models.annotationmodels/imageannotation) クラスのインスタンスを初期化します。

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

### getImagePath() {#getImagePath--}
```
public final String getImagePath()
```


画像パスを取得または設定します

**Returns:**
java.lang.String -
### setImagePath(String value) {#setImagePath-java.lang.String-}
```
public final void setImagePath(String value)
```


画像パスを取得または設定します

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| 値 | java.lang.String |  |

### getImageData() {#getImageData--}
```
public final String getImageData()
```


画像データを取得または設定します

**Returns:**
java.lang.String -
### setImageData(String value) {#setImageData-java.lang.String-}
```
public final void setImageData(String value)
```


画像データを取得または設定します

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| 値 | java.lang.String |  |

### getImageExtension() {#getImageExtension--}
```
public final String getImageExtension()
```


画像データを取得または設定します

**Returns:**
java.lang.String -
### setImageExtension(String value) {#setImageExtension-java.lang.String-}
```
public final void setImageExtension(String value)
```




**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| 値 | java.lang.String |  |

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


注釈の回転角度を取得または設定します

**Returns:**
java.lang.Double
### setAngle(Double value) {#setAngle-java.lang.Double-}
```
public final void setAngle(Double value)
```


注釈の回転角度を取得または設定します

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| 値 | java.lang.Double |  |

### getZIndex() {#getZIndex--}
```
public final Integer getZIndex()
```


z-index を取得または設定します。デフォルト値は 0 です

 **z-index** プロパティは要素のスタック順序を指定します。

**Returns:**
java.lang.Integer -
### setZIndex(Integer value) {#setZIndex-java.lang.Integer-}
```
public final void setZIndex(Integer value)
```


アノテーションのペンの色を取得または設定します

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| 値 | java.lang.Integer |  |

### getImage() {#getImage--}
```
public final System.Drawing.Image getImage()
```


画像オブジェクトを取得します

**Returns:**
com.aspose.ms.System.Drawing.Image -
### equals(ImageAnnotation other) {#equals-com.groupdocs.annotation.models.annotationmodels.ImageAnnotation-}
```
public final boolean equals(ImageAnnotation other)
```


IEquatable の Equals メソッドを使用して Image Annotations を比較します

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| other | [ImageAnnotation](../../com.groupdocs.annotation.models.annotationmodels/imageannotation) | 現在のオブジェクトと比較するための ImageAnnotation オブジェクト |

**Returns:**
boolean -
### equals(Object o) {#equals-java.lang.Object-}
```
public boolean equals(Object o)
```


標準のオブジェクト Equals メソッドを使用して Image Annotations を比較します

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


Image Annotation のハッシュコードを返します

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
