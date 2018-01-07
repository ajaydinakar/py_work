 if c.find('|'):
            cmmd=cmmd.split('|')
            var1=cmmd[0]
            var2=cmmd[1]
            one_cmd(var1)
            var2=var2+" "+"md.txt"
            one_cmd(var2)
        elif cmmd.find('>'):
            cmmd=cmmd.split('>')
            var1=cmmd[0]
            var2=cmmd[1]
            one_cmd(var1)
            temp=open('/root/mdr.txt','r')
            ofile=open('out.txt','a')
            for line in temp.readlines():
                ofile.write(line)
            temp.close()
            ofile.close()
        elif cmmd.find('>>'):
            cmmd=cmmd.split('>>')
            var1=cmmd[0]
            var2=cmmd[1]
            one_cmd(var1)
            temp=open('/root/mdr.txt','r')
            ofile=open('out.txt','a')
            for line in temp.readlines():
                ofile.write(line)
            temp.close()
            ofile.close()

        elif cmmd.find('>'):
            cmmd=cmmd.split('>')
            var1=cmmd[0]
            var2=cmmd[1]
            one_cmd(var1)
        else:
