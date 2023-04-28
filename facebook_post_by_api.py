import facebook as fb


token='...q3xZB8b8nIlb3QoIstE04GR6HpgZAtk8QD1vf6glp4...' #use your permanent token
asafb = fb.GraphAPI(token)
id = '19537...' #your page ID where you are going to post
pages_data = asafb.get_object('19537.../posts') #to get posts

try:
    asafb.put_object(id, 'photos', message= '👀 something : ...' +'\n'+'' #interesting #facts' ,url=kart) # url= replace kart by url in ''
except Exception as e:
    print(e)

#example of post https://www.facebook.com/saintereso13/posts/pfbid02nTui77PAPcgFaXpvqmnmeTn596mcSDmjzL7SadMsUZAmSZZoF3NYvunN4ifJcedPl

