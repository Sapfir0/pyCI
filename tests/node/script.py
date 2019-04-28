import requests
import string
import random

port = "7080"
url = "http://localhost:"+port

routes = "/register", "/signIn", "/post/1"


def getMethods():
    for i in routes:
        req = requests.get(url+i)
        print(req.status_code)
        if (req.status_code != 200):
            print("GET запрос провалился на " + url+i)



def stringGenerator(size=25, chars=string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def register(email, login, password):
    req = requests.post(url+"/register", data  = {"email":email, 
                                                "login": login,
                                                "password": password,
                                                "repassword": password })
    if (req.status_code != 200):
        print("POST запрос провалился на register")                                         
    req = requests.get(url+"/logout")



def signIn():
    req = requests.post(url+"/signIn", data  = {"email":"testingEmail@mail.ru", 
                                                "password": "1234567" })
    if (req.status_code != 200):
        print("Авторизация провалена")
        return False


def postArticle(header,content):
    req = requests.post(url+"/createArticle", data  = {"header": header, 
                                                        "content": content })
    if (req.status_code != 200):
        print("Статья не отправлена")
        return False


def stressUsers(countUsers):
    for i in range(1, countUsers):
        randomEmail = stringGenerator(random.randint(7, 20))+"@mail.ru"
        randomLogin = stringGenerator(random.randint(5, 15))
        randomPassword = stringGenerator(random.randint(5, 25))
        if ( not register(randomEmail, randomLogin, randomPassword) ):
            return False

def stessArticles(countArticles):
    for i in range(1, countArticles):
        randomHeader = stringGenerator(random.randint(20, 65))
        randomContent = stringGenerator(random.randint(5000, 45000))
        if ( not postArticle(randomHeader, randomContent) ):
            return False


def runStressTest():
    stressUsers(1000)
    stessArticles(1000)

# getMethods()
# runStressTest()


