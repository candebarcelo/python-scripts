import PyPDF2
import sys
import os


# input from terminal: file.pdf with watermark[1] and then files.pdf to watermark[2:]
watermark_file = PyPDF2.PdfFileReader(open(sys.argv[1], "rb"))
input_file_list = sys.argv[2:]  # list of all input files


# watermark the pdfs
def watermark(watermark_file, input_file_list):
    for item in input_file_list:
        file = PyPDF2.PdfFileReader(open(item, "rb"))  # open each file
        # define output here so that it's cleared for each file
        output_pdf = PyPDF2.PdfFileWriter()
        # for each page (getNumPages gets the number of pages in pdf
        for i in range(file.getNumPages()):
            page = file.getPage(i)
            # mergePage merges each page with the watermark pdf
            page.mergePage(watermark_file.getPage(0))
            output_pdf.addPage(page)

        with open(('merged_' + item), "wb") as merged_file:
            # writes the file, and creates it if it doesn't exist
            output_pdf.write(merged_file)

        print('done!', item)


watermark(watermark_file, input_file_list)
