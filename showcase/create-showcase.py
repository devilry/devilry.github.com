from sys import argv
from os.path import dirname, abspath, join, split
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
bigsingleimagetpl = readtpl('bigsingleimagetpl')
bigimagetpl = readtpl('bigimagetpl')
onlytexttpl = readtpl('onlytext')

parts = []
partnames = [x.strip() for x in open(join(showcase_dir, 'index.txt')).readlines()]
print partnames
previous_smallimg_floatleft = True # did the previous part have its image on the left?
for part in partnames:
    if part.strip() == '':
        continue
    p = [x.strip() for x in part.split(': ')]
    partname = p[0]
    if len(p) > 1:
        imagesize, multi = p[1].split(',')
    else:
        imagesize, multi = '', ''
    print "Parsing", partname

    tpl = onlytexttpl
    if imagesize:
        if multi == 'single':
            singleimage_name = "%(partname)s.%(single_image_ext)s" % vars()
            singleimage_src = '%s/%s' % (showcase_dir, singleimage_name)
            if imagesize == 'small':
                tpl = singleimagetpl
            else:
                tpl = bigsingleimagetpl
        elif imagesize == 'big' and multi == 'multi':
            imagenames = [item for item in listdir(showcase_dir) \
                    if item.startswith('%s.multi.' % partname)]
            imagenames.sort()
            images = '\n'.join([
                '<img src="%s/%s" alt="" title=""/>' % (showcase_dir, i)\
                for i in imagenames])
            tpl = bigimagetpl

    extraclasses = ''
    if imagesize == 'small':
        if previous_smallimg_floatleft:
            extraclasses = 'right'
        else:
            extraclasses = 'left'
        previous_smallimg_floatleft = not previous_smallimg_floatleft
    else:
        previous_smallimg_floatleft = True

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
