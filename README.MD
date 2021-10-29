# mad-y

Currently following this guide https://discordjs.guide/

app in early development.

next steps:

    - firsts commands

## Libraries

    discord.js

## Installation

``` npm install ```

add the DISCORD_TOKEN value to your env vars.

``` DISCORD_TOKEN=YOURSUPERSECRETTOKEN ```

## How to Deploy 

```docker build -t mad-y:0.1 . ```

create a environment variable in your user system path.

``` $env:USERPROFILE/docker.env ```

and add the next environment variable:

``` DISCORD_TOKEN=YOURSUPERSECRETTOKEN ```

finally run this:

build it!

``` docker run --env-file $env:USERPROFILE/docker.env --name mady -d mady:0.1 ```

run it!

``` docker run --name mady -d mady:0.1 ```


