# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import shutil

from rocm_docs import ROCmDocs


shutil.copy2('../CONTRIBUTING.md','./contributing.md')
shutil.copy2('../RELEASE.md','./release.md')
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

    {"file":"tutorials/quick_start/windows", "os":["windows"]},
    {"file":"tutorials/quick_start/linux", "os":["linux"]},

    {"file":"tutorials/install/linux/index", "os":["linux"]},
    {"file":"tutorials/install/linux/install_overview", "os":["linux"]},
    {"file":"tutorials/install/linux/prerequisites", "os":["linux"]},

    {"file":"tutorials/install/docker", "os":["linux"]},
    {"file":"tutorials/install/magma_install", "os":["linux"]},
    {"file":"tutorials/install/pytorch_install", "os":["linux"]},
    {"file":"tutorials/install/tensorflow_install", "os":["linux"]},

    {"file":"tutorials/install/windows/index", "os":["windows"]},
    {"file":"tutorials/install/windows/prerequisites", "os":["windows"]},
    {"file":"tutorials/install/windows/cli/index", "os":["windows"]},
    {"file":"tutorials/install/windows/gui/index", "os":["windows"]},

    {"file":"about/release/linux_support", "os":["linux"]},
    {"file":"about/release/windows_support", "os":["windows"]},

    {"file":"about/compatibility/docker_image_support_matrix", "os":["linux"]},

    {"file":"reference/libraries/gpu_libraries/communication", "os":["linux"]},
    {"file":"reference/compilers_tools/index", "os":["linux"]},
    {"file":"reference/computer_vision", "os":["linux"]},

    {"file":"how_to/deep_learning_rocm", "os":["linux"]},
    {"file":"how_to/gpu_aware_mpi", "os":["linux"]},
    {"file":"how_to/system_debugging", "os":["linux"]},

    {"file":"rocm_ai/rocm_ai", "os":["linux"]},
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
