import json

from pytok.tiktok import PyTok

def main():
    with PyTok() as api:
        user = api.user(username="therock")

        videos = [video.info() for video in user.videos()]
        with open("out.json", "w") as f:
            json.dump(videos, f)

if __name__ == "__main__":
    main()
