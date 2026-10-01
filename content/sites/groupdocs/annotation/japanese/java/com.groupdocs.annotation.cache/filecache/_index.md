---
title: "FileCache"
second_title: "GroupDocs.Annotation for Java API リファレンス"
description: "ローカルのディスク上キャッシュを表します。"
type: docs
weight: 10
url: /ja/java/com.groupdocs.annotation.cache/filecache/
---
**Inheritance:**
java.lang.Object

**All Implemented Interfaces:**
[com.groupdocs.annotation.cache.ICache](../../com.groupdocs.annotation.cache/icache)
```
public class FileCache implements ICache
```

ローカルのディスク上キャッシュを表します。
## コンストラクタ

| コンストラクタ | 説明 |
| --- | --- |
| [FileCache()](#FileCache--) | 新しい [FileCache](../../com.groupdocs.annotation.cache/filecache) クラスのインスタンスを初期化します。 |
| [FileCache(String path)](#FileCache-java.lang.String-) | 新しい [FileCache](../../com.groupdocs.annotation.cache/filecache) クラスのインスタンスを初期化します。 |
## メソッド

| メソッド | 説明 |
| --- | --- |
| [getKeys(String filter)](#getKeys-java.lang.String-) | ファイル名にフィルタが含まれるすべてのファイル名を返します。 |
| [set(String key, Object value)](#set-java.lang.String-java.lang.Object-) | データをローカルディスクにシリアライズします。 |
### FileCache() {#FileCache--}
```
public FileCache()
```


新しい [FileCache](../../com.groupdocs.annotation.cache/filecache) クラスのインスタンスを初期化します。

### FileCache(String path) {#FileCache-java.lang.String-}
```
public FileCache(String path)
```


新しい [FileCache](../../com.groupdocs.annotation.cache/filecache) クラスのインスタンスを初期化します。

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| パス | java.lang.String | キャッシュデータが保存されるパス |

### getKeys(String filter) {#getKeys-java.lang.String-}
```
public final System.Collections.Generic.IGenericEnumerable<String> getKeys(String filter)
```


ファイル名にフィルタが含まれるすべてのファイル名を返します。

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| フィルタ | java.lang.String | 使用するフィルタです。 |

**Returns:**
com.aspose.ms.System.Collections.Generic.IGenericEnumerable<java.lang.String> - ファイル名にフィルタが含まれるファイル名。
### set(String key, Object value) {#set-java.lang.String-java.lang.Object-}
```
public final void set(String key, Object value)
```


データをローカルディスクにシリアライズします。

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| キー | java.lang.String | キャッシュエントリの一意の識別子です。 |
| 値 | java.lang.Object | シリアライズするオブジェクトです。 |

