import json
import random
import string
import sqlite3
from random import randint


def random_string(string_length):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(string_length))


conn = sqlite3.connect('C:\\Users\elip\\Jobs.sqlite')
c = conn.cursor()
productName = ""
vulnerability = ""
likelihood = ""
path = ""
Hash = ""
filename = ""
"""for row in c.execute('SELECT * FROM jobs Where Filename=?', ('DDSSetup',)):
    productName = row[3]
    likelihood = str(random.uniform(0, 1))
    vulnerability = str(random.randint(1, 9))
    path = row[1] + "." + row[8]
    Hash = row[0]
    filename = row[1]"""


data = {"554227C913441925412DFFB264D59273ADAF1A100954FB692FE20B1D11EFB46D":{"FileName":"C:\\Input\\DDSSetup.exe","Vendor":"Dell Inc.","Description":"Installer for Dell Data Security","ProductVersion":"10.1.0.9","FileVersion":"10.1.0.9","PathList":[{"Path":"C:\\Input\\PROPSYS12.dll","Likelihood":5,"Vulnerability":"DLL Hijacking"},{"Path":"C:\\Input\\edputil12.dll","Likelihood":5,"Vulnerability":"DLL Hijacking"}]}
}
with open('C:\\Users\\elip\\output\\result' + "_" + filename.replace("\\", "_") + '.txt', 'w') as outfile:
    json.dump(data, outfile)
