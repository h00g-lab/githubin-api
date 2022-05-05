from flask import Response
from flask_restx import Namespace, Resource
from io import BytesIO
from zipfile import ZipFile
import lizard
import os
import requests

api = Namespace("", description="Github integration")

@api.route('/<string:username>/<string:repository>')
class GithubIntegration(Resource):
    def get(self, username, repository):
        resp = requests.get(f"https://api.github.com/repos/{username}/{repository}/zipball/master?recursive=1")

        try:
            with ZipFile(BytesIO(resp.content)) as zf:
                zf.extractall(f'__temp_code/{username}/{repository}');

            result = os.popen(f"lizard ./__temp_code/{username}/{repository}").read().splitlines()
            return result;

        except Exception as error:
            return Response(str(error), status=500)