import json,os,sys,random,urllib.request as rq
U=os.environ.get("MAKEFUN_ENV_URL")or sys.exit(9)
def post(p,b):
 r=rq.Request(U+p,data=json.dumps(b).encode())
 with rq.urlopen(r)as f:return json.load(f)
KN=[-33,-31,-18,-14,14,18,31,33];K8=[-17,-16,-15,-1,1,15,16,17]
BD=[-17,-15,15,17];RD=[-16,-1,1,16];QD=BD+RD
PW=[0,0,1,1,2,4,0]
S="EEEEEEEEQVMQMUICDFHIMLHCCGFGHGGBAEEGGFFBBEEDEEICAECBCHJBEEEEEEEEEEEEEEEE[[YVWUY]QQOMLKOOIHGEEEGGGFEDDDEEEFDEEEEDGFFFGEEDEEEEEEEE0:A?M9C7<@NIHMFC?MIMOUNKDGGKIMGHCEGGIGGDBDGFGGHCA?CEEGCC8C>ACACB>@CAAA=9BDBEDBB?BCFFEDC@CEHHHGFCCDGHGGECBEEGFECB@CDEECB?A?BCBC?=AE;AB@FDBGCCIMG?CIKJIKIEEEGKIIFEDGGHIGFEEGGGGIGFEGGEFGIEAECCCC@CCCCDDDCBDEFCECECEDEEEFEEEFGFGFEEDEGGFFEDCEFFGEDCCCDEEDCABDBEDCECIJIKMFIKIILMOMHKEGHIGKMGBCFHHIDCABCEFDFB?BCCEEEA?CCDEGD<CCEGGFABGFGGGGFEGGGGEEFEFFFEEEEEEEEEGEEEEEFFFFFEEEEEGEFEEEFFEFFEEEEEFGGEAEIGMKKKB@EECLILCCFFILKLAACCEGEEDBDDEEEECECEEEGEADGEFGEEECDFCBA?DHHIIGFGCGIJLHIECFFKKIGFEHHKLJLICIGKIIJHCAGFFGFEBBACCBAAAAB?EAC@=HGC>AEGIECDDE@ADHECCFHBCCCAABCA?EA@??A?CCB??ACAEFD=?CFFCIGABCA><ACCCGECCGGGGJHGFGHGGKKGDHHIHIHECEGHIHFCCEGGHGFDACEGGEEC?ACCACB?"
VM=[0,82,337,365,477,1025,0];VE=[0,94,281,297,512,936,0]
MG=[0]*1920;EG=[0]*1920
for _i,_c in enumerate(S):
 _v=(ord(_c)-69)*8;_t=_i//128+1;_j=_i%128;_g=_j//64;_r=(_j%64)//8;_f=_j%8;_b=(VM,VE)[_g][_t]+_v;_a=(MG,EG)[_g]
 _a[_t*128+_r*16+_f]=_b;_a[(_t+8)*128+(7-_r)*16+_f]=-_b
CAST=[(1,116,118,119,(117,118),(116,117,118),0),(2,116,114,112,(113,114,115),(116,115,114),0),(4,4,6,7,(5,6),(4,5,6),1),(8,4,2,0,(1,2,3),(4,3,2),1)]
_R=random.Random(20261117)
Z=[[_R.getrandbits(64)for _ in range(128)]for _ in range(15)]
ZS=_R.getrandbits(64);ZC=[_R.getrandbits(64)for _ in range(16)];ZE=[_R.getrandbits(64)for _ in range(128)]
B=[0]*128;SD=0;CS=0;EP=-1;HF=0;HK=0;KG=[116,4];MNP=[0,0];PL=[set(),set()]
ST=[];TT={};ND=[0];LIM=[60000]
KL=[[0,0]for _ in range(128)]
SM=[0];SE=[0];PH=[0]
class TO(Exception):pass
def inc():
 ND[0]+=1
 if (ND[0]&511)==0 and ND[0]>LIM[0]:raise TO()
def at(s,by):
 pc=8*by;b=B
 for d in((15,17)if by==0 else(-15,-17)):
  t=s+d
  if not t&0x88 and b[t]==pc+1:return 1
 for d in KN:
  t=s+d
  if not t&0x88 and b[t]==pc+2:return 1
 for d in K8:
  t=s+d
  if not t&0x88 and b[t]==pc+6:return 1
 for ds,ty in((BD,3),(RD,4)):
  for d in ds:
   t=s+d
   while not t&0x88:
    p=b[t]
    if p:
     if p==pc+ty or p==pc+5:return 1
     break
    t+=d
 return 0
