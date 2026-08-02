import urllib.request, urllib.parse, json, os, re, time

INVIDIOUS = "https://inv.nadeko.net"
DIR = r'D:\AI_Project\projects\video'

missing = [
    '8otvzGlcvoc', 'CbC1mhxwr30', 'eXp8TC0Sm6o', 'FXXjrF3GYy8',
    'GxkAFdBNI0c', 'HCZCfBWg5u8', 'hmbfqAQLo0Q', 'iMy7jYzGeEo',
    'IOfxvsdBpDQ', 'IvM0iV5bI_c', 'J04REnA4VFQ', 'kUNn6-ONJG8',
    'MIME05FAhJg', 'OWfF98UvGEM', 'QI7oUwNrQ34', 'TaMne2P-kHU',
    'Vo7byizKZ3o', 'wOMDsWrSyic', 'Xx86hL0P83Q', 'Y9Fv8FaqvQE',
    'YoHuVfr_rjk', 'YttzbKkdjWY', 'ZEfWLJdCY3M'
]

def fetch_subtitles(vid):
    # Step 1: Get caption list
    url = f"{INVIDIOUS}/api/v1/captions/{vid}"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, timeout=15) as resp:
        data = json.loads(resp.read())
    
    captions = data.get('captions', [])
    if not captions:
        return None
    
    # Prefer Russian
    target = None
    for c in captions:
        if c['languageCode'] == 'ru' and 'auto' not in c['label'].lower():
            target = c
            break
    if not target:
        for c in captions:
            if c['languageCode'] == 'ru':
                target = c
                break
    if not target:
        target = captions[0]
    
    # Step 2: Download caption content
    sub_url = f"{INVIDIOUS}/api/v1/captions/{vid}?label={urllib.parse.quote(target['label'])}"
    req2 = urllib.request.Request(sub_url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req2, timeout=15) as resp2:
        content = resp2.read().decode('utf-8')
    
    # Parse to plain text
    lines = []
    seen = set()
    for line in content.split('\n'):
        line = line.strip()
        if not line or line.startswith('WEBVTT') or line.startswith('Kind:') or \
           line.startswith('Language:') or '-->' in line or line.isdigit() or line == 'NOTE':
            continue
        clean = re.sub(r'<[^>]+>', '', line)
        if clean and clean not in seen:
            seen.add(clean)
            lines.append(clean)
    
    return ' '.join(lines), target['label']

for vid in missing:
    txt_path = os.path.join(DIR, f'{vid}_transcript.txt')
    if os.path.exists(txt_path) and os.path.getsize(txt_path) > 100:
        print(f'SKIP {vid}: already exists', flush=True)
        continue
    
    try:
        result = fetch_subtitles(vid)
        if result:
            text, label = result
            with open(txt_path, 'w', encoding='utf-8') as f:
                f.write(text)
            print(f'OK {vid}: {len(text)} chars ({label})', flush=True)
        else:
            print(f'NO SUBS {vid}', flush=True)
    except Exception as e:
        err = str(e)[:100]
        if '429' in err:
            print(f'RATE LIMITED at {vid}, waiting...', flush=True)
            time.sleep(30)
            try:
                result = fetch_subtitles(vid)
                if result:
                    text, label = result
                    with open(txt_path, 'w', encoding='utf-8') as f:
                        f.write(text)
                    print(f'OK {vid} (retry): {len(text)} chars ({label})', flush=True)
                else:
                    print(f'NO SUBS {vid}', flush=True)
            except Exception as e2:
                print(f'FAIL {vid}: {str(e2)[:100]}', flush=True)
        else:
            print(f'FAIL {vid}: {err}', flush=True)
    
    time.sleep(2)

print('\n=== DONE ===', flush=True)
