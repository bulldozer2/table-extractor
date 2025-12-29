import os
from img2table.document import Image
from img2table.ocr import TesseractOCR
import pandas as pd

# OCR engine
ocr = TesseractOCR(lang="eng")

# Your folders
folders = [
    r"/workspaces/table-extractor/jkia embarked",
    r"/workspaces/table-extractor/jkia landed"
]

output_dir = "extracted_tables"
os.makedirs(output_dir, exist_ok=True)

table_count = 0

for folder in folders:
    for file in os.listdir(folder):
        if file.lower().endswith((".png", ".jpg", ".jpeg")):
            image_path = os.path.join(folder, file)
            img = Image(image_path)

            tables = img.extract_tables(ocr=ocr)

            for table in tables:
                df = table.df
                table_count += 1

                output_file = f"{output_dir}/table_{table_count}.csv"
                df.to_csv(output_file, index=False)

                print(f"Saved: {output_file}")