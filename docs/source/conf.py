#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
# GridAPPS-D documentation build configuration file, created by
# sphinx-quickstart on Wed May  3 11:38:35 2017.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
import subprocess

# sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, os.path.abspath('../../applications'))


# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
	'sphinx.ext.autodoc',
	'javasphinx',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# Add support for markdown
from recommonmark.parser import CommonMarkParser

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = ['.rst', '.md']

source_parsers = {
    '.md': CommonMarkParser,
}

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'GridAPPS-D'
copyright = '2017-2018, Battelle Memorial Institute All rights reserved.'
author = 'The GridAPPS-D Team and Community'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '1.0'
# The full version, including alpha/beta/rc tags.
release = '1.0'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['api_docs/gridlabd-cim.rst',
                    'installing_gridappsd/bootstrap.rst',
                    'installing_gridappsd/activate.rst',
                    'installing_gridappsd/download.rst',
                    'installing_gridappsd/prereq.rst',
                    'installing_gridappsd/start_platform.rst',
                    'installing_gridappsd/testing.rst',
                    'installing_gridappsd/FNCS_build_instructions.md',
                    'installing_gridappsd/GridLAB-D_build_instructions.md',
                    'developer_resources/design.rst',
                    'developer_resources/CDPSM.rst',
                    'developer_resources/Developing_Apps.rst',
                    'developer_resources/Eclipse_Setup.rst',
                    'developer_resources/Execution_Workflow.rst',
                    'developer_resources/RC1_Tasks.rst',
                    'developer_resources/UML_Diagrams.rst',
                    'hosted_applications/NREL_APPS/*.rst',
                    'hosted_applications/PNNL_Apps/*.rst',
                    'installing_gridappsd/installingWithDocker.rst',
                    'overview/architecture.rst',
                    'overview/conceptual_design_summary.rst',
                    'overview/contactus.rst',
                    'overview/definitions.rst',
                    'overview/version_history.rst',
                    'using_gridappsd/Developing_Apps.rst',
                    'using_gridappsd/logging_status.rst',
                    'using_gridappsd/rc1_overview.rst',
                    'using_gridappsd/run_configuration.rst',
                    'using_gridappsd/starting_in_viz.rst',
                    'using_gridappsd/api_examples/config_data_manager.rst',
                    'using_gridappsd/api_examples/inputs_outputs.rst',
                    'using_gridappsd/api_examples/pg_data_manager.rst',
                    'using_gridappsd/api_examples/simulation_request.rst',
                    'using_gridappsd/api_examples/starting_in_java.rst',
                    'using_gridappsd/api_examples/starting_in_python.rst',
                    'using_gridappsd/api_examples/starting_in_websockets.rst',
                    'using_gridappsd/api_examples/timeseries_data_api.rst',
                    'using_gridappsd/Uploading_model_using_blazegraph_workbench.rst',
                    'using_gridappsd/api_examples/weather.rst']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True

# Map to external documents for linking to other java resources 
javadoc_url_map = {
#    'com.netflix.curator' : ('http://netflix.github.com/curator/doc', 'javadoc'),
#    'org.springframework' : ('http://static.springsource.org/spring/docs/3.1.x/javadoc-api/', 'javadoc'),
#    'org.springframework.data.redis' : ('http://static.springsource.org/spring-data/data-redis/docs/current/api/', 'javadoc')
}

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# default was '_static'
html_static_path = []


# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'GridAPPS-Ddoc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'GridAPPS-D.tex', 'GridAPPS-D Documentation',
     'The GridAPPS-D Team', 'manual'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'gridapps-d', 'GridAPPS-D Documentation',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'GridAPPS-D', 'GridAPPS-D Documentation',
     author, 'GridAPPS-D', 'One line description of project.',
     'Miscellaneous'),
]



# -- Options for Epub output ----------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project
epub_author = author
epub_publisher = author
epub_copyright = copyright

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']



# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {'https://docs.python.org/': None}

# Custom event handlers for Volttron #
def setup(app):
    """
    Registers callback method on sphinx events. callback method used to
    dynamically generate api-docs rst files which are then converted to html
    by readthedocs
    :param app:
    """
    app.connect('builder-inited', generate_apidoc)
#    app.connect('build-finished', clean_apirst)


def generate_apidoc(app):
    print('BUILIDING JAVADOCS '+ __file__)
    print('CWD: '+os.getcwd())
    path_to_src = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../pnnl.goss.gridappsd/src'))
    path_to_output = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../source'))
    print(path_to_src)
    cmd = [
        'javasphinx-apidoc', 
        path_to_src,
        '-o',
        'source/api_docs',
        '-c',
        'cache'
    ]
    subprocess.call(cmd)

# def clean_apirst(app, exception):

#     shutil.rmtree(apidocs_base_dir)