import sys
import os

input_folder = sys.argv[1]
extension = sys.argv[2]
	
for filename in os.listdir(input_folder):
	clean_filename = os.path.splitext(filename)[0]
	new_filename = clean_filename + extension
	os.rename(os.path.join(input_folder, filename), os.path.join(input_folder,new_filename))

print("\nDone\n")