import sys
from pathlib import Path
from PIL import Image,ImageDraw,ImageFont,ImageFilter,ImageChops
import numpy as np
sys.path.insert(0,str(Path(__file__).resolve().parents[2]))
from engine.scene3d import Camera as SharedCamera, Material
import math,subprocess,json,sys

W,H=1280,720;FPS=30
ANCHOR=True
FONT={}
def configure(config):
    global FONT
    if (config['width'],config['height'])!=(1280,720):
        raise ValueError('This example is composed for 1280x720; recompose before changing size')
    if not config.get('font'):
        raise ValueError('Pass --font with a local CJK font file')
    FONT={n:ImageFont.truetype(config['font'],n) for n in [16,18,20,24,28,32,40,46]}
def smooth(v):v=np.clip(v,0,1);return v*v*(3-2*v)
def text(im,s,xy,n=28,c='#e7e1d5',anchor='la'):
    d=ImageDraw.Draw(im);d.text((xy[0]+2,xy[1]+2),s,font=FONT[n],fill='#080d12',anchor=anchor,stroke_width=2);d.text(xy,s,font=FONT[n],fill=c,anchor=anchor)
class Camera:
    """Keep this composition offset while sharing projection with the character example."""
    def __init__(self,eye,target,focal=1080):
        fov=math.degrees(2*math.atan(H/(2*focal)))
        self.shared=SharedCamera(eye,target,W,H,fov)
    def p(self,pts):
        q=self.shared.project_many(pts)[...,:2].copy()
        q[...,1]+=H*.05
        return q
    def depth(self,pts):return self.shared.project_many(pts)[...,2]

def glow(im,xy,r=10,col=(109,229,249),strength=1):
    if not ANCHOR:return
    x,y=xy;lay=Image.new('RGB',im.size);d=ImageDraw.Draw(lay);d.ellipse((x-r*2,y-r*2,x+r*2,y+r*2),fill=tuple(int(a*strength*.65) for a in col));lay=lay.filter(ImageFilter.GaussianBlur(r));im.paste(ImageChops.add(im,lay));d=ImageDraw.Draw(im);d.ellipse((x-r*.42,y-r*.42,x+r*.42,y+r*.42),fill=col)
def meshheight(x,y):
    ridge=np.abs(np.sin(x*.47+y*.21+.4*np.sin(y*.47))+.42*np.sin(y*.77-x*.19+.35*np.sin(x*.31)))
    rough=.12*np.sin(x*5.9+y*4.5)+.09*np.sin(x*10.1-y*7.2)
    hills=(.4+ridge**1.6)*1.6
    valley=np.exp(-((y-(.5*np.sin(x*.5)))**2)/3)
    return np.maximum(-.1,hills*(1-.88*valley)+rough*.45)
xs=np.linspace(-22,22,240);ys=np.linspace(-17,18,190);X,Y=np.meshgrid(xs,ys);Z=meshheight(X,Y)
terrain=np.stack([X,Y,Z],-1);gy,gx=np.gradient(Z,ys[1]-ys[0],xs[1]-xs[0]);norm=np.stack([-gx,-gy,np.ones_like(Z)],-1);norm/=np.linalg.norm(norm,axis=-1)[...,None]
light=np.array([-.7,-.3,.8]);light/=np.linalg.norm(light);shade=np.maximum(0,norm@light)
grain=np.sin(X*22+Y*15)*np.sin(Y*19-X*12)
terrain_material=Material((91,82,67),roughness=.15,ambient=.3)
colors=np.clip(terrain_material.shade(norm,light).astype(float)+grain[...,None]*np.array([3,3,2]),0,255).astype('uint8')

def poly(im,cam,pts,fill,outline=None,width=1):
    q=cam.p(pts);d=ImageDraw.Draw(im);d.polygon([tuple(p) for p in q],fill=fill)
    if outline:d.line([tuple(p) for p in q]+[tuple(q[0])],fill=outline,width=width)
