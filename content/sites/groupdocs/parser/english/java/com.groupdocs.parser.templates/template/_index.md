---
title: Template
second_title: GroupDocs.Parser for Java API Reference
description: Provides the document template.
type: docs
weight: 10
url: /java/com.groupdocs.parser.templates/template/
---
**Inheritance:**
java.lang.Object

**All Implemented Interfaces:**
java.lang.Iterable
```
public class Template implements Iterable<TemplateItem>
```

Provides the document template. It consists of [TemplateItem](../../com.groupdocs.parser.templates/templateitem) objects which represent the items of the template such as text field and table definitions.

**Learn more:**

 *  [Working with templates][]


[Working with templates]: https://docs.groupdocs.com/display/parserjava/Working+with+templates
## Constructors

| Constructor | Description |
| --- | --- |
| [Template(Iterable<? extends TemplateItem> items)](#Template-java.lang.Iterable---extends-com.groupdocs.parser.templates.TemplateItem--) | Initializes a new instance of the [Template](../../com.groupdocs.parser.templates/template) class. |
| [Template(Iterable<? extends TemplateItem> items, TemplateOptions options)](#Template-java.lang.Iterable---extends-com.groupdocs.parser.templates.TemplateItem--com.groupdocs.parser.templates.TemplateOptions-) | Initializes a new instance of the [Template](../../com.groupdocs.parser.templates/template) class. |
## Methods

| Method | Description |
| --- | --- |
| [getCount()](#getCount--) | Gets the total number of template items. |
| [get(int index)](#get-int-) | Gets the template item by an index. |
| [getOptions()](#getOptions--) | Gets the template options. |
| [iterator()](#iterator--) |  |
| [load(String filePath)](#load-java.lang.String-) | Loads a template from a file. |
| [load(InputStream stream)](#load-java.io.InputStream-) | Loads a template from a stream. |
| [save(String filePath)](#save-java.lang.String-) | Saves a template to a file. |
| [save(OutputStream stream)](#save-java.io.OutputStream-) | Saves a template to a stream. |
### Template(Iterable<? extends TemplateItem> items) {#Template-java.lang.Iterable---extends-com.groupdocs.parser.templates.TemplateItem--}
```
public Template(Iterable<? extends TemplateItem> items)
```


Initializes a new instance of the [Template](../../com.groupdocs.parser.templates/template) class.

Usage:

```
// Create an array of template fields
 TemplateItem[] fields = new TemplateItem[]
 {
     new TemplateField(new TemplateRegexPosition("From"), "From", 0),
     new TemplateField(
         new TemplateLinkedPosition("From", new Size(100, 10), new TemplateLinkedPositionEdges(false, false, false, true)),
         "FromCompany",
         0),
     new TemplateField(
         new TemplateLinkedPosition("FromCompany", new Size(100, 30), new TemplateLinkedPositionEdges(false, false, false, true)),
         "FromAddress",
         0)
 };
 // Create a document template
 Template template = new Template(java.util.Arrays.asList(fields));
 
```

**Parameters:**
| Parameter | Type | Description |
| --- | --- | --- |
| items | java.lang.Iterable<? extends com.groupdocs.parser.templates.TemplateItem> | The collection of [TemplateItem](../../com.groupdocs.parser.templates/templateitem) objects. |

### Template(Iterable<? extends TemplateItem> items, TemplateOptions options) {#Template-java.lang.Iterable---extends-com.groupdocs.parser.templates.TemplateItem--com.groupdocs.parser.templates.TemplateOptions-}
```
public Template(Iterable<? extends TemplateItem> items, TemplateOptions options)
```


Initializes a new instance of the [Template](../../com.groupdocs.parser.templates/template) class.

**Parameters:**
| Parameter | Type | Description |
| --- | --- | --- |
| items | java.lang.Iterable<? extends com.groupdocs.parser.templates.TemplateItem> | The collection of [TemplateItem](../../com.groupdocs.parser.templates/templateitem) objects. |
| options | [TemplateOptions](../../com.groupdocs.parser.templates/templateoptions) | The template options. |

### getCount() {#getCount--}
```
public int getCount()
```


Gets the total number of template items.

**Returns:**
int - An integer that represents the total number of template items.
### get(int index) {#get-int-}
```
public TemplateItem get(int index)
```


Gets the template item by an index.

**Parameters:**
| Parameter | Type | Description |
| --- | --- | --- |
| index | int | The zero-based index of the template item. |

**Returns:**
[TemplateItem](../../com.groupdocs.parser.templates/templateitem) - An instance of [TemplateItem](../../com.groupdocs.parser.templates/templateitem) class.
### getOptions() {#getOptions--}
```
public TemplateOptions getOptions()
```


Gets the template options.

**Returns:**
[TemplateOptions](../../com.groupdocs.parser.templates/templateoptions) - An instance of [TemplateOptions](../../com.groupdocs.parser.templates/templateoptions) class.
### iterator() {#iterator--}
```
public Iterator<TemplateItem> iterator()
```




**Returns:**
java.util.Iterator<com.groupdocs.parser.templates.TemplateItem>
### load(String filePath) {#load-java.lang.String-}
```
public static Template load(String filePath)
```


Loads a template from a file.

**Parameters:**
| Parameter | Type | Description |
| --- | --- | --- |
| filePath | java.lang.String | The path to the file. |

**Returns:**
[Template](../../com.groupdocs.parser.templates/template) - An instance of [Template](../../com.groupdocs.parser.templates/template) class with loaded template.
### load(InputStream stream) {#load-java.io.InputStream-}
```
public static Template load(InputStream stream)
```


Loads a template from a stream.

**Parameters:**
| Parameter | Type | Description |
| --- | --- | --- |
| stream | java.io.InputStream | The input stream. |

**Returns:**
[Template](../../com.groupdocs.parser.templates/template) - An instance of [Template](../../com.groupdocs.parser.templates/template) class with loaded template.
### save(String filePath) {#save-java.lang.String-}
```
public void save(String filePath)
```


Saves a template to a file.

**Parameters:**
| Parameter | Type | Description |
| --- | --- | --- |
| filePath | java.lang.String | The path to the file. |

### save(OutputStream stream) {#save-java.io.OutputStream-}
```
public void save(OutputStream stream)
```


Saves a template to a stream.

**Parameters:**
| Parameter | Type | Description |
| --- | --- | --- |
| stream | java.io.OutputStream | The output stream. |

