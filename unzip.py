from zipfile import ZipFile

zip_file = '/home/bsetec/Desktop/indai.zip'
password = 'india123'

with ZipFile(zip_file) as zf:
	zf.extractall(pwd=bytes(password))