---
title: DataMatrixEncodeMode
second_title: Справочник по API GroupDocs.Signature для .NET
description: Режим кодирования кодировщика DataMatrix по умолчанию Auto
type: docs
weight: 220
url: /ru/net/groupdocs.signature.domain.extensions/datamatrixencodemode/
---
## DataMatrixEncodeMode enumeration

Режим кодирования кодировщика DataMatrix, по умолчанию Auto

```csharp
public enum DataMatrixEncodeMode
```

### Ценности

| Имя | Ценность | Описание |
| --- | --- | --- |
| Auto | `0` | Автоматически выбирать лучший режим кодирования для кодирования DataMatrix |
| ASCII | `1` | Кодирует один буквенно-цифровой или два цифровых символа на байт |
| Full | `6` | Кодировать 8-битные значения |
| Custom | `7` | Кодировать с помощью кодировки, указанной в BarcodeGenerator.Parameters.Barcode.DataMatrix.CodeTextEncoding |
| C40 | `8` | Использует кодировку C40. Кодирует прописные буквенно-цифровые, строчные и специальные символы |
| Text | `9` | Использует кодировку текста. Кодирует строчные буквенно-цифровые, прописные и специальные символы. |
| EDIFACT | `10` | Использует кодировку EDIFACT. Использует шесть бит на символ, кодирует цифры, заглавные буквы и множество знаков препинания, но не поддерживает строчные буквы. |
| ANSIX12 | `11` | Использует кодировку ANSI X12. |
| ExtendedCodetext | `12` | Режим ExtendedCodetext позволяет вручную переключать схемы кодирования в код-текст. Формат: "\Encodation_scheme_name:text\Encodation_scheme_name:text". Допустимые схемы кодирования: EDIFACT, ANSIX12, ASCII, C40, Text, Auto. Расширенный код- пример текста: @"\ansix12:ANSIX12TEXT\ascii:обратная косая черта должна быть удвоена \\ \edifact:EdifactEncodedText" Все символы обратной косой черты (\) должны быть удвоены в тексте. |

### Смотрите также

* пространство имен [GroupDocs.Signature.Domain.Extensions](../../groupdocs.signature.domain.extensions)
* сборка [GroupDocs.Signature](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Signature.dll -->
