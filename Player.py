#***Made By AnoDude***
#My first time going up 20 lines in one code with Python
from os import system
from time import sleep
def slep():
    sleep(0.25)
def clear():
        _ = system('cls')
def begin():
    clear()
    print("********Made By AnoDude**********")
    print(">>Start : 1")
    print(">>Exit  : 2")
    a=input()
    if a=='1':
        startone()
    elif a=='2':
        qui()
    else:
        retry()
def qui():
    quit
def retry():
    clear()
    print("Incorrect input // press 'enter' to retry")
    a=input()
    begin()
def startone():
    clear()
    o=13
    g="_"
    p="O"
    s="."
    wl="|"
    g1=g
    g2=24*g
    s1=s*o
    s2=s1
    s3=(2*o)*s
    print(wl+s3+wl)
    print(wl+s1+s2+wl)
    print(wl+g1+p+g2+wl)
    def start(s3,o,g,p,s,wl,g1,g2,s1,s2):
        i=1
        j=24
        def mov(s3,o,g,p,s,wl,g1,g2,s1,s2,i,j):
            def right(s3,o,g,p,s,wl,g1,g2,s1,s2,i,j):
                i=i+1
                j=j-1
                if j<=0:
                    j=0
                    i=25
                g1=i*g
                g2=j*g
                print(wl+s3+wl)
                print(wl+s1+s2+wl)
                print(wl+g1+p+g2+wl)
                mov(s3,o,g,p,s,wl,g1,g2,s1,s2,i,j)
            def left(s3,o,g,p,s,wl,g1,g2,s1,s2,i,j):
                i=i-1
                j=j+1
                if i<=0:
                    i=0
                    j=25
                g1=i*g
                g2=j*g
                print(wl+s3+wl)
                print(wl+s1+s2+wl)
                print(wl+g1+p+g2+wl)
                mov(s3,o,g,p,s,wl,g1,g2,s1,s2,i,j)
            def jmp(s3,o,g,p,s,wl,g1,g2,s1,s2,i,j):
                s1=i*s
                s2=j*s
                g1=o*g
                g2=g1
                print(wl+s3+wl)
                print(wl+s1+p+s2+wl)
                print(wl+g1+g2+wl)
                slep()
                s1=o*s
                s2=s1
                g1=i*g
                g2=j*g
                clear()
                print(wl+s3+wl)
                print(wl+s1+s2+wl)
                print(wl+g1+p+g2+wl)
                mov(s3,o,g,p,s,wl,g1,g2,s1,s2,i,j)
            def rjmp(s3,o,g,p,s,wl,g1,g2,s1,s2,i,j):
                print(wl+s3+wl)
                print(wl+s1+s2+wl)
                print(wl+g1+p+g2+wl)
                slep()
                i=i+1
                j=j-1
                if j<=0:
                    j=0
                    i=25
                s1=i*s
                s2=j*s
                g1=o*g
                g2=g1
                clear()
                print(wl+s3+wl)
                print(wl+s1+p+s2+wl)
                print(wl+g1+g2+wl)
                slep()
                i=i+1
                j=j-1
                if j<=0:
                    j=0
                    i=25
                g1=i*g
                g2=j*g
                s1=o*s
                s2=s1
                clear()
                print(wl+s3+wl)
                print(wl+s1+s2+wl)
                print(wl+g1+p+g2+wl)
                mov(s3,o,g,p,s,wl,g1,g2,s1,s2,i,j)
            def ljmp(s3,o,g,p,s,wl,g1,g2,s1,s2,i,j):
                print(wl+s3+wl)
                print(wl+s1+s2+wl)
                print(wl+g1+p+g2+wl)
                slep()
                clear()
                j=j+1
                i=i-1
                if i<=0:
                    i=0
                    j=25
                s1=i*s
                s2=j*s
                g1=o*g
                g2=g1
                print(wl+s3+wl)
                print(wl+s1+p+s2+wl)
                print(wl+g1+g2+wl)
                slep()
                clear()
                j=j+1
                i=i-1
                if i<=0:
                    i=0
                    j=25
                g1=i*g
                g2=j*g
                s1=o*s
                s2=s1
                print(wl+s3+wl)
                print(wl+s1+s2+wl)
                print(wl+g1+p+g2+wl)
                mov(s3,o,g,p,s,wl,g1,g2,s1,s2,i,j)
            m="/"
            m=input()
            if m=='r':
                clear()
                right(s3,o,g,p,s,wl,g1,g2,s1,s2,i,j)
            elif m=='l':
                clear()
                left(s3,o,g,p,s,wl,g1,g2,s1,s2,i,j)
            elif m=='j':
                clear()
                jmp(s3,o,g,p,s,wl,g1,g2,s1,s2,i,j)
            elif m=='rj':
                clear()
                rjmp(s3,o,g,p,s,wl,g1,g2,s1,s2,i,j)
            elif m=='lj':
                clear()
                ljmp(s3,o,g,p,s,wl,g1,g2,s1,s2,i,j)
            elif m=='exit':
                qui()
            else:
                mov(s3,o,g,p,s,wl,g1,g2,s1,s2,i,j)
            
        mov(s3,o,g,p,s,wl,g1,g2,s1,s2,i,j)
    start(s3,o,g,p,s,wl,g1,g2,s1,s2)
                            
begin()
