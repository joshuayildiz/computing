# .bashrc

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

# prompt
PS1='[\u@\h \W]\$ '

# stuff
export PAGER=nobs

# acme
alias acme='acme -f /mnt/font/BerkeleyMonoVariable-Regular/10a/font'