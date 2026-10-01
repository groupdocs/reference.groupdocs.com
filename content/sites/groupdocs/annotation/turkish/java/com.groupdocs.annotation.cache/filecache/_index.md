---
title: "FileCache"
second_title: "GroupDocs.Annotation Java için API Referansı"
description: "Yerel bir disk üzerindeki önbelleği temsil eder."
type: docs
weight: 10
url: /tr/java/com.groupdocs.annotation.cache/filecache/
---
**Inheritance:**
java.lang.Object

**All Implemented Interfaces:**
[com.groupdocs.annotation.cache.ICache](../../com.groupdocs.annotation.cache/icache)
```
public class FileCache implements ICache
```

Yerel bir disk üzerindeki önbelleği temsil eder.
## Yapıcılar

| Yapıcı | Açıklama |
| --- | --- |
| [FileCache()](#FileCache--) | Yeni bir [FileCache](../../com.groupdocs.annotation.cache/filecache) sınıfı örneği başlatır. |
| [FileCache(String path)](#FileCache-java.lang.String-) | Yeni bir [FileCache](../../com.groupdocs.annotation.cache/filecache) sınıfı örneği başlatır. |
## Metotlar

| Metot | Açıklama |
| --- | --- |
| [getKeys(String filter)](#getKeys-java.lang.String-) | Dosya adında filtre içeren tüm dosya adlarını döndürür. |
| [set(String key, Object value)](#set-java.lang.String-java.lang.Object-) | Verileri yerel diske serileştirir. |
### FileCache() {#FileCache--}
```
public FileCache()
```


Yeni bir [FileCache](../../com.groupdocs.annotation.cache/filecache) sınıfı örneği başlatır.

### FileCache(String path) {#FileCache-java.lang.String-}
```
public FileCache(String path)
```


Yeni bir [FileCache](../../com.groupdocs.annotation.cache/filecache) sınıfı örneği başlatır.

**Parameters:**
| Parametre | Tür | Açıklama |
| --- | --- | --- |
| yol | java.lang.String | Önbellek verilerinin kaydedileceği yol |

### getKeys(String filter) {#getKeys-java.lang.String-}
```
public final System.Collections.Generic.IGenericEnumerable<String> getKeys(String filter)
```


Dosya adında filtre içeren tüm dosya adlarını döndürür.

**Parameters:**
| Parametre | Tür | Açıklama |
| --- | --- | --- |
| filtre | java.lang.String | Kullanılacak filtre. |

**Returns:**
com.aspose.ms.System.Collections.Generic.IGenericEnumerable<java.lang.String> - Dosya adında filtre içeren dosya adları.
### set(String key, Object value) {#set-java.lang.String-java.lang.Object-}
```
public final void set(String key, Object value)
```


Verileri yerel diske serileştirir.

**Parameters:**
| Parametre | Tür | Açıklama |
| --- | --- | --- |
| anahtar | java.lang.String | Önbellek girdisi için benzersiz bir tanımlayıcı. |
| değer | java.lang.Object | Serileştirilecek nesne. |

