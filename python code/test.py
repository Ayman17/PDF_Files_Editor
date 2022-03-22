import PyPDF2
from PyPDF2 import PdfFileMerger, PdfFileReader, PdfFileWriter

#Function to check if input process is valide
def processcheck():
    p = int(input("What do you want to do: "))

    #check if num is valid
    while p > 4 or p < 1:
        p = int(input("Please enter a valid number: "))
    return p


#Function 1 to merge PDFs
def merge_PDFs(input_files, path_output):
    pdf_writer = PdfFileWriter()

    #merge two pdfs
    for path in input_files:
        pdf_reader = PdfFileReader(path)
        for page in range(pdf_reader.getNumPages()):
            pdf_writer.addPage(pdf_reader.getPage(page))

    #add name to merged pdf
    with open(path_output, "wb") as out:
        pdf_writer.write(out)


#Function 2 to extract page from PDF file
def extract_page(pdf_path, page_num):
    extracted_page = PdfFileWriter()
    new_page_name = "Extracted Page.pdf"

    #Extract the page
    for path in pdf_path:
        pdf_reader = PdfFileReader(path)
        extracted_page.addPage(pdf_reader.getPage(page_num - 1))

    #Add name to extracted pdf
    with open(new_page_name, "wb") as out:
        extracted_page.write(out)


#Function 3 to split pages from PDF file
def split_PDFs(pdfpath, name_of_splitedf):
    pdf = PdfFileReader(pdfpath)

    #Split one page from pdf
    for page in range(pdf.getNumPages()):
        pdf_splited = PdfFileWriter()
        pdf_splited.addPage(pdf.getPage(page))

        #Add name to one page of splited pdf
        name = f'{name_of_splitedf + "-" + str((page + 1))}.pdf'
        with open(name, 'wb') as out:
            pdf_splited.write(out)


while True:
    #Print choices for user
    print("\nPlease choose process:")
    print("Enter 1 to merge two pdf files.")
    print("Enter 2 to extract a single page from the pdf.")
    print("Enter 3 to split a pdf into separate pages.")
    print("Enter 4 to stop.\n")
    process = processcheck()

    #Merge
    if process == 1:
        input_files = []
        for counter in range(2):
            input_files.append(input("enter path of PDF" + str(counter + 1) + ": "))
        path_output = f'{input("enter name of merged PDF: ")}.pdf'
        merge_PDFs(input_files, path_output)

    #Extract
    elif process == 2:
        pdf_path = []
        pdf_path.append(input("Please paste the pdf path here: "))
        page_num = int(input("Please enter the page number: "))
        extract_page(pdf_path, page_num)

    #Split
    elif process == 3:
        pdf_path = input("Please paste the pdf path here: ")
        name_of_splitedf = input("Please enter name of splited fils: ")
        split_PDFs(pdf_path, name_of_splitedf)

    #Stop
    else:
        break