# -*- coding:utf-8 -*-

def rewrite(origin_text):
    res_text=""
    i=0
    while True:
        current_text=origin_text[i]
        current_uni=ord(current_text)

        if current_text=='Α' or current_uni == 0x0386 or 0x1f08 <= current_uni <= 0x1f0f or 0x1f88 <= current_uni <= 0x1f8f or 0x1fb8 <= current_uni <= 0x1fbc:
            res_text+='A'
        elif current_text=='Β':
            res_text+='B'
        elif current_text=='Γ':
            res_text+='G'
        elif current_text=='Δ':
            res_text+='D'
        elif current_text=='Ε' or current_uni == 0x0388 or 0x1f18 <= current_uni <= 0x1f1d or 0x1f98 <= current_uni <= 0x1f9f or 0x1fc8 <= current_uni <= 0x1fc9:
            res_text+='E'
        elif current_text=='Ζ':
            res_text+='Z'
        elif current_text=='Η' or current_uni == 0x0389 or 0x1f28 <= current_uni <= 0x1f2f or 0x1fca <= current_uni <= 0x1fcc:
            res_text+='Ē'
        elif current_text=='Θ':
            res_text+='Th'
        elif current_text=='Ι' or current_uni == 0x03aa or current_uni == 0x038a or 0x1f38 <= current_uni <= 0x1f3f or 0x1fd8 <= current_uni <= 0x1fdb:
            res_text+='I'
        elif current_text=='Κ':
            res_text+='K'
        elif current_text=='Λ':
            res_text+='L'
        elif current_text=='Μ':
            res_text+='M'
        elif current_text=='Ν':
            res_text+='N'
        elif current_text=='Ξ':
            res_text+='X'
        elif current_text=='Ο' or current_uni == 0x038c or 0x1f48 <= current_uni <= 0x1f4d or 0x1ff8 <= current_uni <= 0x1ff9:
            res_text+='O'
        elif current_text=='Π':
            res_text+='P'
        elif current_text=='Ρ' or 0x1fec == current_uni:
            res_text+='R'
        elif current_text=='Σ':
            res_text+='S'
        elif current_text=='C':
            res_text+='S'
        elif current_text=='Τ':
            res_text+='T'
        elif current_text=='Υ' or 0x03d2 <= current_uni <= 0x03d4 or current_uni == 0x03ab or current_uni == 0x038e or 0x1f59 <= current_uni <= 0x1f5f or 0x1fe8 <= current_uni <= 0x1feb:
            res_text+='Y'
        elif current_text=='Φ':
            res_text+='Ph'
        elif current_text=='Χ':
            res_text+='Ch'
        elif current_text=='Ψ':
            res_text+='Ps'
        elif current_text=='Ω' or current_uni == 0x038f or 0x1f68 <= current_uni <= 0x1f6f or 0x1fa8 <= current_uni <= 0x1faf or 0x1ffa <= current_uni <= 0x1ffc:
            res_text+='Ō'
        elif current_text=='Ϝ':
            res_text+='W'
        elif current_text=='Ϙ':
            res_text+='Ḳ'
    
        elif current_text=='α' or current_uni == 0x03ac or 0x1f00 <= current_uni <= 0x1f07 or 0x1f70 <= current_uni <= 0x1f71 or 0x1f80 <= current_uni <= 0x1f87 or 0x1fb0 <= current_uni <= 0x1fb7:
            res_text+='a'
        elif current_text=='β':
            res_text+='b'
        elif current_text=='γ':
            res_text+='g'
        elif current_text=='δ':
            res_text+='d'
        elif current_text=='ε' or current_uni == 0x03ad or 0x1f10 <= current_uni <= 0x1f15 or 0x1f72 <= current_uni <= 0x1f73:
            res_text+='e'
        elif current_text=='ζ':
            res_text+='z'
        elif current_text=='η' or current_uni == 0x03ae or 0x1f20 <= current_uni <= 0x1f27 or 0x1f74 <= current_uni <= 0x1f75 or 0x1f90 <= current_uni <= 0x1f97 or 0x1fc2 <= current_uni <= 0x1fc7:
            res_text+='ē'
        elif current_text=='θ':
            res_text+='th'
        elif current_text=='ι' or current_uni == 0x03ca or current_uni == 0x03af or current_uni == 0x0390 or 0x1f30 <= current_uni <= 0x1f37 or 0x1f76 <= current_uni <= 0x1f77 or 0x1fd0 <= current_uni <= 0x1fd7:
            res_text+='i'
        elif current_text=='κ':
            res_text+='k '
        elif current_text=='λ':
            res_text+='l'
        elif current_text=='μ':
            res_text+='m'
        elif current_text=='ν':
            res_text+='n'
        elif current_text=='ξ':
            res_text+='x'
        elif current_text=='ο' or current_uni == 0x03cc or 0x1f40 <= current_uni <= 0x1f45 or 0x1f78 <= current_uni <= 0x1f79:
            res_text+='o'
        elif current_text=='π':
            res_text+='p'
        elif current_text=='ρ' or 0x1fe4 <= current_uni <= 0x1fe5:
            res_text+='r'
        elif current_text=='σ':
            res_text+='s'
        elif current_text=='ς':
            res_text+='s'
        elif current_text=='ϲ':
            res_text+='s'
        elif current_text=='τ':
            res_text+='t'
        elif current_text=='υ' or current_uni == 0x03cd or current_uni == 0x03cb or current_uni == 0x03b0 or 0x1f50 <= current_uni <= 0x1f57 or 0x1f7a <= current_uni <= 0x1f7b or 0x1fe0 <= current_uni <= 0x1fe3 or 0x1fe6 <= current_uni <= 0x1fe7:
            res_text+='y'
        elif current_text=='φ':
            res_text+='ph'
        elif current_text=='χ':
            res_text+='ch'
        elif current_text=='ψ':
            res_text+='ps'
        elif current_text=='ω' or current_uni == 0x03ce or 0x1f60 <= current_uni <= 0x1f67 or 0x1f7c <= current_uni <= 0x1f7d or 0x1fa0 <= current_uni <= 0x1fa7 or 0x1ff2 <= current_uni <= 0x1ff7:
            res_text+='ō'
        elif current_text=='ϝ':
            res_text+='w'
        elif current_text=='ϙ':
            res_text+='ḳ'
        elif current_text=='ϐ':
            res_text+='b'
        elif current_text=='«':
            res_text+='“'
        elif current_text=='»':
            res_text+='”'
        elif current_text=='᾿':
            res_text+="'"
        elif current_text==';':
            res_text+="?"
        elif current_text=='·':
            res_text+=":"
    
        else:
            res_text+=current_text
            if current_text not in ["'",","," ","\n",";","\t","."]:
                print(current_text+' '+str(current_uni))
        i+=1
        if i==len(origin_text):
            break
    return res_text

if __name__=='__main__':
    f=open('example/origin.txt',encoding='utf-8')
    origin_text=""
    while True:
        read_res=f.readline()
        if read_res:
            origin_text+=read_res
        else:
            break
    f.close()

    print(origin_text)
    print('\n')

    res_text = rewrite(origin_text)

    print('\n')
    print(res_text)
    g = open("example/result.txt",'w',encoding='utf-8')
    g.write(res_text)
    g.close()
