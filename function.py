
#基于一注真题_建筑结构[2001-6]的问题设计



def Σx(Mx,Ix,b,h,bf,hf):  #此函数只负责计算，不负责输入
    y= (b*h*h+(bf-b)*hf*hf)/(b*h+(bf-b)*hf)/2   
    Σx=Mx*y/Ix
    print(Σx)
    
#从这里开始往下是主函数

    
Ix = int(input())
Mx = int(input())
b =  int(input())  #腹板宽度

h =  int(input())  #总高度

bf = int(input()) #缘板宽度

hf = int(input()) #翼缘板高度

Σx(Mx,Ix,b,h,bf,hf)