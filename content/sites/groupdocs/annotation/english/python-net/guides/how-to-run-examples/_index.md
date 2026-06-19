---
title: How to Run Examples
linkTitle: "Run examples"
second_title: GroupDocs.Annotation for Python via .NET API References
description: 
type: docs
url: /python-net/guides/how-to-run-examples/
is_root: false
weight: 170
---


Before running an example make sure that GroupDocs.Annotation for Python via .NET has been installed successfully.

The complete examples project for **GroupDocs.Annotation for Python via .NET** is hosted on [GitHub](https://github.com/groupdocs-annotation/GroupDocs.Annotation-for-Python-via-.NET). It contains standalone, runnable scripts together with the sample documents they use, so the examples work out of the box.

## Prerequisites

- [Python](https://www.python.org/) 3.5 – 3.14 installed and on your `PATH`.
- [git](https://git-scm.com/) to clone the repository (or download the ZIP).
- On Linux and macOS, the native libraries listed in the [System Requirements](https://docs.groupdocs.com/annotation/python-net/system-requirements/) (`libgdiplus`, `libfontconfig1`, `libicu-dev`, and fonts).
- Optionally, a GroupDocs.Annotation license to remove the [evaluation watermark](https://docs.groupdocs.com/annotation/python-net/licensing-and-subscription/).

## Get the code

Clone the repository with your favourite git client, or download the ZIP from GitHub:

```bash
git clone https://github.com/groupdocs-annotation/GroupDocs.Annotation-for-Python-via-.NET.git
cd GroupDocs.Annotation-for-Python-via-.NET
```

## Project Structure

The examples live under the `Examples/` folder, organized by topic. Directory names are kebab-case and each script is standalone:

```text
GroupDocs.Annotation-for-Python-via-.NET/
├── Dockerfile
└── Examples/
    ├── requirements.txt
    ├── run_all_examples.py
    ├── licensing/
    │   ├── set_license_from_file.py
    │   ├── set_license_from_stream.py
    │   └── set_metered_license.py
    ├── getting-started/
    │   └── hello-world/
    │       └── hello_world.py
    └── developer-guide/
        ├── basic-usage/
        │   ├── add-annotations/
        │   ├── comments-and-replies/
        │   ├── get-annotations/
        │   ├── get-document-info/
        │   ├── get-supported-file-formats/
        │   └── remove-annotations/
        └── advanced-usage/
            ├── loading-documents/
            └── saving-documents/
```

## Setup

Create and activate a virtual environment, then install the dependencies listed in `Examples/requirements.txt`:

```ps
py -m venv .venv
.venv\Scripts\activate
py -m pip install -r Examples/requirements.txt
```

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r Examples/requirements.txt
```

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r Examples/requirements.txt
```

To run the examples without the evaluation watermark, point the `GROUPDOCS_LIC_PATH` environment variable at your license file. The example scripts read this variable and apply the license automatically:

```ps
$env:GROUPDOCS_LIC_PATH = "C:\path\to\GroupDocs.Annotation.lic"
```

```bash
export GROUPDOCS_LIC_PATH="/path/to/GroupDocs.Annotation.lic"
```

```bash
export GROUPDOCS_LIC_PATH="/path/to/GroupDocs.Annotation.lic"
```

See [Licensing and Evaluation](https://docs.groupdocs.com/annotation/python-net/licensing-and-subscription/) for details on obtaining and applying a license.

## Run

Run every example at once with the runner script:

```bash
python Examples/run_all_examples.py
```

Or run a single example by passing its path directly:

```bash
python Examples/developer-guide/basic-usage/add-annotations/add_area_annotation.py
```

The repository ships with all the sample documents and resources used by the examples, so the scripts run out of the box.

Without a license the examples run in evaluation mode, which adds a watermark to each output document. There is no document-open limit, so every example completes successfully whether or not a license is applied. The `run_all_examples.py` runner launches each example in its own process and keeps the working directory set to the example's folder, so each script finds its input and output files.

## Run with Docker

The repository includes a `Dockerfile` that installs the native dependencies and Python packages so you can run the examples in a clean, reproducible container. From the repository root:

```bash
docker build -t groupdocs-annotation-examples .
docker run --rm groupdocs-annotation-examples
```

To use a license inside the container, mount it and pass `GROUPDOCS_LIC_PATH`:

```bash
docker run --rm \
  -v /path/to/GroupDocs.Annotation.lic:/app/GroupDocs.Annotation.lic:ro \
  -e GROUPDOCS_LIC_PATH=/app/GroupDocs.Annotation.lic \
  groupdocs-annotation-examples
```

## Continuous integration

Because the examples run headlessly and exit with a non-zero status on failure, they fit naturally into a CI pipeline. Install `Examples/requirements.txt`, supply the license through the `GROUPDOCS_LIC_PATH` environment variable (store the license as a protected secret), make sure the Linux native dependencies are present on the runner, and invoke `python Examples/run_all_examples.py` as a build step. The provided `Dockerfile` is a convenient base image for such jobs.

## Troubleshooting

- **Evaluation watermark on the output** — you are running unlicensed in evaluation mode. Set `GROUPDOCS_LIC_PATH` to a valid license to produce output without the watermark. See [Licensing and Evaluation](https://docs.groupdocs.com/annotation/python-net/licensing-and-subscription/).
- **Missing or substituted fonts** — install fonts so annotated output matches the original: `apt install libfontconfig1 ttf-mscorefonts-installer`.
- **ICU / globalization errors on Linux** — install ICU: `apt install libicu-dev`.
- **`ModuleNotFoundError: No module named 'groupdocs'`** — the package is not installed in the active environment. Activate your virtual environment and re-run `pip install -r Examples/requirements.txt`.

## Contribute

If you would like to add or improve an example, we encourage you to contribute to the project. All examples in this repository are open source and can be freely used in your own applications. To contribute, fork the repository, edit the code, and create a pull request. We will review the changes and include them if found helpful.
</content>
</invoke>
