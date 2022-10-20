
from machine.plugins.base import MachineBasePlugin
from machine.plugins.decorators import respond_to
from machine.plugins.decorators import listen_to
from machine.plugins.decorators import process
from machine.plugins.decorators import schedule
from machine.plugins.decorators import on
from datetime import datetime

import re


class ListeningPlugin(MachineBasePlugin):

    @respond_to(r"^I love you")
    async def spread_love(self, msg):
        await msg.reply("I love you too!")

    @respond_to(r"You deserve (?P<num_stars>\d+) stars!")
    async def award(self, msg, num_stars):
        stars_back = int(num_stars) + 1
        await msg.reply("Well, you deserve {}!".format(stars_back))

    @listen_to(r"go for it")
    @listen_to(r"go 4 it")
    async def go_for_it(self, msg):
        await msg.say("https://a-z-animals.com/media/animals/images/original/gopher_2.jpg")

    @process("reaction_added")
    async def match_reaction(self, event):
        emoji = event["reaction"]
        channel = event["item"]["channel"]
        ts = event["item"]["ts"]
        await self.react(channel, ts, emoji)

    # @schedule(hour="9-17", minute="*/30")
    # async def movement_reminder(self):
    #     await self.say("general", "<!here> maybe now is a good time to take a short walk!")

    @on("bathroom_used")
    async def call_cleaning_department(self, **kwargs):
        # await self.say("dre-bot-development", "<!here> Somebody used the toilet!")
        await self.say("dre-bot-development", "Somebody used the toilet!")
        # await self.react("dre-bot-development", str(datetime.now()), "roll_of_paper")

    @respond_to(r"I have used the bathroom")
    async def broadcast_bathroom_usage(self, msg):
        self.emit('bathroom_used', toilet_flushed=True)


