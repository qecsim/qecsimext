import qecsimext

# -- Project information --------------------------------------------------
project = 'qecsimext'
copyright = '2016, David Tuckett'
author = 'David Tuckett'

version = qecsimext.__version__
release = qecsimext.__version__

# -- General configuration ------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode', # adds links to Python source code
    # 'sphinx.ext.intersphinx', # adds links to other sphinx docs
    'sphinx_rtd_theme',  # read the docs theme
]
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
# intersphinx_mapping = {'python': ('https://docs.python.org/3', None)} # adds links to Python docs

# -- Options for HTML output ----------------------------------------------

html_theme = 'sphinx_rtd_theme'

html_theme_options = {
    # Toc options
    'navigation_depth': 3,
    # 'titles_only': False,
}

# -- Options for autodoc --------------------------------------------------

autodoc_member_order = 'bysource'
