from playwright.sync_api import sync_playwright
import pandas as pd


def main():
    
    with sync_playwright() as p:
        
        checkin_date = '2024-04-05'
        checkout_date = '2023-04-06'
        
        page_url = f'https://holidayz.makemytrip.com/holidays/india/search?depCity=New%20Delhi&dateSearched=25%2F05%2F2024&dest=Kedarnath&destValue=Kedarnath&glp=true&pdo=false&affiliate=MMT&rooms=2%2C0%2C0%2C0%2C%2C%2C'
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(page_url, timeout=60000)

        packages = page.locator('//div[@class="packageTextContainer"]').all()

        print(f'There are: {len(packages)} hotels.')


        packages_list = []
        for package in packages:
            package_dict = {}
            package_dict['package'] = package.locator('//p[@class="packageHead"]').inner_text()
            package_dict['price'] = package.locator('//div[contains(@class, "includeWrapper")]').inner_text()
        
            packages_list.append(package_dict)
        
        df = pd.DataFrame(packages_list)
        df.to_excel('packages_list.xlsx', index=False) 
        df.to_csv('packages_list.csv', index=False) 
        excel_file_path = '/path/to/directory/packages_list.xlsx'
        csv_file_path = '/path/to/directory/packages_list.csv'

        
        browser.close()
            
if __name__ == '__main__':
    main()