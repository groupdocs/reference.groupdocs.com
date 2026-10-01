---
title: "ReleasePageStream"
second_title: "GroupDocs.Annotation for Java API リファレンス"
description: "出力ページプレビュー ストリームを解放するメソッドを定義するデリゲートです。"
type: docs
weight: 12
url: /ja/java/com.groupdocs.annotation.options.pagepreview/releasepagestream/
---
**Inheritance:**
java.lang.Object, com.aspose.ms.System.Delegate, com.aspose.ms.System.MulticastDelegate
```
public abstract class ReleasePageStream extends System.MulticastDelegate
```

出力ページプレビュー ストリームを解放するメソッドを定義するデリゲートです。
## コンストラクタ

| コンストラクタ | 説明 |
| --- | --- |
| [ReleasePageStream()](#ReleasePageStream--) |  |
## メソッド

| メソッド | 説明 |
| --- | --- |
| [invoke(int pageNumber, OutputStream pageStream)](#invoke-int-java.io.OutputStream-) |  |
| [beginInvoke(int pageNumber, OutputStream pageStream, System.AsyncCallback callback, Object state)](#beginInvoke-int-java.io.OutputStream-com.aspose.ms.System.AsyncCallback-java.lang.Object-) |  |
| [endInvoke(System.IAsyncResult result)](#endInvoke-com.aspose.ms.System.IAsyncResult-) |  |
### ReleasePageStream() {#ReleasePageStream--}
```
public ReleasePageStream()
```


### invoke(int pageNumber, OutputStream pageStream) {#invoke-int-java.io.OutputStream-}
```
public abstract void invoke(int pageNumber, OutputStream pageStream)
```




**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| pageNumber | int |  |
| pageStream | java.io.OutputStream |  |

### beginInvoke(int pageNumber, OutputStream pageStream, System.AsyncCallback callback, Object state) {#beginInvoke-int-java.io.OutputStream-com.aspose.ms.System.AsyncCallback-java.lang.Object-}
```
public final System.IAsyncResult beginInvoke(int pageNumber, OutputStream pageStream, System.AsyncCallback callback, Object state)
```




**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| pageNumber | int |  |
| pageStream | java.io.OutputStream |  |
| callback | com.aspose.ms.System.AsyncCallback |  |
| state | java.lang.Object |  |

**Returns:**
com.aspose.ms.System.IAsyncResult
### endInvoke(System.IAsyncResult result) {#endInvoke-com.aspose.ms.System.IAsyncResult-}
```
public final void endInvoke(System.IAsyncResult result)
```




**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| result | com.aspose.ms.System.IAsyncResult |  |