def gn(cap_only=0):
 ms=[];us=SD;b=B;en=1-us
 def add(s,t):
  if (t>>4)==(0 if us==0 else 7):
   for pr in(5,4,3,2):ms.append(s|(t<<7)|(pr<<14))
  else:ms.append(s|(t<<7))
 for s in PL[us]:
  p=b[s]
  t7=p&7;r=s>>4
  if t7==1:
   d=-16 if us==0 else 16;home=6 if us==0 else 1
   t=s+d
   if not b[t]:
    if not cap_only:
     add(s,t)
     if r==home and not b[t+d]:ms.append(s|((t+d)<<7))
    elif (t>>4)==(0 if us==0 else 7):add(s,t)
   for dd in(d-1,d+1):
    t=s+dd
    if t&0x88:continue
    q=b[t]
    if q and (q>8)==en:add(s,t)
    elif t==EP:ms.append(s|(t<<7))
  elif t7==2 or t7==6:
   for d in(KN if t7==2 else K8):
    t=s+d
    if not t&0x88:
     q=b[t]
     if(not q or(q>8)==en)and(not cap_only or q):ms.append(s|(t<<7))
  else:
   for d in(BD if t7==3 else RD if t7==4 else QD):
    t=s+d
    while not t&0x88:
     q=b[t]
     if q:
      if (q>8)==en:ms.append(s|(t<<7))
      break
     if not cap_only:ms.append(s|(t<<7))
     t+=d
 if cap_only:return ms
 for bit,kf,kt,rf,em,sf,cu in CAST:
  if cu==us and CS&bit and b[kf]==6+8*us and b[rf]==4+8*us and all(not b[e]for e in em)and all(not at(x,1-us)for x in sf):ms.append(kf|(kt<<7))
 return ms
def mk(m):
 global SD,CS,EP,HF,HK
 f=m&127;t=(m>>7)&127;pr=m>>14;p=B[f];cap=B[t];us=SD
 epc=-1
 if (p&7)==1 and t==EP and not cap and (f&7)!=(t&7):
  epc=t+16 if us==0 else t-16;cap=B[epc]
 ST.append((m,cap,CS,EP,HF,HK,epc))
 HK^=ZC[CS]
 if EP>=0:HK^=ZE[EP]
 HK^=Z[p][f]
 if cap:
  csq=epc if epc>=0 else t;HK^=Z[cap][csq];B[csq]=0;PL[1-us].discard(csq);i=cap*128+csq;SM[0]-=MG[i];SE[0]-=EG[i]
  if (cap&7)>1:
   MNP[1-us]-=1;PH[0]-=PW[cap&7]
 i=p*128+f;SM[0]-=MG[i];SE[0]-=EG[i]
 B[t]=(pr|(8*us))if pr else p;B[f]=0;HK^=Z[B[t]][t]
 i=B[t]*128+t;SM[0]+=MG[i];SE[0]+=EG[i]
 if pr:
  PH[0]+=PW[pr]
 PL[us].discard(f);PL[us].add(t)
 if (p&7)==6:
  KG[us]=t
  if t-f==2:B[t-1]=B[t+1];B[t+1]=0;HK^=Z[B[t-1]][t-1]^Z[B[t-1]][t+1];PL[us].discard(t+1);PL[us].add(t-1);r=B[t-1];SM[0]+=MG[r*128+t-1]-MG[r*128+t+1];SE[0]+=EG[r*128+t-1]-EG[r*128+t+1]
  elif f-t==2:B[t+1]=B[t-2];B[t-2]=0;HK^=Z[B[t+1]][t+1]^Z[B[t+1]][t-2];PL[us].discard(t-2);PL[us].add(t+1);r=B[t+1];SM[0]+=MG[r*128+t+1]-MG[r*128+t-2];SE[0]+=EG[r*128+t+1]-EG[r*128+t-2]
  CS&=~(3<<(2*us))
 for sq,bit in((119,1),(112,2),(7,4),(0,8)):
  if f==sq or t==sq:CS&=~bit
 EP=(f+t)//2 if (p&7)==1 and abs(t-f)==32 else -1
 HF=0 if (p&7)==1 or cap else HF+1
 if pr:MNP[us]+=1
 HK^=ZC[CS]
 if EP>=0:HK^=ZE[EP]
 SD=1-us;HK^=ZS
