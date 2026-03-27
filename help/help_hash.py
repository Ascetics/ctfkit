import hashlib

text = 'password'
md5_hash = hashlib.md5(text.encode('utf-8')).hexdigest()
print(md5_hash)

sha256_hash = hashlib.sha256(text.encode()).hexdigest()
print(sha256_hash)