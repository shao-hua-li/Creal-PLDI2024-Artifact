# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Creal-PLDI2024-Artifact'
copyright = '2024, Shaohua Li'
author = ''

release = 'v1.1'
version = 'v1.1'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'

latex_elements = {
    'classoptions': ',oneside',  # Add other options here as needed, separated by commas
    'babel': '\\usepackage[english]{babel}',
}