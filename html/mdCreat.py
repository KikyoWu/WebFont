f1=open(r"C:\Users\blackwalnutlabs\Desktop\04\前端\html\1.txt",'r',encoding="UTF-8")
with open(r"C:\Users\blackwalnutlabs\Desktop\04\前端\html\2.txt",'w',encoding='utf-8') as f2:
    for l in f1:
        if ".md" in l:
            f2.write(l)

f3=open(r"C:\Users\blackwalnutlabs\Desktop\04\前端\html\2.txt",'r',encoding="UTF-8")
with open(r"C:\Users\blackwalnutlabs\Desktop\04\前端\html\SUMMARY.md",'w',encoding='utf-8',newline='') as f4:
    for l in f3:
        l1=l.split(".md")
        l2=l.split("\n")
        n_l='*'+' '+'['+l1[0]+']'+'('+l2[0]+')'
        f4.write(n_l)
        f4.write('\n')

f5=open(r"C:\Users\blackwalnutlabs\Desktop\04\前端\html\SUMMARY.md",'r',encoding="UTF-8")
for l in f5:
    l1=l.split('(')
    l2=l1[-1].split(')')
    f_name=l2[0]
    with open(r"C:\Users\blackwalnutlabs\Desktop\04\前端\html\{}".format(f_name),'w',encoding="UTF-8") as n_f:
        n_f.write('#'+' '+f_name)