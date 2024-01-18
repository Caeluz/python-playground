import fitz  # PyMuPDF
import os

def extract_images_from_pdf(pdf_path, output_folder):
    # Open the PDF file
    pdf_document = fitz.open(pdf_path)

    # Iterate through each page in the PDF
    for page_number in range(pdf_document.page_count):
        page = pdf_document[page_number]

        # Get the images on the page
        images = page.get_images(full=True)

        # Iterate through each image on the page
        for img_index, img_info in enumerate(images):
            image_index = img_info[0]
            base_image = pdf_document.extract_image(image_index)

            # Get image information
            image_bytes = base_image["image"]
            image_ext = base_image["ext"]

            # Save the image
            image_filename = f"{output_folder}/page_{page_number + 1}_img_{img_index + 1}.{image_ext}"
            with open(image_filename, "wb") as image_file:
                image_file.write(image_bytes)

    # Close the PDF document
    pdf_document.close()

if __name__ == "__main__":
    pdf_path = r'C:\Users\ADMIN\Documents\lgu\System\LGU MAGAZINE.pdf'
    output_folder = r'C:\Users\ADMIN\Documents\lgu\System\New folder Test'

    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    extract_images_from_pdf(pdf_path, output_folder)
