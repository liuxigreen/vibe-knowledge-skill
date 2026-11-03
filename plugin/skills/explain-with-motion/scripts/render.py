"""Render a local Python scene by explicit time; no network or package installation.
Scene contract: configure(config), frame(t)->PIL RGB image. Project config is JSON.
"""
import argparse,importlib.util,json,math,subprocess,sys,shutil
from pathlib import Path

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('project',type=Path);p.add_argument('--preview',action='store_true');p.add_argument('--font',type=Path);p.add_argument('--start',type=float,default=0);p.add_argument('--end',type=float);a=p.parse_args()
    try:
        from PIL import Image,ImageDraw
        root=a.project.resolve();cfg=json.loads((root/'project.json').read_text(encoding='utf-8-sig'));r=cfg['render'];duration=float(cfg['duration']);fps=float(cfg['fps']);w,h=int(r['width']),int(r['height'])
        if not all(math.isfinite(v) and v>0 for v in [duration,fps,w,h]):raise ValueError('invalid video dimensions, duration or fps')
        end=duration if a.end is None else a.end
        if not math.isfinite(a.start) or not math.isfinite(end) or not 0<=a.start<end<=duration:raise ValueError('invalid start/end')
        count=round((end-a.start)*fps)
        if count<1 or abs(count/fps-(end-a.start))>1e-6:raise ValueError('clip interval must contain a whole number of frames')
        scene=(root/r['scene']).resolve()
        if not scene.is_relative_to(root) or not scene.is_file():raise ValueError('scene must be an existing file inside the project')
        font=a.font or (root/r['font'] if r.get('font') else None)
        if font and not font.is_file():raise ValueError('font file not found')
        spec=importlib.util.spec_from_file_location('video_scene',scene);module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
        module.configure({'width':w,'height':h,'font':str(font.resolve()) if font else None,'seed':r.get('seed',42)})
        out=root/'out';out.mkdir(exist_ok=True)
        def picture(t):
            im=module.frame(t)
            if im.size!=(w,h):raise ValueError(f'scene returned {im.size}, expected {(w,h)}')
            return im.convert('RGB')
        if a.preview:
            times=r.get('preview_times',[duration*v for v in [.1,.3,.5,.7,.9]])
            if not times or not all(isinstance(t,(int,float)) and math.isfinite(t) and 0<=t<duration for t in times):raise ValueError('invalid preview times')
            thumbw=640;thumbh=round(h*thumbw/w);sheet=Image.new('RGB',(thumbw*2,(thumbh+26)*math.ceil(len(times)/2)),(16,21,27))
            for i,t in enumerate(times):
                im=picture(t);im.save(out/f'frame-{t:06.2f}.png');x=i%2*thumbw;y=i//2*(thumbh+26);sheet.paste(im.resize((thumbw,thumbh)),(x,y+26));ImageDraw.Draw(sheet).text((x+8,y+5),f'{t:.3f} s',fill='white')
            sheet.save(out/'preview.jpg',quality=92);print(out/'preview.jpg');return 0
        if not shutil.which('ffmpeg'):raise ValueError('ffmpeg missing from PATH')
        if w%2 or h%2:raise ValueError('H264 yuv420p requires even width and height')
        output=out/('film.mp4' if a.start==0 and end==duration else 'clip.mp4')
        command=['ffmpeg','-v','error','-y','-f','rawvideo','-pix_fmt','rgb24','-s',f'{w}x{h}','-r',str(fps),'-i','pipe:0','-an','-c:v','libx264','-preset','fast','-crf','18','-pix_fmt','yuv420p','-movflags','+faststart',str(output)]
        proc=subprocess.Popen(command,stdin=subprocess.PIPE)
        try:
            for n in range(count):proc.stdin.write(picture(a.start+n/fps).tobytes())
            proc.stdin.close();code=proc.wait()
            if code:raise RuntimeError(f'ffmpeg exited {code}')
        finally:
            if proc.poll() is None:proc.kill();proc.wait()
        print(output);return 0
    except (OSError,ValueError,KeyError,TypeError,ImportError,RuntimeError) as e:
        print(f'NOT RENDERED: {e}',file=sys.stderr);return 2
if __name__=='__main__':sys.exit(main())
