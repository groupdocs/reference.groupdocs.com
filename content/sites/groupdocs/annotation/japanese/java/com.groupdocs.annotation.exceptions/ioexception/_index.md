---
title: "IOException"
second_title: "GroupDocs.Annotation for Java API リファレンス"
description: "ファイル処理が失敗したときにスローされる例外です。"
type: docs
weight: 14
url: /ja/java/com.groupdocs.annotation.exceptions/ioexception/
---
**Inheritance:**
java.lang.Object, java.lang.Throwable, java.lang.Exception, java.lang.RuntimeException, com.aspose.ms.System.Exception, com.groupdocs.foundation.exception.GroupDocsException, [com.groupdocs.annotation.exceptions.AnnotatorException](../../com.groupdocs.annotation.exceptions/annotatorexception)
```
public class IOException extends AnnotatorException
```

ファイル処理が失敗したときにスローされる例外です。
## コンストラクタ

| コンストラクタ | 説明 |
| --- | --- |
| [IOException(String message)](#IOException-java.lang.String-) | 新しい [IOException](../../com.groupdocs.annotation.exceptions/ioexception) クラスのインスタンスを初期化します。 |
| [IOException(String message, RuntimeException innerException)](#IOException-java.lang.String-java.lang.RuntimeException-) | 新しい [IOException](../../com.groupdocs.annotation.exceptions/ioexception) クラスのインスタンスを初期化します。 |
### IOException(String message) {#IOException-java.lang.String-}
```
public IOException(String message)
```


新しい [IOException](../../com.groupdocs.annotation.exceptions/ioexception) クラスのインスタンスを初期化します。

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| メッセージ | java.lang.String | エラーを説明するメッセージ。 |

### IOException(String message, RuntimeException innerException) {#IOException-java.lang.String-java.lang.RuntimeException-}
```
public IOException(String message, RuntimeException innerException)
```


新しい [IOException](../../com.groupdocs.annotation.exceptions/ioexception) クラスのインスタンスを初期化します。

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| メッセージ | java.lang.String | 例外の原因を説明するエラーメッセージ。 |
| innerException | java.lang.RuntimeException | 現在の例外の原因となる例外、または内部例外が指定されていない場合は null 参照（Visual Basic の Nothing）です。 |

