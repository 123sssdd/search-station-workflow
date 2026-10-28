from lib import *
d=D(2400,1500)
d.text(1200,78,"学习闭环 · 总架构（bot 角色与数据流）",52,800)
d.text(1200,124,"搜索 → 评估 → 沉淀 → Sketchmind manifest → Notion / GitHub",26)
# roles row
d.zone(40,160,2320,300,B,"【角色】")
roles=[("BrainStorm 01","牵头决策"),("Brainstorm 02","复核"),("优化规划师","方案"),("Memory","归档"),("Todos","待办"),("手绘风技术配图","画图")]
for i,(n,t) in enumerate(roles):
    x=80+i*378; d.box(x,250,340,170); d.text(x+170,320,n,28,700); d.text(x+170,370,t,24)
# pipeline
d.zone(40,500,2320,560,G,"【数据流】")
X=[80,640,1200,1760]; Wd=500
d.box(X[0],600,Wd,400); d.text(X[0]+250,655,"① 搜索 · Searcher",28,700)
d.lines(X[0]+40,715,["降级顺序：","Firecrawl 优先","→ SearXNG","→ RSSHub","小红书 / SkillHub：搜 skill"],23,anchor="start")
d.box(X[1],600,Wd,400); d.text(X[1]+250,655,"② 评估 · 质量评估",28,700)
d.lines(X[1]+250,730,["5 分制打分"],24); d.hl(X[1]+130,775,240,40); d.text(X[1]+250,805,"均分 ≥ 4.0 通过",24,700)
d.box(X[2],600,Wd,400); d.text(X[2]+250,655,"③ 沉淀",28,700)
d.lines(X[2]+250,730,["rounds/ 证据文件","+ lock"],24)
d.box(X[3],600,Wd,400); d.text(X[3]+250,655,"④ Sketchmind manifest",28,700)
d.lines(X[3]+250,730,["看板数据文件","manifest.json"],24)
for i in range(3): d.arrow([(X[i]+Wd,800),(X[i+1]-4,800)])
# outputs
d.zone(40,1100,2320,360,Y,"【落地】")
d.box(500,1190,620,220); d.text(810,1260,"Notion · 学习中枢",28,700); d.text(810,1310,"五库",24)
d.box(1300,1190,620,220); d.text(1610,1260,"GitHub 仓库",28,700); d.text(1610,1310,"search-station-workflow",24)
d.arrow([(2010,1000),(2010,1150),(810,1150),(810,1186)])
d.arrow([(2010,1150),(1610,1150),(1610,1186)])
d.text(2050,1140,"同步",22,anchor="start")
d.save("architecture")
