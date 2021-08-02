# Fanfare Bot 🎺

Notify all of your presence with the **Fanfare Bot**, a bot that joins a voice channel on your Discord server at the same time you do to play a custom fanfare of your choosing.

Fanfare can run concurrently on multiple servers, so if you and your friends hang out on a bunch of different servers (and you are able to add bots to them), then it should work just fine!

## How to Use

**Before you start**, make sure you have created an Application in Discord's [Developer Portal](https://discord.com/developers/applications). Fanfare uses the `DISCORD_CLIENT_SECRET` environment variable to store the client secret, so store it there.

1. Get the **Discord User ID** of the users you want to make fanfares for. Make sure _Developer Mode_ is enabled in your Discord Advanced settings, then right click a user and select _Copy ID_.

![](https://i.imgur.com/f6OVaRM.gif)

![](https://i.imgur.com/gRWTmYd.gif)

2. Configure users and sounds in the [`sounds.json`](/sounds.json) file, using the **Discord User ID** as the key, and the sound filename as the value (place sounds in the [`sound`](/sound) folder):

```json
{
    "discorduserid": "soundfile.mp3",
    "126867061447196672": "brap.mp3"
}
```

3. Install the requirements and run the `__init__.py` file:

```shell
$ virtualenv env --python=python3

$ source env/bin/activate

$ pip install -r requirements.txt

$ python __init__.py
```

If you did everything right, you should then see a login success message with your bot account's name.

If you did everything right but it's broken, then it's still probably your fault.
If you insist that it's my fault then let me know, or make a pull request :)