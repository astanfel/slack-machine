from machine.plugins.base import MachineBasePlugin
from machine.plugins.decorators import listen_to
import re
import gitlab as gl
import logging as logger

git = gl.Gitlab(private_token='glpat-oVydRTFobzctxDLq51bQ')


class GitlabPlugin(MachineBasePlugin):

    @listen_to(regex=r"^DRE MRs$")
    async def get_mrs(self, msg):
        name = msg.sender.profile.real_name_normalized
        sofi_group = git.groups.get('sofiinc')
        # gitlab_user = sofi_group.members.list(search=name, active=True)
        gitlab_user = git.users.list(search=name, active=True)
        # await msg.say(f"Getting MRs assigned to {name}: \n {gitlab_user}", ephemeral=True)
        await msg.say(f"Getting MRs assigned to {name}: \n {gitlab_user}")
        group = git.groups.get('sofiinc/dsi')
        logger.info(group)
        mrs = group.mergerequests.list(get_all=True, state="opened",
                                       order_by='updated_at', reviewer_id=gitlab_user[0].id)
        # mr_info = [(mr.title, mr.assignee["username"], mr.web_url) for mr in mrs]
        mr_string = []
        for mr in mrs:
            mr_string.append(f'<{mr.web_url}|{mr.title}> Assignee: {mr.assignee["username"]}')
        #await msg.say("\n".join(mr_string), ephemeral=True)
        await msg.say("\n".join(mr_string))
