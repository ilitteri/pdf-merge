import subprocess
from PyPDF2 import PdfFileReader, PdfFileMerger

def readPDF_files(file):
    with open(file, 'r') as paths:
        pdfs = [PdfFileReader(open(path.rstrip('\n'), 'rb')) for path in paths.readlines()]
    return pdfs

def merge_pdf(files):
    merger = PdfFileMerger()
    for pdf in files:
        merger.append(pdf)
    merger.write('merged_file.pdf')

def main():
    #subprocess.call('./get_path.sh')
    files = readPDF_files('paths.txt')
    merge_pdf(files)

if __name__ == "__main__":
    main()