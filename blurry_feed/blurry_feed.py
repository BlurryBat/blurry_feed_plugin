# -*- coding: utf-8 -*-

"""
Copyright (c) BlurryBat <blurrybat2019@gmail.com>

Blurry Feed
---------------
A plugin that lets you subscribe to RSS and Atom Feeds
"""

from __future__ import unicode_literals, print_function

import logging
logger = logging.getLogger(__name__)

from pelican import signals

class BlurryFeed():
    """
        A class created to fetch feed
    """

    def __init__(self, generator):

        import yaml

        self.yaml_file = generator.settings['BLURRY_FEED_YAML']
        with open(self.yaml_file, 'r') as stream:
            try:
                self.sources=yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                logger.warning(exc)
                return None

    def fetch(self):
        """
            returns feed entries
        """

        import feedparser

        entries=[]
        for source in self.sources['sources']:
            NewsFeed = feedparser.parse(source['href'])
            temp_dict={}
            for entry in NewsFeed['entries']:
                entries.append(entry)

        return entries


def fetch_blurry_feed(gen, metadata):
    """
        registered handler for blurry feed plugin
    """

    if 'BLURRY_FEED_YAML' in gen.settings.keys():
        gen.context['blurry_feed'] = gen.plugin_instance.fetch()


def feed_parser_initialization(generator):
    """
        Initialization of feed parser
    """

    generator.plugin_instance = BlurryFeed(generator)


def register():
    """
        Plugin registration
    """

    try:
        signals.article_generator_init.connect(feed_parser_initialization)
        signals.article_generator_context.connect(fetch_blurry_feed)
    except ImportError:
        logger.warning('`blurry_feed` failed to load dependency `feedparser`.'
                       '`blurry_feed` plugin not loaded.')
