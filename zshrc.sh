# pnpm
export PNPM_HOME="/Users/joshua/Library/pnpm"
case ":$PATH:" in
  *":$PNPM_HOME:"*) ;;
  *) export PATH="$PNPM_HOME:$PATH" ;;
esac
# pnpm end

# sublime text/merge
export PATH=$PATH:/Applications/Sublime\ Text.app/Contents/SharedSupport/bin
export PATH=$PATH:/Applications/Sublime\ Merge.app/Contents/SharedSupport/bin

# flutter
export PATH="$HOME/code/flutter/bin:$PATH"
