---
title: "PreviewOptions"
second_title: "GroupDocs.Annotation for Java API リファレンス"
description: "ドキュメントプレビューオプションを表します。"
type: docs
weight: 11
url: /ja/java/com.groupdocs.annotation.options.pagepreview/previewoptions/
---
**Inheritance:**
java.lang.Object
```
public class PreviewOptions
```

ドキュメントプレビューオプションを表します。
## コンストラクタ

| コンストラクタ | 説明 |
| --- | --- |
| [PreviewOptions(CreatePageStream createPageStream)](#PreviewOptions-com.groupdocs.annotation.options.pagepreview.CreatePageStream-) | 新しいインスタンスの [PreviewOptions](../../com.groupdocs.annotation.options.pagepreview/previewoptions) クラスを初期化します。 |
| [PreviewOptions(CreatePageStream createPageStream, ReleasePageStream releasePageStream)](#PreviewOptions-com.groupdocs.annotation.options.pagepreview.CreatePageStream-com.groupdocs.annotation.options.pagepreview.ReleasePageStream-) | 新しいインスタンスの [PreviewOptions](../../com.groupdocs.annotation.options.pagepreview/previewoptions) クラスを初期化します。 |
## メソッド

| メソッド | 説明 |
| --- | --- |
| [getCreatePageStream()](#getCreatePageStream--) | 出力ページプレビュー ストリームを作成するメソッドを定義するデリゲート。 |
| [setCreatePageStream(CreatePageStream value)](#setCreatePageStream-com.groupdocs.annotation.options.pagepreview.CreatePageStream-) | 出力ページプレビュー ストリームを作成するメソッドを定義するデリゲート。 |
| [getReleasePageStream()](#getReleasePageStream--) | 出力ページプレビュー ストリームを削除するメソッドを定義するデリゲート |
| [setReleasePageStream(ReleasePageStream value)](#setReleasePageStream-com.groupdocs.annotation.options.pagepreview.ReleasePageStream-) | 出力ページプレビュー ストリームを削除するメソッドを定義するデリゲート |
| [getWidth()](#getWidth--) | ページプレビューの幅。 |
| [setWidth(int value)](#setWidth-int-) | ページプレビューの幅。 |
| [getHeight()](#getHeight--) | ページプレビューの高さ。 |
| [setHeight(int value)](#setHeight-int-) | ページプレビューの高さ。 |
| [getPageNumbers()](#getPageNumbers--) | プレビューされるページ番号。 |
| [setPageNumbers(int[] value)](#setPageNumbers-int---) | プレビューされるページ番号。 |
| [getPreviewFormat()](#getPreviewFormat--) | プレビュー画像の形式。 |
| [setPreviewFormat(int value)](#setPreviewFormat-int-) | プレビュー画像の形式。 |
| [getResolution()](#getResolution--) |  |
| [setResolution(int value)](#setResolution-int-) |  |
| [getRenderComments()](#getRenderComments--) | プレビューでコメントが生成されるかどうかを制御するプロパティ。 |
| [setRenderComments(boolean value)](#setRenderComments-boolean-) | プレビューでコメントが生成されるかどうかを制御するプロパティ。 |
| [getRenderAnnotations()](#getRenderAnnotations--) | プレビューで注釈が生成されるかどうかを制御するプロパティ。 |
| [setRenderAnnotations(boolean value)](#setRenderAnnotations-boolean-) | プレビューで注釈が生成されるかどうかを制御するプロパティ。 |
| [getWorksheetColumns()](#getWorksheetColumns--) | 生成するワークシート列。 |
| [getWorksheetColumnsInternal()](#getWorksheetColumnsInternal--) |  |
| [setWorksheetColumns(List<WorksheetColumnsRange> value)](#setWorksheetColumns-java.util.List-com.groupdocs.annotation.options.pagepreview.WorksheetColumnsRange--) | 生成するワークシート列。 |
| [setWorksheetColumnsInternal(System.Collections.Generic.List<WorksheetColumnsRange> value)](#setWorksheetColumnsInternal-com.aspose.ms.System.Collections.Generic.List-com.groupdocs.annotation.options.pagepreview.WorksheetColumnsRange--) |  |
### PreviewOptions(CreatePageStream createPageStream) {#PreviewOptions-com.groupdocs.annotation.options.pagepreview.CreatePageStream-}
```
public PreviewOptions(CreatePageStream createPageStream)
```


新しいインスタンスの [PreviewOptions](../../com.groupdocs.annotation.options.pagepreview/previewoptions) クラスを初期化します。

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| createPageStream | [CreatePageStream](../../com.groupdocs.annotation.options.pagepreview/createpagestream) | 出力ページプレビュー ストリームを作成するメソッドを定義するデリゲート。 |

### PreviewOptions(CreatePageStream createPageStream, ReleasePageStream releasePageStream) {#PreviewOptions-com.groupdocs.annotation.options.pagepreview.CreatePageStream-com.groupdocs.annotation.options.pagepreview.ReleasePageStream-}
```
public PreviewOptions(CreatePageStream createPageStream, ReleasePageStream releasePageStream)
```


新しいインスタンスの [PreviewOptions](../../com.groupdocs.annotation.options.pagepreview/previewoptions) クラスを初期化します。

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| createPageStream | [CreatePageStream](../../com.groupdocs.annotation.options.pagepreview/createpagestream) | 出力ページプレビュー ストリームを作成するメソッドを定義するデリゲート。 |
| releasePageStream | [ReleasePageStream](../../com.groupdocs.annotation.options.pagepreview/releasepagestream) | 出力ページプレビュー ストリームを解放するメソッドを定義するデリゲート。 |

### getCreatePageStream() {#getCreatePageStream--}
```
public final CreatePageStream getCreatePageStream()
```


出力ページプレビュー ストリームを作成するメソッドを定義するデリゲート。

**Returns:**
[CreatePageStream](../../com.groupdocs.annotation.options.pagepreview/createpagestream) - 
### setCreatePageStream(CreatePageStream value) {#setCreatePageStream-com.groupdocs.annotation.options.pagepreview.CreatePageStream-}
```
public final void setCreatePageStream(CreatePageStream value)
```


出力ページプレビュー ストリームを作成するメソッドを定義するデリゲート。

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| value | [CreatePageStream](../../com.groupdocs.annotation.options.pagepreview/createpagestream) |  |

### getReleasePageStream() {#getReleasePageStream--}
```
public final ReleasePageStream getReleasePageStream()
```


出力ページプレビュー ストリームを削除するメソッドを定義するデリゲート

**Returns:**
[ReleasePageStream](../../com.groupdocs.annotation.options.pagepreview/releasepagestream) - 
### setReleasePageStream(ReleasePageStream value) {#setReleasePageStream-com.groupdocs.annotation.options.pagepreview.ReleasePageStream-}
```
public final void setReleasePageStream(ReleasePageStream value)
```


出力ページプレビュー ストリームを削除するメソッドを定義するデリゲート

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| value | [ReleasePageStream](../../com.groupdocs.annotation.options.pagepreview/releasepagestream) |  |

### getWidth() {#getWidth--}
```
public final int getWidth()
```


ページプレビューの幅。

**Returns:**
int -
### setWidth(int value) {#setWidth-int-}
```
public final void setWidth(int value)
```


ページプレビューの幅。

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| 値 | int |  |

### getHeight() {#getHeight--}
```
public final int getHeight()
```


ページプレビューの高さ。

**Returns:**
int -
### setHeight(int value) {#setHeight-int-}
```
public final void setHeight(int value)
```


ページプレビューの高さ。

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| 値 | int |  |

### getPageNumbers() {#getPageNumbers--}
```
public final int[] getPageNumbers()
```


プレビューされるページ番号。

**Returns:**
int[] -
### setPageNumbers(int[] value) {#setPageNumbers-int---}
```
public final void setPageNumbers(int[] value)
```


プレビューされるページ番号。

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| 値 | int[] |  |

### getPreviewFormat() {#getPreviewFormat--}
```
public final int getPreviewFormat()
```


プレビュー画像の形式。

**Returns:**
int -
### setPreviewFormat(int value) {#setPreviewFormat-int-}
```
public final void setPreviewFormat(int value)
```


プレビュー画像の形式。

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| 値 | int |  |

### getResolution() {#getResolution--}
```
public int getResolution()
```




**Returns:**
int
### setResolution(int value) {#setResolution-int-}
```
public void setResolution(int value)
```




**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| 値 | int |  |

### getRenderComments() {#getRenderComments--}
```
public final boolean getRenderComments()
```


プレビューでコメントが生成されるかどうかを制御するプロパティ。デフォルト状態 - true。現在、MS Word ドキュメントでのみサポートされています。

**Returns:**
boolean -
### setRenderComments(boolean value) {#setRenderComments-boolean-}
```
public final void setRenderComments(boolean value)
```


プレビューでコメントが生成されるかどうかを制御するプロパティ。デフォルト状態 - true。現在、MS Word ドキュメントでのみサポートされています。

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| 値 | boolean |  |

### getRenderAnnotations() {#getRenderAnnotations--}
```
public final boolean getRenderAnnotations()
```


プレビューで注釈が生成されるかどうかを制御するプロパティ。デフォルト状態 - true。

**Returns:**
boolean -
### setRenderAnnotations(boolean value) {#setRenderAnnotations-boolean-}
```
public final void setRenderAnnotations(boolean value)
```


プレビューで注釈が生成されるかどうかを制御するプロパティ。デフォルト状態 - true。

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| 値 | boolean |  |

### getWorksheetColumns() {#getWorksheetColumns--}
```
public final List<WorksheetColumnsRange> getWorksheetColumns()
```


生成するワークシート列。指定された順序で生成が進行します。

**Returns:**
java.util.List<com.groupdocs.annotation.options.pagepreview.WorksheetColumnsRange> -
### getWorksheetColumnsInternal() {#getWorksheetColumnsInternal--}
```
public System.Collections.Generic.List<WorksheetColumnsRange> getWorksheetColumnsInternal()
```




**Returns:**
com.aspose.ms.System.Collections.Generic.List<com.groupdocs.annotation.options.pagepreview.WorksheetColumnsRange>
### setWorksheetColumns(List<WorksheetColumnsRange> value) {#setWorksheetColumns-java.util.List-com.groupdocs.annotation.options.pagepreview.WorksheetColumnsRange--}
```
public final void setWorksheetColumns(List<WorksheetColumnsRange> value)
```


生成するワークシート列。指定された順序で生成が進行します。

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| 値 | java.util.List<com.groupdocs.annotation.options.pagepreview.WorksheetColumnsRange> |  |

### setWorksheetColumnsInternal(System.Collections.Generic.List<WorksheetColumnsRange> value) {#setWorksheetColumnsInternal-com.aspose.ms.System.Collections.Generic.List-com.groupdocs.annotation.options.pagepreview.WorksheetColumnsRange--}
```
public void setWorksheetColumnsInternal(System.Collections.Generic.List<WorksheetColumnsRange> value)
```




**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| 値 | com.aspose.ms.System.Collections.Generic.List<com.groupdocs.annotation.options.pagepreview.WorksheetColumnsRange> |  |

