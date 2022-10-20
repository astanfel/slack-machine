from machine.plugins.base import MachineBasePlugin
from machine.plugins.decorators import listen_to
import re


class UltimateQuestionPlugin(MachineBasePlugin):

    @listen_to(regex=r"^42$")
    async def question(self, msg):
        await msg.say("You're telling me the Answer to the Ultimate Question of Life, the Universe and Everything, " +
                      "but I don't know the question :cry:")
