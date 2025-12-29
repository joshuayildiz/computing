# pnpm
export PNPM_HOME="/Users/joshua/Library/pnpm"
case ":$PATH:" in
  *":$PNPM_HOME:"*) ;;
  *) export PATH="$PNPM_HOME:$PATH" ;;
esac
# pnpm end

# elixir
export PATH=$HOME/.elixir-install/installs/otp/28.1/bin:$PATH
export PATH=$HOME/.elixir-install/installs/elixir/1.19.4-otp-28/bin:$PATH

# sublime text/merge
export PATH=$PATH:/Applications/Sublime\ Text.app/Contents/SharedSupport/bin
export PATH=$PATH:/Applications/Sublime\ Merge.app/Contents/SharedSupport/bin

# haskell
[ -f "/Users/joshua/.ghcup/env" ] && . "/Users/joshua/.ghcup/env" # ghcup-env