def cube(im,cam,x,y,z,dx,dy,dz,color=(91,91,83),windows=False):
    p=np.array([[x,y,z],[x+dx,y,z],[x+dx,y+dy,z],[x,y+dy,z],[x,y,z+dz],[x+dx,y,z+dz],[x+dx,y+dy,z+dz],[x,y+dy,z+dz]])
    faces=[([0,1,5,4],.62),([1,2,6,5],.43),([2,3,7,6],.68),([3,0,4,7],.83),([4,5,6,7],1.12)]
    faces.sort(key=lambda f:np.mean(cam.depth(p[f[0]])),reverse=True)
    for idx,k in faces:poly(im,cam,p[idx],tuple(min(255,int(c*k)) for c in color))
    if windows:
        for j in range(1,int(dz/.45)):
            for i in range(1,4):
                zz=z+.15+j*.43;xx=x+dx*i/4
                poly(im,cam,[(xx-.06,y-.005,zz),(xx+.06,y-.005,zz),(xx+.06,y-.005,zz+.15),(xx-.06,y-.005,zz+.15)],(136,119,72) if (i+j)%4 else (50,66,67))
def pipe(im,cam,points,width=18,color=(47,79,89)):
    q=[tuple(p) for p in cam.p(points)];d=ImageDraw.Draw(im)
    for i in range(len(q)-1):
        a,b=q[i:i+2];d.line([a,b],fill=(13,22,27),width=width+7)
        for off,k in [(0,1),(-2,1.35),(-4,1.7)]:d.line([(a[0],a[1]+off),(b[0],b[1]+off)],fill=tuple(min(255,int(c*k)) for c in color),width=max(2,width-abs(off)*3))
    for x,y in q:d.ellipse((x-width*.55,y-width*.55,x+width*.55,y+width*.55),outline='#72898b',width=2)
def follow(points,p):
    points=np.array(points,float);lens=np.linalg.norm(np.diff(points,axis=0),axis=1);dist=float(np.clip(p,0,1))*sum(lens)
    for i,L in enumerate(lens):
        if dist<=L:return points[i]+(points[i+1]-points[i])*(dist/L)
        dist-=L
    return points[-1]
def watertrail(im,cam,points,p,width=4):
    dense=[follow(points,v) for v in np.linspace(max(0,p-.18),p,30)];q=cam.p(dense);d=ImageDraw.Draw(im)
    d.line([tuple(a) for a in q],fill='#65c9df',width=width);glow(im,q[-1],10)

def terrain_scene(t):
    cam=Camera((10-t*.3,-18+t*.55,18-t*.25),(-1+t*.5,1,0),1150+t*18)
    im=Image.new('RGB',(W,H),'#101412');q=cam.p(terrain)
    # Painter sorting by view depth preserves surface relief and silhouette.
    depths=cam.depth(terrain);order=np.argsort(-((depths[:-1,:-1]+depths[1:,1:])*.5).ravel());d=ImageDraw.Draw(im)
    ny,nx=Z.shape[0]-1,Z.shape[1]-1
    for k in order:
        iy,ix=divmod(int(k),nx);quad=[q[iy,ix],q[iy,ix+1],q[iy+1,ix+1],q[iy+1,ix]]
        if max(p[0] for p in quad)<0 or min(p[0] for p in quad)>W or max(p[1] for p in quad)<0 or min(p[1] for p in quad)>H:continue
        d.polygon([tuple(p) for p in quad],fill=tuple(colors[iy,ix]))
    # River hugs the valley; surface water is a distinct material.
    rr=[]
    for x in np.linspace(-15,7,150):
        y=.5*math.sin(x*.5);rr.append((x,y,float(meshheight(x,y))+.04))
    for i in range(len(rr)-1):
        x,y,z=rr[i];xx,yy,zz=rr[i+1];ww=.18+.05*math.sin(x*.73)
        poly(im,cam,[(x,y-ww,z),(xx,yy-ww,zz),(xx,yy+ww,zz),(x,y+ww,z)],(26,66,74))
    pts=cam.p(rr);d.line([tuple(p) for p in pts],fill='#397b88',width=3)
    # Physical treatment plant, not merely a text label.
    for j in range(3):
        x=3+j*.9;cube(im,cam,x,-.25,.3,.7,1.2,.15,(112,112,91));poly(im,cam,[(x+.08,-.18,.46),(x+.62,-.18,.46),(x+.62,.85,.46),(x+.08,.85,.46)],(47,106+8*j,118+8*j))
    cube(im,cam,5.9,.3,.3,1.2,1.0,.6,(137,131,107))
    p=smooth((t-.2)/2.6);point=follow(rr,p);watertrail(im,cam,rr,p,4)
    for name,pos in [('水源',(-8,1.1,1)),('处理设施',(5.3,1.8,1))]:
        xy=cam.p([pos])[0];text(im,name,xy,20,'#c8c7b1',anchor='mm')
    text(im,'拧开之前', (65,50),40);text(im,'水，先走过一段旅程。',(65,108),28,'#a6d4df')
    return im,tuple(cam.p([point])[0])