def um():
 global SD,CS,EP,HF,HK
 m,cap,CS,EP,HF,HK,epc=ST.pop()
 f=m&127;t=(m>>7)&127;pr=m>>14;us=1-SD;SD=us
 p=B[t]
 i=p*128+t;SM[0]-=MG[i];SE[0]-=EG[i]
 if pr:
  PH[0]-=PW[pr]
  p=1|(8*us);MNP[us]-=1
 i=p*128+f;SM[0]+=MG[i];SE[0]+=EG[i]
 B[f]=p;B[t]=0;PL[us].add(f);PL[us].discard(t)
 if cap:
  csq=epc if epc>=0 else t;B[csq]=cap;PL[1-us].add(csq);i=cap*128+csq;SM[0]+=MG[i];SE[0]+=EG[i]
  if (cap&7)>1:
   MNP[1-us]+=1;PH[0]+=PW[cap&7]
 if (p&7)==6:
  KG[us]=f
  if t-f==2:B[t+1]=B[t-1];B[t-1]=0;PL[us].add(t+1);PL[us].discard(t-1);r=B[t+1];SM[0]+=MG[r*128+t+1]-MG[r*128+t-1];SE[0]+=EG[r*128+t+1]-EG[r*128+t-1]
  elif f-t==2:B[t-2]=B[t+1];B[t+1]=0;PL[us].add(t-2);PL[us].discard(t+1);r=B[t-2];SM[0]+=MG[r*128+t-2]-MG[r*128+t+1];SE[0]+=EG[r*128+t-2]-EG[r*128+t+1]
def mn():
 global SD,EP,HF,HK
 ST.append((-1,0,CS,EP,HF,HK,-1))
 HK^=ZS
 if EP>=0:HK^=ZE[EP]
 EP=-1;HF+=1;SD=1-SD
def un():
 global SD,CS,EP,HF,HK
 _m,_c,CS,EP,HF,HK,_e=ST.pop();SD=1-SD
def ev():
 s=(SM[0]*PH[0]+SE[0]*(24-PH[0]))//24
 return s if SD==0 else -s
def od(ms,ttm,ply=0):
 b=B;kl=KL[ply]
 def sc(m):
  if m==ttm:return 1<<28
  cap=b[(m>>7)&127]
  if cap:return(1<<24)+VM[cap&7]*16-VM[b[m&127]&7]
  if m==kl[0]:return 1<<23
  if m==kl[1]:return(1<<23)-1
  return 0
 ms.sort(key=sc,reverse=True)
 return ms
def qs(a,b,ply):
 inc()
 if ply>28:return ev()
 chk=at(KG[SD],1-SD)
 if not chk:
  st=ev()
  if st>=b:return b
  if st>a:a=st
  ms=gn(1)
 else:ms=gn()
 best=-30000;leg=0
 for m in od(ms,0,ply):
  f=m&127;t=(m>>7)&127
  if not chk:
   cap=B[t]
   if cap and not m>>14 and st+VM[cap&7]+180<a:continue
  k=KG[SD];p7=B[f]&7
  need=chk or p7==6 or(p7==1 and t==EP)or(f&7)==(k&7)or(f>>4)==(k>>4)or abs((f&7)-(k&7))==abs((f>>4)-(k>>4))
  mk(m)
  if need and at(KG[1-SD],SD):um();continue
  leg=1;s=-qs(-b,-a,ply+1);um()
  if s>best:best=s
  if s>a:a=s
  if a>=b:break
 if not leg:return -29000+ply if chk else a
 return best if chk else a
