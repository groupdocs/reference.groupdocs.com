---
title: CompareOptions
second_title: GroupDocs.Comparison for .NET API Reference
description: Allows to set different compare options.
type: docs
weight: 220
url: /net/groupdocs.comparison.options/compareoptions/
---
## CompareOptions class

Allows to set different compare options.

```csharp
public class CompareOptions
```

## Constructors

| Name | Description |
| --- | --- |
| [CompareOptions](compareoptions)() | Initializes a new instance of the [`CompareOptions`](../compareoptions) class. |

## Properties

| Name | Description |
| --- | --- |
| [CalculateCoordinates](../../groupdocs.comparison.options/compareoptions/calculatecoordinates) { get; set; } | Indicates whether to calculate coordinates for changed components. |
| [CalculateCoordinatesMode](../../groupdocs.comparison.options/compareoptions/calculatecoordinatesmode) { get; set; } | Specifies the coordinate calculation for changed components mode. |
| [ChangedItemStyle](../../groupdocs.comparison.options/compareoptions/changeditemstyle) { get; set; } | Describes style for changed components. |
| [CompareBookmarks](../../groupdocs.comparison.options/compareoptions/comparebookmarks) { get; set; } | Control to turn on comparison of bookmarks in Word format. |
| [CompareDocumentProperty](../../groupdocs.comparison.options/compareoptions/comparedocumentproperty) { get; set; } | Control to turn on comparison of built and custom properties in Word format. |
| [CompareImagesPdf](../../groupdocs.comparison.options/compareoptions/compareimagespdf) { get; set; } | Control to turn on comparison of images in PDF format. |
| [CompareVariableProperty](../../groupdocs.comparison.options/compareoptions/comparevariableproperty) { get; set; } | Control to turn on comparison of variables properties in Word format. |
| [DeletedItemStyle](../../groupdocs.comparison.options/compareoptions/deleteditemstyle) { get; set; } | Describes style for deleted components. |
| [DetalisationLevel](../../groupdocs.comparison.options/compareoptions/detalisationlevel) { get; set; } | Gets or sets the comparison detail level. |
| [DetectStyleChanges](../../groupdocs.comparison.options/compareoptions/detectstylechanges) { get; set; } | Indicates whether to detect style changes or not. |
| [DiagramMasterSetting](../../groupdocs.comparison.options/compareoptions/diagrammastersetting) { get; set; } | Gets or sets the path value for master or use compare without path of master. This option only for Diagram. |
| [DirectoryCompare](../../groupdocs.comparison.options/compareoptions/directorycompare) { get; set; } | Control to turn on comparison of folders. |
| [ExtendedSummaryPage](../../groupdocs.comparison.options/compareoptions/extendedsummarypage) { get; set; } | Indicates whether to add extended file comparison information to the summary page or not. |
| [FolderComparisonExtension](../../groupdocs.comparison.options/compareoptions/foldercomparisonextension) { get; set; } | Gets or sets the format of the resulting folder comparison file. |
| [GenerateSummaryPage](../../groupdocs.comparison.options/compareoptions/generatesummarypage) { get; set; } | Indicates whether to add summary page with detected changes statistics to resultant document or not. |
| [HeaderFootersComparison](../../groupdocs.comparison.options/compareoptions/headerfooterscomparison) { get; set; } | Control to turn on comparison of header/footer contents. |
| [IgnoreChangeSettings](../../groupdocs.comparison.options/compareoptions/ignorechangesettings) { get; set; } | Gets or sets settings to ignore changes based on similarity. |
| [ImagesInheritanceMode](../../groupdocs.comparison.options/compareoptions/imagesinheritancemode) { get; set; } | Specifies the source of images inheritance when image comparison is disabled. |
| [InsertedItemStyle](../../groupdocs.comparison.options/compareoptions/inserteditemstyle) { get; set; } | Describes style for inserted components. |
| [LeaveGaps](../../groupdocs.comparison.options/compareoptions/leavegaps) { get; set; } | Indicates whether to display empty lines instead of inserted / deleted components in the final document or not (used with ShowInsertedContent or ShowDeletedContent properties). |
| [MarkChangedContent](../../groupdocs.comparison.options/compareoptions/markchangedcontent) { get; set; } | Indicates whether to use frames for shapes in Word Processing and for rectangles in Image documents. |
| [MarkLineBreaks](../../groupdocs.comparison.options/compareoptions/marklinebreaks) { get; set; } | Gets or sets a value indicating whether to mark line breaks. |
| [MarkNestedContent](../../groupdocs.comparison.options/compareoptions/marknestedcontent) { get; set; } | Gets or sets a value indicating whether to mark the children of the deleted or inserted element as deleted or inserted. |
| [OriginalSize](../../groupdocs.comparison.options/compareoptions/originalsize) { get; set; } | Get or sets the original sizes of compared documents. |
| [PaperSize](../../groupdocs.comparison.options/compareoptions/papersize) { get; set; } | Gets or sets the result document paper size. |
| [PasswordSaveOption](../../groupdocs.comparison.options/compareoptions/passwordsaveoption) { get; set; } | Gets or sets the password save option. |
| [RevisionAuthorName](../../groupdocs.comparison.options/compareoptions/revisionauthorname) { get; set; } | Gets or sets revision author name. Enabled if not null. |
| [SensitivityOfComparison](../../groupdocs.comparison.options/compareoptions/sensitivityofcomparison) { get; set; } | Gets or sets a sensitivity of comparison. |
| [SensitivityOfComparisonForTables](../../groupdocs.comparison.options/compareoptions/sensitivityofcomparisonfortables) { get; set; } | Gets or sets a sensitivity of comparison for tables. |
| [ShowDeletedContent](../../groupdocs.comparison.options/compareoptions/showdeletedcontent) { get; set; } | Indicates whether to show deleted components in resultant document or not. |
| [ShowInsertedContent](../../groupdocs.comparison.options/compareoptions/showinsertedcontent) { get; set; } | Indicates whether to show inserted components in resultant document or not. |
| [ShowOnlyChanged](../../groupdocs.comparison.options/compareoptions/showonlychanged) { get; set; } | Controls to enable the display of only changed items. |
| [ShowOnlySummaryPage](../../groupdocs.comparison.options/compareoptions/showonlysummarypage) { get; set; } | Indicates whether to leave in the resulting document only a page with statistics of detected changes in the resulting document or not. |
| [ShowRevisions](../../groupdocs.comparison.options/compareoptions/showrevisions) { get; set; } | Indicates whether to display others revisions in the resulting document or not. |
| [UserMasterPath](../../groupdocs.comparison.options/compareoptions/usermasterpath) { get; set; } | Path to user master's template for Diagrams. |
| [WordsSeparatorChars](../../groupdocs.comparison.options/compareoptions/wordsseparatorchars) { set; } | Gets or sets an array of delimiters to split text into words. |
| [WordTrackChanges](../../groupdocs.comparison.options/compareoptions/wordtrackchanges) { get; set; } | Control to turn on comparison of Words Track Revisions. |

### See Also

* namespace [GroupDocs.Comparison.Options](../../groupdocs.comparison.options)
* assembly [GroupDocs.Comparison](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Comparison.dll -->
