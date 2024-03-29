---
title: WithOptions
second_title: Справочник по API GroupDocs.Conversion для .NET
description: Установить параметры преобразования
type: docs
weight: 10
url: /ru/net/groupdocs.conversion.fluent/iconversionconvertoptions/withoptions/
---
## WithOptions(ConvertOptions) {#withoptions}

Установить параметры преобразования

```csharp
public IConversionCompletedOrConvert WithOptions(ConvertOptions convertOptions)
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| convertOptions | ConvertOptions | Параметры преобразования |

### Возвращаемое значение

Интерфейс для продолжения построения конверсии

### Смотрите также

* interface [IConversionCompletedOrConvert](../../iconversioncompletedorconvert)
* class [ConvertOptions](../../../groupdocs.conversion.options.convert/convertoptions)
* interface [IConversionConvertOptions](../../iconversionconvertoptions)
* пространство имен [GroupDocs.Conversion.Fluent](../../iconversionconvertoptions)
* сборка [GroupDocs.Conversion](../../../)

---

## WithOptions(Func&lt;string, FileType, ConvertOptions&gt;) {#withoptions_1}

Установить параметры преобразования

```csharp
public IConversionCompletedOrConvert WithOptions(
    Func<string, FileType, ConvertOptions> convertOptionsProvider)
```

| Параметр | Описание |
| --- | --- |
| convertOptionsProvider | Конвертировать поставщик опций |
| convertOptionsProvider arg2arg2 | Тип исходного файла |

### Возвращаемое значение

Интерфейс для продолжения построения конверсии

### Смотрите также

* interface [IConversionCompletedOrConvert](../../iconversioncompletedorconvert)
* class [FileType](../../../groupdocs.conversion.filetypes/filetype)
* class [ConvertOptions](../../../groupdocs.conversion.options.convert/convertoptions)
* interface [IConversionConvertOptions](../../iconversionconvertoptions)
* пространство имен [GroupDocs.Conversion.Fluent](../../iconversionconvertoptions)
* сборка [GroupDocs.Conversion](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Conversion.dll -->
