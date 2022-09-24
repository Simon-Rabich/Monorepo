from octokit import Octokit


def rest_request():
    # Make an unauthenticated request for simon's public repositories
    repos = Octokit().repos.list_for_user(username="Simon-Rabich")
    for repo in repos.json:
        print(repo["name"])


if __name__ == '__main__':
    rest_request()
