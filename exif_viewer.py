# Importing the exifread library to read EXIF metadata
import exifread

try:
    # Opening the image file in binary mode
    with open("sample2.jpg", 'rb') as file:

        # Processing the file to extract EXIF metadata
        tags = exifread.process_file(file)
        
        # Checking if any EXIF data is found
        if not tags:
            print("No EXIF metadata found.")
        else:
            
            # Looping through each tag (metadata key)
            for tag in tags.keys():
                # Printing the tag name and its value
                print(f"{tags[tag].tag}: {tags[tag].printable}")

# If the image file is not found, this message will be printed
except FileNotFoundError:
    print("File not found.")
