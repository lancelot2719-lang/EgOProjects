import subprocess, os, re, glob

DIR = r'D:\AI_Project\projects\video'
COOKIES = os.path.join(DIR, 'fresh_cookies.txt')

missing = [
    '8otvzGlcvoc', 'CbC1mhxwr30', 'eXp8TC0Sm6o', 'FXXjrF3GYy8',
    'GxkAFdBNI0c', 'HCZCfBWg5u8', 'hmbfqAQLo0Q', 'iMy7jYzGeEo',
    'IOfxvsdBpDQ', 'IvM0iV5bI_c', 'J04REnA4VFQ', 'kUNn6-ONJG8',
    'MIME05FAhJg', 'OWfF98UvGEM', 'QI7oUwNrQ34', 'TaMne2P-kHU',
    'Vo7byizKZ3o', 'wOMDsWrSyic', 'Xx86hL0P83Q', 'Y9Fv8FaqvQE',
    'YoHuVfr_rjk', 'YttzbKkdjWY', 'ZEfWLJdCY3M'
]

for vid in missing:
    url = f'https://www.youtube.com/watch?v={vid}'
    out_template = os.path.join(DIR, vid)
    
    cmd = [
        'yt-dlp', '--write-auto-sub', '--sub-lang', 'ru', '--skip-download',
        '--cookies', COOKIES, url, '-o', out_template, '--no-playlist'
    ]
    
    print(f'--- {vid} ---', flush=True)
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
    output = result.stdout + result.stderr
    
    if 'ERROR' in output.upper() and 'sign in' in output:
        print(f'  AUTH FAILED: need fresh cookies', flush=True)
        continue
    
    # Find created subtitle file
    sub_files = glob.glob(os.path.join(DIR, f'{vid}*.vtt')) + \
                glob.glob(os.path.join(DIR, f'{vid}*.srt')) + \
                glob.glob(os.path.join(DIR, f'{vid}*.ttml'))
    
    if sub_files:
        sub_path = sub_files[0]
        with open(sub_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Parse VTT/SRT to plain text
        lines = []
        seen = set()
        for line in content.split('\n'):
            line = line.strip()
            if not line:
                continue
            if line.startswith('WEBVTT') or line.startswith('Kind:') or \
               line.startswith('Language:') or '-->' in line or \
               line.isdigit() or line == 'NOTE':
                continue
            clean = re.sub(r'<[^>]+>', '', line)
            if clean and clean not in seen:
                seen.add(clean)
                lines.append(clean)
        
        text = ' '.join(lines)
        txt_path = os.path.join(DIR, f'{vid}_transcript.txt')
        with open(txt_path, 'w', encoding='utf-8') as f:
            f.write(text)
        
        print(f'  OK: {len(text)} chars', flush=True)
        os.remove(sub_path)
    else:
        # Check if youtube said no subs
        if 'doesn\'t have subtitles' in output:
            print(f'  NO SUBS on YouTube', flush=True)
        else:
            print(f'  FAILED: {output[-200:]}', flush=True)

print('\n=== DONE ===', flush=True)
