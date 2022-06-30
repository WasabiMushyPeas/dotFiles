if status is-interactive
    # Commands to run in interactive sessions can go here
    fm6000 -f /home/jack/.config/fetchMaster6000/dog.txt -c "random" -d Awesome -sh Fish
    starship init fish | source
    task list project.isnt:RandoProjects
end
