'''
Copyright 2021 @Rory Wirch

Determines the skribblio cheater CLI logic.
'''
import click

@click.command()
@click.option('--token', help='This is the word you are trying to guess.')
@click.option('--words', default='resources/word-list.txt',
                help='This is the source for the word list. The tool includes Skribblio\'s default word list.')
def main(token, words):
    '''
    Skribblio cheater is meant to help you guess words in the online game skribbl found here:
    https://skribbl.io/?S9as0Nx6PeYN
    '''
    click.echo('token: %s' % token)
    click.echo('word list: %s' % words)