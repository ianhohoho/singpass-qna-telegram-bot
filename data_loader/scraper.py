import requests
import json
import warnings
warnings.filterwarnings('ignore')

base_url = "https://ask.gov.sg/singpass?index=&isViewingMore=true&page={}&index=&_data=routes%2F%24agencyCode%2Findex"
page = 1
all_data = []

while True:
    url = base_url.format(page)
    print(url)
    response = requests.get(url, verify=False)
    
    if response.status_code == 200:
        try:
            data = response.json()
            question_list_items = data.get("questionListItems", [])
            
            if not question_list_items:
                print(f"No more items found on page {page}. Stopping.")
                break
            
            print(f"Page {page}: Found {len(question_list_items)} items")
            
            all_data.extend(question_list_items)
            page += 1
        except json.JSONDecodeError:
            print(f"Error decoding JSON on page {page}. Stopping.")
            break
    else:
        print(f"Error fetching page {page}: Status code {response.status_code}")
        break

print(f"Finished processing all pages. Total items collected: {len(all_data)}")

# Write all data to a single JSON file
output_file = "singpass_data.json"
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(all_data, f, ensure_ascii=False, indent=2)

print(f"Data has been written to {output_file}")