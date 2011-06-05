from sys import argv
from glob import glob
from os import sep
from os.path import splitext, dirname, abspath, join, split, exists

if len(argv) != 2:
    raise SystemExit("usage: %s <dirname>" % argv[0])

def readtpl(name):
    return open(join(this_dir, '%s.html' % name)).read()

def path_to_urlpath(path):
    return '/'.join(split(path))

showcase_dir = argv[1]
this_dir = abspath(dirname(__file__))
outfile = '%(showcase_dir)s.html' % vars()
single_image_ext = 'single.png'

template = readtpl('tpl')
singleimagetpl = readtpl('singleimagetpl')
onlytexttpl = readtpl('onlytext')

parts = []
for filename in glob('%(showcase_dir)s%(sep)s*.html' % vars()):
    name = splitext(filename)[0]
    singleimage_path = "%(name)s.%(single_image_ext)s" % vars()
    if exists(singleimage_path):
        singleimage_src = path_to_urlpath(singleimage_path)
        tpl = singleimagetpl
    else:
        tpl = onlytexttpl

    text = open(filename).read()
    parts.append(tpl % dict(vars()))

main = '\n\n'.join(parts)
out = template % dict(main=main)
open(outfile, 'wb').write(out)
print 'Output written to %s.' % outfile
