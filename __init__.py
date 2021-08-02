import discord, asyncio

from os import environ
from json import load

intents = discord.Intents.default()

# soundslist loaded from external json file for ease of use :)
with open('sounds.json') as file:
    ENTRANCE_SOUNDS = load(file)

class Client(discord.Client):
    async def on_connect(self):
        # solution for running on multiple servers at once
        # each server has its own asyncio.Queue that is made once it uses the bot for the first time
        self.contexts = {}

    async def on_ready(self):
        print(f'Logged in as {self.user}')

    async def play_vc_audio(self, channel, audio):
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio(source=f'sound/{audio}'))

        while vc.is_playing():
            await asyncio.sleep(1)

        await vc.disconnect()

    async def on_voice_state_update(self, member, before, after):
        if after.channel:
            if str(member.id) in ENTRANCE_SOUNDS and (not before.channel or before.channel.id != after.channel.id):
                queue = self.get_context_queue(member.guild)
                await queue.put((after.channel, member.id))

    async def queue_worker(self, queue):
        while True:
            args = await queue.get() # a tuple of channel, user id

            # run the function on the given id
            await self.play_vc_audio(args[0], ENTRANCE_SOUNDS[str(args[1])])
            
            queue.task_done()

    # returns the appropriate asyncio queue for the given guild
    # this hopefully means we can have several concurrent queues that will handle multiple servers
    def get_context_queue(self, guild):
        if not guild in self.contexts:
            self.contexts[guild] = asyncio.Queue()
            asyncio.create_task(self.queue_worker(self.contexts[guild]))
            print(f'New context created for guild {guild}')

        return self.contexts[guild]

client = Client(intents=intents)
client.run(environ['DISCORD_CLIENT_SECRET'])