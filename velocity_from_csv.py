import glob
import csv

folder_path = "./videos/Distilled"  
csv_files_pattern = folder_path + "/*.csv"
csv_files = glob.glob(csv_files_pattern)

velocities = []

for file_path in csv_files:
    try:
        with open(file_path, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            data = list(reader)
            velocity = data[-1][10]
            velocities.append(velocity)
                
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        
print(velocities)

input_filename = 'videos/DistilledData.csv'

# Your list of values to write
new_column_data = ['Value A', 'Value B', 'Value C', 'Value D']

# Create a temporary file to write the modified data
output_filename = 'videos/DistilledData_updated.csv'

with open(input_filename, 'r', newline='') as infile, \
        open(output_filename, 'w', newline='') as outfile:
    reader2 = csv.reader(infile)
    writer = csv.writer(outfile)

    # Read the header row and write it to the new file
    header = next(reader2)
    writer.writerow(header + ['ScriptVelocity']) # Add the new column header

    # Iterate through the rows and add data from the list
    for i, row in enumerate(reader2):
        if i < len(velocities):  # Ensure you don't go out of bounds
            row.append(velocities[i])  # Add the new value to the row
        else:
            row.append('') # Add an empty string if list is shorter than CSV rows
        writer.writerow(row)

# Replace the original file with the updated file
import os
os.replace(output_filename, input_filename)
