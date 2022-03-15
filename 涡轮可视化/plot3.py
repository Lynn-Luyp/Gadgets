import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import imageio
import os 
os.chdir('E:\zll\\figure')

def circle(a,b,r):
    theta = np.arange(0, 2*np.pi, 0.01)
    x = a + r * np.cos(theta)
    y = b + r * np.sin(theta)
    return x,y

def create_gif(image_list, gif_name, duration=0.35):
    frames = []
    for image_name in image_list:
        frames.append(imageio.imread(image_name))
    imageio.mimsave(gif_name, frames, 'GIF', duration=duration)
    return

def main():
    image_list = ['fig'+str(x)+'.png' for x in range(len(tmp))]
    gif_name = 'circle.gif'
    duration = 0.01
    create_gif(image_list, gif_name, duration)


def circle_point(angle):
    o1_x = 85*np.cos((180-angle)/180*np.pi)
    o1_y = 85*np.sin((180-angle)/180*np.pi)
    o2_x = 85*np.cos(-angle/180*np.pi)
    o2_y = 85*np.sin(-angle/180*np.pi)
    return (o1_x,o1_y,o2_x,o2_y)


def plot_circle(angle,curve,center,blade):
    if blade == 1:
        theta = np.arange((-angle/180)*np.pi, ((curve-angle)/180)*np.pi, 0.01)
        x = center[0] + 100 * np.cos(theta)
        y = center[1] + 100 * np.sin(theta)
    elif blade == 2:
        theta = np.arange((1-angle/180)*np.pi, (1-angle/180+curve/180)*np.pi, 0.01)
        x = center[2] + 100 * np.cos(theta)
        y = center[3] + 100 * np.sin(theta)
    return (x,y)

def auto(tmp):
    for count in range(len(tmp)):
        fig,ax = plt.subplots()
        x,y = circle(0,0,200)
        ax.plot(x,y)
        center = circle_point(tmp[count][0])
        x,y = plot_circle(tmp[count][0],tmp[count][1],center,1)
        ax.plot(x,y)
        x,y = plot_circle(tmp[count][2],tmp[count][3],center,2)
        ax.plot(x,y)
        ax.axis('equal')
        ax.set_xlim([-600,400])
        ax.get_yaxis().set_visible(False)
        ax.get_xaxis().set_visible(False)
        ax.spines['left'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['top'].set_visible(False)
        ax.spines['bottom'].set_visible(False)
        ax.text(-360,200,'$U$',fontsize = 15)
        ax.arrow(-400,160,120,0,length_includes_head = True,width = 4, head_width = 20,head_length = 20,fc = 'k',ec = 'k')
        ax.arrow(-400,50,120,0,length_includes_head = True,width = 4, head_width = 20,head_length = 20,fc = 'k',ec = 'k')
        ax.arrow(-400,-60,120,0,length_includes_head = True,width = 4, head_width = 20,head_length = 20,fc = 'k',ec = 'k')
        ax.arrow(-400,-170,120,0,length_includes_head = True,width = 4, head_width = 20,head_length = 20,fc = 'k',ec = 'k')
        plt.savefig(r'E:\zll\figure\fig{}.png'.format(count))
        
def calculate_curve(angle):
    if angle < 90:
        curve1 = angle + 90
        curve2 = -angle + 90
    elif (90 <= angle) and (angle < 270):
        curve1 = -angle + 270
        curve2 = angle - 90
    elif (270 <= angle) and (angle <= 360):
        curve1 = angle - 270
        curve2 = -angle + 450
    return (angle,curve1,angle,curve2)


tmp = []
for _ in np.arange(0,360,1):
    tmp.append(calculate_curve(_))
auto(tmp)
main()




