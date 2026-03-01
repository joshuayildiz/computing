#!/bin/sh
set -e

# dotfiles in ~
ln -sf "$(pwd)/zshrc"     "$HOME/.zshrc"
ln -sf "$(pwd)/gitconfig" "$HOME/.gitconfig"

# plugins for sublime text
subl_plugin() {
	path="$HOME/Library/Application Support/Sublime Text/Packages/User/$2"
	cp "$(pwd)/sublime-text/$1" "$path"
	echo "subl_plugin: $1"
}

subl_plugin settings.json Preferences.sublime-settings
subl_plugin commands.json Default.sublime-commands
subl_plugin align.py      align.py

# packages
rm Brewfile && brew bundle dump
