---
title: GetInstance
second_title: GroupDocs.Redaction for .NET API 参考
description: 提供具有内置格式默认配置的单例实例
type: docs
weight: 10
url: /zh/net/groupdocs.redaction.configuration/redactorconfiguration/getinstance/
---
## RedactorConfiguration.GetInstance method

提供具有内置格式默认配置的单例实例。

```csharp
public static RedactorConfiguration GetInstance()
```

### 返回值

配置实例

### 例子

以下示例演示如何添加自定义格式处理程序。

```csharp
var adobePhotoshopSettings = new DocumentFormatConfiguration();
adobePhotoshopSettings.ExtensionFilter = ".psd";
adobePhotoshopSettings.DocumentType = typeof(MyAdobePhotoshopFormatInstance);
var configuration = RedactorConfiguration.GetInstance();
configuration.AvailableFormats.Add(adobePhotoshopSettings);
```

### 也可以看看

* class [RedactorConfiguration](../../redactorconfiguration)
* 命名空间 [GroupDocs.Redaction.Configuration](../../redactorconfiguration)
* 部件 [GroupDocs.Redaction](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Redaction.dll -->
