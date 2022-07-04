from flask import Response
from flask_restx import Namespace, Resource
from io import BytesIO
from zipfile import ZipFile
import lizard
import os
import requests
import shutil
import asyncio
from serializers import Lizard

api = Namespace("", description="Github integration")

async def fetch(url):
    async with aiohttp.ClientSession() as session, async_timeout.timeout(10):
        async with session.get(url) as response:
            return await response.text()


@api.route('/<string:username>/<string:repository>')
class GithubIntegration(Resource):
    def get(self, username, repository):

        resp = loop.run_until_complete(asyncio.gather(
            fetch(f"https://api.github.com/repos/{username}/{repository}/zipball")
        ))
        
        try:
            with ZipFile(BytesIO(resp.content)) as zf:
                zf.extractall(f'__temp_code/{username}/{repository}');

            result = os.popen(f"lizard ./__temp_code/{username}/{repository}").read().splitlines()

            shutil.rmtree(f"__temp_code/", ignore_errors=True)

            parsed_result = Lizard(result)
            return parsed_result.__dict__;

        except Exception as error:
            return Response(str(error), status=500)
