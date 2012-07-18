from xml.dom.minidom import parseString
import os
import shutil


#xml imput
inputXml = 'test.xml';


outputdir = "/Users/jochen/Desktop/"

#read file
f = open(inputXml,'r')

data = f.read()

#print data
albumName =""

#pares String
dom = parseString(data)

# find album name
for prop in dom.getElementsByTagName('property'):
     if prop.getAttribute('name') == 'name':
        albumName = prop.getAttribute('value')


print albumName;

outputdir = outputdir+albumName;

os.mkdir(outputdir)

picasaFiles = dom.getElementsByTagName('files')[0]

for filename in picasaFiles.getElementsByTagName('filename'):
    org =  filename.childNodes[0].nodeValue
    bild = org.replace("[G]","/Volumens/foo").replace("\\","/") 
    print bild;
    #shutil.copyfile(bild, )


