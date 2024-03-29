---
title: FuncTTResult
second_title: GroupDocs.Metadata for .NET API リファレンス
description: 1 つのパラメーターを持ちメソッドによって指定された型の値を返すメソッドをカプセル化しますTResultパラメータ
type: docs
weight: 80
url: /ja/net/groupdocs.metadata.common/func-2/
---
## Func&lt;T,TResult&gt; delegate

1 つのパラメーターを持ち、メソッドによって指定された型の値を返すメソッドをカプセル化します。*TResult*パラメータ。

```csharp
public delegate TResult Func<in T, out TResult>(T arg);
```

| パラメータ | 説明 |
| --- | --- |
| T | このデリゲートがカプセル化するメソッドのパラメーターの型。 |
| TResult | このデリゲートがカプセル化するメソッドの戻り値の型。 |
| arg | このデリゲートがカプセル化するメソッドのパラメーター。 |

### 戻り値

このデリゲートがカプセル化するメソッドの戻り値。

### 関連項目

* 名前空間 [GroupDocs.Metadata.Common](../../groupdocs.metadata.common)
* 組み立て [GroupDocs.Metadata](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Metadata.dll -->
