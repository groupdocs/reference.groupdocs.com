---
title: RedactionPolicy
second_title: Справочник по API GroupDocs.Redaction для .NET
description: Представляет политику очистки содержащую набор определенных исправлений которые необходимо применить.
type: docs
weight: 410
url: /ru/net/groupdocs.redaction/redactionpolicy/
---
## RedactionPolicy class

Представляет политику очистки, содержащую набор определенных исправлений, которые необходимо применить.

```csharp
public class RedactionPolicy
```

## Конструкторы

| Имя | Описание |
| --- | --- |
| [RedactionPolicy](redactionpolicy#constructor)() | Создает новый экземпляр политики редактирования. |
| [RedactionPolicy](redactionpolicy#constructor_1)(Redaction[]) | Создает новый экземпляр политики редактирования с определенным списком исправлений. |

## Характеристики

| Имя | Описание |
| --- | --- |
| [Redactions](../../groupdocs.redaction/redactionpolicy/redactions) { get; } | Получает массив полностью настроенных[`Redaction`](../redaction) -производные классы. |

## Методы

| Имя | Описание |
| --- | --- |
| static [Load](../../groupdocs.redaction/redactionpolicy/load#load)(Stream) | Загружает экземпляр[`RedactionPolicy`](../redactionpolicy) из потока. |
| static [Load](../../groupdocs.redaction/redactionpolicy/load#load_1)(string) | Загружает экземпляр[`RedactionPolicy`](../redactionpolicy) из пути к файлу. |
| [Save](../../groupdocs.redaction/redactionpolicy/save#save)(Stream) | Сохраняет политику редактирования в потоке. |
| [Save](../../groupdocs.redaction/redactionpolicy/save#save_1)(string) | Сохраняет политику редактирования в файл. |

### Примечания

**Узнать больше**

* Подробнее о правилах: [Использование политик редактирования](https://docs.groupdocs.com/redaction/net/use-redaction-policies/)
* Подробнее о применении правок: [Основы редактирования](https://docs.groupdocs.com/redaction/net/redaction-basics/)

### Примеры

В следующем примере показано, как применить политику редактирования ко всем файлам в заданной входящей папке и сохранить в одной из исходящих папок — для успешно обновленных файлов и для неудачно обновленных.

В следующем примере содержится пример XML-файла политики с примерами конфигураций для всех типов исправлений.

```csharp
RedactionPolicy policy = RedactionPolicy.Load("RedactionPolicy.xml");
foreach (var fileEntry in Directory.GetFileNames("C:\\Inbound")) 
{
     using (Redactor redactor = new Redactor(Path.Combine("C:\\Inbound\\", fileEntry)))
     {
    	     RedactorChangeLog result = redactor.Apply(policy);
    	     String resultFolder = result.Status != RedactionStatus.Failed ? "C:\\Outbound\\Done\\" : "C:\\Outbound\\Failed\\";
    	     using (Stream fileStream = File.Open(Path.Combine(resultFolder, fileEntry), FileMode.Open, FileAccess.ReadWrite))
   	     {
               redactor.Save(fileStream, new RasterizationOptions() { Enabled = false });
   	     }        
     }
}   
```

```csharp
<?xml version="1.0" encoding="utf-8"?>  
<redactionPolicy xmlns = "http://www.groupdocs.com/redaction" >
  <regexRedaction regularExpression="(dolor)" actionType="ReplaceString" replacement="foobar" />  
  <exactPhraseRedaction searchPhrase = "dolor" caseSensitive="true" actionType="DrawBox" color="Red" />   
  
  <cellColumnRedaction regularExpression = "(foo)bar1" replacement="[red1]" columnIndex="1" worksheetIndex="2" /> 
  <cellColumnRedaction regularExpression = "(foo)bar2" replacement="[red2]" wokrsheetName="Sample" /> 
  
  <eraseMetadataRedaction filter = "All" />
  <metadataSearchRedaction filter="Title, Author" replacement="foobar" valueExpression="(metasearch)" keyExpression="" />  
  
 <annotationRedaction regularExpression = "(anno1)" replacement="foobar" />  
 <deleteAnnotationRedaction regularExpression = "(anno2)" />

 <imageAreaRedaction pointX="15" pointY="17" width="200" height="10" color="#AA50FC"  />  
 <imageAreaRedaction pointX = "110" pointY="120" width="60" height="20" color="Magenta"  />  
</redactionPolicy>
```

### Смотрите также

* пространство имен [GroupDocs.Redaction](../../groupdocs.redaction)
* сборка [GroupDocs.Redaction](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Redaction.dll -->
