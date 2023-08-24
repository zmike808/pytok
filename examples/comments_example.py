import json

from pytok.tiktok import PyTok

videos = [
    {
        'id': '7058106162235100462',
        'author': {
            'uniqueId': 'charlesmcbryde'
        }
    }
]

with PyTok(chrome_version=104) as api:
    for video in videos:
        comments = list(
            api.video(
                id=video['id'], username=video['author']['uniqueId']
            ).comments(count=1000)
        )
        with open("out.json", "w") as f:
            json.dump(comments, f)
