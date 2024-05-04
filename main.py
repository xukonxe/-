import interactions
# Use the following method to import the internal module in the current same directory
from . import internal_t
import os
# aiofiles module is recommended for file operation
import aiofiles
# 监听interactions.py事件
from interactions.api.events import MessageCreate
# 可以创建后台任务
from interactions import Task, IntervalTrigger


class 五子棋十房间(interactions.Extension):
    module_base: interactions.SlashCommand = interactions.SlashCommand(
        name="进入房间",
        description="进入一个五子棋房间"
    )
    module_group: interactions.SlashCommand = module_base.group(
        name="棋牌室_五子棋",
        description="所有和五子棋有关的命令"
    )

    @module_group.subcommand("ping", sub_cmd_description="Replace the description of this command")
    @interactions.slash_option(
        name = "option_name",
        description = "Option description",
        required = True,
        opt_type = interactions.OptionType.STRING
    )
    async def module_group_ping(self, ctx: interactions.SlashContext, option_name: str):
        await ctx.send(f"Pong {option_name}!")
        internal_t.internal_t_testfunc()

    @module_base.subcommand("pong", sub_cmd_description="Replace the description of this command")
    @interactions.slash_option(
        name = "option_name",
        description = "Option description",
        required = True,
        opt_type = interactions.OptionType.STRING
    )
    async def module_group_pong(self, ctx: interactions.SlashContext, option_name: str):
        # The local file path is inside the directory of the module's main script file
        async with aiofiles.open(f"{os.path.dirname(__file__)}/example_file.txt") as afp:
            file_content: str = await afp.read()
        await ctx.send(f"Pong {option_name}!\nFile content: {file_content}")
        internal_t.internal_t_testfunc()

    
    # The command to start the task
    @module_base.subcommand("test", sub_cmd_description="Start the background task")
    async def module_base_starttask(self, ctx: interactions.SlashContext):
        await ctx.send("Task started")