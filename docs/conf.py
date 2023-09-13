# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import shutil

from rocm_docs import ROCmDocs


shutil.copy2('../CONTRIBUTING.md','./contribute/index.md')
shutil.copy2('../RELEASE.md','./about/release-notes.md')
# Keep capitalization due to similar linking on GitHub's markdown preview.
shutil.copy2('../CHANGELOG.md','./CHANGELOG.md')

latex_engine = "xelatex"

# configurations for PDF output by Read the Docs
project = "ROCm Documentation"
author = "Advanced Micro Devices, Inc."
copyright = "Copyright (c) 2023 Advanced Micro Devices, Inc. All rights reserved."
version = "5.7.0"
release = "5.7.0"

setting_all_article_info = True
all_article_info_os = ["linux", "windows"]
all_article_info_author = ""

# pages with specific settings
article_pages = [
    {
        "file":"release",
        "os":["linux", "windows"],
        "date":"2023-07-27"
    },

    {"file":"tutorials/quick-start/windows", "os":["windows"]},
    {"file":"tutorials/quick-start/linux", "os":["linux"]},

    {"file":"tutorials/install/linux/index", "os":["linux"]},
    {"file":"tutorials/install/linux/install-options", "os":["linux"]},
    {"file":"tutorials/install/linux/prerequisites", "os":["linux"]},

    {"file":"tutorials/install/docker", "os":["linux"]},
    {"file":"tutorials/install/magma-install", "os":["linux"]},
    {"file":"tutorials/install/pytorch-install", "os":["linux"]},
    {"file":"tutorials/install/tensorflow-install", "os":["linux"]},

    {"file":"tutorials/install/windows/index", "os":["windows"]},
    {"file":"tutorials/install/windows/prerequisites", "os":["windows"]},
    {"file":"tutorials/install/windows/cli/index", "os":["windows"]},
    {"file":"tutorials/install/windows/gui/index", "os":["windows"]},

    {"file":"about/compatibility/linux-support", "os":["linux"]},
    {"file":"about/compatibility/windows-support", "os":["windows"]},

    {"file":"about/compatibility/docker-image-support-matrix", "os":["linux"]},

    {"file":"reference/libraries/gpu-libraries/index", "os":["linux"]},
    {"file":"reference/compilers-tools/index", "os":["linux"]},
    {"file":"reference/index", "os":["linux"]},

    {"file":"how-to/deep-learning-rocm", "os":["linux"]},
    {"file":"how-to/gpu-aware-mpi", "os":["linux"]},
    {"file":"how-to/system-debugging", "os":["linux"]},
    {"file":"how-to/index", "os":["linux", "windows"]},

    {"file":"rocm-ai", "os":["linux", "windows"]},
    {"file":"rocm-a-z", "os":["linux", "windows"]},

]

external_toc_path = "./sphinx/_toc.yml"

docs_core = ROCmDocs("ROCm Documentation")
docs_core.setup()

external_projects_current_project = "rocm"

for sphinx_var in ROCmDocs.SPHINX_VARS:
    globals()[sphinx_var] = getattr(docs_core, sphinx_var)
html_theme_options = {
    "link_main_doc": False
}
