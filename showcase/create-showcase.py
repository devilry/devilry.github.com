from sys import argv
from glob import glob
from os import sep
from os.path import splitext, dirname, abspath, join

if len(argv) != 2:
    raise SystemExit("usage: %s <dirname>" % argv[0])

showcase_dir = argv[1]
this_dir = abspath(dirname(__file__))
template = open(join(this_dir, 'tpl.html')).read()
singleimagetpl = open(join(this_dir, 'singleimagetpl.html')).read()
outfile = '%(showcase_dir)s.html' % vars()
single_image_ext = 'single.png'
print this_dir

parts = []
for filename in glob('%(showcase_dir)s%(sep)s*.html' % vars()):
    name = splitext(filename)[0]
    single_image_src = "%(showcase_dir)s/%(filename)s.%(single_image_ext)s" % vars()
    text = open(filename).read()
    parts.append(singleimagetpl % dict(
        src=single_image_src,
        text=text))

main = '\n\n'.join(parts)
out = template % dict(main=main)
open(outfile, 'wb').write(out)
