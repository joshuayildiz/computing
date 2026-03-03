# omz start
export ZSH="$HOME/.oh-my-zsh"
plugins=(git)

# prompt
ZSH_THEME=""
fpath+=("$(brew --prefix)/share/zsh/site-functions")
autoload -U promptinit; promptinit
prompt pure

# omz end
source $ZSH/oh-my-zsh.sh
