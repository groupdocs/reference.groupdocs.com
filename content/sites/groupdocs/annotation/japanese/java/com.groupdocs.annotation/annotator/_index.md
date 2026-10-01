---
title: "Annotator"
second_title: "GroupDocs.Annotation for Java API リファレンス"
description: "文書の注釈プロセスを制御するメインクラスを表します。"
type: docs
weight: 10
url: /ja/java/com.groupdocs.annotation/annotator/
---
**Inheritance:**
java.lang.Object

**All Implemented Interfaces:**
com.aspose.ms.System.IDisposable, java.io.Closeable
```
public class Annotator implements System.IDisposable, Closeable
```

文書の注釈プロセスを制御するメインクラスを表します。
## コンストラクタ

| コンストラクタ | 説明 |
| --- | --- |
| [Annotator(String filePath)](#Annotator-java.lang.String-) | ドキュメントパスを受け入れるアノテータクラスを初期化する |
| [Annotator(String filePath, LoadOptions loadOptions)](#Annotator-java.lang.String-com.groupdocs.annotation.options.LoadOptions-) | ドキュメントパスを受け入れるアノテータクラスを初期化する |
| [Annotator(String filePath, AnnotatorSettings settings)](#Annotator-java.lang.String-com.groupdocs.annotation.AnnotatorSettings-) | ドキュメントパスを受け入れるアノテータクラスを初期化する |
| [Annotator(String filePath, LoadOptions loadOptions, AnnotatorSettings settings)](#Annotator-java.lang.String-com.groupdocs.annotation.options.LoadOptions-com.groupdocs.annotation.AnnotatorSettings-) | ドキュメントパスを受け入れるアノテータクラスを初期化する |
| [Annotator(InputStream inputStream)](#Annotator-java.io.InputStream-) | ドキュメントストリームを受け入れるアノテータクラスを初期化する |
| [Annotator(InputStream inputStream, LoadOptions loadOptions)](#Annotator-java.io.InputStream-com.groupdocs.annotation.options.LoadOptions-) | ドキュメントストリームを受け入れるアノテータクラスを初期化する |
| [Annotator(InputStream inputStream, AnnotatorSettings settings)](#Annotator-java.io.InputStream-com.groupdocs.annotation.AnnotatorSettings-) | ドキュメントストリームを受け入れるアノテータクラスを初期化する |
| [Annotator(InputStream inputStream, LoadOptions loadOptions, AnnotatorSettings settings)](#Annotator-java.io.InputStream-com.groupdocs.annotation.options.LoadOptions-com.groupdocs.annotation.AnnotatorSettings-) | inputStream ストリームを受け入れるアノテータクラスを初期化する |
## メソッド

| メソッド | 説明 |
| --- | --- |
| [getDocument()](#getDocument--) | ドキュメント |
| [getRotation()](#getRotation--) | ドキュメントの回転 |
| [setRotation(Byte value)](#setRotation-java.lang.Byte-) | ドキュメントの回転 |
| [getProcessPages()](#getProcessPages--) | ドキュメントページ |
| [setProcessPages(int value)](#setProcessPages-int-) | ドキュメントページ |
| [save()](#save--) | 注釈の追加、更新、または削除後にドキュメントを保存します。 |
| [save(SaveOptions saveOptions)](#save-com.groupdocs.annotation.options.export.SaveOptions-) | 注釈の追加、更新、または削除後にドキュメントを保存します。 |
| [save(OutputStream document)](#save-java.io.OutputStream-) | 注釈の追加、更新、または削除後にドキュメントを保存します。 |
| [save(String filePath)](#save-java.lang.String-) | 注釈の追加、更新、または削除後にドキュメントを保存します。 |
| [save(OutputStream outputStream, SaveOptions saveOptions)](#save-java.io.OutputStream-com.groupdocs.annotation.options.export.SaveOptions-) | outputStream の注釈の追加、更新、または削除後に保存します。 |
| [save(String filePath, SaveOptions saveOptions)](#save-java.lang.String-com.groupdocs.annotation.options.export.SaveOptions-) | 注釈の追加、更新、または削除後にドキュメントを保存します。 |
| [dispose()](#dispose--) | 破棄 |
| [add(AnnotationBase annotation)](#add-com.groupdocs.annotation.models.annotationmodels.AnnotationBase-) | ドキュメントに注釈を追加します |
| [add(List<AnnotationBase> annotations)](#add-java.util.List-com.groupdocs.annotation.models.annotationmodels.AnnotationBase--) | ドキュメントに注釈のコレクションを追加します。 |
| [update(AnnotationBase newAnnotation)](#update-com.groupdocs.annotation.models.annotationmodels.AnnotationBase-) | ドキュメントの注釈を更新します。 |
| [update(List<AnnotationBase> annotations)](#update-java.util.List-com.groupdocs.annotation.models.annotationmodels.AnnotationBase--) | ドキュメント注釈のコレクションを更新します。 |
| [remove(int annotationId)](#remove-int-) | ID によってドキュメントから注釈を削除します。 |
| [remove(AnnotationBase annotation)](#remove-com.groupdocs.annotation.models.annotationmodels.AnnotationBase-) | ドキュメントから注釈を削除します。 |
| [remove(AnnotationBase[] annotationsToDelete)](#remove-com.groupdocs.annotation.models.annotationmodels.AnnotationBase...-) | 提供された注釈 ID によってドキュメントから注釈のコレクションを削除します。 |
| [remove(List<Integer> annotationsIdsToDelete)](#remove-java.util.List-java.lang.Integer--) | 提供された注釈 ID によってドキュメントから注釈のコレクションを削除します。 |
| [removeInternal(List<AnnotationBase> annotationsToDelete)](#removeInternal-java.util.List-com.groupdocs.annotation.models.annotationmodels.AnnotationBase--) | ドキュメントから注釈のコレクションを削除します。 |
| [get()](#get--) | ドキュメント注釈のコレクションを取得します。 |
| [getVersionsList()](#getVersionsList--) | バージョンを取得します。 |
| [getVersion(Object version)](#getVersion-java.lang.Object-) | バージョンから注釈を取得します。 |
| [get(int type)](#get-int-) | 注釈タイプでドキュメント注釈のコレクションを取得します。 |
| [importAnnotationsFromDocument(String outputPath)](#importAnnotationsFromDocument-java.lang.String-) | ドキュメントから XML ファイルへ注釈をインポートします。 |
| [exportAnnotationsFromDocument(String filePath)](#exportAnnotationsFromDocument-java.lang.String-) | XML ドキュメントから注釈をエクスポートします。 |
| [close()](#close--) |  |
### Annotator(String filePath) {#Annotator-java.lang.String-}
```
public Annotator(String filePath)
```


ドキュメントパスを受け入れるアノテータクラスを初期化する

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
|  | filePath | java.lang.String | ファイルパス |

--------------------

 **Learn more** 

 *  
 *   |

### Annotator(String filePath, LoadOptions loadOptions) {#Annotator-java.lang.String-com.groupdocs.annotation.options.LoadOptions-}
```
public Annotator(String filePath, LoadOptions loadOptions)
```


ドキュメントパスを受け入れるアノテータクラスを初期化する

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| filePath | java.lang.String | ファイルパス |
|  | loadOptions | [LoadOptions](../../com.groupdocs.annotation.options/loadoptions) | ロードオプション |

--------------------

 **Learn more** 

 *  
 *  
 *  
 *   |

### Annotator(String filePath, AnnotatorSettings settings) {#Annotator-java.lang.String-com.groupdocs.annotation.AnnotatorSettings-}
```
public Annotator(String filePath, AnnotatorSettings settings)
```


ドキュメントパスを受け入れるアノテータクラスを初期化する

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| filePath | java.lang.String | ファイルパス |
|  | settings | [AnnotatorSettings](../../com.groupdocs.annotation/annotatorsettings) | アノテータ設定 |

--------------------

 **Learn more** 

 *  
 *   |

### Annotator(String filePath, LoadOptions loadOptions, AnnotatorSettings settings) {#Annotator-java.lang.String-com.groupdocs.annotation.options.LoadOptions-com.groupdocs.annotation.AnnotatorSettings-}
```
public Annotator(String filePath, LoadOptions loadOptions, AnnotatorSettings settings)
```


ドキュメントパスを受け入れるアノテータクラスを初期化する

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| filePath | java.lang.String | ファイルパス |
| loadOptions | [LoadOptions](../../com.groupdocs.annotation.options/loadoptions) | ロードオプション |
|  | settings | [AnnotatorSettings](../../com.groupdocs.annotation/annotatorsettings) | アノテータ設定 |

--------------------

 **Learn more** 

 *  
 *  
 *  
 *   |

### Annotator(InputStream inputStream) {#Annotator-java.io.InputStream-}
```
public Annotator(InputStream inputStream)
```


ドキュメントストリームを受け入れるアノテータクラスを初期化する

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
|  | inputStream | java.io.InputStream | ドキュメントストリーム |

--------------------

 **Learn more** 

 *  
 *   |

### Annotator(InputStream inputStream, LoadOptions loadOptions) {#Annotator-java.io.InputStream-com.groupdocs.annotation.options.LoadOptions-}
```
public Annotator(InputStream inputStream, LoadOptions loadOptions)
```


ドキュメントストリームを受け入れるアノテータクラスを初期化する

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| inputStream | java.io.InputStream | ドキュメントストリーム |
|  | loadOptions | [LoadOptions](../../com.groupdocs.annotation.options/loadoptions) | ロードオプション |

--------------------

 **Learn more** 

 *  
 *  
 *  
 *   |

### Annotator(InputStream inputStream, AnnotatorSettings settings) {#Annotator-java.io.InputStream-com.groupdocs.annotation.AnnotatorSettings-}
```
public Annotator(InputStream inputStream, AnnotatorSettings settings)
```


ドキュメントストリームを受け入れるアノテータクラスを初期化する

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| inputStream | java.io.InputStream | ドキュメントストリーム |
|  | settings | [AnnotatorSettings](../../com.groupdocs.annotation/annotatorsettings) | アノテータ設定 |

--------------------

 **Learn more** 

 *  
 *   |

### Annotator(InputStream inputStream, LoadOptions loadOptions, AnnotatorSettings settings) {#Annotator-java.io.InputStream-com.groupdocs.annotation.options.LoadOptions-com.groupdocs.annotation.AnnotatorSettings-}
```
public Annotator(InputStream inputStream, LoadOptions loadOptions, AnnotatorSettings settings)
```


inputStream ストリームを受け入れるアノテータクラスを初期化する

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| inputStream | java.io.InputStream | ドキュメントストリーム |
| loadOptions | [LoadOptions](../../com.groupdocs.annotation.options/loadoptions) | ロードオプション |
|  | settings | [AnnotatorSettings](../../com.groupdocs.annotation/annotatorsettings) | アノテータ設定 |

--------------------

 **Learn more** 

 *  
 *  
 *  
 *   |

### getDocument() {#getDocument--}
```
public final Document getDocument()
```


ドキュメント

**Returns:**
[Document](../../com.groupdocs.annotation/document) - 
### getRotation() {#getRotation--}
```
public final Byte getRotation()
```


ドキュメントの回転

**Returns:**
java.lang.Byte -
### setRotation(Byte value) {#setRotation-java.lang.Byte-}
```
public final void setRotation(Byte value)
```


ドキュメントの回転

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| 値 | java.lang.Byte |  |

### getProcessPages() {#getProcessPages--}
```
public final int getProcessPages()
```


ドキュメントページ

**Returns:**
int -
### setProcessPages(int value) {#setProcessPages-int-}
```
public final void setProcessPages(int value)
```


ドキュメントページ

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| 値 | int |  |

### save() {#save--}
```
public final void save()
```


注釈の追加、更新、または削除後にドキュメントを保存します。

--------------------

 **Learn more about saving annotated documents** 

 *  
 *  
 *  

### save(SaveOptions saveOptions) {#save-com.groupdocs.annotation.options.export.SaveOptions-}
```
public final void save(SaveOptions saveOptions)
```


注釈の追加、更新、または削除後にドキュメントを保存します。

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
|  | saveOptions | [SaveOptions](../../com.groupdocs.annotation.options.export/saveoptions) | 保存オプションです。 |

--------------------

 **Learn more about saving annotated documents** 

 *  
 *  
 *   |

### save(OutputStream document) {#save-java.io.OutputStream-}
```
public final void save(OutputStream document)
```


注釈の追加、更新、または削除後にドキュメントを保存します。

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
|  | ドキュメント | java.io.OutputStream | 出力ストリームです。 |

--------------------

 **Learn more about saving annotated documents** 

 *  
 *  
 *   |

### save(String filePath) {#save-java.lang.String-}
```
public final void save(String filePath)
```


注釈の追加、更新、または削除後にドキュメントを保存します。

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
|  | filePath | java.lang.String | 出力ファイルパスです。 |

--------------------

 **Learn more about saving annotated documents** 

 *  
 *  
 *   |

### save(OutputStream outputStream, SaveOptions saveOptions) {#save-java.io.OutputStream-com.groupdocs.annotation.options.export.SaveOptions-}
```
public final void save(OutputStream outputStream, SaveOptions saveOptions)
```


outputStream の注釈の追加、更新、または削除後に保存します。

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| outputStream | java.io.OutputStream | 出力ストリームです。 |
|  | saveOptions | [SaveOptions](../../com.groupdocs.annotation.options.export/saveoptions) | 保存オプションです。 |

--------------------

 **Learn more about saving annotated documents** 

 *  
 *  
 *   |

### save(String filePath, SaveOptions saveOptions) {#save-java.lang.String-com.groupdocs.annotation.options.export.SaveOptions-}
```
public final void save(String filePath, SaveOptions saveOptions)
```


注釈の追加、更新、または削除後にドキュメントを保存します。

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| filePath | java.lang.String | 出力ファイルパスです。 |
|  | saveOptions | [SaveOptions](../../com.groupdocs.annotation.options.export/saveoptions) | 保存オプションです。 |

--------------------

 **Learn more about saving annotated documents** 

 *  
 *  
 *   |

### dispose() {#dispose--}
```
public final void dispose()
```


破棄

### add(AnnotationBase annotation) {#add-com.groupdocs.annotation.models.annotationmodels.AnnotationBase-}
```
public final void add(AnnotationBase annotation)
```


ドキュメントに注釈を追加します

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
|  | annotation | [AnnotationBase](../../com.groupdocs.annotation.models.annotationmodels/annotationbase) | 追加するアノテーションです。 |

--------------------

 **Learn more** 

 *   |

### add(List<AnnotationBase> annotations) {#add-java.util.List-com.groupdocs.annotation.models.annotationmodels.AnnotationBase--}
```
public final void add(List<AnnotationBase> annotations)
```


ドキュメントに注釈のコレクションを追加します。

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
|  | アノテーション | java.util.List<com.groupdocs.annotation.models.annotationmodels.AnnotationBase> | 追加するアノテーションのリストです。 |

--------------------

 **Learn more** 

 *   |

### update(AnnotationBase newAnnotation) {#update-com.groupdocs.annotation.models.annotationmodels.AnnotationBase-}
```
public final void update(AnnotationBase newAnnotation)
```


ドキュメントの注釈を更新します。

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
|  | newAnnotation | [AnnotationBase](../../com.groupdocs.annotation.models.annotationmodels/annotationbase) | 更新するアノテーションです（Id を指定する必要があります）。 |

--------------------

 **Learn more** 

 *   |

### update(List<AnnotationBase> annotations) {#update-java.util.List-com.groupdocs.annotation.models.annotationmodels.AnnotationBase--}
```
public final void update(List<AnnotationBase> annotations)
```


ドキュメント注釈のコレクションを更新します。

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
|  | アノテーション | java.util.List<com.groupdocs.annotation.models.annotationmodels.AnnotationBase> | 設定されるアノテーションのリストです。 |

--------------------

 **Learn more** 

 *   |

### remove(int annotationId) {#remove-int-}
```
public final void remove(int annotationId)
```


ID によってドキュメントから注釈を削除します。

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
|  | annotationId | int | 削除すべきアノテーションの ID です。 |

--------------------

 **Learn more** 

 *   |

### remove(AnnotationBase annotation) {#remove-com.groupdocs.annotation.models.annotationmodels.AnnotationBase-}
```
public final void remove(AnnotationBase annotation)
```


ドキュメントから注釈を削除します。

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
|  | annotation | [AnnotationBase](../../com.groupdocs.annotation.models.annotationmodels/annotationbase) | 削除すべきアノテーションです。 |

--------------------

 **Learn more** 

 *   |

### remove(AnnotationBase[] annotationsToDelete) {#remove-com.groupdocs.annotation.models.annotationmodels.AnnotationBase...-}
```
public final void remove(AnnotationBase[] annotationsToDelete)
```


提供された注釈 ID によってドキュメントから注釈のコレクションを削除します。

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
|  | annotationsToDelete | [AnnotationBase\[\]](../../com.groupdocs.annotation.models.annotationmodels/annotationbase) | 削除すべきアノテーションの ID です。 |

--------------------

 **Learn more** 

 *   |

### remove(List<Integer> annotationsIdsToDelete) {#remove-java.util.List-java.lang.Integer--}
```
public final void remove(List<Integer> annotationsIdsToDelete)
```


提供された注釈 ID によってドキュメントから注釈のコレクションを削除します。

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
|  | annotationsIdsToDelete | java.util.List<java.lang.Integer> | 削除すべきアノテーションの ID です。 |

--------------------

 **Learn more** 

 *   |

### removeInternal(List<AnnotationBase> annotationsToDelete) {#removeInternal-java.util.List-com.groupdocs.annotation.models.annotationmodels.AnnotationBase--}
```
public final void removeInternal(List<AnnotationBase> annotationsToDelete)
```


ドキュメントから注釈のコレクションを削除します。

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
|  | annotationsToDelete | java.util.List<com.groupdocs.annotation.models.annotationmodels.AnnotationBase> | 削除すべきアノテーションです。 |

--------------------

 **Learn more** 

 *   |

### get() {#get--}
```
public final List<AnnotationBase> get()
```


ドキュメント注釈のコレクションを取得します。

**Returns:**
java.util.List<com.groupdocs.annotation.models.annotationmodels.AnnotationBase> - アノテーションのリストです。

--------------------

 **Learn more** 

 *  
### getVersionsList() {#getVersionsList--}
```
public final List<Object> getVersionsList()
```


バージョンを取得します。

**Returns:**
java.util.List<java.lang.Object> - バージョンのリストです。
### getVersion(Object version) {#getVersion-java.lang.Object-}
```
public final List<AnnotationBase> getVersion(Object version)
```


バージョンから注釈を取得します。

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| バージョン | java.lang.Object | 返すバージョンのキーです。 |

**Returns:**
java.util.List<com.groupdocs.annotation.models.annotationmodels.AnnotationBase> - 特定のバージョンからのアノテーションのリストです。null の場合は最後のものが返されます。
### get(int type) {#get-int-}
```
public final List<AnnotationBase> get(int type)
```


注釈タイプでドキュメント注釈のコレクションを取得します。

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
|  | タイプ | int | 返す必要があるアノテーションのタイプです。 |

--------------------

 **Learn more** 

 *   |

**Returns:**
java.util.List<com.groupdocs.annotation.models.annotationmodels.AnnotationBase> - タイプ別のアノテーションのリストです。
### importAnnotationsFromDocument(String outputPath) {#importAnnotationsFromDocument-java.lang.String-}
```
public final void importAnnotationsFromDocument(String outputPath)
```


ドキュメントから XML ファイルへ注釈をインポートします。

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
|  | outputPath | java.lang.String | 出力ファイルパスです。 |

--------------------

 **Learn more** 

 *   |

### exportAnnotationsFromDocument(String filePath) {#exportAnnotationsFromDocument-java.lang.String-}
```
public final void exportAnnotationsFromDocument(String filePath)
```


XML ドキュメントから注釈をエクスポートします。

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
|  | filePath | java.lang.String | 入力ファイルのパスです。 |

--------------------

 **Learn more** 

 *   |

### close() {#close--}
```
public void close()
```