def city_scene(t):
    local=t-2.7;cam=Camera((12-local*.2,-19+local*.18,11-local*.18),(0,0,-.8),1110+local*20)
    im=Image.new('RGB',(W,H),'#111a20')
    # Cut ground slab: thickness, strata, street top, and volumetric buildings.
    cube(im,cam,-10,-1,-3,20,8,3,(85,68,48))
    for z in [-2.65,-2.15,-1.65,-1.1,-.6]:poly(im,cam,[(-10,-1.01,z),(10,-1.01,z),(10,-1.01,z+.08),(-10,-1.01,z+.08)],(57,48,38))
    poly(im,cam,[(-10,-1,.015),(10,-1,.015),(10,7,.015),(-10,7,.015)],(48,58,58))
    poly(im,cam,[(-10,1,.04),(10,1,.04),(10,2.4,.04),(-10,2.4,.04)],(26,34,39))
    for x in range(-10,10,2):poly(im,cam,[(x,1.66,.06),(x+.8,1.66,.06),(x+.8,1.74,.06),(x,1.74,.06)],(142,133,95))
    buildings=[(-8,4,1.2,1.4,2.5),(-5.6,4,1.5,1.3,3.3),(-2.5,4,1.4,1.8,2.6),(1,4,1.8,1.7,4),(4.4,4,1.6,1.5,3),(7,3.8,1.4,1.6,2)]
    for x,y,dx,dy,dz in sorted(buildings,key=lambda r:cam.depth([(r[0],r[1],0)])[0],reverse=True):cube(im,cam,x,y,0,dx,dy,dz,(104,114,111),True)
    # Plant basin array stays at left of the underground view.
    for j in range(3):
        x=-9+j*1.4;cube(im,cam,x,-.5,.04,1.1,1.2,.3,(126,128,115));poly(im,cam,[(x+.1,-.4,.35),(x+1,-.4,.35),(x+1,.6,.35),(x+.1,.6,.35)],(38,100+15*j,122+13*j))
    main=[(-9,-1.25,-1.5),(-4,-1.25,-1.5),(1,-1.25,-1.5),(6,-1.25,-1.5),(6,-1.25,0),(6,2.8,.15)]
    pipe(im,cam,main,22)
    for x in [-5,0,4]:pipe(im,cam,[(x,-1.25,-1.5),(x,-1.25,-2.5),(x+1.2,-1.25,-2.5)],11,(47,69,73))
    p=smooth((local-.3)/2.5);watertrail(im,cam,main,p,7)
    text(im,'处理之后，进入城市。',(65,52),32)
    xy=cam.p([(-7.2,-.3,.8)])[0];text(im,'净化 · 消毒',xy,20,'#d7d6bd',anchor='mm')
    xy=cam.p([(0,-1.4,-2.7)])[0];text(im,'地下管网',xy,24,'#a6d4df',anchor='mm')
    return im,tuple(cam.p([follow(main,p)])[0])

