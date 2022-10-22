#!/usr/bin/env python
# coding: utf-8

# In[1]:


days = 10000 // 86400
h = 10000//3600
min = 10000 % 3600 // 60
sec = 10000 % 60
print(f" {days}:{h}:{min}:{sec}")


# In[2]:


print("Чтобы закончить вычисления введите STOP")
while True:
    sign = input('Введите знак (+;-;/; *):')
    if sign.lower() == "stop":
        break
    elif sign in '+-/*':
        a = float(input("Введите число 1: "))
        b = float(input("Введите число 2: "))
        if sign == "+":
            print("Итог: ", a+b)
        elif sign == "-":
            print("Итог: ", a-b)
        elif sign == "*":
            print("Итог: ",a*b)
        elif sign == "/":
            print("Итог: ", a/b)
        else:
            print("Вы ввели неверный знак!")
            


# In[3]:


print(str(input()) + "$" + str(input()))


# In[4]:


print(str(input()), str(input()), sep = "$")


# In[5]:


name = input("Введите имя:")
age = int(input("Введите возраст:"))
for i in range(age):
    print(f"С днем рождения, {name}")


# In[ ]:




