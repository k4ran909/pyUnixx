import sys

from .version import __version__

run_as_module = False

if sys.argv[0] == "-m":
    run_as_module = True

    import time

    from .configs import Var
    from .startup import *
    from .startup._database import UnixxDB
    from .startup.BaseClient import UnixxClient
    from .startup.connections import session_file, vc_connection
    from .startup.funcs import _version_changes, autobot, enable_inline, update_envs
    from .version import unixx_version

    start_time = time.time()
    _ult_cache = {}

    udB = UnixxDB()
    update_envs()

    LOGS.info(f"Connecting to {udB.name}...")
    if udB.ping():
        LOGS.info(f"Connected to {udB.name} Successfully!")

    BOT_MODE = udB.get_key("BOTMODE")
    DUAL_MODE = udB.get_key("DUAL_MODE")

    if BOT_MODE:
        if DUAL_MODE:
            udB.del_key("DUAL_MODE")
            DUAL_MODE = False
        unixx_bot = None
    else:
        unixx_bot = UnixxClient(
            session_file(LOGS),
            udB=udB,
            app_version=unixx_version,
            device_model="Unixx",
            proxy=udB.get_key("TG_PROXY"),
        )

    if not BOT_MODE:
        unixx_bot.run_in_loop(autobot())
    else:
        if not udB.get_key("BOT_TOKEN"):
            LOGS.critical(
                '"BOT_TOKEN" not Found! Please add it, in order to use "BOTMODE"'
            )

            sys.exit()

    asst = UnixxClient(None, bot_token=udB.get_key("BOT_TOKEN"), udB=udB)

    if BOT_MODE:
        unixx_bot = asst
        if udB.get_key("OWNER_ID"):
            try:
                unixx_bot.me = unixx_bot.run_in_loop(
                    unixx_bot.get_entity(udB.get_key("OWNER_ID"))
                )
            except Exception as er:
                LOGS.exception(er)
    elif not asst.me.bot_inline_placeholder:
        unixx_bot.run_in_loop(enable_inline(unixx_bot, asst.me.username))

    vcClient = vc_connection(udB, unixx_bot)

    _version_changes(udB)

    HNDLR = udB.get_key("HNDLR") or "."
    DUAL_HNDLR = udB.get_key("DUAL_HNDLR") or "/"
    SUDO_HNDLR = udB.get_key("SUDO_HNDLR") or HNDLR
else:
    print("pyUnixx 2024 © TeamUnixx")

    from logging import getLogger

    LOGS = getLogger("pyUnixx")

    unixx_bot = asst = udB = vcClient = None
