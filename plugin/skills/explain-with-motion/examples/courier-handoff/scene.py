import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[2]))
from engine.scene3d import Camera,Material,Scene
from PIL import ImageDraw,ImageFont

def configure(config):
    global W,H,FONT
    W,H=config['width'],config['height'];FONT=config.get('font')

def smooth(a,b,t):
    t=max(0,min(1,(t-a)/(b-a)));return t*t*(3-2*t)

def frame(t):
    cam=Camera((4,-7,4),(0,0,.75),W,H,38);s=Scene(cam,(221,235,229))
    ground=Material((171,196,173));s.box((0,0,-.12),(7,5,.24),ground);s.faces=[(float('inf'),p,c) for _,p,c in s.faces]
    stone=Material((211,202,179));s.box((1.8,.65,.8),(.18,.18,1.6),stone);s.box((1.8,-.65,.8),(.18,.18,1.6),stone);s.box((1.8,0,1.55),(.16,1.4,.12),stone)
    for y in [-.45,0,.45]:s.box((1.8,y,.56),(.07,.07,1.05),Material((86,111,105)))
    blue=Material((63,127,151));orange=Material((220,133,75));skin=Material((219,174,138));parcel=Material((194,151,97))
    cx=-.65; rx=.65
    transfer=smooth(3.5,5,t);bx=(cx+.32)*(1-transfer)+(.54)*transfer; by=-.03; bz=.85
    # Both hands approach the parcel before transfer, and remain in contact during it.
    reach=smooth(2.3,3.5,t); receiver_hand=(rx-.23+(bx+.18-(rx-.23))*reach,by,bz)
    courier_hand=(bx-.17,by,bz) if t<5 else (bx-.17-.48*smooth(5,5.7,t),by,bz)
    s.character(cx,0,blue,skin,courier_hand,1);s.character(rx,0,orange,skin,receiver_hand,-1)
    s.box((bx,by,bz),(.38,.34,.31),parcel);s.box((bx,by,bz+.16),(.08,.35,.01),Material((239,214,168)))
    im=s.render();d=ImageDraw.Draw(im)
    font=ImageFont.truetype(FONT,30) if FONT else ImageFont.load_default(size=30)
    d.text((45,35),'A small handoff',font=font,fill=(39,64,66))
    return im
