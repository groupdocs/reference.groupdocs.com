---
title: GetFieldsByName
second_title: Справочник по API GroupDocs.Parser для .NET
description: Возвращает набор данных поля где имя равноfieldName .
type: docs
weight: 50
url: /ru/net/groupdocs.parser.data/documentdata/getfieldsbyname/
---
## DocumentData.GetFieldsByName method

Возвращает набор данных поля, где имя равно*fieldName* .

```csharp
public IList<FieldData> GetFieldsByName(string fieldName)
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| fieldName | String | Имя поля. |

### Возвращаемое значение

Коллекция[`FieldData`](../../fielddata) объекты; пустая коллекция, если данные поля не найдены.

### Примеры

Найти поля по имени поля:

[`FieldData`](../../fielddata) класс представляет данные поля. В зависимости от поля[`PageArea`](../../fielddata/pagearea) property может содержать любого из наследников[`PageArea`](../../pagearea) сорт. Например,[`ParseForm`](../../../groupdocs.parser/parser/parseform) method извлекает только текстовые поля.

```csharp
// Получаем все поля с именем "Адрес"
IList<FieldData> addressFields = data.GetFieldsByName("Address");
if(addressFields.Count == 0) {
    Console.WriteLine("Address not found");
}
else {
    Console.WriteLine("Address");
    // Перебираем коллекцию полей
    for (int i = 0; i < addressFields.Count; i++) {
        PageTextArea area = addressFields[i].PageArea as PageTextArea;
        Console.WriteLine(area == null ? "Not a template field" : area.Text);       
         
        // Если это связанное поле:
        if(addressFields[i].LinkedField != null) {
            Console.Write("Linked to ");
            PageTextArea linkedArea = addressFields[i].LinkedField.PageArea as PageTextArea;
            Console.WriteLine(area == null ? "Not a template field" : area.Text);           
        }
    }
}
```

### Смотрите также

* class [FieldData](../../fielddata)
* class [DocumentData](../../documentdata)
* пространство имен [GroupDocs.Parser.Data](../../documentdata)
* сборка [GroupDocs.Parser](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Parser.dll -->
