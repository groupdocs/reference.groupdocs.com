---
title: Cr2Functions1DPackage
second_title: GroupDocs.Metadata for .NET API Reference
description: Represents Canon MakerNotes tags.
type: docs
weight: 2980
url: /net/groupdocs.metadata.formats.raw.cr2/cr2functions1dpackage/
---
## Cr2Functions1DPackage class

Represents Canon MakerNotes tags.

```csharp
public sealed class Cr2Functions1DPackage : RawDictionaryBasePackage
```

## Constructors

| Name | Description |
| --- | --- |
| [Cr2Functions1DPackage](cr2functions1dpackage)() | Initializes a new instance of the [`Cr2Functions1DPackage`](../cr2functions1dpackage) class. |

## Properties

| Name | Description |
| --- | --- |
| [AEBSequenceAutoCancel](../../groupdocs.metadata.formats.raw.cr2/cr2functions1dpackage/aebsequenceautocancel) { get; } | Gets the AEBSequenceAutoCancel. |
| [AFPointActivationArea](../../groupdocs.metadata.formats.raw.cr2/cr2functions1dpackage/afpointactivationarea) { get; } | Gets the AFPointActivationArea. |
| [AFPointIllumination](../../groupdocs.metadata.formats.raw.cr2/cr2functions1dpackage/afpointillumination) { get; } | Gets the AFPointIllumination. |
| [AFPointSelection](../../groupdocs.metadata.formats.raw.cr2/cr2functions1dpackage/afpointselection) { get; } | Gets the AFPointSelection. |
| [AFPointSpotMetering](../../groupdocs.metadata.formats.raw.cr2/cr2functions1dpackage/afpointspotmetering) { get; } | Gets the AFPointSpotMetering. |
| [AIServoContinuousShooting](../../groupdocs.metadata.formats.raw.cr2/cr2functions1dpackage/aiservocontinuousshooting) { get; } | Gets the AIServoContinuousShooting. |
| [AIServoTrackingSensitivity](../../groupdocs.metadata.formats.raw.cr2/cr2functions1dpackage/aiservotrackingsensitivity) { get; } | Gets the AIServoTrackingSensitivity. |
| [Count](../../groupdocs.metadata.common/metadatapackage/count) { get; } | Gets the number of metadata properties. |
| [ExposureLevelIncrements](../../groupdocs.metadata.formats.raw.cr2/cr2functions1dpackage/exposurelevelincrements) { get; } | Gets the ExposureLevelIncrements. |
| [FillFlashAutoReduction](../../groupdocs.metadata.formats.raw.cr2/cr2functions1dpackage/fillflashautoreduction) { get; } | Gets the FillFlashAutoReduction. |
| [FinderDisplayDuringExposure](../../groupdocs.metadata.formats.raw.cr2/cr2functions1dpackage/finderdisplayduringexposure) { get; } | Gets the FinderDisplayDuringExposure. |
| [FocusingScreen](../../groupdocs.metadata.formats.raw.cr2/cr2functions1dpackage/focusingscreen) { get; } | Gets the FocusingScreen. |
| [ISOSpeedExpansion](../../groupdocs.metadata.formats.raw.cr2/cr2functions1dpackage/isospeedexpansion) { get; } | Gets the ISOSpeedExpansion. |
| [Item](../../groupdocs.metadata.formats.raw/rawdictionarybasepackage/item) { get; } | Gets the Raw tag with the specified id. (2 indexers) |
| [Keys](../../groupdocs.metadata.common/metadatapackage/keys) { get; } | Gets a collection of the metadata property names. |
| [LCDPanels](../../groupdocs.metadata.formats.raw.cr2/cr2functions1dpackage/lcdpanels) { get; } | Gets the LCDPanels. |
| [LensAFStopButton](../../groupdocs.metadata.formats.raw.cr2/cr2functions1dpackage/lensafstopbutton) { get; } | Gets the LensAFStopButton. |
| [ManualTv](../../groupdocs.metadata.formats.raw.cr2/cr2functions1dpackage/manualtv) { get; } | Gets the ManualTv. |
| [MetadataType](../../groupdocs.metadata.common/metadatapackage/metadatatype) { get; } | Gets the metadata type. |
| [MirrorLockup](../../groupdocs.metadata.formats.raw.cr2/cr2functions1dpackage/mirrorlockup) { get; } | Gets the MirrorLockup. |
| [PropertyDescriptors](../../groupdocs.metadata.common/metadatapackage/propertydescriptors) { get; } | Gets a collection of descriptors that contain information about properties accessible through the GroupDocs.Metadata search engine. |
| [SafetyShiftInAvOrTv](../../groupdocs.metadata.formats.raw.cr2/cr2functions1dpackage/safetyshiftinavortv) { get; } | Gets the SafetyShiftInAvOrTv. |
| [ShutterAELButton](../../groupdocs.metadata.formats.raw.cr2/cr2functions1dpackage/shutteraelbutton) { get; } | Gets the ShutterAELButton. |
| [ShutterCurtainSync](../../groupdocs.metadata.formats.raw.cr2/cr2functions1dpackage/shuttercurtainsync) { get; } | Gets the ShutterCurtainSync. |
| [ShutterReleaseNoCFCard](../../groupdocs.metadata.formats.raw.cr2/cr2functions1dpackage/shutterreleasenocfcard) { get; } | Gets the ShutterReleaseNoCFCard. |
| [SwitchToRegisteredAFPoint](../../groupdocs.metadata.formats.raw.cr2/cr2functions1dpackage/switchtoregisteredafpoint) { get; } | Gets the SwitchToRegisteredAFPoint. |
| [USMLensElectronicMF](../../groupdocs.metadata.formats.raw.cr2/cr2functions1dpackage/usmlenselectronicmf) { get; } | Gets the USMLensElectronicMF. |

