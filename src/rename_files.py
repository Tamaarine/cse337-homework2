# Run this script from the repository's root.
import re
import os

def rename(path):
    files = os.listdir(path)
    
    # File format we are fixing is fixed so we can make the regex pattern
    p = re.compile(r'snap\d{3}.txt')
    
    # Filters out all the non-files
    files = [file for file in files if not os.path.isdir(os.path.join(path, file))]
    
    # Filter out only the snap files
    files = [file for file in files if p.match(file) is not None]
    
    files.sort()
    
    if len(files):
        txt_index = files[0].find(".txt")
        counter = int(files[0][:txt_index][-3:])
    
    for file in files:
        if p.match(file) is not None:
            txt_index = file.find(".txt")
            if counter != int(file[:txt_index][-3:]):
                old_full_path = os.path.join(path, file)
                new_full_path = os.path.join(path, f"snap{counter:03}.txt")
                
                # Re-raise the same error that's caught back to the user
                try:
                    os.rename(old_full_path, new_full_path)
                except FileExistsError as e:
                    # For windows, if dst exists not matter what it is
                    # FileExistsError will be raised
                    raise e
                except IsADirectoryError as e:
                    # src is a file
                    # dst is a directory
                    # incompatible move
                    raise e
            counter += 1