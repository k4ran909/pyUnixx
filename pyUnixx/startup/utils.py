from importlib import util
from sys import modules

# for addons


def load_addons(plugin_name):
    if plugin_name.startswith("__"):
        return
    from .. import HNDLR, LOGS, asst, udB, unixx_bot
    from .._misc import _supporter as xxx
    from .._misc._assistant import asst_cmd, callback, in_pattern
    from .._misc._decorators import unixx_cmd
    from .._misc._supporter import Config, admin_cmd, sudo_cmd
    from .._misc._wrappers import eod, eor
    from ..configs import Var
    from ..dB._core import HELP

    path = "addons/" + plugin_name
    name = path.replace("/", ".").replace("\\", ".")
    spec = util.spec_from_file_location(name, path + ".py")
    mod = util.module_from_spec(spec)
    mod.LOG_CHANNEL = udB.get_key("LOG_CHANNEL")
    mod.udB = udB
    mod.asst = asst
    mod.tgbot = asst
    mod.unixx_bot = unixx_bot
    mod.ub = unixx_bot
    mod.bot = unixx_bot
    mod.unixx = unixx_bot
    mod.borg = unixx_bot
    mod.telebot = unixx_bot
    mod.jarvis = unixx_bot
    mod.friday = unixx_bot
    mod.eod = eod
    mod.edit_delete = eod
    mod.LOGS = LOGS
    mod.in_pattern = in_pattern
    mod.hndlr = HNDLR
    mod.handler = HNDLR
    mod.HNDLR = HNDLR
    mod.CMD_HNDLR = HNDLR
    mod.Config = Config
    mod.Var = Var
    mod.eor = eor
    mod.edit_or_reply = eor
    mod.asst_cmd = asst_cmd
    mod.unixx_cmd = unixx_cmd
    mod.on_cmd = unixx_cmd
    mod.callback = callback
    mod.Redis = udB.get_key
    mod.admin_cmd = admin_cmd
    mod.sudo_cmd = sudo_cmd
    mod.HELP = HELP.get("Addons", {})
    mod.CMD_HELP = HELP.get("Addons", {})
    modules["ub"] = xxx
    modules["var"] = xxx
    modules["jarvis"] = xxx
    modules["support"] = xxx
    modules["userbot"] = xxx
    modules["telebot"] = xxx
    modules["fridaybot"] = xxx
    modules["jarvis.utils"] = xxx
    modules["uniborg.util"] = xxx
    modules["telebot.utils"] = xxx
    modules["userbot.utils"] = xxx
    modules["userbot.events"] = xxx
    modules["jarvis.jconfig"] = xxx
    modules["userbot.config"] = xxx
    modules["fridaybot.utils"] = xxx
    modules["fridaybot.Config"] = xxx
    modules["userbot.uniborgConfig"] = xxx
    spec.loader.exec_module(mod)
    modules["addons." + plugin_name] = mod
    doc = (
        modules[f"addons.{plugin_name}"].__doc__.format(i=HNDLR)
        if modules[f"addons.{plugin_name}"].__doc__
        else ""
    )
    if "Addons" in HELP.keys():
        update_cmd = HELP["Addons"]
        try:
            update_cmd.update({plugin_name: doc})
        except BaseException:
            pass
    else:
        try:
            HELP.update({"Addons": {plugin_name: doc}})
        except BaseException as em:
            pass
