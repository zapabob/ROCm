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

setting_all_article_info = True
all_article_info_os = ["linux"]
all_article_info_author = ""

# pages with specific settings
article_pages = [
    {"file":"deploy/linux/index", "os":["linux"]},
    {"file":"deploy/linux/install_overview", "os":["linux"]},
    {"file":"deploy/linux/prerequisites", "os":["linux"]},
    {"file":"deploy/linux/quick_start", "os":["linux"]},
    {"file":"deploy/linux/install", "os":["linux"]},
    {"file":"deploy/linux/upgrade", "os":["linux"]},
    {"file":"deploy/linux/uninstall", "os":["linux"]},
    {"file":"deploy/linux/package_manager_integration", "os":["linux"]},
    {"file":"deploy/docker", "os":["linux"]},
    
    {"file":"release/gpu_os_support", "os":["linux"]},
    {"file":"release/docker_support_matrix", "os":["linux"]},
    
    {"file":"reference/gpu_libraries/communication", "os":["linux"]},
    {"file":"reference/ai_tools", "os":["linux"]},
    {"file":"reference/management_tools", "os":["linux"]},
    {"file":"reference/validation_tools", "os":["linux"]},
    {"file":"reference/framework_compatibility/framework_compatibility", "os":["linux"]},
    {"file":"reference/computer_vision", "os":["linux"]},
    
    {"file":"how_to/deep_learning_rocm", "os":["linux"]},
    {"file":"how_to/gpu_aware_mpi", "os":["linux"]},
    {"file":"how_to/magma_install/magma_install", "os":["linux"]},
    {"file":"how_to/pytorch_install/pytorch_install", "os":["linux"]},
    {"file":"how_to/system_debugging", "os":["linux"]},
    {"file":"how_to/tensorflow_install/tensorflow_install", "os":["linux"]},

    {"file":"examples/machine_learning", "os":["linux"]},
    {"file":"examples/inception_casestudy/inception_casestudy", "os":["linux"]},
    
    {"file":"understand/file_reorg", "os":["linux"]},

    {"file":"understand/isv_deployment_win", "os":["windows"]},
]

external_toc_path = "./sphinx/_toc.yml"

docs_core = ROCmDocs("ROCm Documentation Home")
docs_core.setup()

external_projects_current_project = "rocm"

for sphinx_var in ROCmDocs.SPHINX_VARS:
    globals()[sphinx_var] = getattr(docs_core, sphinx_var)
html_theme_options = {
    "link_main_doc": False
}
