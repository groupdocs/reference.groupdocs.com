---
title: ParserSettings
second_title: GroupDocs.Parser for Java API Reference
description: Provides the settings which are used to customize data extraction.
type: docs
weight: 27
url: /java/com.groupdocs.parser.options/parsersettings/
---
**Inheritance:**
java.lang.Object
```
public class ParserSettings
```

Provides the settings which are used to customize data extraction.

**Learn more:**

 *  [Logging][]


[Logging]: https://docs.groupdocs.com/display/parserjava/Logging
## Constructors

| Constructor | Description |
| --- | --- |
| [ParserSettings(ILogger logger)](#ParserSettings-com.groupdocs.parser.options.ILogger-) | Initializes a new instance of the [ParserSettings](../../com.groupdocs.parser.options/parsersettings) class. |
## Methods

| Method | Description |
| --- | --- |
| [getLogger()](#getLogger--) | Gets the logger which is used for logging events and errors during data extraction. |
### ParserSettings(ILogger logger) {#ParserSettings-com.groupdocs.parser.options.ILogger-}
```
public ParserSettings(ILogger logger)
```


Initializes a new instance of the [ParserSettings](../../com.groupdocs.parser.options/parsersettings) class.

**Parameters:**
| Parameter | Type | Description |
| --- | --- | --- |
| logger | [ILogger](../../com.groupdocs.parser.options/ilogger) | An instance of class that implements [ILogger](../../com.groupdocs.parser.options/ilogger) interface. |

### getLogger() {#getLogger--}
```
public ILogger getLogger()
```


Gets the logger which is used for logging events and errors during data extraction.

**Returns:**
[ILogger](../../com.groupdocs.parser.options/ilogger) - An instance of class that implements [ILogger](../../com.groupdocs.parser.options/ilogger) interface.