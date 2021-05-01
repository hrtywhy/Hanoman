import base64
import os
import sys

os_name = sys.platform

def encode_base64(file, qPath):
    global os_name
    
    org_file_path = bytes(file, "utf-8")
    if "win" in os_name:
        org_file_name = file.rfind("\\")
    else:
        org_file_name = file.rfind("/")
    org_file_name = file[org_file_name+1:]
    f = open(file, "rb")
    org_content = f.read()
    f.close()
    os.remove(file)
    new_content = base64.b64encode(org_content)
    f = open(qPath + org_file_name + ".eb64", "wb")
    f.write(org_file_path + b"\n")
    f.write(new_content)
    f.close()

def decode_base64(file):
    f = open(file, "rb")
    org_content = f.read()
    f.close()
    org_content = org_content.splitlines()
    org_file_path = org_content[0]
    org_content.remove(org_file_path)
    new_content = []
    for i in org_content:
        new_content.append(base64.b64decode(i))   
    f = open(org_file_path, "wb")
    for i in new_content:
        f.write(i + b"\n")
    f.close()
    os.remove(file)
