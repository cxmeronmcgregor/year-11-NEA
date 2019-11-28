import hashlib

passwd = ""

hashed_password = hashlib.md5(passwd.encode("utf-8")).hexdigest()

print(hashed_password)
