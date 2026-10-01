---
title: "AnnotationBase"
second_title: "GroupDocs.Annotation for Java API リファレンス"
description: "すべての注釈タイプの基本クラス"
type: docs
weight: 10
url: /ja/java/com.groupdocs.annotation.models.annotationmodels/annotationbase/
---
**Inheritance:**
java.lang.Object

**All Implemented Interfaces:**
com.aspose.ms.System.ICloneable, java.lang.Cloneable, com.aspose.ms.System.IEquatable
```
public abstract class AnnotationBase implements System.ICloneable, Cloneable, System.IEquatable<AnnotationBase>
```

すべての注釈タイプの基本クラス
## コンストラクタ

| コンストラクタ | 説明 |
| --- | --- |
| [AnnotationBase()](#AnnotationBase--) |  |
## メソッド

| メソッド | 説明 |
| --- | --- |
| [getCounter()](#getCounter--) |  |
| [setCounter(int counter)](#setCounter-int-) |  |
| [getId()](#getId--) | アノテーションの一意識別子を取得または設定します |
| [setId(int value)](#setId-int-) | アノテーションの一意識別子を取得または設定します |
| [getCreatedOn()](#getCreatedOn--) | アノテーションの作成日を取得または設定します |
| [setCreatedOn(Date value)](#setCreatedOn-java.util.Date-) | アノテーションの作成日を取得または設定します |
| [getMessage()](#getMessage--) | アノテーションのメッセージを取得または設定します |
| [setMessage(String value)](#setMessage-java.lang.String-) | アノテーションのメッセージを取得または設定します |
| [getPageNumber()](#getPageNumber--) | アノテーション対象のページ番号を取得または設定します |
| [setPageNumber(Integer value)](#setPageNumber-java.lang.Integer-) | アノテーション対象のページ番号を取得または設定します |
| [getReplies()](#getReplies--) | 注釈の返信コレクションを表します |
| [setReplies(List<Reply> value)](#setReplies-java.util.List-com.groupdocs.annotation.models.Reply--) | 注釈の返信コレクションを表します |
| [getStateBeforeAnnotation()](#getStateBeforeAnnotation--) | 注釈前のテキスト状態 |
| [setStateBeforeAnnotation(Object value)](#setStateBeforeAnnotation-java.lang.Object-) | 注釈前のテキスト状態 |
| [getType()](#getType--) | 注釈タイプを取得または設定します |
| [setType(int value)](#setType-int-) | 注釈タイプを取得または設定します |
| [getUser()](#getUser--) | 注釈作成者を取得または設定します |
| [setUser(User value)](#setUser-com.groupdocs.annotation.models.User-) | 注釈作成者を取得または設定します |
| [equals(AnnotationBase other)](#equals-com.groupdocs.annotation.models.annotationmodels.AnnotationBase-) | IEquatable Equals メソッドを使用してベース注釈を比較します |
| [equals(Object obj)](#equals-java.lang.Object-) | 標準オブジェクトの Equals メソッドを使用して Base アノテーションを比較します |
| [hashCode()](#hashCode--) | AnnotationBase の Message、PageNumber、Type プロパティの HashCode を返します |
| [deepClone()](#deepClone--) | 同じ値を持つ新しいインスタンスを返します |
| [toString()](#toString--) |  |
| [toString(ToStringStyle toStringStyle)](#toString-org.apache.commons.lang3.builder.ToStringStyle-) |  |
### AnnotationBase() {#AnnotationBase--}
```
public AnnotationBase()
```


### getCounter() {#getCounter--}
```
public static int getCounter()
```




**Returns:**
int
### setCounter(int counter) {#setCounter-int-}
```
public static void setCounter(int counter)
```




**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| カウンタ | int |  |

### getId() {#getId--}
```
public final int getId()
```


アノテーションの一意識別子を取得または設定します

**Returns:**
int -
### setId(int value) {#setId-int-}
```
public final void setId(int value)
```


アノテーションの一意識別子を取得または設定します

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| 値 | int |  |

### getCreatedOn() {#getCreatedOn--}
```
public final Date getCreatedOn()
```


アノテーションの作成日を取得または設定します

**Returns:**
java.util.Date -
### setCreatedOn(Date value) {#setCreatedOn-java.util.Date-}
```
public final void setCreatedOn(Date value)
```


アノテーションの作成日を取得または設定します

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| 値 | java.util.Date |  |

### getMessage() {#getMessage--}
```
public final String getMessage()
```


アノテーションのメッセージを取得または設定します

**Returns:**
java.lang.String -
### setMessage(String value) {#setMessage-java.lang.String-}
```
public final void setMessage(String value)
```


アノテーションのメッセージを取得または設定します

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| 値 | java.lang.String |  |

### getPageNumber() {#getPageNumber--}
```
public final Integer getPageNumber()
```


アノテーション対象のページ番号を取得または設定します

**Returns:**
java.lang.Integer -
### setPageNumber(Integer value) {#setPageNumber-java.lang.Integer-}
```
public final void setPageNumber(Integer value)
```


アノテーション対象のページ番号を取得または設定します

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| 値 | java.lang.Integer |  |

### getReplies() {#getReplies--}
```
public final List<Reply> getReplies()
```


注釈の返信コレクションを表します

**Returns:**
java.util.List<com.groupdocs.annotation.models.Reply> -
### setReplies(List<Reply> value) {#setReplies-java.util.List-com.groupdocs.annotation.models.Reply--}
```
public final void setReplies(List<Reply> value)
```


注釈の返信コレクションを表します

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| 値 | java.util.List<com.groupdocs.annotation.models.Reply> |  |

### getStateBeforeAnnotation() {#getStateBeforeAnnotation--}
```
public final Object getStateBeforeAnnotation()
```


注釈前のテキスト状態

**Returns:**
java.lang.Object -
### setStateBeforeAnnotation(Object value) {#setStateBeforeAnnotation-java.lang.Object-}
```
public final void setStateBeforeAnnotation(Object value)
```


注釈前のテキスト状態

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| 値 | java.lang.Object |  |

### getType() {#getType--}
```
public final int getType()
```


注釈タイプを取得または設定します

**Returns:**
int -
### setType(int value) {#setType-int-}
```
public final void setType(int value)
```


注釈タイプを取得または設定します

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| 値 | int |  |

### getUser() {#getUser--}
```
public final User getUser()
```


注釈作成者を取得または設定します

**Returns:**
[User](../../com.groupdocs.annotation.models/user) - 
### setUser(User value) {#setUser-com.groupdocs.annotation.models.User-}
```
public final void setUser(User value)
```


注釈作成者を取得または設定します

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| value | [User](../../com.groupdocs.annotation.models/user) |  |

### equals(AnnotationBase other) {#equals-com.groupdocs.annotation.models.annotationmodels.AnnotationBase-}
```
public final boolean equals(AnnotationBase other)
```


IEquatable Equals メソッドを使用してベース注釈を比較します

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| other | [AnnotationBase](../../com.groupdocs.annotation.models.annotationmodels/annotationbase) | 現在のオブジェクトと比較するための AnnotationBase オブジェクト |

**Returns:**
boolean -
### equals(Object obj) {#equals-java.lang.Object-}
```
public boolean equals(Object obj)
```


標準オブジェクトの Equals メソッドを使用して Base アノテーションを比較します

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


AnnotationBase の Message、PageNumber、Type プロパティの HashCode を返します

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
