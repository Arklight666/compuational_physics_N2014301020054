# 第三次作业
## 摘要:
    作业L1 在屏幕上让你的英文名字水平移动起来
    作业L2 在80*80点阵上用字符拼出你想画的东西，并让它旋转起来，希望脑洞大开！（比如字符、火柴人、火箭等等）
## 背景：
    在课程主页上复习这两次课程的内容，初步掌握python和matplotlib的语法规则
## 正文
```python        
        print('To make my name roll you need input 18 firstly')
    a=int(input('input 18:'))
    for i in range(a):
        print (i*' '+'######                                                   ') 
        print (i*' '+'#     #                   #                              ') 
        print (i*' '+'#     #       ####     #######       ####       # ###### ') 
        print (i*' '+'#####       #     #       #        #     #      ##       ') 
        print (i*' '+'#          # # # #        #       # # # #       #        ') 
        print (i*' '+'#          #              #       #             #        ') 
        print (i*' '+'#           #####         ##       #####        #        ') 
        if i==a-1:
            break
        import time
        time.sleep(0.2)
        import os
        i=os.system('cls')
```       
### 作业2(选做未做）
## 结论
### 作业1运行结果
![截图1](https://github.com/Arklight666/compuational_physics_N2014301020054/blob/master/%E4%BD%9C%E4%B8%9A3.jpg)
![截图2](https://github.com/Arklight666/compuational_physics_N2014301020054/blob/master/%E4%BD%9C%E4%B8%9A3%E8%BF%90%E8%A1%8C%E7%BB%93%E6%9E%9C.jpg)
## 致谢
Thanks Ranfeng


