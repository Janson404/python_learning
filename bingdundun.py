#!/usr/bin/python
# # -*- coding: utf-8 -*
# 项目实现：该项目运用了 turtle 包进行绘制，
# 该包有很强大的功能，主要帮助用户进行绘图等功能，绘制图很方便，
# @author Janson
# time :2022.2.12
import turtle
# 绘制图像的名称 
turtle.title('我爱冰墩墩')

# 绘画速度 
turtle.speed(12) 

 
# 绘制左手外
# 提起画笔
turtle.penup()
# 把笔放在指定的初始位置
turtle.setpos(177,112)
turtle.pen(pensize=3,pencolor='lightgray')
turtle.fillcolor("white")
# 图像颜色填充开始
turtle.begin_fill()
turtle.pendown()
# 设置画笔当前朝向的角度
turtle.setheading(80)
turtle.circle(-45, 200)
turtle.circle(-300, 23)
turtle.end_fill()

# 绘制左手内
turtle.penup()
turtle.setpos(182, 95)
turtle.pen(pensize=1,pencolor='black')
turtle.fillcolor("black")
turtle.begin_fill()
turtle.setheading(95)
turtle.pendown()
turtle.circle(-37, 160)
turtle.circle(-20, 50)
turtle.circle(-200, 30)
turtle.end_fill() 

# 绘制轮廓
# 绘制头顶
turtle.penup()
turtle.setpos(-73, 230)
turtle.pen(pensize=3,pencolor='lightgray')
turtle.fillcolor("white")
turtle.begin_fill()
turtle.pendown()
turtle.setheading(20)
turtle.circle(-250, 35)

# 绘制左耳
turtle.setheading(50)
turtle.circle(-42, 180)

# 绘制左侧
turtle.setheading(-50)
turtle.circle(-190, 30)
turtle.circle(-320, 45)

# 绘制左腿
turtle.circle(120, 30)
turtle.circle(200, 12)
turtle.circle(-18, 85)
turtle.circle(-180, 23)
turtle.circle(-20, 110)
turtle.circle(15, 115)
turtle.circle(100, 12)
# 绘制右腿
turtle.circle(15, 120)
turtle.circle(-15, 110)
turtle.circle(-150, 30)
turtle.circle(-15, 70)
turtle.circle(-150, 10)
turtle.circle(200, 35)
turtle.circle(-150, 20)
# 绘制右手
turtle.setheading(-120)
turtle.circle(50, 30)
turtle.circle(-35, 200)
turtle.circle(-300, 23)
# 绘制右侧
turtle.setheading(86)
turtle.circle(-300, 26)
# 绘制右耳
turtle.setheading(122)
turtle.circle(-53, 160)
turtle.end_fill()
 
# 绘制右耳内
turtle.penup()
turtle.setpos(-130, 180)
turtle.pen(pensize=1,pencolor='black')
turtle.fillcolor("black")
turtle.begin_fill()
turtle.pendown()
turtle.setheading(120)
turtle.circle(-28, 160)
turtle.setheading(210)
turtle.circle(150, 20)
turtle.end_fill()
 
# 绘制左耳内
turtle.penup()
turtle.setpos(90, 230)
turtle.setheading(40)
turtle.begin_fill()
turtle.pendown()
turtle.circle(-30, 170)
turtle.setheading(125)
turtle.circle(150, 23)
turtle.end_fill()
 
# 绘制右手内
turtle.penup()
turtle.setpos(-180, -55)
turtle.fillcolor("black")
turtle.begin_fill()
turtle.setheading(-120)
turtle.pendown()
turtle.circle(50, 30)
turtle.circle(-27, 200)
turtle.circle(-300, 20)
turtle.setheading(-90)
turtle.circle(300, 14)
turtle.end_fill()
 
# 绘制左腿内
turtle.penup()
turtle.setpos(108, -168)
turtle.fillcolor("black")
turtle.begin_fill()
turtle.pendown()
turtle.setheading(-115)
turtle.circle(110, 15)
turtle.circle(200, 10)
turtle.circle(-18, 80)
turtle.circle(-180, 13)
turtle.circle(-20, 90)
turtle.circle(15, 60)
turtle.setheading(42)
turtle.circle(-200, 29)
turtle.end_fill()
# 绘制右腿内
turtle.penup()
turtle.setpos(-38, -210)
turtle.fillcolor("black")
turtle.begin_fill()
turtle.pendown()
turtle.setheading(-155)
turtle.circle(15, 100)
turtle.circle(-10, 110)
turtle.circle(-100, 30)
turtle.circle(-15, 65)
turtle.circle(-100, 10)
turtle.circle(200, 15)
turtle.setheading(-14)
turtle.circle(-200, 27)
turtle.end_fill()
 
# 绘制右眼
# 绘制眼圈
turtle.penup()
turtle.setpos(-64, 120)
turtle.begin_fill()
turtle.pendown()
turtle.setheading(40)
turtle.circle(-35, 152)
turtle.circle(-100, 50)
turtle.circle(-35, 130)
turtle.circle(-100, 50)
turtle.end_fill()
# 绘制眼珠
turtle.penup()
turtle.setpos(-47, 55)
turtle.fillcolor("white")
turtle.begin_fill()
turtle.pendown()
turtle.setheading(0)
turtle.circle(25, 360)
turtle.end_fill()
turtle.penup()
turtle.setpos(-45, 62)
turtle.pencolor("darkslategray")
turtle.fillcolor("darkslategray")
turtle.begin_fill()
turtle.pendown()
turtle.setheading(0)
turtle.circle(19, 360)
turtle.end_fill()
turtle.penup()
turtle.setpos(-45, 68)
turtle.fillcolor("black")
turtle.begin_fill()
turtle.pendown()
turtle.setheading(0)
turtle.circle(10, 360)
turtle.end_fill()
turtle.penup()
turtle.setpos(-47, 86)
turtle.pencolor("white")
turtle.fillcolor("white")
turtle.begin_fill()
turtle.pendown()
turtle.setheading(0)
turtle.circle(5, 360)
turtle.end_fill()
 
