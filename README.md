# devilry.github.com


Devilry website
This is the main website.

Contains links to different part of the documentation. etc.

## Testing it locally

Install jekyll locally (http://jekyllrb.com/), run:

    $ jekyll serve --watch

Then open http://localhost:4000/.


## Building the LESS sources

### Development
Comment out the line with ``css/styles.css`` in ``_layouts/base.html``, and
comment in the lines for the less sources right above.

NEVER COMMIT in development mode. It makes the website hang in IE8.

## Production
Make sure the ``less.XXXX.js`` and ``less/styles.less`` is not imported, and
that ``css/styles.css`` is imported in ``_layouts/base.html``.

The first time, you have to install lessc locally (in ``node_modules/``) with:

    $ npm install

To build the LESS sources to css, use:

    $ node_modules/.bin/lessc -x less/styles.less css/styles.css

Then test and commit the changes.

DOT NOT use your global ``lessc``, it may not be 100% compatible with the
version we have specified in ``package.json``.


## Components
We use these components to build the website.

### Jekyll
Jekyll is the blog aware static site builder supported by github pages. See:
https://help.github.com/categories/20/articles and http://jekyllrb.com/.

### Twitter Bower
A package manager for the web. We use it to update our CSS and JavaScript
dependencies, like Bootstrap and jQuery.  https://github.com/bower/bower.
Configured in ``component.json``, and installs packages to ``components/``.
This means that you should **never edit anything in components/**. 

### Twitter Bootstrap
CSS and javascript library. See: http://twitter.github.io/bootstrap/index.html.

### Less
CSS builder with lots of useful additions, like variables, reusable mixins,
etc. Used by Twitter Bootstrap, and we use it to extend and customize
Bootstrap. See: http://lesscss.org/.

### jQuery
Required by Twitter Bootstrap javascript components.

### Font Awesome
The iconic font designed for Bootstrap
