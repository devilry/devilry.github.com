from sys import argv
from os.path import dirname, abspath, join, split, exists
from os import listdir

if len(argv) != 2:
    raise SystemExit("usage: %s <dirname>" % argv[0])

def readtpl(name):
    return open(join(this_dir, '%s.html' % name)).read()

def path_to_urlpath(path):
    return '/'.join(split(path))

showcase_dir = argv[1].replace('/', '')
this_dir = abspath(dirname(__file__))
outdir = dirname(this_dir)
outfile = '%(showcase_dir)s.html' % vars()
single_image_ext = 'single.png'

template = readtpl('tpl')
singleimagetpl = readtpl('singleimagetpl')
bigimagetpl = readtpl('bigimagetpl')
onlytexttpl = readtpl('onlytext')

parts = []
partnames = [x.strip() for x in open(join(showcase_dir, 'index.txt')).readlines()]
print partnames
pervious_img_floatleft = True # did the previous part have its image on the left?
for part in partnames:
    p = [x.strip() for x in part.split(': ')]
    partname = p[0]
    if len(p) > 1:
        imagesize, multi = p[1].split(',')
    else:
        imagesize, multi = '', ''
    print "Parsing", partname

    tpl = onlytexttpl
    if imagesize:
        if imagesize == 'small':
            singleimage_name = "%(partname)s.%(single_image_ext)s" % vars()
            singleimage_src = '%s/%s' % (showcase_dir, singleimage_name)
            tpl = singleimagetpl
        elif imagesize == 'big' and multi == 'multi':
            imagenames = [item for item in listdir(showcase_dir) \
                    if item.startswith('%s.multi.' % partname)]
            imagenames.sort()
            images = '\n'.join([
                '<li><img src="%s/%s"/></li>' % (showcase_dir, i)\
                for i in imagenames])
            tpl = bigimagetpl
            

    extraclasses = ''
    if imagesize == 'small':
        if pervious_img_floatleft:
            pervious_img_floatleft = False
            extraclasses = 'right'
        else:
            extraclasses = 'left'
    else:
        pervious_img_floatleft = True

    infofilename = join(showcase_dir, "%s.html" % partname)
    head, text = open(infofilename).read().split('----')
    heading, subheading = head.strip().split('\n')
    print "   Adding", heading
    #print text
    parts.append(tpl % vars())

main = '\n\n'.join(parts)
out = template % dict(main=main)
open(outfile, 'wb').write(out)
print 'Output written to %s' % outfile
