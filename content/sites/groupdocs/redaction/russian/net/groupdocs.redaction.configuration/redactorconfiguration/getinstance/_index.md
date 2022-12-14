---
title: GetInstance
second_title: Справочник по API GroupDocs.Redaction для .NET
description: Предоставляет одноэлементный экземпляр с конфигурацией встроенных форматов по умолчанию.
type: docs
weight: 10
url: /ru/net/groupdocs.redaction.configuration/redactorconfiguration/getinstance/
---
## RedactorConfiguration.GetInstance method

Предоставляет одноэлементный экземпляр с конфигурацией встроенных форматов по умолчанию.

```csharp
public static RedactorConfiguration GetInstance()
```

### Возвращаемое значение

Экземпляр конфигурации

### Примеры

В следующем примере показано, как добавить пользовательский обработчик формата.

```csharp
var adobePhotoshopSettings = new DocumentFormatConfiguration();
adobePhotoshopSettings.ExtensionFilter = ".psd";
adobePhotoshopSettings.DocumentType = typeof(MyAdobePhotoshopFormatInstance);
var configuration = RedactorConfiguration.GetInstance();
configuration.AvailableFormats.Add(adobePhotoshopSettings);
```

### Смотрите также

* class [RedactorConfiguration](../../redactorconfiguration)
* пространство имен [GroupDocs.Redaction.Configuration](../../redactorconfiguration)
* сборка [GroupDocs.Redaction](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Redaction.dll -->
