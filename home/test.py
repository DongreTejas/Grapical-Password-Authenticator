import hashlib

with open(r"C:\Users\Tejaspc\OneDrive\Documents\New folder\Graphical-Password-User-Authentincation\static\images\about.jpg", "rb") as f:
    img_hash = hashlib.sha256()
    while chunk := f.read(8192):
        img_hash.update(chunk)
print(img_hash.hexdigest())