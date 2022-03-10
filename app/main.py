from typing import Optional
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi_rss import RSSFeed, RSSResponse, Item, Category, CategoryAttrs
import requests
import json
import re
import datetime

app = FastAPI()


DOCKER_HUB_API_ENDPOINT = 'https://hub.docker.com/v2'

# redirect to swagger documentation


@app.get("/", include_in_schema=False)
async def welcome():
    return RedirectResponse("/docs")


@app.get("/repos/{org}", tags=["docker-hub"])
def get_repos_from_dockerhub(org: str):
    url = f'{DOCKER_HUB_API_ENDPOINT}/repositories/{org}'
    try:
        r = requests.get(url)
        r = json.loads(r.text)
    except Exception as e:
        raise(e)

    result = [x["name"] for x in r["results"]]
    return result


@app.get("/tags/{org}/{repo}", tags=["docker-hub"])
def get_tags_from_dockerrepo(org: str, repo: str, regex: str = None, rss: bool = False, pages: int = 1, page_size: int = 10):
    if org == "_":
        org = "library"

    final = []
    for count in list(range(pages)):
        url = f'{DOCKER_HUB_API_ENDPOINT}/repositories/{org}/{repo}/tags?page_size={page_size}&status=active&currently_tagged=true&page={count+1}'
        try:
            r = requests.get(url)
            r = json.loads(r.text)
            for item in r["results"]:
                docker_pull = f"docker pull {repo}/{org}:{item['name']}"
                if org == "library":
                    docker_pull = f"docker pull {repo}:{item['name']}"
                if regex:
                    if re.match(regex, item["name"]):
                        final.append({"name": item["name"], "last_updated": item["last_updated"], "pull": docker_pull})
                else:
                    final.append({"name": item["name"], "last_updated": item["last_updated"], "pull": docker_pull})
        except Exception as e:
            raise(e)


    feed_data = {
        'title': 'docker-hub-tags',
        'link': 'https://rss.sam-services.de',
        'description': 'An api who list tags for an given docker repository',
        'language': 'en-us',
        'copyright': 'Copyright 2022 S. Warkentin',
        'docs': 'https://rss.sam-services.de/docs',
        'ttl': 3600,
        'item':  [Item(title=f"{repo} {x['name']}", pub_date=x["last_updated"], description=x["pull"]) for x in final]
    }
    
    if rss:
        feed = RSSFeed(**feed_data)
        return RSSResponse(feed)

    return final
