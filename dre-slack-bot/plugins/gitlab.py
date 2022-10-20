from machine.plugins.base import MachineBasePlugin
from machine.plugins.decorators import respond_to, listen_to
import re
import gitlab as gl
import logging as logger




class GitlabPlugin(MachineBasePlugin):

    @respond_to(regex=r"^my mrs$")
    # @listen_to(regex=r"^merge-requests$")
    async def get_mrs(self, msg):
        name = msg.sender.profile.real_name_normalized
        sofi_group = git.groups.get('sofiinc')
        gitlab_user = sofi_group.members.list(query=name, active=True)
        # gitlab_user = git.users.list(search=name, active=True)
        # await msg.say(f"Getting MRs assigned to {name}: \n {gitlab_user}", ephemeral=True)
        await msg.reply_dm(f"Getting MRs assigned to {name}")
        group = git.groups.get('sofiinc/dsi')
        logger.info(group)
        mrs = group.mergerequests.list(get_all=True, state="opened",
                                       order_by='updated_at', reviewer_id=gitlab_user[0].id)
        # mr_info = [(mr.title, mr.assignee["username"], mr.web_url) for mr in mrs]
        mr_string = []
        for mr in mrs:
            mr_string.append(f'<{mr.web_url}|{mr.title}> Assignee: {mr.assignee["username"]}')
        # await msg.say("\n".join(mr_string), ephemeral=True)
        await msg.reply_dm("\n".join(mr_string))

    # @respond_to(regex=r"Tag MR https:\/\/gitlab\.com\/(?P<mr_project>.+)\/-\/merge_requests\/(?P<mr_id>\d+)")
    # @respond_to(regex=r"Tag MR <(?P<mr_url>.+)>")
    @listen_to(regex=r"^:meeseeks-box:\s*<(?P<mr_url>.+)>")
    async def tag_mr_reviewers(self, msg, mr_url):
        # print(mr_url)
        # await msg.say(f'Here is the URL {mr_url}')
        result = re.match(r'https://gitlab\.com/(?P<mr_project>.+)/-/merge_requests/(?P<mr_id>\d+)',
                          mr_url.strip(),
                          re.IGNORECASE)
        if result:
            # await msg.say(f'Here is the result {result}')
            # await msg.say(f'Here is the project {result["mr_project"]} and the id {result["mr_id"]}')
            project = git.projects.get(result["mr_project"])
            editable_mr = project.mergerequests.get(id=result["mr_id"])
            # await msg.say(f'Here is the editable_mr {editable_mr}')
            editable_mr.labels = ['ready-for-review']
            editable_mr.save()
            await msg.reply_dm("MR is labeled for review!")
        else:
            await msg.reply_dm("I couldn't find that MR to label ¯\\_(ツ)_/¯")
