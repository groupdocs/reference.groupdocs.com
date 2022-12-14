---
title: DocumentFormatInstance
second_title: .NET API Başvurusu için GroupDocs.Redaction
description: Belirli bir belge biçimini temsil eder. Kendi belge türlerinizi eklemek için bu sınıfı uygulayın.
type: docs
weight: 110
url: /tr/net/groupdocs.redaction.integration/documentformatinstance/
---
## DocumentFormatInstance class

Belirli bir belge biçimini temsil eder. Kendi belge türlerinizi eklemek için bu sınıfı uygulayın.

```csharp
public abstract class DocumentFormatInstance
```

## Özellikleri

| İsim | Tanım |
| --- | --- |
| [Password](../../groupdocs.redaction.integration/documentformatinstance/password) { get; set; } | Parola korumalı belgeler için bir parola alır veya ayarlar. |

## yöntemler

| İsim | Tanım |
| --- | --- |
| virtual [Initialize](../../groupdocs.redaction.integration/documentformatinstance/initialize)(DocumentFormatConfiguration, RedactorSettings) | Belge biçimi işleyici örneğinin başlatılmasını gerçekleştirir. |
| [IsRedactionAccepted](../../groupdocs.redaction.integration/documentformatinstance/isredactionaccepted)(RedactionDescription) | Şunları kontrol eder:[`IRedactionCallback`](../../groupdocs.redaction.redactions/iredactioncallback) uygulama ve belirtilirse onu çağırır. |
| virtual [Load](../../groupdocs.redaction.integration/documentformatinstance/load)(Stream) | Belgeyi bir akıştan yükler. |
| virtual [PerformBinaryCheck](../../groupdocs.redaction.integration/documentformatinstance/performbinarycheck)(Stream) | Verilen akışın bu biçim örneği tarafından desteklenen bir belge içerip içermediğini kontrol eder. |
| abstract [Save](../../groupdocs.redaction.integration/documentformatinstance/save)(Stream) | Belgeyi bir akışa kaydeder. |

### Notlar

**Daha fazla bilgi edin**

* Özel biçimlerin uygulanması hakkında daha fazla ayrıntı: [Özel biçim işleyici oluştur](https://docs.groupdocs.com/redaction/net/create-custom-format-handler/)

### Örnekler

Aşağıdaki örnek, özel biçim işleyicisi için boş bir saplamanın nasıl oluşturulacağını gösterir.

Aşağıdaki örnek, başlatma verilerinin nasıl kullanılacağını gösterir.

```csharp
public class DummyDocument : DocumentFormatInstance
{     
    public override void Load(Stream output)
    {
        // dosya içeriğini yükle
    }

    public override void Save(Stream output)
    {
        // değişiklikleri dosyaya kaydet;
    }
}
```

```csharp
public class MyCustomHandler : DocumentFormatInstance
{
    private string MyProperty { get; set; }
    
    // Diğer özel kod 
    ...

    public override void Initialize(DocumentFormatConfiguration config)
    {
        base.Initialize(config);
        if (config.InitializationData.ContainsKey("MyProperty"))
        {
            MyProperty = config.InitializationData["MyProperty"];
        }
    }
}

// Özel biçimi GroupDocs.Redaction'a ekleme
var mySettings = new DocumentFormatConfiguration();
mySettings.ExtensionFilter = ".foo";
mySettings.DocumentType = typeof(MyCustomHandler);
mySettings.InitializationData.Add("MyProperty", "bar");
var configuration = RedactorConfiguration.GetInstance();
configuration.AvailableFormats.Add(mySettings);
```

### Ayrıca bakınız

* ad alanı [GroupDocs.Redaction.Integration](../../groupdocs.redaction.integration)
* toplantı [GroupDocs.Redaction](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Redaction.dll -->
