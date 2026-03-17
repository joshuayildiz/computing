# Homebrew shellenv
eval "$(/opt/homebrew/bin/brew shellenv)"

# Prompt
fpath+=("$(brew --prefix)/share/zsh/site-functions")
autoload -U promptinit; promptinit
prompt pure

# Path
export PATH="$PATH:$HOME/.bin"
export PATH="$PATH:$HOME/go/bin"