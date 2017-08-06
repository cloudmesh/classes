# -*- coding: utf-8 -*-
# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
# import sys
import sys
sys.setrecursionlimit(1500)

theme_foundation = False
theme_bootstrap  = not theme_foundation

if theme_foundation:

    import foundation_sphinx_theme
    sys.path[0:0] = [os.path.abspath('_themes/foundation-sphinx-theme')]

elif theme_bootstrap:

    import sphinx_bootstrap_theme

# sys.path.insert(0, os.path.abspath('.'))



# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# Needs_Sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.mathjax',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
    'sphinx.ext.graphviz',
    'sphinxcontrib.bibtex'
]

extensions += ['sphinx-prompt']    

source_parsers = {
   '.md': 'recommonmark.parser.CommonMarkParser',
}

if theme_foundation:    
    extensions += ['foundation_sphinx_theme']
    extensions += ['sphinxcontrib.fulltoc']
        



# Add any paths that contain templates here, relative to this directory.
if theme_foundation:
    templates_path = ['_templates/foundation']
else:
    templates_path = ['_templates']
# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
source_suffix = ['.rst', '.md']

# The encoding of source files.
#
# source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'classes'
copyright = u'2016, Gregor von Laszewski'
author = u'Gregor von Laszewski'
version = u''
release = u'Draft'
language = None
todo_include_todos = True

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#
# today = ''
#
# Else, today_fmt is used as the format for a strftime call.
#
# today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = []

# The reST default role (used for this markup: `text`) to use for all
# documents.
#
# default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#
# add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#
# add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#
# show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
# modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
# keep_warnings = False

# If true, `todo` and `todoList` produce output, else they produce nothing.



# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = 'alabaster'
if theme_foundation:
    html_theme = 'foundation_sphinx_theme'

    html_theme_options = {
            'motto': 'This page is under construction and will change. Content will go live Jan. 9, 2017',

            # Your stylesheet relative to the _static dir.
            # Default is 'foundation/css/basic.css'
            #'stylesheet': 'foundation/css/cards.css',
            'stylesheet': 'foundation/css/basic.css',        

            # Logo image in SVG format. If the browser doesn't support SVG
            # It will try to load JPG with the same name.
            'logo_screen': '',

            # Logo for small screens. If ommited, logo_screen will be used.
            'logo_mobile': '',

            # Path to your favicon.ico file relative to the _static dir.
            # 'favicon': '',

            # Use this if the top-level items of the toctree don't fit in the top-bar navigation.
            # If True, the whole toctree will be placed inside a single top-level item.
            'top_bar_force_fit': True,

            # The title of the aformentioned top-level item. Default is "Sections"
            'top_bar_content_title': 'Sections',

            # If set, Google Analytics code will be appended to body of each page.
            'google_analytics_id': 'your-google-analytics-id',

            # The "og:title", "og:type", "og:url", "og:site_name" and "og:description" Open Graph tags
            # will be generated automatically, but you should specify the
            # path to the image that you want to be used
            # in the required "og:image" property relative to the _static dir.
            'opengraph_image': 'path/to/your/opengraph-image.jpg',

            # Any custom additional OG tags
            'opengraph_tags': {
                    'foo': 'bar', # will be rendered as <meta property="og:foo" content="bar" />
            },

            # The "description" meta tag will be created automatically, but
            # you can specify additional meta tags here.
            'meta_tags': {
                    'foo': 'bar', # will be rendered as <meta name="foo" content="bar">
            },

            # The value for "description" and "og:description" metatags.
            # If omitted, the value of "motto" will be used.
            'seo_description': 'This is an example of the Foundation Sphinx Theme output.',

            # Use this as the base for Open Graph URLs without trailing slash.
            # 'base_url': 'http://example.com',

            # If true a bar with Facebook, Google+ and Twitter social buttons will be displayed
            # underneath the header.
            # 'social_buttons': True,

            # ID of your Facebook app associated with the Facebook Like button.
            # 'facebook_app_id': '123456789',

            # A Twitter ID used for the via mention of the Twitter button.
            # 'twitter_id': 'FoundationSphinx',

            # Flattr button settings.
            # 'flattr_id': 'andypipkin', # Your Flattr ID
            # 'flattr_title': '', # If missing docstitle or title will be used.
            # 'flattr_description': '', # If missing seo_description or motto will be used.
            # 'flattr_tags': '', # Optional.


            # If "author" and "copyright_year" are set they will override the "copyright" setting.

            # Author's name.
            'author': 'Gregor von Laszewski, Badi Abdul-Wahid',

            # Author's link.
            # 'author_link': 'http://peterhudec.com',

            # Year to be used in the copyright statement.
            'copyright_year': '2016, 2017',

            # Author's Google+ id. If set a G+ authorship link will be added.
            # 'google_plus_id': '117034840853387702598',


            # Fork me on GitHub ribbon will be displayed if "github_user",
            # "github_repo" and "github_ribbon_image" are set:
            # https://github.com/blog/273-github-ribbons
            # Ribbons are hidden on small screens!

            # Your GitHub ID.
            'github_user': 'cloudmesh',

            # The repository slug.
            'github_repo': 'classes',

            # Path to the ribbon image relative to the "_static" directory.
            'github_ribbon_image': 'forkme_right_gray_6d6d6d.png',

            # Position of the ribbon "left" or "right".
            'github_ribbon_position': 'right',
    }

    html_theme_path = foundation_sphinx_theme.HTML_THEME_PATH

