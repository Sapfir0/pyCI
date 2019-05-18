import requests
import string
import random
import timeit

port = "7080"
url = "http://localhost:"+port

routes = "/register", "/signIn", "/post/1"


def getMethods():
    for i in routes:
        req = requests.get(url+i)
        print(req.status_code)
        if (req.status_code != 200):
            print("GET запрос провалился на " + url+i)
            return False
    # for j in range(1, 999999999, 1):
    #     articlePages = "/post/" + str(j)
    #     print(url+articlePages)
    #     req = requests.get(url+articlePages)
    #     if (req.status_code != 200): #надо добавить ответ
    #         print("У нас на сайте " + str(j) + " страниц со статьями!")
    #         break

    return True



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


def postArticle(header,disclaimer,content, authorId):
    req = requests.post(url+"/createArticle", data  = {"header": header, 
                                                        "disclaimer": disclaimer, 
                                                        "content": content,
                                                        "authorId": authorId })
    # if (req.status_code != 200): #на нашем сайте это реализовано как говно
    #     print("Статья не отправлена")
    #     return False
#timeToOneIterationUsers, timeToOneIterationArticles

def stressUsers(countUsers):
    for i in range(1, countUsers):
        randomEmail = stringGenerator(random.randint(7, 20))+"@mail.ru"
        randomLogin = stringGenerator(random.randint(5, 15))
        randomPassword = stringGenerator(random.randint(5, 25))
        t = timeit.Timer(lambda: register(randomEmail, randomLogin, randomPassword))
        print("Юзер №" + str(i) + " пошел. Время выполнения " + str(t.timeit(number=1)) )
           

def stessArticles(countArticles):
    for i in range(1, countArticles):
        randomHeader = stringGenerator(random.randint(20, 65))
        randomDisclaymer = stringGenerator(random.randint(20,200))
        randomContent = stringGenerator(random.randint(1000, 20000))
        randomAuthorId = random.randint(0,200)
        t = timeit.Timer(lambda: postArticle(randomHeader, randomDisclaymer, randomContent, randomAuthorId))
        print("Статья №" + str(i) + " написана. Время выполнения " + str(t.timeit(number=1)))
        




def runStressTest():
    signIn()
    stessArticles(45)

# getMethods()
runStressTest()
