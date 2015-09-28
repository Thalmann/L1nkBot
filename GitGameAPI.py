import requests

# Made from the API definition: https://github.com/SickTeam/GitGameServer/wiki/GitGame-definition

git_game_server_url = "some_url"

def create_game(owner, repo, username, token):
    payload = {"owner": owner, "repo": repo, "username": username, "token": token}
    return requests.post(git_game_server_url + "/game", payload)

def get_game(game_id):
    return requests.get(git_game_server_url + "/game/" + game_id + "/setup")

def setup_game(game_id, contributors, exclude_merges, lowercase):
    payload = {"contributors": contributors, "excludeMerges": exclude_merges, "lowerCase": lower_case}
    return requests.post(git_game_server_url + "/game/" + game_id + "/setup", payload)

def get_players(game_id):
    return request.get(git_game_server_url + "/game/" + game_id + "/players")

def add_player(game_id, username
