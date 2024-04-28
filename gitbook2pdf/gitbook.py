import sys
from gitbook2pdf import Gitbook2PDF

from weasyprint.text.ffi import fontconfig
fontconfig.FcInitLoadConfigAndFonts()


def usage() :
    print("usage : python gitbook.py <url|file path> [pdfname]")

if __name__ == '__main__':
    # if len(sys.argv) == 3 :
    #     fname = sys.argv[2]
    #     url = sys.argv[1]
    # elif len(sys.argv) == 2 and sys.argv[1] != "--help" :
    #     fname = None
    #     url = sys.argv[1]
    # else :
    #     usage()
    #     exit(0)
    url = sys.argv[1] if sys.argv[1:] else 'https://dcm.nephen.cn'
    fname = sys.argv[2] if sys.argv[2:] else None
    
     
    Gitbook2PDF(url,fname).run()
