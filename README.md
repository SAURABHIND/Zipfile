Steps for Zip file



# Option 1
> zip -e -P india iit.zip /home/bsetec/package.json


# Option 2

> git clone https://github.com/smihica/pyminizip.git

> virtualenv env
> source env/bin/python
> python setup.py install
> pip install pyminizip		# it's not required we have already install the package

#----------------- PYTHON SCRIPT ----------------------#

import pyminizip
compression_level = 5  # we can set compression level upto 1-9
pyminizip.compress("/home/bsetec/package.json","/home/bsetec","/home/bsetec/Desktop/dst.zip", "password", compression_level)