elif theme_bootstrap:
    html_theme = 'bootstrap'
    html_theme_path = sphinx_bootstrap_theme.get_html_theme_path()
    html_theme_options = {
    # Navigation bar title. (Default: ``project`` value)
    'navbar_title': "classes",

    # Tab name for entire site. (Default: "Site")
    'navbar_site_name': "Site",

    # A list of tuples containing pages or urls to link to.
    # Valid tuples should be in the following forms:
    #    (name, page)                 # a link to a page
    #    (name, "/aa/bb", 1)          # a link to an arbitrary relative url
    #    (name, "http://example.com", True) # arbitrary absolute url
    # Note the "1" or "True" value above as the third argument to indicate
    # an arbitrary url.
    'navbar_links': [
        ("Lessons",
             "lesson/index.html",
             True),
        ("Changes",
             "changelog.html",
             True),
        ("Fork",
             "https://github.com/cloudmesh/classes",
             True),        
        ("Piazza",
             "https://piazza.com/class/ix39m27czn5uw",
             True),


    ],

    # Render the next and previous page links in navbar. (Default: true)
    'navbar_sidebarrel': False,

    # Render the current pages TOC in the navbar. (Default: true)
    'navbar_pagenav': True,

    # Tab name for the current pages TOC. (Default: "Page")
    'navbar_pagenav_name': "Page",

    # Global TOC depth for "site" navbar tab. (Default: 1)
    # Switching to -1 shows all levels.
    'globaltoc_depth': 2,

    # Include hidden TOCs in Site navbar?
    #
    # Note: If this is "false", you cannot have mixed ``:hidden:`` and
    # non-hidden ``toctree`` directives in the same page, or else the build
    # will break.
    #
    # Values: "true" (default) or "false"
    'globaltoc_includehidden': "true",

    # HTML navbar class (Default: "navbar") to attach to <div> element.
    # For black navbar, do "navbar navbar-inverse"
    'navbar_class': "navbar navbar-inverse",
    # 'navbar_class': "navbar",    

    # Fix navigation bar to top of page?
    # Values: "true" (default) or "false"
    'navbar_fixed_top': "true",

    # Location of link to source.
    # Options are "nav" (default), "footer" or anything else to exclude.
    'source_link_position': "nav",

    # Bootswatch (http://bootswatch.com/) theme.
    #
    # Options are nothing (default) or the name of a valid theme
    # such as "amelia" or "cosmo".
    # 'bootswatch_theme': "cosmo",
    'bootswatch_theme': "cerulean",

    # Choose Bootstrap version.
    # Values: "3" (default) or "2" (in quotes)
    'bootstrap_version': "3",
}


# The name for this set of Sphinx documents.
# "<project> v<release> documentation" by default.
#
html_title = u'Big Data Classes'
# html_short_title = None
# html_logo = None
# html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
#
# html_extra_path = []

# If not None, a 'Last updated on:' timestamp is inserted at every page
# bottom, using the given strftime format.
# The empty string is equivalent to '%b %d, %Y'.
#
# html_last_updated_fmt = None

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#
# html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#
# html_sidebars = {}
html_sidebars = { '**': ['globaltoc.html',
                         'localtoc.html',
                         'i524-links.html',
                         'searchbox.html'], }



