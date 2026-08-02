import pickle, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
with open(r'D:\AI_Project\booklm_chunks.pkl','rb') as f:
    chunks = pickle.load(f)
from collections import defaultdict
folders = defaultdict(set)
for c in chunks:
    s = c.metadata.get('source','')
    folders[s.split('\\')[0]].add(s)
fin = folders['Финансы']
fin_txt = [s for s in fin if s.endswith('.txt')]
fin_pdf = [s for s in fin if s.endswith('.pdf')]
print('Финансы: %d PDF, %d TXT (total %d)' % (len(fin_pdf), len(fin_txt), len(fin)))
for t in sorted(fin_txt):
    print('  TXT: ' + t)
