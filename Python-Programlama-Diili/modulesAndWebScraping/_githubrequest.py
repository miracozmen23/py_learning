import requests


class Github:
    def __init__(self):
        self.api_url = 'https://api.github.com'
        self.token = 'tokentokentoken'
        
    def getUser(self,username):
        response = requests.get(self.api_url + '/users/' + username)
        return response.json()
    
    def getRepositories(self,username):
        response = requests.get(self.api_url + '/users/' + username + '/repos')
        return response.json()
    
    def createRepository(self,name):
        response = requests.get(self.api_url + '/users/repos?access_token='+ self.token,json={})
        return response.json()
        
        
github = Github()

while(True):
    print("Menü".center(50,'*'))
    secim = input("1-Find Users\n2-Get Repos\n3-Create Repository\n4-Exit\nSeçim:")
    if secim == '1':
        username = input("Username: ")
        result = github.getUser(username) 
        print(f"name: {result['name']} public repos: {result['public_repos']} followers: {result['followers']}")   
    
    elif secim == '2':
        username = input('Username: ')
        result = github.getRepositories(username)
        for repo in result:
            print(repo['name'])
    elif secim == '3':
        name = input('repository name: ')
        result = github.createRepository(name)
    elif secim == '4':
        break
    else:
        print("hatalı seçim yaptınız")