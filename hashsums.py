import hashlib

def md5(option):
    hasher = hashlib.md5()
    with open(option,"rb") as afile:
        buf = afile.read()
        hasher.update(buf)
    return hasher.hexdigest()

def sha1(option):
    hasher = hashlib.sha1()
    with open(option,"rb") as afile:
        buf = afile.read()
        hasher.update(buf)
    return hasher.hexdigest()

def sha224(option):
    hasher = hashlib.sha224()
    with open(option, "rb") as afile:
        buf = afile.read()
        hasher.update(buf)
    return hasher.hexdigest()

def sha384(option):
    hasher = hashlib.sha384()
    with open(option, "rb") as afile:
        buf = afile.read()
        hasher.update(buf)
    return hasher.hexdigest()

def sha256(option):
    hasher = hashlib.sha256()
    with open(option, "rb") as afile:
        buf = afile.read()
        hasher.update(buf)
    return hasher.hexdigest()

def sha512(option):
    hasher = hashlib.sha512()
    with open(option, "rb") as afile:
        buf = afile.read()
        hasher.update(buf)
    return hasher.hexdigest()