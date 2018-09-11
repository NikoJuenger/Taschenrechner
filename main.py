import requests
print("Hello World!")


def request_git():
    url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'

    r = requests.get(url)

    # Statuscode 200 == ok
    print(r.status_code)
    # Save the response
    response_dict = r.json()
    print(response_dict.keys())

    print("Incomplete result? ", response_dict['incomplete_results'])
    if response_dict['incomplete_results']:
        print("Total repositorys: ", response_dict['total_count'])
    else:
        print("Total repositorys: ", response_dict['total_count'])


request_git()
