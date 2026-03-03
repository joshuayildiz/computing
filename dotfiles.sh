#!/bin/sh
set -e

# dotfiles in ~
ln -sf "$(pwd)/zshrc"     ~/.zshrc
ln -sf "$(pwd)/gitconfig" ~/.gitconfig

# dotfiles in ~/.config
mkdir -p ~/.config
[ ! -e ~/.config/ghostty ] && ln -sf "$(pwd)/ghostty" ~/.config/ghostty

# dotfiles in sublime directory
sublfile() {
	subluser="$HOME/Library/Application Support/Sublime Text/Packages/User"
	cp sublime-text/$1 "$subluser/$2"
}
sublfile settings.json Preferences.sublime-settings
sublfile packages.json "Package Control.sublime-settings"

# packages
rm -f Brewfile && brew bundle dump
