import facebook as fb


token='...q3xZB8b8nIlb3QoIstE04GR6HpgZAtk8QD1vf6glp4...'
asafb = fb.GraphAPI(token)
id = '19537...' #your page ID where you are going to post
pages_data = asafb.get_object('19537.../posts')

try:
    asafb.put_object(id, 'photos', message= '👀 something : ...' +'\n'+'' #interesting #facts' ,url=kart) #+'\n'+' this mean new line

#example of post https://www.facebook.com/saintereso13/posts/pfbid02nTui77PAPcgFaXpvqmnmeTn596mcSDmjzL7SadMsUZAmSZZoF3NYvunN4ifJcedPl

