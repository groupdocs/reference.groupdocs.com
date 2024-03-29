---
title: SearchPhaseCompleted
second_title: GroupDocs.Search for .NET API 参考
description: 搜索阶段完成时发生
type: docs
weight: 70
url: /zh/net/groupdocs.search.events/eventhub/searchphasecompleted/
---
## EventHub.SearchPhaseCompleted event

搜索阶段完成时发生。

```csharp
public event EventHandler<SearchPhaseEventArgs> SearchPhaseCompleted;
```

### 例子

该示例演示了如何使用事件。

```csharp
string indexFolder = @"c:\MyIndex\";
string documentsFolder = @"c:\MyDocuments\";

// 创建索引
Index index = new Index(indexFolder);

// 索引指定文件夹中的文档
index.Add(documentsFolder);

// 订阅事件
index.Events.SearchPhaseCompleted += (sender, args) =>
{
    Console.WriteLine("Search phase: " + args.SearchPhase);
    Console.WriteLine("Words: " + args.Words.Length);
};

SearchOptions options = new SearchOptions();
options.UseSynonymSearch = true;
options.UseWordFormsSearch = true;
options.FuzzySearch.Enabled = true;
options.UseHomophoneSearch = true;
SearchResult result = index.Search("Einstein", options);
```

### 也可以看看

* class [SearchPhaseEventArgs](../../searchphaseeventargs)
* class [EventHub](../../eventhub)
* 命名空间 [GroupDocs.Search.Events](../../eventhub)
* 部件 [GroupDocs.Search](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Search.dll -->
