# Skribblio-cheater

Skribblio-cheater is in the beginning stages of development. Currently it only consists of a basic Click based CLI.

Soon it will be able to help users in guessing words in the game [Skribbl](https://scribble-io.online/).

## Goals for Skribblio-cheater

1. Help me beat my friends when playing Skribbl.
2. Learn more about python packaging. Once complete I plan on publishing skribblio-cheater to [PyPi](https://pypi.org/) so that it can easily be installed in the command line with pip.

## Requirements

* Python 3
* Click (7.1.2)
* [virtualenv](https://virtualenv.pypa.io/en/latest/) (for development and testing)

## Setup

[clone](https://github.com/git-guides/git-clone) the repository: git clone https://github.com/RoryWirch/skribblio-cheater.git

### Install via pip

1. run the command: pip install -e .
2. skribblio-cheater can now be run from the command line by typing "cheater"

####or

### Run on Docker

1. Download and install [Docker](https://docs.docker.com/get-docker/)
2. Build the docker image: docker build -t skribblio-cheater .
3. Run the new docker image: docker run -it skribblio-cheater cheater
