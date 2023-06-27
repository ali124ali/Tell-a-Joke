from abc import ABC, abstractmethod
import requests
import ast
from os import system
from time import sleep

# -------------------------------- abstractor class -----------------------------------

class Joke(ABC):

    @abstractmethod
    def get_random_joke(self):
        pass
        

# ---------------------------------- Humaor Jokes --------------------------------------

class Humor_jokes(Joke):

    def get_random_joke(self):

        url = "https://humor-jokes-and-memes.p.rapidapi.com/jokes/random"

        querystring = {"max-length":"200","include-tags":"one_liner","min-rating":"7","exclude-tags":"nsfw","keywords":"rocket"}

        headers = {
            "X-RapidAPI-Key": "ba8bf3b2b8msh37bd724d52be8b9p1369d2jsn9ae8de731a74",
            "X-RapidAPI-Host": "humor-jokes-and-memes.p.rapidapi.com"
        }

        self.response = requests.get(url, headers=headers, params=querystring)

        if self.status():
            self.response = self.response.json()

            print(f">>>> {self.response['joke']}\nha ha ha ...\n\n\n")
            print("\n******************************************************\n\n")

        else:
            print("------- Sorry! Somting Went Wrong We'll Fix It ASAP :( !!! -------\n\n")

    def status(self):
        if self.response.status_code == 200:
            return True

        return False

# ---------------------------------- Joke by Ninjas --------------------------------------

class Jokes_by_ninjas(Joke):

    def get_random_joke(self):

        url = "https://jokes-by-api-ninjas.p.rapidapi.com/v1/jokes"

        headers = {
            "X-RapidAPI-Key": "ba8bf3b2b8msh37bd724d52be8b9p1369d2jsn9ae8de731a74",
            "X-RapidAPI-Host": "jokes-by-api-ninjas.p.rapidapi.com"
        }

        self.response = requests.get(url, headers=headers)

        if self.status():
            self.response = ast.literal_eval(self.response.text)
            
            print(f"### {self.response[0]['joke']}\n\n")
            print("\n******************************************************\n\n")

        else:
            print("------- Sorry! Somting Went Wrong We'll Fix It ASAP :( !!! -------\n\n")

    def status(self):
        if self.response.status_code == 200:
            return True

        return False

# ---------------------------------- Dad Jokes --------------------------------------

class Dad_jokes(Joke):

    def get_random_joke(self):

        url = "https://dad-jokes.p.rapidapi.com/random/joke"

        headers = {
            "X-RapidAPI-Key": "ba8bf3b2b8msh37bd724d52be8b9p1369d2jsn9ae8de731a74",
            "X-RapidAPI-Host": "dad-jokes.p.rapidapi.com"
        }

        self.response = requests.get(url, headers=headers)

        if self.status():
            self.response = self.response.json()['body'][0]

            print(f"++ {self.response['setup']}\n")
            print(f"-- {self.response['punchline']}\n:-|")
            print("\n******************************************************\n\n")
  
        else:
            print("------- Sorry! Somting Went Wrong We'll Fix It ASAP :( !!! -------\n\n")

    def status(self):
        if self.response.status_code == 200:
            return True

        return False

# ---------------------------------- Select Joker --------------------------------------

class Humourist:
    def __init__(self, source):
        self.source = source

        self.tell_joke()

    def tell_joke(self):
        system('clear')

        if self.source == 'h':
            print('Today Joke Is:\n\n')

            Today_Joke = Humor_jokes()
            Today_Joke.get_random_joke()

        elif self.source == 'n':
            print('Today Joke Is:\n\n')

            Today_Joke = Jokes_by_ninjas()
            Today_Joke.get_random_joke()

        elif self.source == 'd':
            print('Today Joke Is:\n\n')
            
            Today_Joke = Dad_jokes()
            Today_Joke.get_random_joke()

        else:
            print("-------------- You Select Wrong Option :( --------------\n")


# ---------------------------------- Settings -------------------------------------

if __name__ == "__main__":

    system('clear')
    print('\n-------------- Wellcome To Joker API --------------\n')

    while True:
        source = input('Please Select One Joker:\nHumor Jokes -->> (h)\nNinjas Jokes -->> (n)\nDad Jokes -->> (d)\nExit -->> (x)\nYour Choice: ')

        if source == 'x':
            print('-------------- Please Come Back Soon :) --------------\n\t\t  By Ali Dehkhodaei')
            sleep(2)
            system('clear')

            break

        else:
            Humourist(source)