# 绘制左眼
# 绘制眼圈
turtle.penup()
turtle.setpos(51, 82)
turtle.fillcolor("black")
turtle.begin_fill()
turtle.pendown()
turtle.setheading(120)
turtle.circle(-32, 152)
turtle.circle(-100, 55)
turtle.circle(-25, 120)
turtle.circle(-120, 45)
turtle.end_fill()
# 绘制眼珠
turtle.penup()
turtle.setpos(79, 60)
turtle.fillcolor("white")
turtle.begin_fill()
turtle.pendown()
turtle.setheading(0)
turtle.circle(24, 360)
turtle.end_fill()
turtle.penup()
turtle.setpos(79, 64)
turtle.pencolor("darkslategray")
turtle.fillcolor("darkslategray")
turtle.begin_fill()
turtle.pendown()
turtle.setheading(0)
turtle.circle(19, 360)
turtle.end_fill()
turtle.penup()
turtle.setpos(79, 70)
turtle.fillcolor("black")
turtle.begin_fill()
turtle.pendown()
turtle.setheading(0)
turtle.circle(10, 360)
turtle.end_fill()
turtle.penup()
turtle.setpos(79, 88)
turtle.pencolor("white")
turtle.fillcolor("white")
turtle.begin_fill()
turtle.pendown()
turtle.setheading(0)
turtle.circle(5, 360)
turtle.end_fill()
 
# 绘制鼻子
turtle.penup()
turtle.setpos(37, 80)
turtle.fillcolor("black")
turtle.begin_fill()
turtle.pendown()
turtle.circle(-8, 130)
turtle.circle(-22, 100)
turtle.circle(-8, 130)
turtle.end_fill()
 
# 绘制嘴
turtle.penup()
turtle.setpos(-15, 48)
turtle.setheading(-36)
turtle.begin_fill()
turtle.pendown()
turtle.circle(60, 70)
turtle.setheading(-132)
turtle.circle(-45, 100)
turtle.end_fill()
 
# 绘制身体上彩虹圈
# 第一个
turtle.penup()
turtle.setpos(-120, 104)
turtle.pen(pensize=5,pencolor='greenyellow')
turtle.pendown()
turtle.setheading(60)
turtle.circle(-145, 136)
turtle.circle(-90, 83)
turtle.circle(-220, 30)
turtle.circle(-120, 100)

#第二个
turtle.penup()
turtle.setpos(-123, 108)
turtle.pen(pensize=5,pencolor='gold')
turtle.pendown()
turtle.setheading(60)
turtle.circle(-150, 136)
turtle.circle(-104, 86)
turtle.circle(-220, 30)
turtle.circle(-126, 102)

#第三个
turtle.penup()
turtle.setpos(-127, 112)
turtle.pen(pensize=5,pencolor='orangered')
turtle.pendown()
turtle.setheading(60)
turtle.circle(-155, 136)
turtle.circle(-116, 86)
turtle.circle(-220, 30)
turtle.circle(-134, 103)
#第四个
turtle.penup()
turtle.setpos(-131, 116)
turtle.pen(pensize=5,pencolor='slateblue')
turtle.pendown()
turtle.setheading(60)
turtle.circle(-160, 144)
turtle.circle(-120, 78)
turtle.circle(-242, 30)
turtle.circle(-135, 105)

#第五个
turtle.penup()
turtle.setpos(-135, 120)
turtle.pen(pensize=5,pencolor='cyan')
turtle.pendown()
turtle.setheading(60)
turtle.circle(-165, 150)
turtle.circle(-130, 78)
turtle.circle(-250, 30)
turtle.circle(-138, 105)

turtle.penup()
 
# 绘制爱心
turtle.penup()
turtle.setpos(220, 115)
turtle.pencolor("brown")
turtle.pensize(1)
turtle.fillcolor("brown")
turtle.begin_fill()
turtle.pendown()
turtle.setheading(36)
turtle.circle(-8, 180)
turtle.circle(-60, 24)
turtle.setheading(110)
turtle.circle(-60, 24)
turtle.circle(-8, 180)
turtle.end_fill()
 
# 绘制五环
# 第一个
turtle.penup()
turtle.setpos(16, -175)
turtle.pendown()
turtle.pencolor("green")
turtle.circle(6)

#第二个
turtle.penup()
turtle.setpos(2, -175)
turtle.pendown()
turtle.pencolor("lightgoldenrod")
turtle.circle(6)

#第三个
turtle.penup()
turtle.setpos(25, -170)
turtle.pendown()
turtle.pencolor("brown")
turtle.circle(6)

#第四个
turtle.penup()
turtle.setpos(10, -170)
turtle.pendown()
turtle.pencolor("black")
turtle.circle(6)

#第五个
turtle.penup()
turtle.setpos(-5, -170)
turtle.pendown()
turtle.pencolor("blue")
turtle.circle(6)
turtle.penup()

# 写字 ： BEIJING 2022
turtle.pencolor("red")
turtle.setpos(-16, -160)
turtle.write("BEIJING 2022", font=('Arial', 10, 'bold italic'))
turtle.hideturtle()
 
turtle.done()
 
 
 
 
 
