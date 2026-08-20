import sqlite3, json, sys, datetime, os

DB = r'C:\Users\x2\.local\share\opencode\opencode.db'
con = sqlite3.connect(DB)
con.row_factory = sqlite3.Row
cur = con.cursor()

sid = sys.argv[2]

cur.execute("SELECT id,title,directory,time_created,time_updated,agent,model,version FROM session WHERE id=?", (sid,))
s = dict(cur.fetchone())

cur.execute("SELECT id, time_created, data FROM message WHERE session_id=? ORDER BY time_created", (sid,))
messages = []
for r in cur.fetchall():
    try:
        md = json.loads(r['data'])
    except Exception:
        md = {}
    role = md.get('role')
    cur.execute("SELECT data FROM part WHERE message_id=? ORDER BY time_created", (r['id'],))
    parts = []
    for p in cur.fetchall():
        try:
            pd = json.loads(p['data'])
        except Exception:
            continue
        if pd.get('type') in ('text', 'reasoning', 'tool', 'file', 'step-start', 'error'):
            parts.append(pd)
    messages.append({
        'message_id': r['id'],
        'role': role,
        'time': datetime.datetime.fromtimestamp(r['time_created']/1000).isoformat() if r['time_created'] else None,
        'parts': parts
    })

meta = {
    'session_id': sid,
    'title': s['title'],
    'project_directory': s['directory'],
    'agent': s['agent'],
    'model': s['model'],
    'created': datetime.datetime.fromtimestamp(s['time_created']/1000).isoformat(),
    'updated_utc': datetime.datetime.fromtimestamp(s['time_updated']/1000).isoformat(),
}

out = {
    '_meta': meta,
    '_project_files': {
        'audio_and_transcripts': 'D:/AI_Project/projects/video/',
        'report': 'D:/AI_Project/projects/video/reports/ai_comparison_report.md',
        'summary': 'D:/AI_Project/projects/video/summary.md',
        'cookies': 'D:/AI_Project/projects/video/fresh_cookies.txt',
        'source_knowledge': 'D:/AI_Project/my_knowledge.txt',
        'this_export': 'D:/AI_Project/projects/video/chat_export.json'
    },
    'messages': messages
}

path = r'D:\AI_Project\projects\video\chat_export.json'
with open(path, 'w', encoding='utf-8') as f:
    json.dump(out, f, ensure_ascii=False, indent=1)
print("WROTE", os.path.abspath(path), len(messages), "messages")

# sanity: count roles
from collections import Counter
c = Counter(m['role'] for m in messages)
print("roles:", dict(c))