def metal_line(d,pts,width=46):
    d.line(pts,fill='#15242b',width=width+8,joint='curve')
    for k in range(width//2,0,-1):
        val=int(45+130*(1-k/(width/2))**.65)
        # Multiple nested strokes give cylinder body, bevel and highlight.
        d.line([(x-3,y-3) for x,y in pts],fill=(val,min(220,val+16),min(230,val+23)),width=max(2,k*2),joint='curve')

def cup_scene(t):
    local=t-5.7;im=Image.new('RGB',(W,H),'#17232a');d=ImageDraw.Draw(im)
    # Wall panels, grout, ledge and counter establish a close interior space.
    for y in range(-20,530,110):
        for x in range(-90,W,180):
            d.rectangle((x,y,x+178,y+108),fill=(31+((x//180+y//110)%3)*2,44+((x//180)%2)*2,48),outline='#27373c')
    d.polygon([(0,525),(1280,525),(1280,720),(0,720)],fill='#444b48')
    for i in range(14):d.line((0,560+i*17,1280,570+i*14),fill='#4b514c',width=1)
    # Sink, faucet base, volumetric gooseneck and control lever.
    d.ellipse((205,513,1135,730),fill='#141d21',outline='#677c80',width=6)
    d.ellipse((231,532,1107,714),fill='#24343a',outline='#3f565b',width=3)
    d.ellipse((290,483,395,523),fill='#192b32',outline='#9aafb2',width=4)
    metal_line(d,[(343,500),(343,328),(350,285),(373,256),(411,244),(684,244),(716,256),(734,280),(734,325)],44)
    d.ellipse((713,312,755,336),fill='#17262a',outline='#9fbec2',width=3)
    metal_line(d,[(365,399),(410,376),(453,377)],13)
    # Clear glass has rear wall, visible rim, interior water and front reflections.
    cx=734;top=480;bottom=656;rx=94;ry=24
    d.ellipse((cx-115,bottom-8,cx+120,bottom+35),fill='#18272d')
    d.polygon([(cx-rx,top),(cx-rx+17,bottom),(cx+rx-17,bottom),(cx+rx,top)],fill='#385963')
    d.ellipse((cx-rx+17,bottom-18,cx+rx-17,bottom+18),fill='#496d75',outline='#86adb3',width=2)
    waterlevel=bottom-18-98*smooth((local-1.15)/2.45)
    d.polygon([(cx-rx+15,waterlevel),(cx-rx+21,bottom-6),(cx+rx-21,bottom-6),(cx+rx-15,waterlevel)],fill='#398da6')
    d.ellipse((cx-rx+15,waterlevel-16,cx+rx-15,waterlevel+16),fill='#65b8cb',outline='#9cdce6',width=2)
    for i in range(3):
        r=((local*50+i*20)%72);d.ellipse((cx-r,waterlevel-r*.19,cx+r,waterlevel+r*.19),outline='#8fd0db',width=1)
    d.line([(cx-rx,top),(cx-rx+17,bottom)],fill='#a6d3d9',width=4);d.line([(cx+rx,top),(cx+rx-17,bottom)],fill='#82a9b4',width=3)
    d.ellipse((cx-rx,top-ry,cx+rx,top+ry),outline='#b0d0cf',width=4)
    d.line((cx-rx+15,top+23,cx-rx+27,bottom-20),fill='#8fbac3',width=5)
    # Water starts only after the marker has entered faucet from the same side.
    if local>.45:
        streamend=min(waterlevel,335+(local-.45)*430)
        d.line((cx,330,cx,streamend),fill='#397f96',width=15);d.line((cx-3,330,cx-3,streamend),fill='#b5ecf2',width=4)
        for j in range(7):
            yy=340+((local*220+j*33)%max(20,waterlevel-340));d.line((cx+4,yy,cx+4,yy+10),fill='#70c5df',width=2)
        glow(im,(cx,min(waterlevel,340+(local-.45)*250)),9)
    else:glow(im,(450+284*smooth(local/.45),264),10)
    text(im,'最后，来到你的杯子。',(65,55),32)
    if t>=7.5:text(im,'一滴水的旅程',(65,112),46,'#acdce5')
    marker=(cx,min(waterlevel,340+max(0,local-.45)*250)) if local>.45 else (450+284*float(smooth(local/.45)),264)
    return im,marker

def finish(im,t):
    # Shaped vignette keeps center legible, without erasing material detail.
    a=np.array(im).astype(float); yy,xx=np.mgrid[0:H,0:W];v=np.clip(1-.19*((xx-W*.52)/(W*.65))**2-.16*((yy-H*.5)/(H*.7))**2,.65,1)
    a*=v[...,None];im=Image.fromarray(np.uint8(np.clip(a,0,255)))
    text(im,'供水旅程示意 · 地形、距离与时间经压缩',(25,684),16,'#a0aba8')
    return im
def frame(t):
    global ANCHOR
    if t<2.65:im,_=terrain_scene(t)
    elif t<3.2:
        ANCHOR=False;a,pa=terrain_scene(t);b,pb=city_scene(t);ANCHOR=True
        u=float(smooth((t-2.65)/.55));im=Image.blend(a,b,u);glow(im,np.array(pa)*(1-u)+np.array(pb)*u,11)
    elif t<5.7:im,_=city_scene(t)
    elif t<6.25:
        ANCHOR=False;a,pa=city_scene(t);b,pb=cup_scene(t);ANCHOR=True
        u=float(smooth((t-5.7)/.55));im=Image.blend(a,b,u);glow(im,np.array(pa)*(1-u)+np.array(pb)*u,11)
    else:im,_=cup_scene(t)
    return finish(im,t)
