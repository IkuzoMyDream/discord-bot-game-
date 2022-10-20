#author wildan phidrai-ngam
#self study project
import discord
from discord.ext import commands
from pistonapi import PistonAPI
import random

token = ""
bot = commands.Bot(command_prefix=".", status=discord.Status.idle, intents=discord.Intents.all(),help_command=None)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

# เอาบอทออก
@bot.command()
async def leave(ctx):
    del players[ctx.guild.id]
    await ctx.voice_client.disconnect()

#บอกคำสั่งทั้งหมด
@bot.command()
async def help(ctx):
    emBed = discord.Embed(title="เกมทั้งหมด", description="รวบรวมเกมทั้งหมดที่ได้จัดทำเอาไว้", color=0xc48bd0)
    emBed.add_field(name=".help", value="เกมทั้งหมด", inline="False")
    emBed.add_field(name=".run ภาษา ```โค้ด```", value="เขียนโค้ด", inline="False")
    emBed.add_field(name=".xo", value="เกม xo", inline="False")
    emBed.add_field(name=".place ตำเเหน่ง", value="เขียน xo ในตำเเหน่งที่ต้องการ", inline="False")
    emBed.add_field(name=".leave", value="ออกจากห้อง", inline="False")
    emBed.set_thumbnail(url='https://divedigital.id/wp-content/uploads/2022/07/Anya-Forger-PFP-PROFILE-PICTURE.jpg')
    emBed.set_footer(text="FRXXSTYLE", icon_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS2kgyYQ47TkWp_PYCUL2TJC3x_QCdth5xChmrvHD-8LEF79sA0X46zY_AtRuDwvqPj2X0&usqp=CAU')
    await ctx.channel.send(embed=emBed)


piston = PistonAPI()

pAliases = {'sh': 'bash', 'bf': 'brainfuck', 'clojure': 'clojure', 'clj': 'clojure', 'cob': 'cobol',
            'coffeescript': 'coffeescript', 'coffee': 'coffeescript', 'crystal': 'crystal', 'cr': 'crystal',
            'dash': 'dash', 'ts': 'typescript', 'node-ts': 'typescript', 'tsc': 'typescript',
            'node-javascript': 'javascript', 'node-js': 'javascript', 'javascript': 'javascript', 'js': 'javascript',
            'cs': 'mono', 'csharp': 'mono', 'elixir': 'elixir', 'exs': 'elixir', 'emacs': 'emacs', 'el': 'emacs',
            'elisp': 'emacs', 'erlang': 'erlang', 'erl': 'erlang', 'escript': 'erlang', 'gawk': 'awk', 'gcc': 'c',
            'cpp': 'c++', 'g++': 'c++', 'gdc': 'd', 'fortran': 'fortran', 'f90': 'fortran', 'go': 'go', 'golang': 'go',
            'golfscript': 'golfscript', 'groovy': 'groovy',
            'gvy': 'groovy', 'haskell': 'haskell', 'hs': 'haskell', 'jl': 'julia', 'kt': 'kotlin', 'lisp': 'lisp',
            'cl': 'lisp', 'sbcl': 'lisp', 'commonlisp': 'lisp', 'lol': 'lolcode', 'lci': 'lolcode', 'lua': 'lua',
            'asm': 'nasm', 'nasm32': 'nasm', 'asm64': 'nasm64', 'nim': 'nim', 'ocaml': 'ocaml', 'ml': 'ocaml',
            'matlab': 'octave', 'm': 'octave', 'osabie': 'osabie', '05AB1E': 'osabie', 'usable': 'osabie',
            'paradoc': 'paradoc', 'pascal': 'pascal', 'freepascal': 'pascal', 'pp': 'pascal', 'pas': 'pascal',
            'perl': 'perl', 'pl': 'perl', 'php8': 'php', 'html': 'php', 'pony': 'ponylang', 'ponyc': 'ponylang',
            'prolog': 'prolog', 'plg': 'prolog', 'pyth': 'pyth', 'py2': 'python2', 'python2': 'python2', 'py': 'python',
            'py3': 'python', 'python3':
                'python', 'raku': 'raku', 'rakudo': 'raku', 'perl6': 'raku', 'p6': 'raku', 'pl6': 'raku',
            'rock': 'rockstar', 'rocky': 'rockstar', 'ruby3': 'ruby', 'rb': 'ruby', 'rs': 'rust', 'sc': 'scala',
            'swift': 'swift', 'v': 'vlang', 'yeethon3': 'yeethon', 'zig': 'zig', 'cow': 'cow', 'bash': 'bash',
            'brainfuck': 'brainfuck', 'cjam': 'cjam', 'cobol': 'cobol', 'dart': 'dart', 'typescript': 'typescript',
            'dotnet': 'dotnet', 'dragon': 'dragon', 'awk': 'awk', 'c': 'c', 'c++': 'c++', 'd': 'd', 'java': 'java',
            'jelly': 'jelly', 'julia': 'julia', 'kotlin': 'kotlin', 'lolcode': 'lolcode', 'mono': 'mono',
            'nasm': 'nasm', 'nasm64': 'nasm64', 'octave': 'octave', 'php': 'php', 'ponylang': 'ponylang',
            'pure': 'pure', 'python': 'python', 'rockstar': 'rockstar', 'ruby': 'ruby', 'rust': 'rust',
            'scala': 'scala', 'vlang': 'vlang', 'yeethon': 'yeethon'}

@bot.command()
async def run(ctx, n, *, code):
    nm = n.lower()
    a = code.replace("```", "")

    try:
        b = (piston.execute(language=nm, version=piston.runtimes[pAliases[nm]]["version"], code=a))
        c = str(b)
        em = discord.Embed(title=f'{pAliases[nm]} code Output!',
                           description=f'```{pAliases[nm]}\nOutput:\n{c}```',
                           color=discord.Color.red())
        await ctx.send(embed=em)
    except Exception as e:
        print(e)
        await ctx.send("**ใจเย็น ๆไอหนุ่ม ยังไม่รับรองภาษานี้!**")

# เกม xo -----------------------------------------------------------------------------------------------

player1 = ""
player2 = ""
turn = ""
gameOver = True

board = []

winningConditions = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]


