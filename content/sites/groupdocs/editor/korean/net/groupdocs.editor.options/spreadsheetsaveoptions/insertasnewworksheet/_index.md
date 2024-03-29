---
title: InsertAsNewWorksheet
second_title: .NET API 참조용 GroupDocs.Editor
description: 부울 플래그는 편집된 워크시트가WorksheetNumbergroupdocs.editor.options/spreadsheetsaveoptions/worksheetnumber property 또는 내용을 바꾸지 않고 기존 워크시트와 이전 워크시트 사이에 삽입해야 합니다. 기본적으로 false  기존 워크시트가 바뀝니다. 값이WorksheetNumbergroupdocs.editor.options/spreadsheetsaveoptions/worksheetnumber 속성이 0으로 설정되었습니다.
type: docs
weight: 20
url: /ko/net/groupdocs.editor.options/spreadsheetsaveoptions/insertasnewworksheet/
---
## SpreadsheetSaveOptions.InsertAsNewWorksheet property

부울 플래그는 편집된 워크시트가[`WorksheetNumber`](../worksheetnumber) property, 또는 내용을 바꾸지 않고 기존 워크시트와 이전 워크시트 사이에 삽입해야 합니다. 기본적으로 false — 기존 워크시트가 바뀝니다. 값이[`WorksheetNumber`](../worksheetnumber) 속성이 '0'으로 설정되었습니다.

```csharp
public bool InsertAsNewWorksheet { get; set; }
```

### 비고

기본적으로 워크시트는 대체됩니다. 즉, 주어진 스프레드시트에 5개의 워크시트가 있고[`WorksheetNumber`](../worksheetnumber) =4이면 4번째 워크시트가 새로 편집된 워크시트 로 대체되고 스프레드시트(5)의 총 워크시트 수는 그대로 유지됩니다. 단, 이 속성 값을진실새로 편집된 워크시트가 4번째 워크시트로 삽입되고 모든 후속 워크시트가 끝으로 이동됩니다. "이전" 4번째 워크시트는 5번째, 가 되고 5번째는 6번째가 되며 스프레드시트의 총 워크시트 양은 1씩 증가합니다. 6과 같습니다.

### 또한보십시오

* class [SpreadsheetSaveOptions](../../spreadsheetsaveoptions)
* 네임스페이스 [GroupDocs.Editor.Options](../../spreadsheetsaveoptions)
* 집회 [GroupDocs.Editor](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Editor.dll -->
