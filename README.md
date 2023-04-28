facebookapi for instalation use   

pip install facebook-sdk

I show you how to create :
1) Facebook app publish it (anyone can see post)  
2) get permanent token (not just 2 month)

https://developers.facebook.com/apps/ create your app

create short acsses token , first token work for about 1 hour. 

token with permisions (for posting):

pages_show_list

pages_read_engagement

pages_read_user_content

pages_manage_posts

pages_manage_engagement


paste your token on this website and get 2 month time limit token

https://developers.facebook.com/tools/debug/accesstoken/ 


then copy 2 month token and paste in Python script , now use OUTPUT token it's permanent, you also can check it https://developers.facebook.com/tools/debug/accesstoken/ 

!!! for public app you need image and secure link, I get from https://www.termsfeed.com, just sign up and get link mine is like:
https://www.termsfeed.com/live/...-db7b-4d...



EXAMPLE OF POST : https://www.facebook.com/saintereso13/posts/pfbid02nTui77PAPcgFaXpvqmnmeTn596mcSDmjzL7SadMsUZAmSZZoF3NYvunN4ifJcedPl
