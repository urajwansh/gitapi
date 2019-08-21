from django.shortcuts import render
from django import forms
from django.http import HttpResponse
import json
import requests


def api_Result(request):
    parameters = {'q': 'user:google', 'sort': 'stars', 'order': 'desc'}
    # api_url = 'https://api.github.com/search/repositories?q=user:google&sort=stars&order=desc'
    api_url = 'https://api.github.com/search/repositories'

    response = requests.get(api_url, parameters)
    json_response = response.json()
    json_dump = []
    for i in range(3):
        json_dump.append(
                            {
                                "name":json_response['items'][i]['name'],
                                "stars":json_response['items'][i]['stargazers_count']
                            }
                        )

    formatted_response = {"results":json_dump}
    return HttpResponse(json.dumps(formatted_response), content_type="application/json")


def homepage(request):
    return HttpResponse("Hello World")