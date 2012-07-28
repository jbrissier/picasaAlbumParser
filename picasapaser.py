from xml.dom.minidom import parseString
import os
import re
import shutil

xmlpath = '.'

#xml imput
#inputXml = 'test.xml';

inputdir = "/Volumens/foo"
outputdir = "/Users/jochen/Desktop/"
disk = "[G]"

def copyAlbum(inputXml):
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
    global outputdir
    outputdir = outputdir+albumName.replace(' ',"_");
    #os.rmdir(outputdir)
    os.mkdir(outputdir)

    picasaFiles = dom.getElementsByTagName('files')[0]

    for filename in picasaFiles.getElementsByTagName('filename'):
        org =  filename.childNodes[0].nodeValue
        bild = org.replace("[G]",inputdir).replace("\\","/") 
        print bild;
        basename = os.path.basename(bild)
        systemcall = 'cp %s %s' % (bild,outputdir+'/'+basename)
        print systemcall
        os.system(systemcall)
        #shutil.copyfile(bild, )



for xml in os.listdir(xmlpath):
    if(re.match(".*\.xml",xml)):
        copyAlbum(xml)        




