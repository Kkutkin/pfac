# AUTEUR                : COUZON PASCAL
# DATE                  : 19-02-2023
# DESCRIPTION           : Analysela configuration d'un pfsense
# PARAMETRE
#       ENTREE          : Fichier de sauvegarde XML d'un pfsense
#       SORTIE          : Ecran


import xml.etree.ElementTree as et
xmlfile = r"config-pfSense.home.arpa-20230218181634.xml"
tree = et.parse(xmlfile)
root = tree.getroot()
headergroup=['name','description','scope','gid','member']
headeruser=['name','description','scope','groupname','HashPassword','uid','priv']
headerinterface=['name','enable','if','ipaddr','ipaddrv6','gateway','blockpriv','blockbogons','media','mediaopt','dhcp6-duid','dhcp6-ia-pd-len']
headerrules=[]
headersshdata=['filename','xmldata']

# récupere la version
def version(root):
    return root[0].text

def lastchange(root):
    return root[1].text

def group(root,header):
    table=[]
    table.append(header)
    raw=[]
    
    for group in root:
        for member in group:
            raw.append(member.text)
            
        table.append(raw)
        raw=[]
    
    return table


def interfaces(root,header):
    table=[]
    table.append(header)
    raw=[]
    for node in root:
        for interface in node:
            raw.append(interface.tag)
            for member in interface:
                if member.text == 'None':
                    raw.append((member.tag + member.text))
                else: 
                    raw.append(member.tag)
                    
        
            table.append(raw)
            raw=[]

    return table



print("version=", version(root))
print("lastchange=",lastchange(root))
#for x in (group(root.iter("group"),headergroup)):
#    print(x)
#for x in (group(root.iter("user"),headeruser)):
#    print(x)
#for x in (group(root.iter("sshkeyfile"),headersshdata)):
#    print(x)
#for x in (group(root.iter("wan"),headersshdata)):
#    print(x)
for x in (interfaces(root.iter("interfaces"),headerinterface)):
    print(x)

