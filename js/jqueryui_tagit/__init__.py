# -*- coding: utf-8 -*-

from fanstatic import Group
from fanstatic import Library
from fanstatic import Resource
from js.jqueryui import ui_autocomplete
from js.jqueryui import ui_widget


library = Library('tagit', 'resources')

js = Resource(library,
              'tag-it.js',
              minified="tag-it.min.js",
              bottom=True,
              depends=[ui_autocomplete, ui_widget, ])
css = Resource(library,
               'jquery.tagit.css',
               minified='jquery.tagit.min.css',
               bottom=False,
               depends=[])

tagit = Group([js, css])
