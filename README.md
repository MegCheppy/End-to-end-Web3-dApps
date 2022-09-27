# Smart Contract Dapp
This is an end-to-end Web3 dapp on the Algorand Blockchain that will help 10 Academy organization generate and distribute Non-Fungible Tokens (NFTs) as certificates that will represent the successful completion of a weekly challenge to trainees, and allow trainees with NFTs to interact with a smart contract to perform pre-defined actions. 

# Requirements for devs
To develop this, you need python 3.6 or higher and install in a virtual environment.

Sut up venv (one time)
- python3 -m venv venv

Activate venv:

- . venv/bin/activate (if your shell is bash/zsh)
- . venv/bin/activate.fish (if your shell is fish)

Install dependencies:

- pip install -r requirements.txt

Run tests:
- First, start an instance of sandbox (requires Docker): ./sandbox up nightly
- pytest
- When finished, the sandbox can be stopped with ./sandbox down
