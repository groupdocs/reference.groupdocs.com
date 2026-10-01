---
title: "CreatePageStream"
second_title: "GroupDocs.Annotation for Java API リファレンス"
description: "出力ページプレビュー ストリームを作成するメソッドを定義するデリゲートです。"
type: docs
weight: 10
url: /ja/java/com.groupdocs.annotation.options.pagepreview/createpagestream/
---
**Inheritance:**
java.lang.Object, com.aspose.ms.System.Delegate, com.aspose.ms.System.MulticastDelegate
```
public abstract class CreatePageStream extends System.MulticastDelegate
```

出力ページプレビュー ストリームを作成するメソッドを定義するデリゲートです。
## コンストラクタ

| コンストラクタ | 説明 |
| --- | --- |
| [CreatePageStream()](#CreatePageStream--) |  |
## メソッド

| メソッド | 説明 |
| --- | --- |
| [invoke(int pageNumber)](#invoke-int-) |  |
| [beginInvoke(int pageNumber, System.AsyncCallback callback, Object state)](#beginInvoke-int-com.aspose.ms.System.AsyncCallback-java.lang.Object-) |  |
| [endInvoke(System.IAsyncResult result)](#endInvoke-com.aspose.ms.System.IAsyncResult-) |  |
### CreatePageStream() {#CreatePageStream--}
```
public CreatePageStream()
```


### invoke(int pageNumber) {#invoke-int-}
```
public abstract OutputStream invoke(int pageNumber)
```




**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| pageNumber | int |  |

**Returns:**
java.io.OutputStream
### beginInvoke(int pageNumber, System.AsyncCallback callback, Object state) {#beginInvoke-int-com.aspose.ms.System.AsyncCallback-java.lang.Object-}
```
public final System.IAsyncResult beginInvoke(int pageNumber, System.AsyncCallback callback, Object state)
```




**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| pageNumber | int |  |
| callback | com.aspose.ms.System.AsyncCallback |  |
| state | java.lang.Object |  |

**Returns:**
com.aspose.ms.System.IAsyncResult
### endInvoke(System.IAsyncResult result) {#endInvoke-com.aspose.ms.System.IAsyncResult-}
```
public final OutputStream endInvoke(System.IAsyncResult result)
```




**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| result | com.aspose.ms.System.IAsyncResult |  |

**Returns:**
java.io.OutputStream