## Methods

| Name | Description |
| --- | --- |
| virtual [AddProperties](../../groupdocs.metadata.common/metadatapackage/addproperties)(Func&lt;MetadataProperty, bool&gt;, PropertyValue) | Adds known metadata properties satisfying the specified predicate. The operation is recursive so it affects all nested packages as well. |
| [Clear](../../groupdocs.metadata.formats.raw/rawdictionarybasepackage/clear)() | Removes all Raw tags stored in the package. |
| [Contains](../../groupdocs.metadata.common/metadatapackage/contains)(string) | Determines whether the package contains a metadata property with the specified name. |
| virtual [FindProperties](../../groupdocs.metadata.common/metadatapackage/findproperties)(Func&lt;MetadataProperty, bool&gt;) | Finds the metadata properties satisfying the specified predicate. The search is recursive so it affects all nested packages as well. |
| [GetEnumerator](../../groupdocs.metadata.common/metadatapackage/getenumerator)() | Returns an enumerator that iterates through the collection. |
| [Remove](../../groupdocs.metadata.formats.raw/rawdictionarybasepackage/remove)(uint) | Removes the property with the specified id. |
| virtual [RemoveProperties](../../groupdocs.metadata.common/metadatapackage/removeproperties)(Func&lt;MetadataProperty, bool&gt;) | Removes metadata properties satisfying the specified predicate. |
| virtual [Sanitize](../../groupdocs.metadata.common/metadatapackage/sanitize)() | Removes writable metadata properties from the package. The operation is recursive so it affects all nested packages as well. |
| [Set](../../groupdocs.metadata.formats.raw/rawdictionarybasepackage/set)(RawTag) | Adds or replaces the specified tag. |
| virtual [SetProperties](../../groupdocs.metadata.common/metadatapackage/setproperties)(Func&lt;MetadataProperty, bool&gt;, PropertyValue) | Sets known metadata properties satisfying the specified predicate. The operation is recursive so it affects all nested packages as well. This method is a combination of [`AddProperties`](../../groupdocs.metadata.common/metadatapackage/addproperties) and [`UpdateProperties`](../../groupdocs.metadata.common/metadatapackage/updateproperties). If an existing property satisfies the predicate its value is updated. If there is a known property missing in the package that satisfies the predicate it is added to the package. |
| [ToList](../../groupdocs.metadata.formats.raw/rawdictionarybasepackage/tolist)() | Creates a list from the package. |
| virtual [UpdateProperties](../../groupdocs.metadata.common/metadatapackage/updateproperties)(Func&lt;MetadataProperty, bool&gt;, PropertyValue) | Updates known metadata properties satisfying the specified predicate. The operation is recursive so it affects all nested packages as well. |

### See Also

* class [RawDictionaryBasePackage](../../groupdocs.metadata.formats.raw/rawdictionarybasepackage)
* namespace [GroupDocs.Metadata.Formats.Raw.Cr2](../../groupdocs.metadata.formats.raw.cr2)
* assembly [GroupDocs.Metadata](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.metadata.dll -->
