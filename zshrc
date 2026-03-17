# Homebrew shellenv
eval "$(/opt/homebrew/bin/brew shellenv)"

# Prompt
fpath+=("$(brew --prefix)/share/zsh/site-functions")
autoload -U promptinit; promptinit
prompt pure
