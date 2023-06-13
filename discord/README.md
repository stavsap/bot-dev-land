# Discord Bot Integration

# Clients

## Discord Python Client SDK

use [pycord](https://guide.pycord.dev/installation)

``` shell
pip install py-cord
```

# Bot creation and integration

## Application creation

1. go to: [Discord developer app](https://discord.com/developers/applications)
2. Click on "New Application"
3. Give it a name and create, congrats you have a discord app.
4. go to "bot" section, there is some configs to tweak, on of them if the bot wil lbe public or private. set what you need.

## Bot token generation

1. go to you app page, to "bot" section
2. click on "Reset Token" button to obtain new token. note! after that its up to you to keep this token!, if its lost a new one will be generated in the same way but you will need to update it in you bot client.
3. store the token safly for bot client to consume in production.


## Invite Link Creation

1. go to you app page, to Oauth2 section and there to url-generator
2. in the scopes, check "bot"
3. in the new permission section select wanted permissions, this permissions will be displayed for the join window when adding the bot to server.

## Tutorials

- [find you server guild id](https://support.discord.com/hc/en-us/articles/206346498-Where-can-I-find-my-User-Server-Message-ID-)
