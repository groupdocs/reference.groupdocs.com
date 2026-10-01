---
title: "返信"
second_title: "GroupDocs.Annotation for Java API リファレンス"
description: "注釈の返信を表します。"
type: docs
weight: 14
url: /ja/java/com.groupdocs.annotation.models/reply/
---
**Inheritance:**
java.lang.Object

**All Implemented Interfaces:**
com.aspose.ms.System.ICloneable, java.lang.Cloneable
```
public class Reply implements System.ICloneable, Cloneable
```

注釈の返信を表します。
## コンストラクタ

| コンストラクタ | 説明 |
| --- | --- |
| [Reply()](#Reply--) |  |
## メソッド

| メソッド | 説明 |
| --- | --- |
| [getId()](#getId--) | 返信ID |
| [setId(int value)](#setId-int-) | 返信ID |
| [getUser()](#getUser--) | 返信作成者 |
| [setUser(User value)](#setUser-com.groupdocs.annotation.models.User-) | 返信作成者 |
| [getComment()](#getComment--) | 返信コメント |
| [setComment(String value)](#setComment-java.lang.String-) | 返信コメント |
| [getRepliedOn()](#getRepliedOn--) | 返信作成日 |
| [setRepliedOn(Date value)](#setRepliedOn-java.util.Date-) | 返信作成日 |
| [getParentReply()](#getParentReply--) | 親返信 |
| [setParentReply(Reply value)](#setParentReply-com.groupdocs.annotation.models.Reply-) | 親返信 |
| [deepClone()](#deepClone--) | 同じ値を持つ新しいインスタンスを返します |
| [clone()](#clone--) |  |
| [toString()](#toString--) |  |
### Reply() {#Reply--}
```
public Reply()
```


### getId() {#getId--}
```
public final int getId()
```


返信ID

**Returns:**
int -
### setId(int value) {#setId-int-}
```
public final void setId(int value)
```


返信ID

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| 値 | int |  |

### getUser() {#getUser--}
```
public final User getUser()
```


返信作成者

**Returns:**
[User](../../com.groupdocs.annotation.models/user) - 
### setUser(User value) {#setUser-com.groupdocs.annotation.models.User-}
```
public final void setUser(User value)
```


返信作成者

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| value | [User](../../com.groupdocs.annotation.models/user) |  |

### getComment() {#getComment--}
```
public final String getComment()
```


返信コメント

**Returns:**
java.lang.String -
### setComment(String value) {#setComment-java.lang.String-}
```
public final void setComment(String value)
```


返信コメント

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| 値 | java.lang.String |  |

### getRepliedOn() {#getRepliedOn--}
```
public final Date getRepliedOn()
```


返信作成日

**Returns:**
java.util.Date -
### setRepliedOn(Date value) {#setRepliedOn-java.util.Date-}
```
public final void setRepliedOn(Date value)
```


返信作成日

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| 値 | java.util.Date |  |

### getParentReply() {#getParentReply--}
```
public final Reply getParentReply()
```


親返信

**Returns:**
[Reply](../../com.groupdocs.annotation.models/reply) - 
### setParentReply(Reply value) {#setParentReply-com.groupdocs.annotation.models.Reply-}
```
public final void setParentReply(Reply value)
```


親返信

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| value | [Reply](../../com.groupdocs.annotation.models/reply) |  |

### deepClone() {#deepClone--}
```
public final Object deepClone()
```


同じ値を持つ新しいインスタンスを返します

**Returns:**
java.lang.Object -
### clone() {#clone--}
```
public Object clone()
```




**Returns:**
java.lang.Object
### toString() {#toString--}
```
public String toString()
```




**Returns:**
java.lang.String
