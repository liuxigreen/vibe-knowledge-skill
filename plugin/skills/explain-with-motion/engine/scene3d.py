"""Small stylized software 3D scene toolkit. Faces use painter sorting, not a depth buffer."""
import math
import numpy as np
from PIL import Image, ImageDraw

def unit(v):
    v=np.asarray(v,dtype=float); n=np.linalg.norm(v)
    return v/n if n else v

class Camera:
    def __init__(self,eye,target,width,height,fov=45):
        if not (width>0 and height>0 and 1<fov<179):raise ValueError('positive dimensions and vertical fov in (1,179) required')
        self.eye=np.array(eye,dtype=float); self.width=width; self.height=height
        target=np.array(target,dtype=float)
        if self.eye.shape!=(3,) or target.shape!=(3,) or not np.isfinite([self.eye,target]).all() or np.linalg.norm(target-self.eye)<1e-9:raise ValueError('distinct finite 3D eye and target required')
        self.forward=unit(target-self.eye)
        world_up=[0,1,0] if abs(self.forward[2])>.98 else [0,0,1]
        self.right=unit(np.cross(self.forward,world_up)); self.up=unit(np.cross(self.right,self.forward)); self.focal=height/(2*math.tan(math.radians(fov)/2))
    def project_many(self,points):
        v=np.asarray(points,dtype=float)-self.eye
        z=v@self.forward
        with np.errstate(divide='ignore',invalid='ignore'):
            return np.stack((self.width/2+self.focal*(v@self.right)/z,self.height/2-self.focal*(v@self.up)/z,z),axis=-1)
    def project(self,point):
        v=np.asarray(point)-self.eye; z=float(v@self.forward)
        if z<=0.01:return None
        return (self.width/2+self.focal*float(v@self.right)/z,self.height/2-self.focal*float(v@self.up)/z,z)

class Material:
    def __init__(self,color,roughness=0,ambient=.48):
        self.color=np.array(color,dtype=float); self.roughness=roughness;self.ambient=ambient
        if self.color.shape!=(3,) or not np.isfinite(self.color).all() or np.any(self.color<0) or np.any(self.color>255) or not 0<=roughness<=1 or not 0<=ambient<=1:raise ValueError('RGB in 0..255 and roughness/ambient in 0..1 required')
    def shade(self,normal,light=(-.4,-.5,1)):
        n=np.asarray(normal,dtype=float); length=np.linalg.norm(n,axis=-1,keepdims=True)
        n=np.divide(n,length,out=np.zeros_like(n),where=length!=0)
        diffuse=np.maximum(0,n@unit(light))
        # Roughness softly lifts shadows in this illustrative Lambert approximation.
        k=self.ambient+(1-self.ambient)*((1-self.roughness)*diffuse+self.roughness*(.25+.75*diffuse))
        result=np.clip(self.color*np.expand_dims(k,-1),0,255).astype(np.uint8)
        return tuple(int(x) for x in result) if result.ndim==1 else result

class Scene:
    def __init__(self,camera,background=(223,235,230)):
        self.camera=camera;self.background=background;self.faces=[]
    def polygon(self,points,material):
        p=np.asarray(points,dtype=float); q=[self.camera.project(v) for v in p]
        if any(v is None for v in q):return
        normal=np.cross(p[1]-p[0],p[2]-p[0]);self.faces.append((sum(v[2] for v in q)/len(q),[(v[0],v[1]) for v in q],material.shade(normal)))
    def box(self,center,size,material):
        x,y,z=center; a,b,c=np.array(size)/2
        v=[(x-a,y-b,z-c),(x+a,y-b,z-c),(x+a,y+b,z-c),(x-a,y+b,z-c),(x-a,y-b,z+c),(x+a,y-b,z+c),(x+a,y+b,z+c),(x-a,y+b,z+c)]
        for ids in [(0,3,2,1),(0,1,5,4),(1,2,6,5),(2,3,7,6),(3,0,4,7),(4,5,6,7)]:self.polygon([v[i] for i in ids],material)
    def heightfield(self,heights,origin,step,material):
        for j in range(len(heights)-1):
            for i in range(len(heights[j])-1):
                x=origin[0]+i*step;y=origin[1]+j*step
                self.polygon([(x,y,heights[j][i]),(x+step,y,heights[j][i+1]),(x+step,y+step,heights[j+1][i+1]),(x,y+step,heights[j+1][i])],material)
    def limb(self,a,b,width,material):
        # Segmented blocks retain legible joints with a deliberately stylized silhouette.
        a=np.asarray(a);b=np.asarray(b)
        for t in np.linspace(0,1,5):self.box(a*(1-t)+b*t,(width,width,width),material)
    def character(self,x,y,shirt,skin,hand,face=1):
        # Contact ellipse is an artistic approximation, not a projected physical shadow.
        self.polygon([(x+.3*math.cos(a),y+.18*math.sin(a),.003) for a in np.linspace(0,math.tau,16)],Material((62,79,69),ambient=1))
        self.box((x,y,.85),(.40,.27,.58),shirt);self.box((x,y,1.32),(.32,.30,.34),skin)
        dark=Material((57,69,76));self.box((x-.12,y,.24),(.14,.19,.48),dark);self.box((x+.12,y,.24),(.14,.19,.48),dark)
        self.box((x-.12,y-.055,.06),(.17,.31,.12),dark);self.box((x+.12,y-.055,.06),(.17,.31,.12),dark)
        shoulder=(x+face*.22,y,1.02); elbow=((shoulder[0]+hand[0])/2,y,.83)
        self.limb(shoulder,elbow,.13,shirt);self.limb(elbow,hand,.12,skin)
    def render(self):
        im=Image.new('RGB',(self.camera.width,self.camera.height),self.background);d=ImageDraw.Draw(im)
        for _,poly,color in sorted(self.faces,reverse=True,key=lambda item:item[0]):d.polygon(poly,fill=color)
        return im
