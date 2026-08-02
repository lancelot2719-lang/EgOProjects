# Snapshot file
# Unset all aliases to avoid conflicts with functions
unalias -a 2>/dev/null || true
shopt -s expand_aliases
# Check for rg availability
if ! (unalias rg 2>/dev/null; command -v rg) >/dev/null 2>&1; then
  function rg {
  local _cc_bin="${CLAUDE_CODE_EXECPATH:-}"
  [[ -x $_cc_bin ]] || _cc_bin=/c/Users/x2/.local/bin/claude.exe
  if [[ ! -x $_cc_bin ]]; then command rg ${1+"$@"}; return; fi
  if [[ -n ${ZSH_VERSION:-} ]]; then
    ARGV0=rg "$_cc_bin" ${1+"$@"}
  elif [[ "$OSTYPE" == "msys" ]] || [[ "$OSTYPE" == "cygwin" ]] || [[ "$OSTYPE" == "win32" ]]; then
    ARGV0=rg "$_cc_bin" ${1+"$@"}
  else
    (exec -a rg "$_cc_bin" ${1+"$@"})
  fi
}
fi
# Shadow pkill to refuse patterns matching the CLI process
unalias pkill 2>/dev/null || true
function pkill {
  if [ -n "${CLAUDE_PID:-}" ] && [ -r "/proc/${CLAUDE_PID}/comm" ]; then
    local _cc_skip="" _cc_a
    local -a _cc_probe=()
    for _cc_a in ${1+"$@"}; do
      if [ -n "$_cc_skip" ]; then _cc_skip=""; continue; fi
      case "$_cc_a" in
        --signal) _cc_skip=1 ;;
        --signal=*|-e|--echo) ;;
        -[0-9]*) ;;
        -[PUGOF]?*) _cc_probe+=("$_cc_a") ;;
        -[ABCDEFGHIJKLMNOPQRSTUVWXYZ][ABCDEFGHIJKLMNOPQRSTUVWXYZ0-9]*) ;;
        *) _cc_probe+=("$_cc_a") ;;
      esac
    done
    if command pgrep ${_cc_probe[@]+"${_cc_probe[@]}"} 2>/dev/null | command grep -qx "${CLAUDE_PID}"; then
      printf 'pkill: refusing to run — this pattern matches the Claude CLI process (PID %s). Narrow the pattern, or target your own children with `pkill -P $$ ...`.\n' "${CLAUDE_PID}" >&2
      return 1
    fi
  fi
  command pkill ${1+"$@"}
}
export PATH='/c/Users/x2/bin:/mingw64/bin:/usr/local/bin:/usr/bin:/bin:/mingw64/bin:/usr/bin:/c/Users/x2/bin:/c/Program Files (x86)/Razer Chroma SDK/bin:/c/Program Files/Razer Chroma SDK/bin:/c/Program Files (x86)/Razer/ChromaBroadcast/bin:/c/Program Files/Razer/ChromaBroadcast/bin:/c/Program Files (x86)/Common Files/Oracle/Java/javapath:/c/Windows/system32:/c/Windows:/c/Windows/System32/Wbem:/c/Windows/System32/WindowsPowerShell/v1.0:/c/Windows/System32/OpenSSH:/d/Program Files (x86)/Microsoft VS Code/bin:/c/Program Files (x86)/NVIDIA Corporation/PhysX/Common:/c/Program Files/Microsoft SQL Server/110/Tools/Binn:/c/Users/x2/AppData/Local/Programs/Python/Python310/Scripts:/c/Users/x2/AppData/Local/Programs/Python/Python310:/d/Program Files (x86)/Python/Scripts:/d/Program Files (x86)/Python:/c/Users/x2/AppData/Local/Microsoft/WindowsApps:/c/Windows/system32/config/systemprofile/AppData/Local/Microsoft/WindowsApps:/cmd:/d/AI_Project/WezTerm:/d/Program Files/nodejs:/c/Program Files/dotnet:/c/Users/x2/AppData/Local/Programs/Python/Launcher:/c/Users/x2/.lmstudio/bin:/c/Users/x2/AppData/Local/Python/bin:/c/Users/x2/AppData/Local/Microsoft/WinGet/Packages/DenoLand.Deno_Microsoft.Winget.Source_8wekyb3d8bbwe:/c/Users/x2/AppData/Local/Microsoft/WinGet/Packages/Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe/ffmpeg-8.1.2-full_build/bin:/c/Users/x2/AppData/Local/Programs/Ollama:/c/Users/x2/AppData/Roaming/npm:/d/AI_Project/npm-global:/c/Users/x2/AppData/Local/Programs/Python/Python314:/c/Users/x2/AppData/Local/Programs/Python/Python311:/c/Users/x2/AppData/Local/Programs/Python/Python310:/usr/bin/vendor_perl:/usr/bin/core_perl:/c/Users/x2/AppData/Roaming/Claude/local-agent-mode-sessions/skills-plugin/7582d004-c3a9-43a3-85b8-2000e2fab166/a05be4c3-5268-4b3e-b77a-8053994c27f7/bin'
