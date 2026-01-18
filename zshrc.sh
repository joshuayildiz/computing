# omz config
export ZSH="$HOME/.oh-my-zsh"
ZSH_THEME="robbyrussell"
plugins=(git)

# pnpm
export PNPM_HOME="/Users/joshua/Library/pnpm"
case ":$PATH:" in
  *":$PNPM_HOME:"*) ;;
  *) export PATH="$PNPM_HOME:$PATH" ;;
esac
# pnpm end

# path
export PATH="$PATH:$HOME/code/flutter/bin"
export PATH="$PATH:$HOME/go/bin"
export PATH="$PATH:/Applications/CMake.app/Contents/bin"
export PATH="$PATH:$HOME/code/upx/build/release"
export PATH="$PATH:$HOME/.zig"

# uv
. "$HOME/.local/bin/env"

# omz source
source $ZSH/oh-my-zsh.sh
