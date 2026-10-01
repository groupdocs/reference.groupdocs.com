---
title: "PageInfo"
second_title: "GroupDocs.Annotation for Java API リファレンス"
description: "ドキュメントページ情報を表します。"
type: docs
weight: 10
url: /ja/java/com.groupdocs.annotation.models/pageinfo/
---
**Inheritance:**
java.lang.Object
```
public class PageInfo
```

ドキュメントページ情報を表します。
## コンストラクタ

| コンストラクタ | 説明 |
| --- | --- |
| [PageInfo()](#PageInfo--) |  |
| [PageInfo(int width, int height)](#PageInfo-int-int-) | 新しい [PageInfo](../../com.groupdocs.annotation.models/pageinfo) クラスのインスタンスを初期化します。 |
| [PageInfo(PageInfo pageInfo)](#PageInfo-com.groupdocs.annotation.models.PageInfo-) | 新しい [PageInfo](../../com.groupdocs.annotation.models/pageinfo) クラスのインスタンスを初期化します。 |
## メソッド

| メソッド | 説明 |
| --- | --- |
| [getWidth()](#getWidth--) | ページ幅 |
| [setWidth(int value)](#setWidth-int-) | ページ幅 |
| [getHeight()](#getHeight--) | ページ高さ |
| [setHeight(int value)](#setHeight-int-) | ページ高さ |
| [getPageNumber()](#getPageNumber--) | ページ番号 |
| [setPageNumber(int value)](#setPageNumber-int-) | ページ番号 |
| [getTextLines()](#getTextLines--) | テキスト行情報 |
| [setTextLines(List<TextLineInfo> value)](#setTextLines-java.util.List-com.groupdocs.annotation.models.TextLineInfo--) | テキスト行情報 |
| [equals(Object obj)](#equals-java.lang.Object-) |  |
| [equals(PageInfo obj1, PageInfo obj2)](#equals-com.groupdocs.annotation.models.PageInfo-com.groupdocs.annotation.models.PageInfo-) |  |
| [hashCode()](#hashCode--) |  |
### PageInfo() {#PageInfo--}
```
public PageInfo()
```


### PageInfo(int width, int height) {#PageInfo-int-int-}
```
public PageInfo(int width, int height)
```


新しい [PageInfo](../../com.groupdocs.annotation.models/pageinfo) クラスのインスタンスを初期化します。

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| 幅 | int | ページ幅。 |
| 高さ | int | ページ高さ。 |

### PageInfo(PageInfo pageInfo) {#PageInfo-com.groupdocs.annotation.models.PageInfo-}
```
public PageInfo(PageInfo pageInfo)
```


新しい [PageInfo](../../com.groupdocs.annotation.models/pageinfo) クラスのインスタンスを初期化します。

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| pageInfo | [PageInfo](../../com.groupdocs.annotation.models/pageinfo) | ページ情報ソース。 |

### getWidth() {#getWidth--}
```
public final int getWidth()
```


ページ幅

**Returns:**
int -
### setWidth(int value) {#setWidth-int-}
```
public final void setWidth(int value)
```


ページ幅

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| 値 | int |  |

### getHeight() {#getHeight--}
```
public final int getHeight()
```


ページ高さ

**Returns:**
int -
### setHeight(int value) {#setHeight-int-}
```
public final void setHeight(int value)
```


ページ高さ

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| 値 | int |  |

### getPageNumber() {#getPageNumber--}
```
public final int getPageNumber()
```


ページ番号

**Returns:**
int -
### setPageNumber(int value) {#setPageNumber-int-}
```
public final void setPageNumber(int value)
```


ページ番号

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| 値 | int |  |

### getTextLines() {#getTextLines--}
```
public final List<TextLineInfo> getTextLines()
```


テキスト行情報

**Returns:**
java.util.List<com.groupdocs.annotation.models.TextLineInfo> -
### setTextLines(List<TextLineInfo> value) {#setTextLines-java.util.List-com.groupdocs.annotation.models.TextLineInfo--}
```
public final void setTextLines(List<TextLineInfo> value)
```


テキスト行情報

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| 値 | java.util.List<com.groupdocs.annotation.models.TextLineInfo> |  |

### equals(Object obj) {#equals-java.lang.Object-}
```
public boolean equals(Object obj)
```




**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| obj | java.lang.Object |  |

**Returns:**
boolean
### equals(PageInfo obj1, PageInfo obj2) {#equals-com.groupdocs.annotation.models.PageInfo-com.groupdocs.annotation.models.PageInfo-}
```
public static boolean equals(PageInfo obj1, PageInfo obj2)
```




**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| obj1 | [PageInfo](../../com.groupdocs.annotation.models/pageinfo) |  |
| obj2 | [PageInfo](../../com.groupdocs.annotation.models/pageinfo) |  |

**Returns:**
boolean
### hashCode() {#hashCode--}
```
public int hashCode()
```




**Returns:**
int
