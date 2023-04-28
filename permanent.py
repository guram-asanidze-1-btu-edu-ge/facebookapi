import facebook

#paste your token on this website and get 2 month time limit token https://developers.facebook.com/tools/debug/accesstoken/ 
graph = facebook.GraphAPI(access_token='...fefSYXdgtzUCVnRZA1sc8jkbU3gknY72mY9GZBx...', version="3.0") #enter your 2 month token here access_token=''
pages_data = graph.get_object("me/accounts")

permanent_page_token = pages_data["data"][0]["access_token"]
page_id = pages_data["data"][0]["id"]
print(pages_data) #use OUTPUT token now it's permanent, you also can check it https://developers.facebook.com/tools/debug/accesstoken/ 


