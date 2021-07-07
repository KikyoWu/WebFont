f1=open(r"03-CSS进阶\1.txt",'r',encoding="UTF-8")
with open(r"03-CSS进阶\2.txt",'w',encoding='utf-8') as f2:
    for l in f1:
        if ".md" in l:
            f2.write(l)

f3=open(r"03-CSS进阶\2.txt",'r',encoding="UTF-8")
with open(r"03-CSS进阶\SUMMARY.md",'w',encoding='utf-8',newline='') as f4:
    for l in f3:
        l1=l.split(".md")
        l2=l.split("\n")
        n_l='*'+' '+'['+l1[0]+']'+'('+l2[0]+')'
        f4.write(n_l)
        f4.write('\n')

f5=open(r"03-CSS进阶\SUMMARY.md",'r',encoding="UTF-8")
for l in f5:
    l1=l.split('(')
    l2=l1[-1].split(')')
    f_name_1=l2[0]
    l3=l2[0].split('.')
    f_name_2=l3[0]
    with open(r"03-CSS进阶\{}".format(f_name_1),'w',encoding="UTF-8") as n_f:
        n_f.write('#'+' '+f_name_2)