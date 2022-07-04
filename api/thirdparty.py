from flask import Response
from flask_restx import Namespace, Resource
from io import BytesIO
from zipfile import ZipFile
import lizard
import os
import requests
import shutil
import asyncio
import aiohttp
import aiohttp
import async_timeout
from serializers import Lizard

api = Namespace("", description="Github integration")

async def fetch(url):
    return await request.get(url)


@api.route('/<string:username>/<string:repository>')
class GithubIntegration(Resource):
    def get(self, username, repository):

        loop = asyncio.get_event_loop()

        resp = loop.run_until_complete(
            fetch(f"https://api.github.com/repos/{username}/{repository}/zipball")
        )
        
        try:
            with ZipFile(BytesIO(resp.content)) as zf:
                zf.extractall(f'__temp_code/{username}/{repository}');

            result = os.popen(f"lizard ./__temp_code/{username}/{repository}").read().splitlines()

            shutil.rmtree(f"__temp_code/", ignore_errors=True)

            parsed_result = Lizard(result)
            return parsed_result.__dict__;

        except Exception as error:
            return Response(str(error), status=500)
