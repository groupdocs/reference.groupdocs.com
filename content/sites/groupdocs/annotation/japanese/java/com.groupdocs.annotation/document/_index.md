---
title: "ドキュメント"
second_title: "GroupDocs.Annotation for Java API リファレンス"
description: "ドキュメントのプロパティを表します"
type: docs
weight: 12
url: /ja/java/com.groupdocs.annotation/document/
---
**Inheritance:**
java.lang.Object

**All Implemented Interfaces:**
java.io.Closeable
```
public class Document implements Closeable
```

ドキュメントのプロパティを表します
## コンストラクタ

| コンストラクタ | 説明 |
| --- | --- |
| [Document(InputStream stream)](#Document-java.io.InputStream-) | 新しい[Document](../../com.groupdocs.annotation/document)クラスのインスタンスを初期化します。 |
| [Document(InputStream stream, String password)](#Document-java.io.InputStream-java.lang.String-) | 新しい[Document](../../com.groupdocs.annotation/document)クラスのインスタンスを初期化します。 |
## メソッド

| メソッド | 説明 |
| --- | --- |
| [setCache(ICache value)](#setCache-com.groupdocs.annotation.cache.ICache-) |  |
| [getName()](#getName--) | ドキュメント名 |
| [setName(String value)](#setName-java.lang.String-) | ドキュメント名 |
| [getStreamSize()](#getStreamSize--) | ドキュメントサイズ |
| [createStream()](#createStream--) | ドキュメントの入力ストリームを作成します |
| [getPassword()](#getPassword--) | ドキュメントのパスワード |
| [setPassword(String value)](#setPassword-java.lang.String-) |  |
| [getRotation()](#getRotation--) | ドキュメントの回転 |
| [setRotation(Byte value)](#setRotation-java.lang.Byte-) | ドキュメントの回転 |
| [getProcessPages()](#getProcessPages--) | ドキュメントページ |
| [setProcessPages(int value)](#setProcessPages-int-) | ドキュメントページ |
| [generatePreview(PreviewOptions previewOptions)](#generatePreview-com.groupdocs.annotation.options.pagepreview.PreviewOptions-) | ドキュメントページのプレビューを生成します。 |
| [getDocumentInfo()](#getDocumentInfo--) | ドキュメントに関する情報を取得します - ドキュメントのタイプやサイズ、ページ数など。 |
| [close()](#close--) |  |
| [addImageToDocument(String dataDir, String jpgFileName, int pageNumber, int imageQuality)](#addImageToDocument-java.lang.String-java.lang.String-int-int-) | 画像の品質を変更し、画像をドキュメントに追加する |
### Document(InputStream stream) {#Document-java.io.InputStream-}
```
public Document(InputStream stream)
```


新しい[Document](../../com.groupdocs.annotation/document)クラスのインスタンスを初期化します。

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| ストリーム | java.io.InputStream | ドキュメントのストリームです。 |

### Document(InputStream stream, String password) {#Document-java.io.InputStream-java.lang.String-}
```
public Document(InputStream stream, String password)
```


新しい[Document](../../com.groupdocs.annotation/document)クラスのインスタンスを初期化します。

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| ストリーム | java.io.InputStream | ドキュメントのストリームです。 |
| パスワード | java.lang.String | ドキュメントのパスワードです。 |

### setCache(ICache value) {#setCache-com.groupdocs.annotation.cache.ICache-}
```
public final void setCache(ICache value)
```




**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| value | [ICache](../../com.groupdocs.annotation.cache/icache) |  |

### getName() {#getName--}
```
public final String getName()
```


ドキュメント名

**Returns:**
java.lang.String -
### setName(String value) {#setName-java.lang.String-}
```
public final void setName(String value)
```


ドキュメント名

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| 値 | java.lang.String |  |

### getStreamSize() {#getStreamSize--}
```
public final long getStreamSize()
```


ドキュメントサイズ

**Returns:**
long -
### createStream() {#createStream--}
```
public final InputStream createStream()
```


ドキュメントの入力ストリームを作成します

**Returns:**
java.io.InputStream
### getPassword() {#getPassword--}
```
public final String getPassword()
```


ドキュメントのパスワード

**Returns:**
java.lang.String
### setPassword(String value) {#setPassword-java.lang.String-}
```
public final void setPassword(String value)
```




**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| 値 | java.lang.String |  |

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

### generatePreview(PreviewOptions previewOptions) {#generatePreview-com.groupdocs.annotation.options.pagepreview.PreviewOptions-}
```
public final void generatePreview(PreviewOptions previewOptions)
```


ドキュメントページのプレビューを生成します。

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| previewOptions | [PreviewOptions](../../com.groupdocs.annotation.options.pagepreview/previewoptions) | ドキュメントのプレビューオプション |

### getDocumentInfo() {#getDocumentInfo--}
```
public final IDocumentInfo getDocumentInfo()
```


ドキュメントに関する情報を取得します - ドキュメントのタイプやサイズ、ページ数など。

**Returns:**
[IDocumentInfo](../../com.groupdocs.annotation/idocumentinfo) - 
### close() {#close--}
```
public void close()
```




### addImageToDocument(String dataDir, String jpgFileName, int pageNumber, int imageQuality) {#addImageToDocument-java.lang.String-java.lang.String-int-int-}
```
public void addImageToDocument(String dataDir, String jpgFileName, int pageNumber, int imageQuality)
```


画像の品質を変更し、画像をドキュメントに追加する

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| dataDir | java.lang.String | 入力PDFファイルへのパスを指定してください |
| jpgFileName | java.lang.String | JPGファイルへのパス |
| pageNumber | int | 画像が挿入されるページ |
| imageQuality | int | 画像品質を1から100に設定します。"1" は最小解像度、"100" は最大です |

