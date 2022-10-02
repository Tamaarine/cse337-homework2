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
        pass
    
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
        shutil.rmtree(self.test_path, ignore_errors=True)
        os.mkdir(self.test_path)
        
        for i in range(1, 100):
            file_name = f"snap{i:03}.txt"
            
            with open(os.path.join(self.test_path, file_name), 'w') as f:
                f.write(f"{i}\n")
        for i in range(1, 21):
            file_name = f"snap{i:03}.txt"
            
            os.remove(os.path.join(self.test_path, file_name))
        
        rename(self.test_path)
        
        ret = os.listdir(self.test_path)
        ret.sort()
        
        exp = [f"snap{i:03}.txt" for i in range(1, 80)]
        
        assert ret == exp