# -*- coding: utf-8 -*-

"""
jishaku.repl
~~~~~~~~~~~~

Repl-related operations and tools for Jishaku.

:copyright: (c) 2019 Devon (Gorialis) R
:license: MIT, see LICENSE for more details.

"""

from discord.ext import commands

# pylint: disable=wildcard-import
from jishaku.repl.compilation import *  # noqa: F401
from jishaku.repl.inspections import all_inspections  # noqa: F401
from jishaku.repl.scope import *  # noqa: F401


def get_var_dict_from_ctx(ctx: commands.Context):
    """
    Returns the dict to be used in REPL for a given Context.
    """

    vardict =  {
        'me': ctx.author,
        'fire': ctx.bot,
        'self': ctx.bot.get_cog('Jishaku'),
        'ksoft': ctx.bot.ksoft,
        'channel': ctx.channel,
        'ctx': ctx,
        'guild': ctx.guild,
        'message': ctx.message
    }
    vardict.update({k: getattr(ctx.bot, k) for k in dir(ctx.bot)})
    return vardict
