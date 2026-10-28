import random, math, json, cairosvg
INK="#142A49"; F="Noto Sans CJK SC"
B,G,Y,P,V="#EAF6FF","#EEF8E8","#FFF8D8","#FCEBF1","#F0EDFF"
class D:
    def __init__(s,W,H,seed=7):
        random.seed(seed); s.W,s.H=W,H; s.o=[]; s.ex=[]; s.n=0
    def _id(s): s.n+=1; return f"e{s.n}"
    def _base(s,t,x,y,w,h,**k):
        e=dict(id=s._id(),type=t,x=x,y=y,width=w,height=h,angle=0,strokeColor=INK,backgroundColor="transparent",
          fillStyle="solid",strokeWidth=2,strokeStyle="solid",roughness=1,opacity=100,groupIds=[],frameId=None,
          roundness=None,seed=random.randint(1,10**6),version=1,versionNonce=random.randint(1,10**6),isDeleted=False,
          boundElements=None,updated=1,link=None,locked=False); e.update(k); s.ex.append(e); return e
    def j(s,a=2.2): return random.uniform(-a,a)
    def lp(s,pts):
        d="M%.1f %.1f"%(pts[0][0]+s.j(),pts[0][1]+s.j())
        for (x0,y0),(x1,y1) in zip(pts,pts[1:]):
            d+=" Q%.1f %.1f %.1f %.1f"%((x0+x1)/2+s.j(3),(y0+y1)/2+s.j(3),x1+s.j(),y1+s.j())
        return d
    def box(s,x,y,w,h,fill="#FFFFFF",sw=3,r=18,dash=None):
        s.o.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}"/>')
        pts=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r),(x+r,y)]
        da=f' stroke-dasharray="{dash}"' if dash else ''
        for k in range(2):
            s.o.append(f'<path d="{s.lp(pts)}" fill="none" stroke="{INK}" stroke-width="{sw if k==0 else sw*.5}" stroke-linecap="round" opacity="{1 if k==0 else .55}"{da}/>')
        s._base("rectangle",x,y,w,h,backgroundColor=fill,strokeWidth=2 if sw<3.3 else 4,roundness={"type":3},strokeStyle="dashed" if dash else "solid")
    def text(s,x,y,t,size=26,weight=400,anchor="middle",color=INK):
        e=t.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")
        s.o.append(f'<text x="{x}" y="{y}" font-family="{F}" font-size="{size}" font-weight="{weight}" text-anchor="{anchor}" fill="{color}">{e}</text>')
        w=sum(size if ord(c)>255 else size*.55 for c in t); h=size*1.25
        ex={"middle":x-w/2,"start":x,"end":x-w}[anchor]
        s._base("text",ex,y-size,w,h,strokeColor=color,text=t,originalText=t,fontSize=size,fontFamily=2,
            textAlign={"middle":"center","start":"left","end":"right"}[anchor],verticalAlign="top",containerId=None,lineHeight=1.25,autoResize=True)
    def lines(s,x,y,arr,size=22,gap=1.45,**k):
        for i,t in enumerate(arr): s.text(x,y+i*size*gap,t,size,**k)
    def hl(s,x,y,w,h,c="#FFE27A"):
        s.o.append(f'<path d="M{x} {y+h*.2} L{x+w} {y} L{x+w+4} {y+h} L{x-3} {y+h*1.05}Z" fill="{c}" opacity=".7"/>')
        s._base("rectangle",x,y,w,h,strokeColor="transparent",backgroundColor=c,opacity=70)
    def arrow(s,pts,label=None,lx=None,ly=None,dash=None,sw=3.2):
        da=f' stroke-dasharray="{dash}"' if dash else ''
        s.o.append(f'<path d="{s.lp(pts)}" fill="none" stroke="{INK}" stroke-width="{sw}" stroke-linecap="round"{da}/>')
        (x0,y0),(x1,y1)=pts[-2],pts[-1]; a=math.atan2(y1-y0,x1-x0)
        for g in(-1,1): s.o.append(f'<path d="M{x1} {y1} L{x1-20*math.cos(a+g*.45):.1f} {y1-20*math.sin(a+g*.45):.1f}" stroke="{INK}" stroke-width="{sw}" stroke-linecap="round"/>')
        xs=[p[0] for p in pts]; ys=[p[1] for p in pts]
        s._base("arrow",pts[0][0],pts[0][1],max(xs)-min(xs),max(ys)-min(ys),points=[[px-pts[0][0],py-pts[0][1]] for px,py in pts],
            lastCommittedPoint=None,startBinding=None,endBinding=None,startArrowhead=None,endArrowhead="arrow",
            roundness={"type":2},strokeStyle="dashed" if dash else "solid")
        if label:
            tw=sum(20 if ord(c)>255 else 11 for c in label)+28
            s.o.append(f'<rect x="{lx-tw/2}" y="{ly-26}" width="{tw}" height="36" rx="8" fill="#FFFEF8"/>')
            s._base("rectangle",lx-tw/2,ly-26,tw,36,strokeColor="transparent",backgroundColor="#FFFEF8")
            s.text(lx,ly,label,20)
    def zone(s,x,y,w,h,fill,title):
        s.box(x,y,w,h,fill,sw=3.4,r=26); s.hl(x+24,y+20,sum(30 if ord(c)>255 else 16 for c in title)+16,40); s.text(x+32,y+52,title,30,700,"start")
    def save(s,name):
        svg=f'<svg xmlns="http://www.w3.org/2000/svg" width="{s.W}" height="{s.H}" viewBox="0 0 {s.W} {s.H}"><rect width="100%" height="100%" fill="#FFFEF8"/>'+"\n".join(s.o)+'</svg>'
        open(name+".svg","w").write(svg); cairosvg.svg2png(bytestring=svg.encode(),write_to=name+".png")
        json.dump({"type":"excalidraw","version":2,"source":"project-diagram-studio/gen","elements":s.ex,
          "appState":{"viewBackgroundColor":"#FFFEF8","gridSize":None},"files":{}},open(name+".excalidraw","w"),ensure_ascii=False)
