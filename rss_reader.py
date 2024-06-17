import argparse
import feedparser
import json
from datetime import datetime


def main():
    parser = argparse.ArgumentParser(prog='RSS Reader', description="RSS Reader using Python")
    parser.add_argument('source', metavar='source', type=str, help='Enter de RSS Source')
    parser.add_argument('-j', '--json', help="Enable json output", action='store_true')
    parser.add_argument('-l', '--limit', type=int, help="Enable limit of RSS news")
    args = parser.parse_args()
    source = args.source
    jsn = args.json
    limit = args.limit
    parsing(source, jsn, limit)


# Data formating function
def format_date(date_string):
    if date_string:
        return datetime(*date_string[:6]).strftime('%Y-%m-%d %H:%M:%S')
    return 'Date unavailable'


def parsing(to_parse_url, is_json, limit):
    feed = to_parse_url
    channel_info = {
        'title': feed.feed.get('title', 'Title undefined'),
        'link': feed.feed.get('link', 'Link undefined'),
        'publish_date': format_date(feed.feed.get('published_parsed')),
        'language': feed.feed.get('language', 'Language undefined'),
        'managingEditor': feed.feed.get('managingEditor', 'Editor undefined'),
        'last_build_date': format_date(feed.feed.get('updated_parsed')),
        'categories': [cat['term'] for cat in feed.feed.get('tags', [])],
        'description': feed.feed.get('description', 'Description undefined')
    }

    feed_items = []
    for entry in feed.entries:
        item = {
            'title': entry.get('title', 'Título não disponível'),
            'author': entry.get('author', 'Autor não disponível'),
            'publish_date': format_date(entry.get('published_parsed')),
            'link': entry.get('link', 'Link não disponível'),
            'categories': [cat['term'] for cat in entry.get('tags', [])],
            'description': entry.get('description', 'Descrição não disponível')
        }
        feed_items.append(item)

        if is_json:
            res = to_json(channel_info, feed_items)
            path = "rss_reader.json"
        else:
            res = to_text(channel_info, feed_items)
            path = "rss_reader.txt"

        with open(path, 'w') as file:
            file.write(res)


def to_text(channel_info, feed_items):
    text = f"Título do Canal: {channel_info['title']}\n"
    text += f"Link do Canal: {channel_info['link']}\n"
    text += f"Data de Publicação: {channel_info['publish_date']}\n"
    text += f"Idioma: {channel_info['language']}\n"
    text += f"Editor Responsável: {channel_info['managingEditor']}\n"
    text += f"Última Data de Construção: {channel_info['last_build_date']}\n"
    text += f"Categorias: {', '.join(channel_info['categories'])}\n"
    text += f"Descrição do Canal: {channel_info['description']}\n"
    text += "\nItens do Feed:\n"

    for item in feed_items:
        text += f"  Título: {item['title']}\n"
        text += f"  Autor: {item['author']}\n"
        text += f"  Data de Publicação: {item['publish_date']}\n"
        text += f"  Link: {item['link']}\n"
        text += f"  Categorias: {', '.join(item['categories'])}\n"
        text += f"  Descrição: {item['description']}\n"
        text += "---\n"

    return text


# Função para converter em JSON
def to_json(channel_info, feed_items):
    return json.dumps({
        'channel': channel_info,
        'items': feed_items
    }, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    main()
