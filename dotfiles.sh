#!/bin/sh
set -e

# dotfiles in ~
ln -sf "$(pwd)/zshrc"     ~/.zshrc
ln -sf "$(pwd)/gitconfig" ~/.gitconfig

# dotfiles in ~/.config
mkdir -p ~/.config
[ ! -e ~/.config/ghostty ] && ln -sf "$(pwd)/ghostty" ~/.config/ghostty

# packages
rm -f Brewfile && brew bundle dump
