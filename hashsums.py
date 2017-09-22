"""
A module that you can use to easily check the different hashsums on files
"""
import hashlib


def md5(option):
    """
    Checks the MD5 hashsum
    """
    hasher = hashlib.md5()
    with open(option, "rb") as afile:
        buf = afile.read()
        hasher.update(buf)
    return hasher.hexdigest()


def sha1(option):
    """
    Checks the SHA1 hashsum
    """
    hasher = hashlib.sha1()
    with open(option, "rb") as afile:
        buf = afile.read()
        hasher.update(buf)
    return hasher.hexdigest()


def sha224(option):
    """
    Checks the SHA224 hashsum
    """
    hasher = hashlib.sha224()
    with open(option, "rb") as afile:
        buf = afile.read()
        hasher.update(buf)
    return hasher.hexdigest()


def sha384(option):
    """
    Checks the SHA384 hashsum
    """
    hasher = hashlib.sha384()
    with open(option, "rb") as afile:
        buf = afile.read()
        hasher.update(buf)
    return hasher.hexdigest()


def sha256(option):
    """
    Checks the SHA256 hashsum
    """
    hasher = hashlib.sha256()
    with open(option, "rb") as afile:
        buf = afile.read()
        hasher.update(buf)
    return hasher.hexdigest()


def sha512(option):
    """
    Checks the SHA512 hashsum
    """
    hasher = hashlib.sha512()
    with open(option, "rb") as afile:
        buf = afile.read()
        hasher.update(buf)
    return hasher.hexdigest()
