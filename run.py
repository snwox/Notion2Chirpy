from module import N2C
import argparse

def main():
    parser = argparse.ArgumentParser(description='Notion2Chirpy')
    parser.add_argument('--tags', type=str,default='',nargs='+',
            metavar='tags',
            help='from zero to infinite')
    parser.add_argument('zip', type=str, 
            metavar='notion-zip-file',
            help='notion out file, extract to MD+SVG')
    parser.add_argument('out', type=str, 
            metavar='chirpy-folder',
            help='chirpy folder ( ex : ./snwox.github.io )')
    parser.add_argument('c', type=str, nargs='+',
            metavar='categories',
            help='at least one category, max 2, seperate with space ')
    parser.add_argument('--title', type=str,default='',
            help='default extracted from notion zip file')
    parser.add_argument('--date', type=str,default='',
            help='default current time, format : YYYY-MM-DD HH:MM:SS +/- TTTT ')
    parser.add_argument('--name', type=str,default='',
            help='default your name in _config.yml')
    parser.add_argument('--link', type=str,default='',
            help='default your twitter in _config.yml')
    parser.add_argument('--toc', type=bool,default='',
            help='default True')
    parser.add_argument('--math', type=bool,default='',
            help='default False')
    parser.add_argument('--comments', type=bool,default='',
            help='default True')
    parser.add_argument('--mermaid', type=bool,default='',
            help='default False')

    args=parser.parse_args()
    N2C.n2c(args.zip,args.out,args.c,args.tags,args.date,args.name,args.link,args.toc,
            args.math,args.comments,args.mermaid,args.title)
if __name__=="__main__":
	main()