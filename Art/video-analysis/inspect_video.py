import sys, json
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent / '.analysis-tools'))
import cv2
from PIL import Image, ImageDraw

root = Path(__file__).parent
video = next(root.parent.glob('*.mp4'))
cap = cv2.VideoCapture(str(video))
fps = cap.get(cv2.CAP_PROP_FPS)
count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
duration = count / fps
print(json.dumps({'file':video.name,'fps':fps,'frames':count,'seconds':duration,'width':cap.get(3),'height':cap.get(4)}))
start = float(sys.argv[1]) if len(sys.argv) > 1 else 0
end = min(float(sys.argv[2]), duration) if len(sys.argv) > 2 else duration
step = float(sys.argv[3]) if len(sys.argv) > 3 else 4
thumb_w = int(sys.argv[4]) if len(sys.argv) > 4 else 480
frames = []
t = start
while t < end:
    cap.set(cv2.CAP_PROP_POS_MSEC, t * 1000)
    ok, frame = cap.read()
    if ok:
        im = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        im.thumbnail((thumb_w, thumb_w))
        frames.append((t,im))
    t += step
for offset in range(0,len(frames),16):
    batch = frames[offset:offset+16]
    cell_h = max(im.height for _,im in batch)+24
    sheet = Image.new('RGB',(thumb_w*4,cell_h*((len(batch)+3)//4)), '#141414')
    draw = ImageDraw.Draw(sheet)
    for i,(t,im) in enumerate(batch):
        x,y = (i%4)*thumb_w,(i//4)*cell_h
        sheet.paste(im,(x,y+24))
        draw.text((x+5,y+4),f'{int(t//60):02}:{t%60:05.2f}',fill='white')
    path = root / f'sheet_{start:g}_{step:g}_{offset//16:02}.jpg'
    sheet.save(path,quality=90)
    print(str(path))
cap.release()
