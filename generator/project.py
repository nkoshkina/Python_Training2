from model.project import Project
import random
import string
import os.path
import getopt
import sys
import jsonpickle

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of projects", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 3
f = "data/projects.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_sign_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_name(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + ":"*2 + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_igs():
    symbols = "0" + "1"
    return "".join([random.choice(symbols)])

def randome_status():
    symbols ="0"+"1"+"2"+"3"
    res = "".join([random.choice(symbols)])
    values = ["development", "release", "stable", "obsolete"]
    return values[int(res)]

def randome_viewStatus():
    symbols = "0"+"1"
    res = "".join([random.choice(symbols)])
    values = ["private", "public"]
    return values[int(res)]



testdata = [
       Project(projectName=random_name("T", 25), status=randome_status(), igs=random_igs(),
            viewStatus=randome_viewStatus(),
            description=random_sign_string("", 50))
    for i in range(n)]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as fout:
    fout.write(jsonpickle.encode(testdata, indent=2))