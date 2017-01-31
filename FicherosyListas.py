#!usr/bin/python3
fich=open("/etc/passwd","r")
usuarios=fich.readlines()
fich.close()
for usuario in usuarios:
    print(usuario.split(':')[0] + "--->" + usuario.split(':')[-1])
