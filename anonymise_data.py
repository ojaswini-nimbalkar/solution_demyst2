import csv
import hashlib

def anonymize_data(input_file, output_file):
    with open(input_file, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        fieldnames = reader.fieldnames
        
        with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()
            
            for row in reader:
                # Anonymize first_name, last_name, and address columns
                row['first_name'] = hashlib.sha256(row['first_name'].encode()).hexdigest()
                row['last_name'] = hashlib.sha256(row['last_name'].encode()).hexdigest()
                row['address'] = hashlib.sha256(row['address'].encode()).hexdigest()
                
                writer.writerow(row)

# Anonymize data.csv and write to anonymized_data.csv
anonymize_data('data.csv', 'anonymized_data.csv')
