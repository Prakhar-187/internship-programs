alphabet=input("Enter any alphabet: ")

dict={1:"a",2:"b",3:"c",4:"d",5:"e",6:"f",7:"g",8:"h",9:"i",10:"j",11:"k",12:"l",13:"m",14:"n",15:"o",16:"p",17:"q",18:"r",19:"s",20:"t",21:"u",22:"v",23:"w",24:"x",25:"y",26:"z"}
# list=[a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z]
if(alphabet==dict[1] or alphabet==[5] or alphabet==[9] or alphabet==[15] or alphabet==[21]):
    print(f"{alphabet} is a vowel")
else:
    print(f"{alphabet} is a consonant")
    