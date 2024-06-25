import csv

# Define the input and output CSV file names
input_csv_file = "data.csv"
output_csv_file = "finished.csv"

# Function to interpret the data and add the raw score and degrees of consciousness
def interpret_data(input_file, output_file):
    with open(input_file, mode='r', newline='') as infile:
        reader = csv.DictReader(infile)
        records = list(reader)
        
    # Add the Raw Score and Degrees of Consciousness to each record
    for record in records:
        communication = int(record["Communication"])
        auditory = int(record["Auditory"])
        visual = int(record["Visual"])
        motor = int(record["Motor"])
        arousal = int(record["Arousal"])
        oromotor_verbal = int(record["Oromotor/Verbal"])
        
        raw_score = communication + auditory + visual + motor + arousal + oromotor_verbal
        
        if raw_score <= 7:
            degrees_of_consciousness = "Unresponsive Wakefulness Syndrome/Vegetative state"
        elif raw_score <= 19:
            degrees_of_consciousness = "Minimally conscious state"
        else:
            degrees_of_consciousness = "Emerged from minimally conscious state"
        
        record["Raw Score"] = raw_score
        record["Degrees of Consciousness"] = degrees_of_consciousness

    # Write the updated records to the output CSV file
    with open(output_file, mode='w', newline='') as outfile:
        fieldnames = records[0].keys()
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(records)

    print(f"Updated records have been written to {output_file}")

# Example usage:
if __name__ == "__main__":
    interpret_data(input_csv_file, output_csv_file)
