function OpenCode-AllProjects {
    $projects = @(
        @{Name = "AI_Project"; Path = "D:\AI_Project"},
        @{Name = "Obsidian"; Path = "D:\AI_Project\Obsidian"},
        @{Name = "Git"; Path = "D:\AI_Project\Git"},
        @{Name = "Finance"; Path = "D:\AI_Project\finance"},
        @{Name = "Health"; Path = "D:\AI_Project\health"},
        @{Name = "Notes"; Path = "D:\AI_Project\notes"},
        @{Name = "Tech"; Path = "D:\AI_Project\tech"}
    )

    foreach ($p in $projects) {
        if (Test-Path $p.Path) {
            Start-Process -FilePath "powershell.exe" -ArgumentList "-NoExit", "-Command", "cd '$($p.Path)'; opencode -m ollama/qwen3.5:latest"
            Start-Sleep -Milliseconds 300
        }
    }
    Write-Output "Projects opened: $($projects.Count)"
}

function OpenCode-Project {
    param([string]$Name)
    $projects = @{
        ai      = "D:\AI_Project"
        obsidian = "D:\AI_Project\Obsidian"
        git     = "D:\AI_Project\Git"
        finance = "D:\AI_Project\finance"
        health  = "D:\AI_Project\health"
        notes   = "D:\AI_Project\notes"
        tech    = "D:\AI_Project\tech"
    }
    if ($projects.ContainsKey($Name)) {
        Set-Location $projects[$Name]
        opencode -m ollama/qwen3.5:latest
    } else {
        Write-Error ("Project '" + $Name + "' not found. Available: " + ($projects.Keys -join ", "))
    }
}

Set-Alias -Name ocp -Value OpenCode-Project
Set-Alias -Name oca -Value OpenCode-AllProjects
