import facebook
#https://developers.facebook.com/apps/ create your app
#create short , first token work for about 1 hour, time you can check here: https://developers.facebook.com/tools/debug/accesstoken/
#token with permisions (for posting):
#pages_show_list
#pages_read_engagement
#pages_read_user_content
#pages_manage_posts
#pages_manage_engagement
#paste your token on this website and get 2 month time limit token https://developers.facebook.com/tools/debug/accesstoken/ 
graph = facebook.GraphAPI(access_token='...fefSYXdgtzUCVnRZA1sc8jkbU3gknY72mY9GZBx...', version="3.0") #enter your 2 month token here access_token=''
pages_data = graph.get_object("me/accounts")

permanent_page_token = pages_data["data"][0]["access_token"]
page_id = pages_data["data"][0]["id"]
print(pages_data) #use OUTPUT token now it's permanent, you also can check it https://developers.facebook.com/tools/debug/accesstoken/ 

#!!! for public app you need image and secure link, I get from https://www.termsfeed.com, just sign up and get link mine is like:
#https://www.termsfeed.com/live/ef069dbc-db7b-4d...

