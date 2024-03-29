from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests


def collect_nutrition_data(food_name):
    # Initialize variables
    calories_value = "Calories not found"
    total_fat_value = "Total fat not found"
    total_protein_value = "Total protein not found"
    total_carbohydrates_value = "Total carbohydrates not found"

    # Configure Chrome options
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')  # Optional: run Chrome in headless mode

    # Initialize Chrome WebDriver with the provided options
    driver = webdriver.Chrome(options=chrome_options)

    # Open the webpage
    driver.get(f"https://www.nutritionix.com/food/{food_name}")

    try:
        # Wait for the calories element to be present on the page
        calories_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.nf-pr[itemprop="calories"]'))
        )

        # Extract the caloric value
        calories_text = calories_element.text.strip()
        calories_value = calories_text.split()[0]
    except Exception as e:
        print("An error occurred while fetching calories:", e)
    
    try:
        # Wait for the total fat element to be present on the page
        total_fat_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//span[contains(text(), "Total Fat")]/following-sibling::span'))
        )

        # Extract the total fat value
        total_fat_text = total_fat_element.text.strip()
        total_fat_value = total_fat_text.split()[0]
    except Exception as e:
        print("An error occurred while fetching total fat:", e)
    
    try:
        # Wait for the total protein element to be present on the page
        total_protein_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//span[contains(text(), "Protein")]/following-sibling::span'))
        )

        # Extract the total protein value
        total_protein_text = total_protein_element.text.strip()
        total_protein_value = total_protein_text.split()[0]
    except Exception as e:
        print("An error occurred while fetching total protein:", e)

    try:
        # Wait for the total carbohydrates element to be present on the page
        total_carbohydrates_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//span[contains(text(), "Total Carbohydrates")]/following-sibling::span'))
        )

        # Extract the total carbohydrates value
        total_carbohydrates_text = total_carbohydrates_element.text.strip()
        total_carbohydrates_value = total_carbohydrates_text.split()[0]
    except Exception as e:
        print("An error occurred while fetching total carbohydrates:", e)
    
    nutrition_data = {
        "Calories": calories_value,
        "Total Fat": total_fat_value,
        "Total Protein": total_protein_value,
        "Total Carbohydrates": total_carbohydrates_value,
    }

    return nutrition_data

def main():
    image_path = input("Enter the image path: ")

    url = "https://r6znkgc19l.execute-api.us-east-1.amazonaws.com/classify"

    payload = {
        "image_path": image_path
    }

    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.put(url, json=payload, headers=headers)

    if response.status_code == 200:
        # Pass the response content to the collect_nutrition_data function
        nutrition_data = collect_nutrition_data(response.content)
        
        # Print the retrieved nutrition data
        print("Nutritional data:", nutrition_data)
    else:
        print("Failed to retrieve image from S3 bucket")

if __name__ == "__main__":
    main()








