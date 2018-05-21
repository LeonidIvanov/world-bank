import json

from flask import (
    Blueprint, render_template
)

from world_bank.db import mongo_db

main = Blueprint('main', __name__)
world_collection = mongo_db.world


@main.route('/')
def index():
    projects_by_countries = dict()
    world_collection_json = world_collection.find()
    for project in world_collection_json:
        if project['countryname'] != project['regionname']:
            if project['countrycode'] in projects_by_countries.keys():
                projects_by_countries[project['countrycode']]['projects'].append({
                    'project_name': project['project_name'],
                    'lendprojectcost': project['lendprojectcost']
                })
                projects_by_countries[project['countrycode']]['sum'] += project['lendprojectcost']
            else:
                projects_by_countries[project['countrycode']] = {
                    'countryname': project['countryname'],
                    'projects': [{
                        'project_name': project['project_name'],
                        'lendprojectcost': project['lendprojectcost']
                    }],
                    'sum': project['lendprojectcost']
                }
    return render_template(
        'choropleth_map/index.html',
        projects_by_countries=json.dumps(projects_by_countries, indent=4))