def se(d,a,b,ply):
 if ply>0 and HF>=100:return 0
 if d==0:return qs(a,b,ply)
 inc()
 chk=at(KG[SD],1-SD)
 if chk:d+=1
 a0,b0=a,b
 ent=TT.get(HK);ttm=0
 if ent:
  ttm=ent[3]
  if ply>0 and ent[0]>=d:
   if ent[2]==0:return ent[1]
   if ent[2]==1:a=max(a,ent[1])
   else:b=min(b,ent[1])
   if a>=b:return ent[1]
 if ply>0 and d>=3 and not chk and MNP[SD]>0:
  mn()
  s=-se(d-3,-b,-b+1,ply+1)
  un()
  if s>=b:return b
 ms=od(gn(),ttm,ply)
 best=-30000;bm=0;leg=0
 for m in ms:
  f=m&127;t=(m>>7)&127;cap=B[t];pr=m>>14
  k=KG[SD];p7=B[f]&7
  need=chk or p7==6 or(p7==1 and t==EP)or(f&7)==(k&7)or(f>>4)==(k>>4)or abs((f&7)-(k&7))==abs((f>>4)-(k>>4))
  mk(m)
  if need and at(KG[1-SD],SD):um();continue
  leg+=1
  red=1 if(d>=3 and leg>3 and not chk and not cap and not pr)else 0
  if leg==1:s=-se(d-1,-b,-a,ply+1)
  else:
   s=-se(d-1-red,-a-1,-a,ply+1)
   if red and s>a:s=-se(d-1,-a-1,-a,ply+1)
   if s>a and s<b:s=-se(d-1,-b,-a,ply+1)
  um()
  if s>best:best=s;bm=m
  if s>a:a=s
  if a>=b:
   if not cap and not pr:
    k2=KL[ply]
    if k2[0]!=m:k2[1]=k2[0];k2[0]=m
   break
 if not leg:return -29000+ply if chk else 0
 TT[HK]=(d,best,2 if best<=a0 else(1 if best>=b0 else 0),bm)
 return best
def pf(fen):
 global SD,CS,EP,HF,HK
 parts=fen.split()
 B[:]=[0]*128
 r=0;f=0
 for c in parts[0]:
  if c=="/":r+=1;f=0
  elif c.isdigit():f+=int(c)
  else:
   p="pnbrqk".find(c.lower())+1|(0 if c.isupper()else 8);sq=r*16+f;B[sq]=p
   if p==6:KG[0]=sq
   if p==14:KG[1]=sq
   f+=1
 SD=0 if parts[1]=="w"else 1
 CS=sum({"K":1,"Q":2,"k":4,"q":8}.get(c,0)for c in parts[2])if len(parts)>2 else 0
 EP=-1
 if len(parts)>3 and parts[3]!="-":EP=(8-int(parts[3][1]))*16+(ord(parts[3][0])-97)
 HF=int(parts[4])if len(parts)>4 else 0
 PL[0].clear();PL[1].clear()
 MNP[0]=MNP[1]=0;SM[0]=0;SE[0]=0;PH[0]=0
 for sq in range(128):
  p=B[sq]
  if not p:continue
  PL[0 if p<8 else 1].add(sq)
  t7=p&7
  i=p*128+sq;SM[0]+=MG[i];SE[0]+=EG[i]
  if t7!=1 and t7!=6:
   MNP[0 if p<8 else 1]+=1;PH[0]+=PW[t7]
 HK=0
 for sq in PL[0]|PL[1]:HK^=Z[B[sq]][sq]
 if SD:HK^=ZS
 HK^=ZC[CS]
 if EP>=0:HK^=ZE[EP]
def uci(m):
 f=m&127;t=(m>>7)&127
 u="abcdefgh"[f&7]+str(8-(f>>4))+"abcdefgh"[t&7]+str(8-(t>>4))
 if m>>14:u+="nbrq"[(m>>14)-2]
 return u
def rt(fen,plies):
 pf(fen)
 ST.clear()
 if len(TT)>300000:TT.clear()
 LIM[0]=85000 if plies<130 else 35000
 ND[0]=0
 ent=TT.get(HK)
 ms=od(gn(),ent[3]if ent else 0)
 best=ms[0];bv=-30001
 d=1
 while d<40:
  try:
   a=-30000;cb=best;res=[]
   for m in ms:
    mk(m)
    if at(KG[1-SD],SD):um();continue
    s=-se(d-1,-30000,-a,1)
    um();res.append((s,m))
    if s>a:a=s;cb=m
   bv=a;best=cb
   res.sort(key=lambda x:-x[0]);ms=[m for s,m in res]
   if bv>27000 or bv<-27000:break
  except TO:break
  d+=1
 return uci(best)
def fb(fen,legal):return legal[0]
def ch(g):
 try:
  mv=rt(g["fen"],g["plies"])
  if mv in g["legal_moves"]:return mv
 except Exception:pass
 return fb(g["fen"],g["legal_moves"])
def main():
 while True:
  g=post("/game",{})
  if g["status"]=="done":break
  while g["status"]=="your_move":
   g=post("/move",{"game":g["game"],"move":ch(g)})
main()
