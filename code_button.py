from PIL import Image
import base64
import os
from sys import argv

def generate_preview(preview, file_name):
    fo=open(file_name, "w")
    fo.write(";SHUI PREVIEW 100x100\n")
    index=0
    row = bytearray()
    for d in preview.getdata():
        r=d[0]>>3
        g=d[1]>>2
        b=d[2]>>3
        rgb = (r << 11) | (g << 5) | b
        row.append((rgb >> 8) & 0xFF)
        row.append(rgb & 0xFF)
        index+=1
        if (index==100):
            index=0
            fo.write(";" + base64.b64encode(row).decode('utf-8') + "\n")
            row = bytearray()
    fo.write(";Write configuration code below\n")
    fo.close()


for d, dirs, files in os.walk("100x100"):
    for f in files:
        pre, ext = os.path.splitext(f)
        if ext=='.png':
            out_file=os.path.join("100x100_snp", pre+'.snippet')
            image=Image.open(os.path.join(d, f))
            generate_preview(image, out_file)
        #
