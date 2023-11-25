import csv

def process_csv(input_file, output_file):
    with open(input_file, 'r', newline='') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        for row in reader:
            modified_row = [cell.replace('\n', ' ').replace('-', '.') for cell in row]
            writer.writerow(modified_row)

if __name__ == "__main__":
    input_file_path = "E:/Desktop/Graphic Design/Crystalat/2023/11/22/test.csv"  # replace with the path to your input CSV file
    output_file_path = "E:/Desktop/Graphic Design/Crystalat/2023/11/22/desc_final_22_11_2023.csv"  # replace with the desired output CSV file path

    process_csv(input_file_path, output_file_path)
    print("CSV processing complete. Check the output file:", output_file_path)
