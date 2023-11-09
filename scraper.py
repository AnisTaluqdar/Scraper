from selenium import webdriver
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.common.by import By
import time
import pandas as pd

columns = ["World Rank", "Natonal Bank", "Name", "Image URLs","Affiliation","Country","H-Index","Cittions" ,"#DBLP"]

def get_scholar_details(row):
    details = row.text.split('\n')
    contents = {}
    contents["World Rank"] =    details[0]
    contents["Natonal Bank"] =  details[1]
    contents["Name"] =          details[2]
    contents["Affiliation"] =   details[3].split(',')[0]
    contents["Country"] =       details[3].split(',')[1].strip()
    contents["H-Index"] =       details[4]
    contents["Cittions" ] =     details[5].replace(',',"")
    contents["#DBLP"] =         details[6].replace(',',"")
    contents["Image URLs"] =    row.find_element(By.CLASS_NAME, "lazyload").get_attribute('src')
    return contents




def main():
   
    
    

    scholar_data = []

    for page_id in range(1,11):
        options = EdgeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        driver = webdriver.Edge(options=options)
        url = f"https://research.com/scientists-rankings/computer-science?page={page_id}"
        driver.get(url)
        time.sleep(20)
        rankings = driver.find_element(By.ID, "rankingItems")
        rows = rankings.find_elements(By.CLASS_NAME, 'cols')
        for idx, row in enumerate(rows):
            if idx%4 == 0:
                scholar_data.append(get_scholar_details(row))
        driver.close()
    

    
    df = pd.DataFrame(scholar_data)
    df.to_csv("best_cs_scientist_details.csv", index =False)

   
    return

if __name__ == "__main__":
    main()