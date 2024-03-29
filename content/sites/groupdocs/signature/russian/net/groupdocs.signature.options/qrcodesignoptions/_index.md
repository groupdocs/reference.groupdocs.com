---
title: QrCodeSignOptions
second_title: Справочник по API GroupDocs.Signature для .NET
description: Представляет параметры подписи QRкода.
type: docs
weight: 1630
url: /ru/net/groupdocs.signature.options/qrcodesignoptions/
---
## QrCodeSignOptions class

Представляет параметры подписи QR-кода.

```csharp
public class QrCodeSignOptions : TextSignOptions
```

## Конструкторы

| Имя | Описание |
| --- | --- |
| [QrCodeSignOptions](qrcodesignoptions#constructor)() | Инициализирует новый экземпляр класса QRCodeSignOptions со значениями по умолчанию. |
| [QrCodeSignOptions](qrcodesignoptions#constructor_1)(string) | Инициализирует новый экземпляр класса QRCodeSignOptions с текстом. |
| [QrCodeSignOptions](qrcodesignoptions#constructor_2)(string, QrCodeType) | Инициализирует новый экземпляр класса BarcodeSignOptions с текстом. |

## Характеристики

| Имя | Описание |
| --- | --- |
| virtual [AllPages](../../groupdocs.signature.options/signoptions/allpages) { get; set; } | Поставить подпись на всех страницах документа. |
| [Appearance](../../groupdocs.signature.options/signoptions/appearance) { get; set; } | Внешний вид дополнительной подписи. |
| [Background](../../groupdocs.signature.options/textsignoptions/background) { get; set; } | Получает или задает настройки фона подписи. |
| [Border](../../groupdocs.signature.options/textsignoptions/border) { get; set; } | Укажите настройки границ |
| [CodeTextAlignment](../../groupdocs.signature.options/qrcodesignoptions/codetextalignment) { get; set; } | Получает или задает выравнивание текста в результирующем изображении QR-кода. Значение по умолчанию — None. |
| [Data](../../groupdocs.signature.options/qrcodesignoptions/data) { get; set; } | Получает или задает пользовательский объект для сериализации в содержимое QR-кода. |
| [DataEncryption](../../groupdocs.signature.options/qrcodesignoptions/dataencryption) { get; set; } | Получает или задает реализацию[`IDataEncryption`](../../groupdocs.signature.domain.extensions/idataencryption) интерфейс для кодирования и декодирования текста подписи QR-кода или свойств данных. |
| [DocumentType](../../groupdocs.signature.options/signoptions/documenttype) { get; set; } | Получить или установить тип документа для параметров подписи[`DocumentType`](../../groupdocs.signature.domain/documenttype) |
| [EncodeType](../../groupdocs.signature.options/qrcodesignoptions/encodetype) { get; set; } | Получает или устанавливает тип QR-кода. |
| [Extensions](../../groupdocs.signature.options/signoptions/extensions) { get; } | Расширения подписи. |
| [Font](../../groupdocs.signature.options/textsignoptions/font) { get; set; } | Получает или задает шрифт подписи. |
| override [ForeColor](../../groupdocs.signature.options/qrcodesignoptions/forecolor) { get; set; } | Получает или задает цвет переднего плана QR-кода bar Использование этого свойства может вызвать проблемы с проверкой. Используйте его осторожно. |
| [FormTextFieldTitle](../../groupdocs.signature.options/textsignoptions/formtextfieldtitle) { get; set; } | Получает или задает заголовок поля текстовой формы для размещения в нем текстовой подписи. Это свойство можно использовать только с SignatureImplementation = TextToFormField. |
| [FormTextFieldType](../../groupdocs.signature.options/textsignoptions/formtextfieldtype) { get; set; } | Получает или задает тип поля формы для размещения в нем текстовой подписи. Это свойство можно использовать только с SignatureImplementation = TextToFormField. Значение по умолчанию — AllTextTypes. |
| [Height](../../groupdocs.signature.options/textsignoptions/height) { get; set; } | Высота подписи на странице документа в значениях измерения (в пикселях, процентах или миллиметрах см.[`MeasureType`](../../groupdocs.signature.domain/measuretype) Свойство SizeMeasureType). |
| [HorizontalAlignment](../../groupdocs.signature.options/textsignoptions/horizontalalignment) { get; set; } | Горизонтальное выравнивание подписи на странице документа. |
| [InnerMargins](../../groupdocs.signature.options/qrcodesignoptions/innermargins) { get; set; } | Получает или задает расстояние между элементами QR-кода и границами результирующего изображения. |
| [Left](../../groupdocs.signature.options/textsignoptions/left) { get; set; } | Левая позиция X подписи на странице документа в значениях измерения (пиксели, проценты или миллиметры, см.[`MeasureType`](../../groupdocs.signature.domain/measuretype) Свойство LocationMeasureType). (работает, если горизонтальное выравнивание не указано). |
| virtual [LocationMeasureType](../../groupdocs.signature.options/textsignoptions/locationmeasuretype) { get; set; } | Тип измерения (пиксели, проценты или миллиметры) для свойств Left и Top. |
| [LogoFilePath](../../groupdocs.signature.options/qrcodesignoptions/logofilepath) { get; set; } | Получает или задает имя файла изображения логотипа QR-кода. Это свойство используется, только если не указан LogoStream. Использование этого свойства может вызвать проблемы с проверкой. Используйте его осторожно. |
| [LogoStream](../../groupdocs.signature.options/qrcodesignoptions/logostream) { get; set; } | Получает или задает поток изображения логотипа QR-кода. Если это свойство указано, оно всегда используется вместо LogoFilePath. Использование этого свойства может вызвать проблемы с проверкой. Используйте его осторожно. |
| virtual [Margin](../../groupdocs.signature.options/textsignoptions/margin) { get; set; } | Получает или задает расстояние между краями подписи и документа. (работает ТОЛЬКО, если указано горизонтальное или вертикальное выравнивание). |
| virtual [MarginMeasureType](../../groupdocs.signature.options/textsignoptions/marginmeasuretype) { get; set; } | Получает или задает тип измерения (пиксели, проценты или миллиметры) для Margin. |
| [Native](../../groupdocs.signature.options/textsignoptions/native) { get; set; } | Получает или задает собственный атрибут. Если он установлен, могут использоваться подписи, специфичные для документа. Например, собственный текстовый водяной знак для документов WordProcessing отличается от обычного. |
| virtual [PageNumber](../../groupdocs.signature.options/signoptions/pagenumber) { get; set; } | Получает или устанавливает номер страницы документа для подписи. Минимальное значение по умолчанию: 1. |
| virtual [PagesSetup](../../groupdocs.signature.options/signoptions/pagessetup) { get; set; } | Параметры для указания подписываемых страниц. |
| [ReturnContent](../../groupdocs.signature.options/qrcodesignoptions/returncontent) { get; set; } | Получает или устанавливает флаг для получения содержимого изображения QR-кода подписи, которая была помещена на страницу документа.[`ReturnContentType`](./returncontenttype) . По умолчанию эта опция отключена. |
| [ReturnContentType](../../groupdocs.signature.options/qrcodesignoptions/returncontenttype) { get; set; } | Указывает тип файла возвращаемого содержимого изображения подписи QR-кода, когда свойство ReturnContent включено. По умолчанию установлено значение Null. Это означает возврат содержимого изображения QR-кода в исходном формате. Этот формат изображения указан в[`Format`](../../groupdocs.signature.domain/qrcodesignature/format) Возможные поддерживаемые значения: FileType.JPEG, FileType.PNG, FileType.BMP. Если предоставленный формат не поддерживается, будет возвращено содержимое изображения QR-кода в формате .png. |
| [RotationAngle](../../groupdocs.signature.options/textsignoptions/rotationangle) { get; set; } | Угол поворота подписи на странице документа (по часовой стрелке). |
| [ShapeType](../../groupdocs.signature.options/textsignoptions/shapetype) { get; set; } | Получает или задает тип формы для размещения текста. Это свойство можно использовать только с SignatureImplementation = TextStamp. Значение по умолчанию — Rectangle. |
| [SignatureID](../../groupdocs.signature.options/textsignoptions/signatureid) { get; set; } | Получает или задает уникальный идентификатор подписи. Его можно использовать в опциях проверки подписи. Свойство поддерживается только для документов Pdf. |
| [SignatureImplementation](../../groupdocs.signature.options/textsignoptions/signatureimplementation) { get; set; } | Получает или задает тип реализации текстовой подписи. |
| [SignatureType](../../groupdocs.signature.options/signoptions/signaturetype) { get; } | Получить тип подписи[`SignatureType`](../../groupdocs.signature.domain/signaturetype) |
| virtual [SizeMeasureType](../../groupdocs.signature.options/textsignoptions/sizemeasuretype) { get; set; } | Тип измерения (пиксели, проценты или миллиметры) для свойств ширины и высоты. |
| [Stretch](../../groupdocs.signature.options/textsignoptions/stretch) { get; set; } | Режим растяжения на странице документа. |
| [Text](../../groupdocs.signature.options/textsignoptions/text) { get; set; } | Получает или задает текст подписи. |
| [TextHorizontalAlignment](../../groupdocs.signature.options/textsignoptions/texthorizontalalignment) { get; set; } | Горизонтальное выравнивание текста внутри подписи. Эта функция поддерживается только для реализаций подписи изображения и аннотации (см.[`TextSignatureImplementation`](../../groupdocs.signature.domain/textsignatureimplementation) Свойство реализации подписи). |
| [TextVerticalAlignment](../../groupdocs.signature.options/textsignoptions/textverticalalignment) { get; set; } | Вертикальное выравнивание текста внутри подписи. Эта функция поддерживается только для реализации подписи изображения (см.[`TextSignatureImplementation`](../../groupdocs.signature.domain/textsignatureimplementation) свойство SignatureImplementation). |
| [Top](../../groupdocs.signature.options/textsignoptions/top) { get; set; } | Верхняя Y позиция подписи на странице документа в значениях измерения (пиксели, проценты или миллиметры, см.[`MeasureType`](../../groupdocs.signature.domain/measuretype)Свойство LocationMeasureType). (работает, если вертикальное выравнивание не указано). |
| [Transparency](../../groupdocs.signature.options/textsignoptions/transparency) { get; set; } | Получает или задает прозрачность подписи (значение от 0,0 (непрозрачная) до 1,0 (прозрачная)). Значение по умолчанию — 0 (непрозрачный). |
| [VerticalAlignment](../../groupdocs.signature.options/textsignoptions/verticalalignment) { get; set; } | Вертикальное выравнивание подписи на странице документа. |
| [Width](../../groupdocs.signature.options/textsignoptions/width) { get; set; } | Ширина подписи на странице документа в значениях измерения (в пикселях, процентах или миллиметрах см.[`MeasureType`](../../groupdocs.signature.domain/measuretype) Свойство SizeMeasureType). |
| [ZOrder](../../groupdocs.signature.options/signoptions/zorder) { get; set; } | Получает или задает положение Z-порядка текстовой подписи. Определяет порядок отображения перекрывающихся подписей. |

### Примечания

**Узнать больше**

* Базовое использование для создания электронной подписи QR-Code с помощью GroupDocs.Signature: [Как подписать документ электронной подписью с помощью QR-кода](https://docs.groupdocs.com/display/signaturenet/eSign+document+with+QR-code+signature)
* Расширенное использование настроек электронной подписи QR-Code с GroupDocs.Signature: [Расширенное использование документа eSign с подписью QR-Code и дополнительными настройками](https://docs.groupdocs.com/display/signaturenet/Sign+document+with+QR-code+signature+-+advanced)

### Смотрите также

* class [TextSignOptions](../textsignoptions)
* пространство имен [GroupDocs.Signature.Options](../../groupdocs.signature.options)
* сборка [GroupDocs.Signature](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Signature.dll -->
