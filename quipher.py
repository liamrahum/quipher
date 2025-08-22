import logging
from rich.logging import RichHandler
import os
from art import tprint

logging.basicConfig(
    level="DEBUG", format="%(message)s", datefmt="[%X]", handlers=[RichHandler()]
)

### TODO: Detect OS
### Fetch AI websites list (ChatGPT, Perplexity, etc)

### Enable Mullvad 'All' DNS (Block Social Medias)

### 

def main():
    logger = logging.getLogger("quipher")
    tprint("Quipher")
    
if __name__ == "__main__":
    main()
