import csv
import random

# Define the ranges for each field
age_range = (0, 100)  # Age range from 0 to 100
gender_options = ["Male", "Female", "Other"]
communication_range = (0, 2)
auditory_range = (0, 4)
visual_range = (0, 5)
motor_range = (0, 6)
arousal_range = (0, 3)
oromotor_verbal_range = (0, 3)

# Define the CSV file name
csv_file = "data.csv"

# Function to generate a random record
def generate_record(entry_id):
    record = {
        "EntryID": entry_id,
        "Age": random.randint(*age_range),
        "Gender": random.choice(gender_options),
        "Communication": random.randint(*communication_range),
        "Auditory": random.randint(*auditory_range),
        "Visual": random.randint(*visual_range),
        "Motor": random.randint(*motor_range),
        "Arousal": random.randint(*arousal_range),
        "Oromotor/Verbal": random.randint(*oromotor_verbal_range),
    }
    return record

# Function to generate and write records to a CSV file
def generate_csv(num_records, file_name=csv_file):
    records = [generate_record(entry_id) for entry_id in range(1, num_records + 1)]
    
    with open(file_name, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=records[0].keys())
        writer.writeheader()
        writer.writerows(records)

    print(f"{num_records} records have been written to {file_name}")

# Example usage:
if __name__ == "__main__":
    # The user can specify the number of entries here
    num_entries = 100  # Change this value as needed
    generate_csv(num_entries)
