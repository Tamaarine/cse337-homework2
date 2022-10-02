# Run this script from the repository's root.
import re
import os

def rename(path):
    files = os.listdir(path)
    
    # Filters out all the non-files
    files = [file for file in files if not os.path.isdir(os.path.join(path, file))]
    
    # Filters out only .txt files
    files = [file for file in files if file.endswith(".txt")]
    
    files.sort()
    
    # File format we are fixing is fixed
    p = re.compile(r'snap\d{3}.txt')
    
    counter = 1
    for file in files:
        if p.match(file) is not None:
            txt_index = file.find(".txt")
            if counter != int(file[:txt_index][-3:]):
                old_full_path = os.path.join(path, file)
                new_full_path = os.path.join(path, f"snap{counter:03}.txt")
                os.rename(old_full_path, new_full_path)
            counter += 1