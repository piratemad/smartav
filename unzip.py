import os, zipfile

extension = ".zip"


for item in os.listdir("samples/zippedMalware"):
    if item.endswith(extension):
        file_name = os.path.abspath(item)
        zip_ref = zipfile.ZipFile(file_name)
        zip_ref.extractall("samples/zippedMalware",pwd="infected")
        zip_ref.close()