@bot.command()
async def xo(ctx, p1: discord.Member, p2: discord.Member):
    global player1
    global player2
    global turn
    global gameOver
    global count

    if gameOver:
        global board
        board = [":white_large_square:", ":white_large_square:", ":white_large_square:",
                 ":white_large_square:", ":white_large_square:", ":white_large_square:",
                 ":white_large_square:", ":white_large_square:", ":white_large_square:"]
        turn = ""
        gameOver = False
        count = 0

        player1 = p1
        player2 = p2

        # print the board
        line = ""
        for x in range(len(board)):
            if x == 2 or x == 5 or x == 8:
                line += " " + board[x]
                await ctx.send(line)
                line = ""
            else:
                line += " " + board[x]

        # determine who goes first
        num = random.randint(1, 2)
        if num == 1:
            turn = player1
            await ctx.send("It is <@" + str(player1.id) + ">'s turn.")
        elif num == 2:
            turn = player2
            await ctx.send("It is <@" + str(player2.id) + ">'s turn.")
    else:
        await ctx.send("A game is already in progress! Finish it before starting a new one.")


@bot.command()
async def place(ctx, pos: int):
    global turn
    global player1
    global player2
    global board
    global count
    global gameOver

    if not gameOver:
        mark = ""
        if turn == ctx.author:
            if turn == player1:
                mark = ":regional_indicator_x:"
            elif turn == player2:
                mark = ":o2:"
            if 0 < pos < 10 and board[pos - 1] == ":white_large_square:":
                board[pos - 1] = mark
                count += 1

                # print the board
                line = ""
                for x in range(len(board)):
                    if x == 2 or x == 5 or x == 8:
                        line += " " + board[x]
                        await ctx.send(line)
                        line = ""
                    else:
                        line += " " + board[x]

                checkWinner(winningConditions, mark)
                print(count)
                if gameOver == True:
                    await ctx.send(mark + " wins!")
                elif count >= 9:
                    gameOver = True
                    await ctx.send("It's a tie!")

                # switch turns
                if turn == player1:
                    turn = player2
                elif turn == player2:
                    turn = player1
            else:
                await ctx.send("Be sure to choose an integer between 1 and 9 (inclusive) and an unmarked tile.")
        else:
            await ctx.send("It is not your turn.")
    else:
        await ctx.send("Please start a new game using the .xo command.")

def checkWinner(winningConditions, mark):
    global gameOver
    for condition in winningConditions:
        if board[condition[0]] == mark and board[condition[1]] == mark and board[condition[2]] == mark:
            gameOver = True

@bot.command()
async def tictactoe_error(ctx, error):
    print(error)
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please mention 2 players for this command.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Please make sure to mention/ping players (ie. <@688534433879556134>).")


@bot.command()
async def place_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please enter a position you would like to mark.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Please make sure to enter an integer.")

bot.run('#ใส่ token here')
