#!/usr/bin/env python
from io import TextIOWrapper
import logging
from rich.logging import RichHandler
import os
import shutil
import sys
import ctypes
from time import sleep
logging.basicConfig(
    level="DEBUG", format="%(message)s", datefmt="[%X]", handlers=[RichHandler()]
)

### TODO: Make script OS agnostic
### Save task beggining time & end time

AI_SITES = [
    "ahrefs.com",
    "aichatting.net",
    "aichattings.com",
    "aistorygenerator.org",
    "app.brainchat.ai",
    "askaichat.app",
    "askcodi.com",
    "bard.google.com",
    "boomy.com",
    "cat-gpt.com",
    "character.ai",
    "chatbotgpt.fr",
    "chatbox.botnation.ai",
    "chatgbt.one",
    "chatgpt.com",
    "chatgptfrance.net",
    "chatgptgratuit.org",
    "chatgptt.me",
    "chatgptx.com",
    "chat.hix.ai",
    "chat.mistral.ai",
    "chaton.ai",
    "chatopenai.de",
    "claude.ai",
    "codegpt.co",
    "copilot.microsoft.com",
    "copilot-proxy.githubusercontent.com",
    "craiyon.com",
    "crushon.ai",
    "deepai.org",
    "deepl.com",
    "deepseek.com",
    "deepseekv3.net",
    "deepseek.me",
    "deepstory.ai",
    "docsbot.ai",
    "dreamily.ai",
    "elevenlabs.io",
    "flatai.org",
    "galaxy.ai",
    "gemini.google.com",
    "genmo.ai",
    "githubcopilot.com",
    "gpt3demo.com",
    "gpt4free.io",
    "gptchatly.com",
    "gptfree.co",
    "gptwhisperer.com",
    "heck.ai",
    "hix.ai",
    "hotbot.com",
    "hyperwriteai.com",
    "inferkit.com",
    "infinite-story.com",
    "llama2.ai",
    "meta.ai",
    "minitoolai.com",
    "monica.im",
    "musely.ai",
    "narraive.com",
    "novelai.net",
    "o1gpt.org",
    "openai.com",
    "origin-tracker.githubusercontent.com",
    "pentestgpt.ai",
    "perchance.org",
    "perplexity.ai",
    "personal.ai",
    "philosopherai.com",
    "pi.ai",
    "playform.io",
    "plottr.com",
    "poe.com",
    "riffusion.com",
    "runwayml.com",
    "rytr.me",
    "sassbook.com",
    "search.brave.com",
    "shortlyai.com",
    "simplified.com",
    "smodin.io",
    "squibler.io",
    "stablediffusionweb.com",
    "storybokai.app",
    "sudowrite.com",
    "sydney.bing.com",
    "tabnine.com",
    "talkai.info",
    "talkie-ai.com",
    "talkto.ai",
    "talkto-api.pfpmaker.workers.dev",
    "talktoo.ai",
    "talktotransformer.com",
    "textsynth.com",
    "toolbaz.com",
    "toolsaday.com",
    "typli.ai",
    "writeholo.com",
    "writeme.ai",
    "writerhand.com",
    "writesonic.com",
    "you.com",
    "grok.com",
    "huggingface.co",
    "hugging-face.org",
    "anthropic.com",
]

SOCIAL_MEDIAS = ["instagram.com", "facebook.com", "meta.com", "tiktok.com"]


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


def backup_hosts():
    shutil.copy(
        r"C:/Windows/System32/drivers/etc/hosts",
        r"C:/Windows/System32/drivers/etc/hosts.quipher.bak",
    )

def block_task(file, list):
    for site in list:
        file.write(f"127.0.0.55\t{site}\n")
        file.write(f"127.0.0.55\twww.{site}\n")

def block_sites(file: TextIOWrapper):
    logger = logging.getLogger("quipher")
    block_task(file,AI_SITES)
    logger.info("Successfully blocked AI")
    block_task(file, SOCIAL_MEDIAS)        
    logger.info("Successfully blocked social medias")


def unblock_sites():
    shutil.move(
        r"C:/Windows/System32/drivers/etc/hosts.quipher.bak",
        r"C:/Windows/System32/drivers/etc/hosts",
    )

def get_disable_quipher():
    return os.path.exists(r'C:/Windows/System32/drivers/etc/hosts.quipher.bak')

def print_logo():
    print('  ___          _         _                 ')
    print(' / _ \  _   _ (_) _ __  | |__    ___  _ __ ')
    print("| | | || | | || || '_ \ | '_ \  / _ \| '__|")
    print('| |_| || |_| || || |_) || | | ||  __/| |   ')
    print(' \__\_\ \__,_||_|| .__/ |_| |_| \___||_|   ')
    print('                 |_|                       ')

def main():
    logger = logging.getLogger("quipher")
    print_logo()
    if get_disable_quipher():
        unblock_sites()
        logger.info("Successfully unblocked sites")
        input("Press Enter to quit")
        return
    backup_hosts()
    with open('C:/Windows/System32/drivers/etc/hosts', 'a+') as hosts:
        block_sites(hosts)

    input("Press Enter to quit")

if __name__ == "__main__":
    if is_admin():
        main()
    else:
        ctypes.windll.shell32.ShellExecuteW(
            None, "runas", sys.executable, " ".join(sys.argv), None, 1
        )
