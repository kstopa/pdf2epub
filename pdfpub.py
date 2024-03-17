import argparse
import pypandoc
from pdf2docx import Converter


def pdf_to_epub(pdf_path, epub_path, ignore_header_footer=True):
    docx_path = pdf_path.replace('.pdf', '.docx')
    # Initialize converter with options to ignore headers and footers
    convert_settings = {
        "ignore_footer": ignore_header_footer,
        "ignore_header": ignore_header_footer,
    }
    cv = Converter(pdf_path)

    # Convert PDF to DOCX with specified settings
    cv.convert(docx_path, **convert_settings)
    cv.close()

    # Step 2: Convert DOCX to EPUB
    output = pypandoc.convert_file(docx_path, 'epub', outputfile=epub_path)
    print(output)


def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='Convert a PDF file to EPUB format.')
    parser.add_argument('pdf_path', type=str, help='Path to the PDF file to convert.')
    args = parser.parse_args()

    # Derive EPUB path from PDF path
    epub_path = args.pdf_path.replace('.pdf', '.epub')

    # Perform conversion
    pdf_to_epub(args.pdf_path, epub_path)
    print(f"Conversion complete. EPUB file saved to: {epub_path}")


if __name__ == '__main__':
    main()
