import csv
import random
from faker import Faker

# Initialize Faker for generating random data
fake = Faker()

def generate_data_csv(filename, num_records):
    fieldnames = ['first_name', 'last_name', 'address', 'date_of_birth']
    
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        
        for _ in range(num_records):
            writer.writerow({
                'first_name': fake.first_name(),
                'last_name': fake.last_name(),
                'address': fake.address().replace("\n", ", "),
                'date_of_birth': fake.date_of_birth(minimum_age=18, maximum_age=80).strftime('%Y-%m-%d')
            })

# Generate 2 million records (adjust as needed)
generate_data_csv('data.csv', 2000000)
