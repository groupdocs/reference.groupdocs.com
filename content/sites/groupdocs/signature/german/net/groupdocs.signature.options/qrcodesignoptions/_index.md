---
title: QrCodeSignOptions
second_title: GroupDocs.Signature für .NET-API-Referenz
description: Repräsentiert die QRCodeSignaturoptionen.
type: docs
weight: 1630
url: /de/net/groupdocs.signature.options/qrcodesignoptions/
---
## QrCodeSignOptions class

Repräsentiert die QR-Code-Signaturoptionen.

```csharp
public class QrCodeSignOptions : TextSignOptions
```

## Konstrukteure

| Name | Beschreibung |
| --- | --- |
| [QrCodeSignOptions](qrcodesignoptions#constructor)() | Initialisiert eine neue Instanz der QRCodeSignOptions-Klasse mit Standardwerten. |
| [QrCodeSignOptions](qrcodesignoptions#constructor_1)(string) | Initialisiert eine neue Instanz der QRCodeSignOptions-Klasse mit Text. |
| [QrCodeSignOptions](qrcodesignoptions#constructor_2)(string, QrCodeType) | Initialisiert eine neue Instanz der BarcodeSignOptions-Klasse mit Text. |

## Eigenschaften

| Name | Beschreibung |
| --- | --- |
| virtual [AllPages](../../groupdocs.signature.options/signoptions/allpages) { get; set; } | Unterschreiben Sie alle Dokumentseiten. |
| [Appearance](../../groupdocs.signature.options/signoptions/appearance) { get; set; } | Zusätzliche Signaturdarstellung. |
| [Background](../../groupdocs.signature.options/textsignoptions/background) { get; set; } | Ruft die Hintergrundeinstellungen der Signatur ab oder legt sie fest. |
| [Border](../../groupdocs.signature.options/textsignoptions/border) { get; set; } | Rahmeneinstellungen festlegen |
| [CodeTextAlignment](../../groupdocs.signature.options/qrcodesignoptions/codetextalignment) { get; set; } | Ruft die Textausrichtung im QR-Code-Ergebnisbild ab oder legt sie fest. Der Standardwert ist „Keine“. |
| [Data](../../groupdocs.signature.options/qrcodesignoptions/data) { get; set; } | Ruft benutzerdefiniertes Objekt ab oder legt es fest, das in QR-Code-Inhalt serialisiert werden soll. |
| [DataEncryption](../../groupdocs.signature.options/qrcodesignoptions/dataencryption) { get; set; } | Ruft die Implementierung von ab oder legt sie fest[`IDataEncryption`](../../groupdocs.signature.domain.extensions/idataencryption) Schnittstelle zum Codieren und Decodieren von QR-Code-Signaturtext oder Dateneigenschaften. |
| [DocumentType](../../groupdocs.signature.options/signoptions/documenttype) { get; set; } | Abrufen oder Festlegen des Dokumenttyps der Signaturoptionen[`DocumentType`](../../groupdocs.signature.domain/documenttype) |
| [EncodeType](../../groupdocs.signature.options/qrcodesignoptions/encodetype) { get; set; } | Ermittelt oder setzt den QR-Code-Typ. |
| [Extensions](../../groupdocs.signature.options/signoptions/extensions) { get; } | Signaturerweiterungen. |
| [Font](../../groupdocs.signature.options/textsignoptions/font) { get; set; } | Ruft die Schriftart der Signatur ab oder legt sie fest. |
| override [ForeColor](../../groupdocs.signature.options/qrcodesignoptions/forecolor) { get; set; } | Ermittelt oder setzt die Vorderfarbe von QR-Code bars Die Verwendung dieser Eigenschaft kann zu Problemen bei der Überprüfung führen. Gehen Sie vorsichtig damit um. |
| [FormTextFieldTitle](../../groupdocs.signature.options/textsignoptions/formtextfieldtitle) { get; set; } | Ruft den Titel des Textformularfelds ab oder legt ihn fest, um eine Textsignatur darin einzufügen. Diese Eigenschaft kann nur mit SignatureImplementation = TextToFormField verwendet werden. |
| [FormTextFieldType](../../groupdocs.signature.options/textsignoptions/formtextfieldtype) { get; set; } | Ruft den Typ des Formularfelds ab oder legt ihn fest, um eine Textsignatur darin einzufügen. Diese Eigenschaft kann nur mit SignatureImplementation = TextToFormField verwendet werden. Der Standardwert ist AllTextTypes. |
| [Height](../../groupdocs.signature.options/textsignoptions/height) { get; set; } | Höhe der Unterschrift auf Dokumentseite in Messwerte (Pixel, Prozent oder Millimeter s[`MeasureType`](../../groupdocs.signature.domain/measuretype) SizeMeasureType-Eigenschaft). |
| [HorizontalAlignment](../../groupdocs.signature.options/textsignoptions/horizontalalignment) { get; set; } | Horizontale Ausrichtung der Signatur auf der Dokumentseite. |
| [InnerMargins](../../groupdocs.signature.options/qrcodesignoptions/innermargins) { get; set; } | Ermittelt oder setzt den Abstand zwischen QR-Code-Elementen und Ergebnisbildrändern. |
| [Left](../../groupdocs.signature.options/textsignoptions/left) { get; set; } | Linke X-Position der Signatur auf Dokumentseite in Messwerte (Pixel, Prozent oder Millimeter siehe[`MeasureType`](../../groupdocs.signature.domain/measuretype) LocationMeasureType-Eigenschaft). (funktioniert, wenn keine horizontale Ausrichtung angegeben ist). |
| virtual [LocationMeasureType](../../groupdocs.signature.options/textsignoptions/locationmeasuretype) { get; set; } | Maßtyp (Pixel, Prozent oder Millimeter) für Left- und Top-Eigenschaften. |
| [LogoFilePath](../../groupdocs.signature.options/qrcodesignoptions/logofilepath) { get; set; } | Ruft den Dateinamen des QR-Code-Logobilds ab oder legt ihn fest. Diese Eigenschaft wird nur verwendet, wenn LogoStream nicht angegeben ist. Die Verwendung dieser Eigenschaft kann Probleme bei der Überprüfung verursachen. Gehen Sie vorsichtig damit um. |
| [LogoStream](../../groupdocs.signature.options/qrcodesignoptions/logostream) { get; set; } | Ruft den QR-Code-Logo-Bildstream ab oder setzt ihn. Wenn diese Eigenschaft angegeben ist, wird sie immer verwendet, anstatt LogoFilePath. Die Verwendung dieser Eigenschaft kann Probleme bei der Überprüfung verursachen. Gehen Sie vorsichtig damit um. |
| virtual [Margin](../../groupdocs.signature.options/textsignoptions/margin) { get; set; } | Ruft den Abstand zwischen Zeichen- und Dokumentkanten ab oder legt ihn fest. (funktioniert NUR, wenn horizontale oder vertikale Ausrichtung angegeben ist). |
| virtual [MarginMeasureType](../../groupdocs.signature.options/textsignoptions/marginmeasuretype) { get; set; } | Ruft den Maßtyp (Pixel, Prozent oder Millimeter) für den Rand ab oder legt ihn fest. |
| [Native](../../groupdocs.signature.options/textsignoptions/native) { get; set; } | Ruft das native Attribut ab oder legt es fest. Wenn es eingestellt ist, können dokumentspezifische Signaturen verwendet werden. Natives Textwasserzeichen für WordProcessing-Dokumente ist beispielsweise anders als normal. |
| virtual [PageNumber](../../groupdocs.signature.options/signoptions/pagenumber) { get; set; } | Ruft die Seitenzahl des Dokuments zum Signieren ab oder legt sie fest. Minimal- und Standardwert ist 1. |
| virtual [PagesSetup](../../groupdocs.signature.options/signoptions/pagessetup) { get; set; } | Optionen zum Angeben von Seiten, die signiert werden sollen. |
| [ReturnContent](../../groupdocs.signature.options/qrcodesignoptions/returncontent) { get; set; } | Holt oder setzt das Flag, um QR-Code-Bildinhalt einer Signatur zu erhalten, die auf der Dokumentseite platziert wurde. Wenn dieses Flag auf „true“ gesetzt ist, behält der QR-Code-Signaturbildinhalt Rohbilddaten im erforderlichen Format bei[`ReturnContentType`](./returncontenttype) . Standardmäßig ist diese Option deaktiviert. |
| [ReturnContentType](../../groupdocs.signature.options/qrcodesignoptions/returncontenttype) { get; set; } | Gibt den Dateityp des zurückgegebenen Bildinhalts der QR-Code-Signatur an, wenn die ReturnContent-Eigenschaft aktiviert ist. Standardmäßig ist sie auf Null gesetzt. Das bedeutet, QR-Code-Bildinhalte im Originalformat zurückzugeben. Dieses Bildformat ist spezifiziert bei[`Format`](../../groupdocs.signature.domain/qrcodesignature/format) Mögliche unterstützte Werte sind: FileType.JPEG, FileType.PNG, FileType.BMP. Wenn das angegebene Format nicht unterstützt wird, wird der QR-Code-Bildinhalt im .png-Format zurückgegeben. |
| [RotationAngle](../../groupdocs.signature.options/textsignoptions/rotationangle) { get; set; } | Rotationswinkel der Unterschrift auf der Dokumentenseite (im Uhrzeigersinn). |
| [ShapeType](../../groupdocs.signature.options/textsignoptions/shapetype) { get; set; } | Ruft den Typ der Form zum Einfügen von Text ab oder legt ihn fest. Diese Eigenschaft kann nur mit SignatureImplementation = TextStamp verwendet werden. Der Standardwert ist Rectangle. |
| [SignatureID](../../groupdocs.signature.options/textsignoptions/signatureid) { get; set; } | Ruft die eindeutige ID der Signatur ab oder legt sie fest. Es kann in Optionen zur Signaturüberprüfung verwendet werden. Eigenschaft wird nur für PDF-Dokumente unterstützt. |
| [SignatureImplementation](../../groupdocs.signature.options/textsignoptions/signatureimplementation) { get; set; } | Ruft den Typ der Textsignaturimplementierung ab oder legt ihn fest. |
| [SignatureType](../../groupdocs.signature.options/signoptions/signaturetype) { get; } | Holen Sie sich den Signaturtyp[`SignatureType`](../../groupdocs.signature.domain/signaturetype) |
| virtual [SizeMeasureType](../../groupdocs.signature.options/textsignoptions/sizemeasuretype) { get; set; } | Maßtyp (Pixel, Prozent oder Millimeter) für Breiten- und Höheneigenschaften. |
| [Stretch](../../groupdocs.signature.options/textsignoptions/stretch) { get; set; } | Dehnungsmodus auf Dokumentseite. |
| [Text](../../groupdocs.signature.options/textsignoptions/text) { get; set; } | Ruft den Signaturtext ab oder legt ihn fest. |
| [TextHorizontalAlignment](../../groupdocs.signature.options/textsignoptions/texthorizontalalignment) { get; set; } | Horizontale Ausrichtung von Text innerhalb einer Signatur. Diese Funktion wird nur für Bild- und Anmerkungssignaturimplementierungen unterstützt (siehe[`TextSignatureImplementation`](../../groupdocs.signature.domain/textsignatureimplementation) SignatureImplementation-Eigenschaft). |
| [TextVerticalAlignment](../../groupdocs.signature.options/textsignoptions/textverticalalignment) { get; set; } | Vertikale Ausrichtung von Text innerhalb einer Signatur. Diese Funktion wird nur für die Bildsignaturimplementierung unterstützt (siehe[`TextSignatureImplementation`](../../groupdocs.signature.domain/textsignatureimplementation) SignatureImplementation-Eigenschaft). |
| [Top](../../groupdocs.signature.options/textsignoptions/top) { get; set; } | Top Y Position der Unterschrift auf Dokumentseite in Messwerte (Pixel, Prozent oder Millimeter s[`MeasureType`](../../groupdocs.signature.domain/measuretype)LocationMeasureType-Eigenschaft). (funktioniert, wenn keine vertikale Ausrichtung angegeben ist). |
| [Transparency](../../groupdocs.signature.options/textsignoptions/transparency) { get; set; } | Holt oder setzt die Signaturtransparenz (Wert von 0,0 (undurchsichtig) bis 1,0 (klar)). Der Standardwert ist 0 (undurchsichtig). |
| [VerticalAlignment](../../groupdocs.signature.options/textsignoptions/verticalalignment) { get; set; } | Vertikale Ausrichtung der Signatur auf der Dokumentenseite. |
| [Width](../../groupdocs.signature.options/textsignoptions/width) { get; set; } | Breite der Signatur auf Dokumentseite in Messwerte (Pixel, Prozent oder Millimeter s[`MeasureType`](../../groupdocs.signature.domain/measuretype) SizeMeasureType-Eigenschaft). |
| [ZOrder](../../groupdocs.signature.options/signoptions/zorder) { get; set; } | Ruft die Position der Textsignatur in Z-Reihenfolge ab oder legt sie fest. Legt die Anzeigereihenfolge überlappender Signaturen fest. |

### Bemerkungen

**Erfahren Sie mehr**

* Grundlegende Verwendung zum Erstellen einer elektronischen QR-Code-Signatur durch GroupDocs.Signature: [So signieren Sie ein Dokument mit einer QR-Code-Signatur](https://docs.groupdocs.com/display/signaturenet/eSign+document+with+QR-code+signature)
* Erweiterte Verwendung der Einstellungen der elektronischen QR-Code-Signatur mit GroupDocs.Signature: [Erweiterte Nutzung zum eSignieren von Dokumenten mit QR-Code-Signatur und zusätzlichen Einstellungen](https://docs.groupdocs.com/display/signaturenet/Sign+document+with+QR-code+signature+-+advanced)

### Siehe auch

* class [TextSignOptions](../textsignoptions)
* namensraum [GroupDocs.Signature.Options](../../groupdocs.signature.options)
* Montage [GroupDocs.Signature](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Signature.dll -->
