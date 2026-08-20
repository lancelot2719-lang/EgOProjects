# =============================================================
#  audit-ai-agents.ps1
#  Аудит установленных AI-агентов и состояния "второго мозга"
#  в D:\AI_Project
#
#  Запуск:
#    powershell -ExecutionPolicy Bypass -File audit-ai-agents.ps1
#
#  Результат: отчёт в консоли + файл
#    D:\AI_Project\_reports\agents_audit_<дата>.md
# =============================================================

$ROOT = "D:\AI_Project"
$AGENTS_DIR = Join-Path $ROOT "agents"      # где лежит коллекция 500-AI-Agents-Projects
$REPORT_DIR = Join-Path $ROOT "_reports"
$STAMP = Get-Date -Format "yyyy-MM-dd_HHmm"
$REPORT_FILE = Join-Path $REPORT_DIR "agents_audit_$STAMP.md"

if (-not (Test-Path $REPORT_DIR)) {
    New-Item -ItemType Directory -Path $REPORT_DIR | Out-Null
}

$lines = New-Object System.Collections.Generic.List[string]
$lines.Add("# Аудит AI-агентов и второго мозга")
$lines.Add("")
$lines.Add("Дата: $(Get-Date -Format 'yyyy-MM-dd HH:mm')")
$lines.Add("Корень проекта: $ROOT")
$lines.Add("")

# -------------------------------------------------------------
# 1. Аудит агентов
# -------------------------------------------------------------
$lines.Add("## 1. Установленные агенты")
$lines.Add("")

if (-not (Test-Path $AGENTS_DIR)) {
    $lines.Add("*Папка $AGENTS_DIR не найдена. Проверьте путь к коллекции 500-AI-Agents-Projects.*")
} else {
    $agentFolders = Get-ChildItem -Path $AGENTS_DIR -Directory -ErrorAction SilentlyContinue

    if ($agentFolders.Count -eq 0) {
        $lines.Add("*В $AGENTS_DIR нет подпапок с агентами.*")
    } else {
        $lines.Add("| # | Агент | requirements.txt | .env настроен | agent.py | README | Статус |")
        $lines.Add("|---|-------|-------------------|----------------|----------|--------|--------|")

        $i = 0
        $configured = 0
        $notConfigured = 0
        $broken = 0

        foreach ($folder in $agentFolders) {
            $i++
            $name = $folder.Name
            $path = $folder.FullName

            $hasReq   = Test-Path (Join-Path $path "requirements.txt")
            $hasEnv   = Test-Path (Join-Path $path ".env")
            $hasEnvEx = Test-Path (Join-Path $path ".env.example")
            $hasAgent = Test-Path (Join-Path $path "agent.py")
            $hasReadme = (Get-ChildItem -Path $path -Filter "README*" -ErrorAction SilentlyContinue).Count -gt 0

            $envStatus = if ($hasEnv) { "да" } elseif ($hasEnvEx) { "нет (есть .env.example)" } else { "нет" }

            if ($hasAgent -and $hasReq -and $hasEnv) {
                $status = "готов к запуску"
                $configured++
            } elseif ($hasAgent -and $hasReq) {
                $status = "требует .env"
                $notConfigured++
            } else {
                $status = "неполный / сломан"
                $broken++
            }

            $lines.Add("| $i | $name | $(if($hasReq){'v'}else{'-'}) | $envStatus | $(if($hasAgent){'v'}else{'-'}) | $(if($hasReadme){'v'}else{'-'}) | $status |")
        }

        $lines.Add("")
        $lines.Add("**Итого агентов:** $($agentFolders.Count)")
        $lines.Add("- Готовы к запуску: $configured")
        $lines.Add("- Требуют настройки .env: $notConfigured")
        $lines.Add("- Неполные/сломанные: $broken")
    }
}

$lines.Add("")

