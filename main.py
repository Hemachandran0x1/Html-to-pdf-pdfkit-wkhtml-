import pdfkit

x = input('Enter Url:')
y = input('Enter pdf name:') + '.pdf'
pdfkit.from_url(x, y)
