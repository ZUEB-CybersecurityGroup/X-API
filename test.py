from xmodules.File_submit import Filesubmit

def test_filesubmit():
    filesubmit = Filesubmit()
    file_dir = "./11"
    filesubmit.main(file_dir)

test_filesubmit()
