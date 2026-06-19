---
title: Install GroupDocs.Annotation for Python via .NET
second_title: GroupDocs.Annotation for Python via .NET API References
description: 
type: docs
url: /python-net/guides/installation/
is_root: false
weight: 40
---


GroupDocs.Annotation for Python via .NET is distributed as a pre-built wheel on [PyPI](https://pypi.org/project/groupdocs-annotation-net/). The PyPI index hosts a separate wheel for each supported platform, and `pip` picks the correct one automatically. Each wheel is self-contained: it bundles the embedded runtime and every managed dependency, so no Microsoft Office, OpenOffice, Adobe Acrobat, or separate runtime install is required.

Before installing, confirm your environment matches the supported platforms and Python versions listed in the [System Requirements](https://docs.groupdocs.com/annotation/python-net/system-requirements/) topic.

## Install Package from PyPI

Open a terminal and run the install command for your platform:

```ps
py -m pip install groupdocs-annotation-net
```

```bash
python3 -m pip install groupdocs-annotation-net
```

```bash
python3 -m pip install groupdocs-annotation-net
```

After running the command you should see output similar to:

```bash
Collecting groupdocs-annotation-net
  Downloading groupdocs_annotation_net-26.6.0-py3-none-win_amd64.whl.metadata (3.0 kB)
  Downloading groupdocs_annotation_net-26.6.0-py3-none-win_amd64.whl (40.0 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 40.0/40.0 MB 2.8 MB/s eta 0:00:00
Installing collected packages: groupdocs-annotation-net
Successfully installed groupdocs-annotation-net-26.6.0
```

The wheel file name will include a platform suffix that matches your operating system — for example `manylinux1_x86_64` on Ubuntu/Debian, `macosx_11_0_arm64` on Apple Silicon, or `win_amd64` on 64-bit Windows.

## Add the Package to `requirements.txt`

For reproducible environments, pin the package version in your `requirements.txt`:

```txt
groupdocs-annotation-net==26.6.0
```

Then install all dependencies in one step:

```bash
pip install -r requirements.txt
```

## Install from a Pre-Downloaded Wheel

If your build environment cannot reach PyPI, download the appropriate wheel from the [GroupDocs Releases website](https://releases.groupdocs.com/annotation/python-net/) and install it locally. Wheels are published for the following four platforms:

- **Windows 64-bit**: file name ends with `win_amd64.whl`
- **Linux x64 (glibc)**: file name ends with `manylinux1_x86_64.whl`
- **macOS Intel**: file name ends with `macosx_10_14_x86_64.whl`
- **macOS Apple Silicon**: file name ends with `macosx_11_0_arm64.whl`

Place the downloaded wheel into your project folder, then install it:

```ps
py -m pip install ./groupdocs_annotation_net-26.6.0-py3-none-win_amd64.whl
```

```bash
python3 -m pip install ./groupdocs_annotation_net-26.6.0-py3-none-manylinux1_x86_64.whl
```

```bash
python3 -m pip install ./groupdocs_annotation_net-26.6.0-py3-none-macosx_10_14_x86_64.whl
```

```bash
python3 -m pip install ./groupdocs_annotation_net-26.6.0-py3-none-macosx_11_0_arm64.whl
```

Expected output:

```bash
Processing ./groupdocs_annotation_net-26.6.0-py3-none-*.whl
Installing collected packages: groupdocs-annotation-net
Successfully installed groupdocs-annotation-net-26.6.0
```

## Platform Prerequisites

On Windows no extra steps are required. On Linux and macOS, install the native libraries the rendering engine depends on:

```bash
apt install libgdiplus libfontconfig1 libicu-dev ttf-mscorefonts-installer
```

```bash
brew install mono-libgdiplus
```

The package runs on Windows, Linux, and macOS. On Linux and macOS the native libraries above provide graphics, fonts, and globalization support for the bundled engine; installing fonts (for example `ttf-mscorefonts-installer`) helps annotated output match the original document. See [System Requirements](https://docs.groupdocs.com/annotation/python-net/system-requirements/) for the full list.

## Verify the Installation

Confirm the package imported correctly:

```bash
python -c "import groupdocs.annotation; print('GroupDocs.Annotation is ready')"
```

You can also list the installed package with `pip show groupdocs-annotation-net` to confirm the version and location.

## Next Steps

- Follow the [Hello, World!](https://docs.groupdocs.com/annotation/python-net/hello-world/) guide to add your first annotation.
- Read the [Features Overview](https://docs.groupdocs.com/annotation/python-net/features-overview/) to see everything you can annotate.
- Clone the [examples repository](https://github.com/groupdocs-annotation/GroupDocs.Annotation-for-Python-via-.NET) and read [How to Run Examples](https://docs.groupdocs.com/annotation/python-net/how-to-run-examples/) to try every documented scenario locally.
</content>
</invoke>
