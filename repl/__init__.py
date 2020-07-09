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

    return {
        'me': ctx.author,
        'fire': ctx.bot,
        'self': ctx.bot.get_cog('Jishaku'),
        'MAIN': ctx.bot.get_cog('Main Commands'),
        'MUSIC': ctx.bot.get_cog('Music'),
        'HYPIXEL': ctx.bot.get_cog('Hypixel Commands'),
        'YOUTUBE': ctx.bot.get_cog('YouTube API'),
        'ksoft': ctx.bot.ksoft,
        'UTILS': ctx.bot.get_cog('Utility Commands'),
        'SETTINGS': ctx.bot.get_cog('Settings'),
        'MOD': ctx.bot.get_cog('Mod Commands'),
        'API': ctx.bot.get_cog('Fire API'),
        'PREMIUM': ctx.bot.get_cog('Premium Commands'),
        'channel': ctx.channel,
        'ctx': ctx,
        'guild': ctx.guild,
        'message': ctx.message
    }
