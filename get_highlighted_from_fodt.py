import os, sys
import xml.etree.ElementTree as ET



# Find the .fodt file
filepath = sys.argv[0]
filedir = os.path.split(filepath)[0]
filename = sys.argv[1]


# Get the xml root and set namespace variables
tree  = ET.parse(os.path.join(filedir,filename))
root = tree.getroot()
office_namespace = '{urn:oasis:names:tc:opendocument:xmlns:office:1.0}'
text_namespace='{urn:oasis:names:tc:opendocument:xmlns:text:1.0}'


# List all the highlighted phrases
highlighted_phrases=[]
for el in root.find(office_namespace+'body').find(office_namespace+'text').findall(text_namespace+'p'):
    for subel in el.findall(text_namespace+'span'):
        highlighted_phrases.append(subel.text)
        print subel.text


# Write out the phrases to a .txt file named like the .fodt file; e.g. words.fodt--> words_highlighted.txt
f=open(os.path.join(filedir,filename.replace(".fodt","")+"_highlighted.txt"),'w')

f.write("\n".join(highlighted_phrases))
f.close()
