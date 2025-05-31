# import requests
# from bs4 import BeautifulSoup
# class SearchBot:
   
#     def ask_user(self):
#         topic = input("What Python topic do you want to learn about? ").strip().lower()
#         self.search_topic(topic)

    # def search_topic(self, topic):
    #     try:
    #         url = f"https://www.w3schools.com/python/python_{topic}.asp"
    #         response = requests.get(url)
    #         soup = BeautifulSoup(response.text, "html.parser")

    #         content_div = soup.find("div", class_="ws-info")
    #         if content_div:
    #            paragraph = content_div.find("p")
    #            if paragraph:
    #             description = paragraph.get_text(strip=True)
    #             print(f"Here's a quick explanation: {description}")
    #            else:
    #             print("Couldn't find an explanation paragraph.")
    #         else:
    #             print("Couldn't find content section on the page.")

    #             print("I searched for:", topic)
    #             print("You can check this site for info:", url)

    #     except :
    #            print("Something went wrong. Maybe no internet or the site has changed.")
# from bs4 import BeautifulSoup
# import requests
import requests
from bs4 import BeautifulSoup

class SearchBot:
    def ask_user(self):
        topic = input("Choose a topic: loops, function, or variables: ").strip().lower()
        self.search_topic(topic)

    def search_topic(self, topic):
        topic_links = {
            "loops": "https://www.w3schools.com/python/python_for_loops.asp",
            "function": "https://www.w3schools.com/python/python_functions.asp",
            "variables": "https://www.w3schools.com/python/python_variables.asp"
        }

        url = topic_links.get(topic)
        if not url:
            print("Sorry, I don't have a page for that topic yet.")
            return

        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, "html.parser")
            found = False
            for h2 in soup.find_all("h2"):
                if topic in h2.get_text().lower():
                    paragraph = h2.find_next("p")
                    if paragraph:
                        print(f"\nHere's a quick explanation about {topic}:\n{paragraph.get_text(strip=True)}")
                    else:
                        print("Found the heading but couldn't find the explanation.")
                    found = True
                    break

            if not found:
                print("Couldn't find a matching explanation on the page.")

            print(f"\nYou can read more here: {url}")

        except Exception as e:
            print("Something went wrong. Maybe no internet or the site has changed.")
            print("Error:", e)

bot = SearchBot()
bot.ask_user()