---
title: Error
second_title: GroupDocs.Viewer for .NET API 参考
description: 写入错误消息 错误日志消息提供有关应用程序流中不可恢复事件的信息
type: docs
weight: 10
url: /zh/net/groupdocs.viewer.logging/ilogger/error/
---
## ILogger.Error method

写入错误消息。 错误日志消息提供有关应用程序流中不可恢复事件的信息。

```csharp
public void Error(string message, Exception exception)
```

| 范围 | 类型 | 描述 |
| --- | --- | --- |
| message | String | 错误信息。 |
| exception | Exception | 例外。 |

### 例外

| 例外 | （健康）状况 |
| --- | --- |
| ArgumentNullException | 抛出时*message*一片空白。 |
| ArgumentNullException | 抛出时*exception*一片空白。 |

### 也可以看看

* interface [ILogger](../../ilogger)
* 命名空间 [GroupDocs.Viewer.Logging](../../ilogger)
* 部件 [GroupDocs.Viewer](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Viewer.dll -->
