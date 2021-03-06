@client.command()
async def cp(ctx, projectname):
    await ctx.channel.purge(limit=1)
    channels = ['sources', 'to-do-list', 'suggestions', 'known-bugs', 'general', 'bot-commands']

    await ctx.guild.create_role(name=f"{projectname} Founder", mentionable=True)
    await ctx.guild.create_role(name=f"{projectname} Dev", mentionable=True)
    asyncio.sleep(3)
    founder = get(ctx.guild.roles, name=f"{projectname} Founder")
    dev = get(ctx.guild.roles, name=f"{projectname} Dev")
    await ctx.message.author.add_roles(founder)

    bot = get(ctx.guild.roles, name='PDBot')

    overwrites = {
        ctx.guild.default_role: discord.PermissionOverwrite(read_messages=False),
        founder: discord.PermissionOverwrite(manage_channels = False,
                                        read_messages = True,
                                        view_channel = True,
                                        send_messages = True,
                                        send_tts_messages = True,
                                        manage_messages = True,
                                        embed_links = True,
                                        attach_files = True,
                                        read_message_history = True,
                                        manage_roles = False,
                                        manage_permissions = False,
                                        manage_webhooks = True),
        dev: discord.PermissionOverwrite(manage_channels = False,
                                        read_messages = True,
                                        view_channel = True,
                                        send_messages = True,
                                        send_tts_messages = True,
                                        manage_messages = True,
                                        embed_links = True,
                                        attach_files = True,
                                        read_message_history = True,
                                        manage_roles = False,
                                        manage_permissions = False,
                                        manage_webhooks = True),
        bot: discord.PermissionOverwrite(manage_channels = True,
                                        read_messages = True,
                                        view_channel = True,
                                        send_messages = True,
                                        send_tts_messages = True,
                                        manage_messages = True,
                                        embed_links = True,
                                        attach_files = True,
                                        read_message_history = True,
                                        manage_roles = True,
                                        manage_permissions = True,
                                        manage_webhooks = True
                                        )
    }

    await ctx.guild.create_category(f"{projectname} Dev", overwrites=overwrites)
    category = get(ctx.guild.categories, name=f"{projectname} Dev")


    for i in channels:
        await ctx.guild.create_text_channel(i, category=category)
    await ctx.guild.create_voice_channel('chat', category=category)
    await ctx.channel.send(f"Category **{projectname}** created!")
