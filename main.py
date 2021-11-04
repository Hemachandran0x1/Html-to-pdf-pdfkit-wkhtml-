import pdfkit
import argparse

parser = argparse.ArgumentParser(description="Html to Pdf")
parser.add_argument("-u", "--url", help="To convert online resource into pdf ", default=0)
parser.add_argument("-f", "--file", help="To convert downloaded html to pdf", default=0)
args = parser.parse_args()
if args.url:
    x = input('Enter pdf name:') + '.pdf'
    pdfkit.from_url(args.url, x)
elif args.file:
    y = input('Enter pdf name:')+'.pdf'
    pdfkit.from_file(args.file, y)
else:
    print("use \"-h\" as command line argument for help")

