# mad-y

## how to reploy 

` docker build -t mad-y:0.1

create a discord_env file in your home with the next information 

DISCORD_TOKEN=YOURSUPERSECRETTOKEN

finally run this

` docker run --env-file ~/discord_env --name mady -d mady:0.1


