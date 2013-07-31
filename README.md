# devilry.github.com


Devilry website
This is the main website.

Contains links to different part of the documentation. etc.

## Testing it locally

Install jekyll locally (http://jekyllrb.com/), run:

    $ jekyll serve --watch

Then open http://localhost:4000/.


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
