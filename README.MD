# mad-y

## testing testing 

pip install -r requirements.txt
add the DISCORD_TOKEN value to your env vars.
and run mad-y

## how to Deploy 

` docker build -t mad-y:0.1

create a discord_env file in your home with the next information 

DISCORD_TOKEN=YOURSUPERSECRETTOKEN

finally run this

` docker run --env-file ~/discord_env --name mady -d mady:0.1


