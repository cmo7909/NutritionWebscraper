import requests
import bs4
from bs4 import BeautifulSoup

def main():
    food_name = input("Enter the name of the food you want the nutritional facts for: ")
    nutrition_data = collect_nutrition_data(food_name)
    if(nutrition_data):
        print(f"Nutrition data for {food_name}:")
        print(f"Calories: {nutrition_data}")
    else:
        print("No nutrition data found")



def collect_nutrition_data(food_name):
    query = f"{food_name} nutrients"

    url = f"https://www.google.com/search?q={query}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    # response = requests.get(url, headers=headers)
    soup = BeautifulSoup(requests.get(url).text)

    # if(response.status_code == 200):
    #     soup = BeautifulSoup(response.text, 'html.parser')
    #     parent_div = soup.find_all("span", class_="abs")
    #     target_element = parent_div.find("span", class_="abs")
    #     calories = target_element.text
    #     return calories
    # else:
    #     print("Failed to fetch data from Google")
    #     return None

    # result = bs4.BeautifulSoup(response.text, "html.parser")
    variable_name = soup.find('table', class_='AYBNrd')
    for x in variable_name:
        print(x)
   
if __name__ == "__main__":
    main()