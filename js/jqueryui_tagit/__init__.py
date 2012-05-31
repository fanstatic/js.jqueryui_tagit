from fanstatic import Group, Library, Resource
from js.jquery import jquery
from js.jqueryui import jqueryui
# there's likely some lighter import option in the jqueryui fanstatic package

library = Library('tagit', 'resources')

js = Resource(library,
              'tag-it.js',
              minified="tag-it.min.js",
              bottom=True,
              depends=[jquery, jqueryui, ])
css = Resource(library,
               'jquery.tagit.css',
               minified='jquery.tagit.min.css',
               bottom=False,
               depends=[])

tagit = Group([js, css])
