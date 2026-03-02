#!/bin/sh
set -e

# dotfiles in ~
ln -sf "$(pwd)/zshrc"     "$HOME/.zshrc"
ln -sf "$(pwd)/gitconfig" "$HOME/.gitconfig"

# packages
rm -f Brewfile && brew bundle dump
