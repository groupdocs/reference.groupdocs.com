---
title: Save
second_title: Справочник по API GroupDocs.Redaction для .NET
description: Сохраняет документ в файл со следующими параметрами AddSuffix  true RasterizeToPDF  true.
type: docs
weight: 60
url: /ru/net/groupdocs.redaction/redactor/save/
---
## Save() {#save}

Сохраняет документ в файл со следующими параметрами: AddSuffix = true, RasterizeToPDF = true.

```csharp
public string Save()
```

### Возвращаемое значение

Путь к отредактированному документу

### Смотрите также

* class [Redactor](../../redactor)
* пространство имен [GroupDocs.Redaction](../../redactor)
* сборка [GroupDocs.Redaction](../../../)

---

## Save(SaveOptions) {#save_1}

Сохраняет документ в файл.

```csharp
public string Save(SaveOptions saveOptions)
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| saveOptions | SaveOptions | Варианты добавления суффикса или растрирования |

### Возвращаемое значение

Путь к отредактированному документу

### Примеры

В следующем примере показано, как сохранить документ с помощью SaveOptions.

```csharp
    using (Redactor redactor = new Redactor(@"C:\sample.pdf"))
    {
       // Здесь идет редактирование документа
       // ...
    
       // Сохраняем документ с параметрами по умолчанию (преобразование страниц в изображения, сохранение в формате PDF)
       redactor.Save();
    
       // Сохраняем документ в исходном формате, перезаписывая исходный файл
       redactor.Save(new SaveOptions() { AddSuffix = false, RasterizeToPDF = false });
    
       // Сохраняем документ в файл "*_Redacted.*" в оригинальном формате
       redactor.Save(new SaveOptions() { AddSuffix = true, RasterizeToPDF = false });
    
       // Сохраняем документ в "*_AnyText.*" (например, временная метка вместо "AnyText") в его имени файла без растеризации
       redactor.Save(new SaveOptions(false, "AnyText"));
    }    
```

### Смотрите также

* class [SaveOptions](../../../groupdocs.redaction.options/saveoptions)
* class [Redactor](../../redactor)
* пространство имен [GroupDocs.Redaction](../../redactor)
* сборка [GroupDocs.Redaction](../../../)

---

## Save(Stream, RasterizationOptions) {#save_2}

Сохраняет документ в поток, включая пользовательское местоположение.

```csharp
public void Save(Stream document, RasterizationOptions rasterizationOptions)
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| document | Stream | Целевой поток |
| rasterizationOptions | RasterizationOptions | Варианты растрирования или нет, а также указание страниц для растеризации |

### Примеры

В следующем примере показано, как установить параметры процесса растеризации.

```csharp
    using (var redactor = new Redactor("SomePresentation.pptx"))
    {
        // редактируем конфиденциальные данные на первом слайде 
    
        var rasterizationOptions = new RasterizationOptions();
        rasterizationOptions.PageIndex = 0;
        rasterizationOptions.PageCount = 1;
        rasterizationOptions.Compliance = PdfComplianceLevel.PdfA1a;
        using (var stream = File.Open(Path.Combine(@"C:\Temp", "PresentationFirstSlide.pdf")))
        {
            redactor.Save(stream, rasterizationOptions);
        }
    }      
```

### Смотрите также

* class [RasterizationOptions](../../../groupdocs.redaction.options/rasterizationoptions)
* class [Redactor](../../redactor)
* пространство имен [GroupDocs.Redaction](../../redactor)
* сборка [GroupDocs.Redaction](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Redaction.dll -->