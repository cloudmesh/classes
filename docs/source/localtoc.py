# -*- coding: utf-8 -*-
"""
``localtoc``: A callable yielding the local TOC tree that contains
list of all headings in the specified page exclude page title.
``localtoc`` need pagename specifing like ``{{ localtoc(pagename) }}``.
"""

def init_localtoc(app):

    def _get_localtoc(docname):
        toc = app.env.get_toc_for(docname, app.builder)
        try:
            del toc[0][0]
            return app.builder.render_partial(toc)['fragment']
        except:
            return ''

    ctx = app.env.config['html_context']
    if 'localtoc' not in ctx:
        ctx['localtoc'] = _get_localtoc


def setup(app):
    app.connect('builder-inited', init_localtoc)