# -------------------------------------------------------------
# 2. Аудит скиллов (.agents/skills, .claude/skills)
# -------------------------------------------------------------
$lines.Add("## 2. Скиллы (skills)")
$lines.Add("")

$skillDirs = @(
    (Join-Path $ROOT ".agents\skills"),
    (Join-Path $ROOT ".claude\skills")
)

foreach ($dir in $skillDirs) {
    if (Test-Path $dir) {
        $lines.Add("### $dir")
        $skills = Get-ChildItem -Path $dir -Directory -ErrorAction SilentlyContinue
        if ($skills.Count -eq 0) {
            $lines.Add("*пусто*")
        } else {
            foreach ($s in $skills) {
                $hasSkillMd = Test-Path (Join-Path $s.FullName "SKILL.md")
                $lines.Add("- $($s.Name) $(if($hasSkillMd){'(SKILL.md найден)'}else{'(SKILL.md отсутствует!)'})")
            }
        }
        $lines.Add("")
    }
}

# -------------------------------------------------------------
# 3. Состояние "второго мозга" — активность папок
# -------------------------------------------------------------
$lines.Add("## 3. Состояние папок второго мозга")
$lines.Add("")

$brainFolders = @("business","ai-clone","health","finance","sales","notes","projects","tech","relationships",
                   "development","esoteric","polemica-notes","badhabit","thinking","communication","time_management")

$lines.Add("| Папка | Файлов | Последнее изменение | Размер (МБ) |")
$lines.Add("|-------|--------|----------------------|-------------|")

foreach ($bf in $brainFolders) {
    $p = Join-Path $ROOT $bf
    if (Test-Path $p) {
        $files = Get-ChildItem -Path $p -Recurse -File -ErrorAction SilentlyContinue
        $count = $files.Count
        $sizeMB = if ($count -gt 0) { [math]::Round(($files | Measure-Object -Property Length -Sum).Sum / 1MB, 2) } else { 0 }
        $lastMod = if ($count -gt 0) { ($files | Sort-Object LastWriteTime -Descending | Select-Object -First 1).LastWriteTime } else { "—" }
        $lines.Add("| $bf | $count | $lastMod | $sizeMB |")
    } else {
        $lines.Add("| $bf | папка отсутствует | — | — |")
    }
}

$lines.Add("")

# -------------------------------------------------------------
# 4. База знаний RAG
# -------------------------------------------------------------
$lines.Add("## 4. База знаний / RAG")
$lines.Add("")

$ragFiles = @("rag_simple.py","booklm.py","booklm_chunks.pkl","convert_all_fb2.py","move_books.py","my_knowledge.txt")
foreach ($f in $ragFiles) {
    $p = Join-Path $ROOT $f
    if (Test-Path $p) {
        $item = Get-Item $p
        $sizeKB = [math]::Round($item.Length / 1KB, 1)
        $lines.Add("- **$f** — есть, $sizeKB КБ, изменён $($item.LastWriteTime)")
    } else {
        $lines.Add("- **$f** — отсутствует")
    }
}

$lines.Add("")

# -------------------------------------------------------------
# 5. Ключевые конфиги
# -------------------------------------------------------------
$lines.Add("## 5. Ключевые конфиги")
$lines.Add("")

$configFiles = @("AGENTS.md","CLAUDE.md","opencode.json","README.md",".claude\memory.md",".claude\projects.md")
foreach ($f in $configFiles) {
    $p = Join-Path $ROOT $f
    if (Test-Path $p) {
        $lines.Add("- **$f** — найден")
    } else {
        $lines.Add("- **$f** — отсутствует")
    }
}

# -------------------------------------------------------------
# Сохранение
# -------------------------------------------------------------
$lines | Out-File -FilePath $REPORT_FILE -Encoding utf8

Write-Host ""
Write-Host "=================================================="
Write-Host " Аудит завершён."
Write-Host " Отчёт сохранён: $REPORT_FILE"
Write-Host "=================================================="
Write-Host ""
Get-Content $REPORT_FILE
