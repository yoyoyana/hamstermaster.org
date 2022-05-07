from __future__ import annotations

import datetime
from typing import Optional

def prompt(prompt: str, *, default: Optional[str] = None, optional: bool = False) -> str:
    default_text = f' [{default}]' if default else ' []'
    default_text = default_text if optional else ''

    while True:
        resp = input(f'{prompt}{default_text}: ')
        if not resp and optional:
            return default

        if not optional and not resp:
            continue

        else:
            break
    return resp


def yes_no(prompt: str, *, default: Optional[bool] = False) -> bool:
    y, n = ('Y', 'n') if default is True else ('y', 'N')
    resp = input(f'{prompt} ({y}/{n}) ').lower()
    if  resp in ('y', 'Y') or (default is True and not resp):
        return True
    else:
        return False


print('Welcome to the interactive post generator!')
title = prompt('What would you like to title the post?')

categories = None
categorize = yes_no('Would you like to categorize the post?')
if categorize:
    categories = prompt('What categories does this post belong in? Separate each with a space')

print('Creating post...')

date = datetime.datetime.now().strftime('%Y-%m-%d')
filename_title = title.lower().replace(' ', '-')
filename = f'_posts/{date}-{filename_title}.md'

CONTENT = """
---
title: {title}{tags}
---

Hello! This is a new post.
Feel free to begin writing in this space.

"""

tags = f'\ntags: {categories}' if categories else ''
post_content = CONTENT.format(title=title, tags=tags)

with open(filename, 'w') as f:
    f.write(post_content)

print(f'Done! The file is located at {filename}. You are free to open and edit it.')
