import requests

categories = {"General Knowledge": 9, 
              "Film": 11,
              "Music": 12,
              "Video Games": 15,
              "Science": 17,
              "Computers": 18,
              "Maths": 19,
              "Sports": 21,
              "History": 23,
              "Celebrities": 26}

difficulties = {"easy", "medium", "hard"}
number_of_questions = [50, 40, 30, 20, 10]

class Data:
    
    def __init__(self):
        self.category = ""
        self.difficulty = ""
        self.urls = []

    def create_api(self):
        while self.category not in categories.keys():
            print("Select a category from the given categories")
            for i,j in zip(range(1, len(categories)), categories.keys()):
                print(f"{i}: {j}")
            self.category = input("   ").title().strip()
        
        while self.difficulty not in difficulties:
            self.difficulty = input(f"Select the difficulty ({'/'.join(difficulties).capitalize()}): ").lower().strip()

        self.urls = [f"https://opentdb.com/api.php?amount={i}&category={categories[self.category]}&difficulty={self.difficulty}&type=boolean" for i in number_of_questions]

    def generate_data(self):
        for url in self.urls:
            response = requests.get(url)
            data = response.json()
            if data["response_code"] == 0:
                return data['results']
