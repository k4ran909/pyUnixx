# py-Unixx Library

Core library of [The Unixx](https://github.com/TeamUnixx/Unixx), a python based telegram userbot.

[![PyPI - Version](https://img.shields.io/pypi/v/py-Unixx?style=round)](https://pypi.org/project/py-Unixx)    
[![PyPI - Downloads](https://img.shields.io/pypi/dm/py-Unixx?label=DOWNLOADS&style=round)](https://pypi.org/project/py-Unixx)    
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/TeamUnixx/Unixx/graphs/commit-activity)
[![Open Source Love svg2](https://badges.frapsoft.com/os/v2/open-source.svg?v=103)](https://github.com/TeamUnixx/Unixx)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](https://makeapullrequest.com)

# Installation
```bash
pip3 install -U py-Unixx
```

# Documentation 
[![Documentation](https://img.shields.io/badge/Documentation-Unixx-blue)]

# Usage
- Create folders named `plugins`, `addons`, `assistant` and `resources`.   
- Add your plugins in the `plugins` folder and others accordingly.   
- Create a `.env` file with following mandatory Environment Variables
   ```
   API_ID
   API_HASH
   SESSION
   REDIS_URI
   REDIS_PASSWORD
   ```
- Check
[`.env.sample`](https://github.com/TeamUnixx/Unixx/blob/main/.env.sample) for more details.   
- Run `python3 -m pyUnixx` to start the bot.   

## Creating plugins
 - ### To work everywhere

```python
@Unixx_cmd(
    pattern="start"
)   
async def _(e):   
    await e.eor("Unixx Started!")   
```

- ### To work only in groups

```python
@Unixx_cmd(
    pattern="start",
    groups_only=True,
)   
async def _(e):   
    await eor(e, "Unixx Started.")   
```

- ### Assistant Plugins 👇

```python
@asst_cmd("start")   
async def _(e):   
    await e.reply("Unixx Started.")   
```

See more working plugins on [the offical repository](https://github.com/TeamUnixx/Unixx)!

> Made with 💕 by [@TeamUnixx](https://t.me/TeamUnixx).    


# License
[![License](https://www.gnu.org/graphics/agplv3-155x51.png)](LICENSE)   
Unixx is licensed under [GNU Affero General Public License](https://www.gnu.org/licenses/agpl-3.0.en.html) v3 or later.

# Credits
* [![TeamUnixx-Devs](https://img.shields.io/static/v1?label=TeamUnixx&message=devs&color=critical)](https://t.me/UnixxDevs)
* [Lonami](https://github.com/Lonami) for [Telethon](https://github.com/LonamiWebs/Telethon)
