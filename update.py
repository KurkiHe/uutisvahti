import json, os, datetime, calendar, email.utils
import requests, feedparser
from concurrent.futures import ThreadPoolExecutor

SITES = {
 'LaLiiga':'https://www.laliiga.com', 'Valioliiga':'https://www.valioliiga.com',
 'SuomiFutis':'https://www.suomifutis.com', 'SuomiKiekko':'https://www.suomikiekko.com',
 'Leijonat':'https://www.leijonat.com', 'NHLSuomi':'https://www.nhlsuomi.com',
 'SuomiKoris':'https://www.suomikoris.com', 'SuomiUrheilu':'https://www.suomiurheilu.com'
}
HEADERS={'User-Agent':'Uutisvahti/1.0 (personal RSS reader)'}

def fetch(item):
 name, base=item
 for suffix in ('/feed/', '/feed', '/rss/'):
  try:
   r=requests.get(base+suffix,headers=HEADERS,timeout=12)
   r.raise_for_status()
   feed=feedparser.parse(r.content)
   if not feed.entries: continue
   stories=[]
   for e in feed.entries:
    dt=e.get('published_parsed') or e.get('updated_parsed')
    ts=calendar.timegm(dt) if dt else 0
    if e.get('title') and e.get('link'):
     stories.append({'site':name,'title':e.title,'url':e.link,'timestamp':ts})
   return name,stories,None
  except Exception: pass
 return name,[], 'RSS-syötettä ei voitu lukea'

old=[]
if os.path.exists('news.json'):
 try: old=json.load(open('news.json',encoding='utf8')).get('articles',[])
 except Exception: pass
by_url={x['url']:x for x in old if x.get('url')}
statuses={}
with ThreadPoolExecutor(max_workers=8) as pool:
 for name,stories,error in pool.map(fetch,SITES.items()):
  statuses[name]={'ok':error is None,'fetched':len(stories),'error':error}
  for story in stories: by_url[story['url']]=story
articles=sorted(by_url.values(),key=lambda x:x.get('timestamp',0),reverse=True)[:2500]
with open('news.json','w',encoding='utf8') as f:
 json.dump({'updated':datetime.datetime.now(datetime.timezone.utc).isoformat(),'statuses':statuses,'articles':articles},f,ensure_ascii=False)
print('Articles:',len(articles),'statuses:',statuses)
