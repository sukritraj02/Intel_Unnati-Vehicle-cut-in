import os
import xml.etree.ElementTree as ET
import pandas as pd

# Define the directory path where the XML files are located
xml_dir = r'C:\Users\sukri\OneDrive\Desktop\projects\idd-detection\Annotations'

# Initialize an empty list to store the data
data = []

# Iterate over all XML files in the directory and subdirectories
for root_dir, sub_dirs, files in os.walk(xml_dir):
    for filename in files:
        if filename.endswith('.xml'):
            file_path = os.path.join(root_dir, filename)
            tree = ET.parse(file_path)
            root = tree.getroot()
            
            # Extract the filename, label, and bounding box coordinates
            file_name = root.find('filename').text
            objects = root.findall('object')
            for obj in objects:
                label = obj.find('name').text
                bndbox = obj.find('bndbox')
                xmin = int(bndbox.find('xmin').text)
                ymin = int(bndbox.find('ymin').text)
                xmax = int(bndbox.find('xmax').text)
                ymax = int(bndbox.find('ymax').text)
                
                # Append the data to the list
                data.append([file_name, label, xmin, ymin, xmax, ymax])

# Create a DataFrame from the list
df = pd.DataFrame(data, columns=['filename', 'label', 'xmin', 'ymin', 'xmax', 'ymax'])

# Save the DataFrame to a CSV file
output_csv = r'C:\Users\sukri\OneDrive\Desktop\projects\idd-detection\annotations.csv'
df.to_csv(output_csv, index=False)