# Additional templates that should be rendered to pages, maps page names to
# template names.
#
# html_additional_pages = {}

# If false, no module index is generated.
#
# html_domain_indices = True

# If false, no index is generated.
#
# html_use_index = True

# If true, the index is split into individual pages for each letter.
#
# html_split_index = False

# If true, links to the reST sources are added to the pages.
#
html_show_sourcelink = False

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
#
html_show_sphinx = False

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#
# html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#
# html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
# html_file_suffix = None

# html_search_language = 'en'

# A dictionary with options for the search language support, empty by default.
# 'ja' uses this config value.
# 'zh' user can custom change `jieba` dictionary path.
#
# html_search_options = {'type': 'default'}

# The name of a javascript file (relative to the configuration directory) that
# implements a search results scorer. If empty, the default will be used.
#
# html_search_scorer = 'scorer.js'

# Output file base name for HTML help builder.
htmlhelp_basename = 'Classesdoc'

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
     # The paper size ('letterpaper' or 'a4paper').
     #
     # 'papersize': 'letterpaper',

     # The font size ('10pt', '11pt' or '12pt').
     #
     'pointsize': '10pt',

     # Additional stuff for the LaTeX preamble.
     #
     # 'preamble': '\input{structure}',

     # Latex figure (float) alignment
     #
     # 'figure_align': 'htbp',
     'maketitle': r'\pagenumbering{arabic}',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    ('notes',
     'i524-notes.tex',
     u'I524 Lecture Notes',
     u'Gregor von Laszewski',
     'book'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#
# latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#
# latex_use_parts = False

# If true, show page references after internal links.
#
# latex_show_pagerefs = False

# If true, show URL addresses after external links.
#
# latex_show_urls = False

# Documents to append as an appendix to all manuals.
#
# latex_appendices = []

# It false, will not define \strong, \code, 	itleref, \crossref ... but only
# \sphinxstrong, ..., \sphinxtitleref, ... To help avoid clash with user added
# packages.
#
# latex_keep_old_macro_names = True

# If false, no module index is generated.
#
# latex_domain_indices = True


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'classes', u'Classes Documentation',
     [author], 1)
]

# If true, show URL addresses after external links.
#
# man_show_urls = False


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'Classes', u'Big Data',
     author, 'Classes', 'One line description of project.',
     'Miscellaneous'),
]

# Documents to append as an appendix to all manuals.
#
# texinfo_appendices = []

# If false, no module index is generated.
#
# texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#
# texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
#
# texinfo_no_detailmenu = False


# -- Options for Epub output ----------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project
epub_author = author
epub_publisher = author
epub_copyright = copyright

# The basename for the epub file. It defaults to the project name.
# epub_basename = project

# The HTML theme for the epub output. Since the default themes are not
# optimized for small screen space, using the same theme for HTML and epub
# output is usually not wise. This defaults to 'epub', a theme designed to save
# visual space.
#
# epub_theme = 'epub'

# The language of the text. It defaults to the language option
# or 'en' if the language is not set.
#
# epub_language = ''

# The scheme of the identifier. Typical schemes are ISBN or URL.
# epub_scheme = ''

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A tuple containing the cover image and cover page html template filenames.
#
# epub_cover = ()

# A sequence of (type, uri, title) tuples for the guide element of content.opf.
#
# epub_guide = ()

# HTML files that should be inserted before the pages created by sphinx.
# The format is a list of tuples containing the path and title.
#
# epub_pre_files = []

# HTML files that should be inserted after the pages created by sphinx.
# The format is a list of tuples containing the path and title.
#
# epub_post_files = []

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']

# The depth of the table of contents in toc.ncx.
#
# epub_tocdepth = 3

# Allow duplicate toc entries.
#
# epub_tocdup = True

# Choose between 'default' and 'includehidden'.
#
# epub_tocscope = 'default'

# Fix unsupported image types using the Pillow.
#
# epub_fix_images = False

# Scale large images.
#
# epub_max_image_width = 0

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#
# epub_show_urls = 'inline'

# If false, no index is generated.
#
# epub_use_index = True


# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {'https://docs.python.org/': None}
