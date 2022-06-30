#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

fm6000 -f /home/jack/.config/fetchMaster6000/dog.txt -c "random" -d Awesome
alias ls='ls --color=auto'
PS1='[\u@\h \W]\$ '
# ~/.bashrc
eval "$(starship init bash)" 2> /dev/null

