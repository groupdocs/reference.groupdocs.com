---
title: Woff2Font
second_title: Справочник по API GroupDocs.Editor для .NET
description: Представляет один шрифт в формате WOFF2 Web Open Font Format
type: docs
weight: 410
url: /ru/net/groupdocs.editor.htmlcss.resources.fonts/woff2font/
---
## Woff2Font class

Представляет один шрифт в формате WOFF2 (Web Open Font Format)

```csharp
public sealed class Woff2Font : FontResourceBase
```

## Конструкторы

| Имя | Описание |
| --- | --- |
| [Woff2Font](woff2font#constructor)(string, Stream) | Создает новый класс Woff2Font из содержимого, представленного в виде потока байтов, и с указанным именем |
| [Woff2Font](woff2font#constructor_1)(string, string) | Создает новый класс Woff2Font из содержимого, представленного в виде строки в кодировке base64, и с указанным именем |

## Характеристики

| Имя | Описание |
| --- | --- |
| [ByteContent](../../groupdocs.editor.htmlcss.resources.fonts/fontresourcebase/bytecontent) { get; } | Возвращает содержимое этого шрифта в виде байтового потока |
| [FilenameWithExtension](../../groupdocs.editor.htmlcss.resources.fonts/fontresourcebase/filenamewithextension) { get; } | Возвращает правильное имя файла этого ресурса шрифта, которое состоит из имени и расширения. Теоретически может отличаться от названия. |
| [IsDisposed](../../groupdocs.editor.htmlcss.resources.fonts/fontresourcebase/isdisposed) { get; } | Определяет, удален ли этот шрифт или нет |
| [Name](../../groupdocs.editor.htmlcss.resources.fonts/fontresourcebase/name) { get; } | Возвращает имя этого ресурса шрифта. Обычно не содержит расширения имени файла и теоретически может отличаться от имени файла. |
| [TextContent](../../groupdocs.editor.htmlcss.resources.fonts/fontresourcebase/textcontent) { get; } | Возвращает содержимое этого шрифта в виде строки в кодировке base64. Это значение кэшируется после первого вызова. |
| override [Type](../../groupdocs.editor.htmlcss.resources.fonts/woff2font/type) { get; } | Возвращает FontType.Woff2 |

## Методы

| Имя | Описание |
| --- | --- |
| [Dispose](../../groupdocs.editor.htmlcss.resources.fonts/fontresourcebase/dispose)() | Удаляет этот ресурс шрифта, удаляя его содержимое и делая большинство методов и свойств нерабочими |
| [Equals](../../groupdocs.editor.htmlcss.resources.fonts/fontresourcebase/equals)(FontResourceBase) | Проверяет этот экземпляр с указанным ресурсом шрифта по ссылке на равенство |
| [Equals](../../groupdocs.editor.htmlcss.resources.fonts/fontresourcebase/equals)(IHtmlResource) | Проверяет этот экземпляр с указанным HTML-ресурсом по ссылке на равенство |
| [Save](../../groupdocs.editor.htmlcss.resources.fonts/fontresourcebase/save)(string) | Сохраняет этот шрифт в указанный файл |
| static [IsValid](../../groupdocs.editor.htmlcss.resources.fonts/woff2font/isvalid#isvalid)(Stream) | Проверяет, является ли указанный поток допустимым шрифтом WOFF2 |
| static [IsValid](../../groupdocs.editor.htmlcss.resources.fonts/woff2font/isvalid#isvalid_1)(string) | Проверяет, является ли указанная строка в кодировке base64 допустимым шрифтом WOFF2 |

## Поля

| Имя | Описание |
| --- | --- |
| const [RequiredHeaderSize](../../groupdocs.editor.htmlcss.resources.fonts/woff2font/requiredheadersize) | Размер заголовка WOFF2 (в байтах), необходимый для его проверки |

## События

| Имя | Описание |
| --- | --- |
| event [Disposed](../../groupdocs.editor.htmlcss.resources.fonts/fontresourcebase/disposed) | Событие, возникающее при удалении этого шрифта |

### Смотрите также

* class [FontResourceBase](../fontresourcebase)
* пространство имен [GroupDocs.Editor.HtmlCss.Resources.Fonts](../../groupdocs.editor.htmlcss.resources.fonts)
* сборка [GroupDocs.Editor](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Editor.dll -->
