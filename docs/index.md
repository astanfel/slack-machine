# Slack Machine

![image](img/logo.png)

[![Join the chat at Slack](https://img.shields.io/badge/chat-slack-green?logo=slack&logoColor=white)](https://join.slack.com/t/slack-machine-chat/shared_invite/zt-1g87tzvlf-8bV_WnY3JZyaYNnRFwRd~w)
[![image](https://img.shields.io/pypi/v/slack-machine.svg)](https://pypi.python.org/pypi/slack-machine)
[![image](https://img.shields.io/pypi/l/slack-machine.svg)](https://pypi.python.org/pypi/slack-machine)
[![image](https://img.shields.io/pypi/pyversions/slack-machine.svg)](https://pypi.python.org/pypi/slack-machine)
[![CI Status](https://github.com/DonDebonair/slack-machine/actions/workflows/ci.yml/badge.svg)](https://github.com/DonDebonair/slack-machine/actions/workflows/ci.yml)
[![image](https://codecov.io/gh/DonDebonair/slack-machine/branch/main/graph/badge.svg)](https://codecov.io/gh/DonDebonair/slack-machine)

Slack Machine is a simple, yet powerful and extendable Slack bot framework. More than just a bot, Slack
Machine is a framework that helps you develop your Slack workspace into a ChatOps powerhouse. Slack Machine is built
with an intuitive plugin system that lets you build bots quickly, but also allows for easy code organization. A
plugin can look as simple as this:

```python
from machine.plugins.base import MachineBasePlugin, Message
from machine.plugins.decorators import respond_to

class DeploymentPlugin(MachineBasePlugin):
    """Deployments"""
    @respond_to(r"deploy (?P<application>\w+) to (?P<environment>\w+)")
    async def deploy(self, msg: Message, application, environment):
        """deploy <application> <environment>: deploy application to target environment"""
        await msg.say(f"Deploying {application} to {environment}")
```

## *Note*

As of v0.30.0 Slack Machine dropped support for the old backend based on the RTM API. As such, Slack Machine is now
fully based on [AsyncIO](https://docs.python.org/3/library/asyncio.html). This means plugins written before the
rewrite to asyncio aren't supported anymore. See [here](migrating.md) for a migration guide to get your old plugins
working with the new version of Slack Machine.

It's really easy!

## Features

- Get started with mininal configuration
- Built on top of the [Slack Events API](https://api.slack.com/apis/connections/events-api) for smoothly responding
  to events in semi real-time. Uses [Socket Mode](https://api.slack.com/apis/connections/socket) so your bot doesn't
  need to be exposed to the internet!
- Support for rich interactions using the [Slack Web API](https://api.slack.com/web)
- High-level API for maximum convenience when building plugins
- Low-level API for maximum flexibility
- Built on top of [AsyncIO](https://docs.python.org/3/library/asyncio.html) to ensure good performance by handling
  communication with Slack concurrently

### Plugin API features:

- Listen and respond to any regular expression
- Capture parts of messages to use as variables in your functions
- Respond to messages in channels, groups and direct message conversations
- Respond with reactions
- Respond in threads
- Respond with ephemeral messages
- Send DMs to any user
- Support for [blocks](https://api.slack.com/reference/block-kit/blocks)
- Support for [message attachments](https://api.slack.com/docs/message-attachments) [Legacy 🏚]
- Listen and respond to any [Slack event](https://api.slack.com/events) supported by the Events API
- Store and retrieve any kind of data in persistent storage (currently Redis, DynamoDB and in-memory storage are
  supported)
- Schedule actions and messages
- Emit and listen for events
- Help texts for Plugins

### Coming Soon

- Support for Interactive Buttons
- ... and much more
