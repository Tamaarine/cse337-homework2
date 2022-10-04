import pytest
import sys
import os
sys.path.insert(1, os.getcwd())
from src.rename_files import rename
import shutil

class TestRenameFiles:
    def setup_method(self):
        self.cwd = os.getcwd()
        self.test_path = os.path.join(self.cwd, "test_files")
        shutil.rmtree(self.test_path, ignore_errors=True) # Delete the path if exist
        
    def teardown_method(self):
        shutil.rmtree(self.test_path, ignore_errors=True) # Delete the path if exist
        
    def test_rename1(self):
        os.mkdir(self.test_path)
        
        for i in range(1, 100, 2):
            file_name = f"snap{i:03}.txt"
            
            with open(os.path.join(self.test_path, file_name), 'w') as f:
                f.write(f"{i}\n")
        
        rename(self.test_path)
        
        ret = os.listdir(self.test_path)
        ret.sort()
        
        exp = [f"snap{i:03}.txt" for i in range(1, 51)]
        
        assert ret == exp
    
    def test_rename2(self):
        os.mkdir(self.test_path)
        
        for i in range(1, 100):
            file_name = f"snap{i:03}.txt"
            
            with open(os.path.join(self.test_path, file_name), 'w') as f:
                f.write(f"{i}\n")
        
        # Removed snap001.txt to snap020.txt
        for i in range(1, 21):
            file_name = f"snap{i:03}.txt"
            
            os.remove(os.path.join(self.test_path, file_name))
        
        rename(self.test_path)
        
        ret = os.listdir(self.test_path)
        ret.sort()
        
        # None of the files should change
        exp = [f"snap{i:03}.txt" for i in range(21,100)]
        
        assert ret == exp
    
    def test_rename3(self):
        os.mkdir(self.test_path)
        
        # files labeled from 5 to 60 inclusive, skipping by 5
        for i in range(5, 65, 5):
            file_name = f"snap{i:03}.txt"
            
            with open(os.path.join(self.test_path, file_name), 'w') as f:
                f.write(f"{i}\n")
        
        # Make some directories
        for i in range(5, 65, 5):
            dir_name = f"snap{i:03}"
            os.mkdir(os.path.join(self.test_path, dir_name))
                
        rename(self.test_path)
        
        ret = os.listdir(self.test_path)
        ret.sort()
        
        # Constructing the expected results
        exp = [f"snap{i:03}.txt" for i in range(5, 17, 1)]
        exp = exp + [f"snap{i:03}" for i in range(5, 65, 5)]
        exp.sort()
        
        # Make sure the names are equal
        assert ret == exp
        
        # Then check the directory and files are the same as well
        for i in range(len(ret)):
            ret_path = os.path.join(self.test_path, ret[i])
            exp_path = os.path.join(self.test_path, exp[i])
            assert os.path.isdir(ret_path) == os.path.isdir(exp_path)
    
    def test_rename4(self):
        os.mkdir(self.test_path)
        
        with pytest.raises(IsADirectoryError):
            # File from snap005.txt to snap060 skipping by 5
            for i in range(5, 65, 5):
                file_name = f"snap{i:03}.txt"
                
                with open(os.path.join(self.test_path, file_name), 'w') as f:
                    f.write(f"{i}\n")
            
            # Make a directory named snap006.txt in same directory it should error out
            os.mkdir(os.path.join(self.test_path, "snap006.txt"))
            
            rename(self.test_path)