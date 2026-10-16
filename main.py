

import pypdf
import sys

inputs = sys.argv[1:]

def combiner(pdf_list):
    merger = pypdf.PdfWriter()

    for super_file in pdf_list:
        merger.append(super_file)

    merger.write("super_file.pdf")
    merger.close()

combiner(inputs)
