def create_youtube_video(title,description):
	video={"title":title,"description":description,"likes":0,"dislikes":0,"comments":{}}
	return video

def like(video):
	if "likes" in video:
		video["likes"]+=1
		return video

def dislike(video):
	if "dislikes" in video:
		video["dislikes"]+=1
		return video

def add_comment(video,username,comments_text):
	video['comments'][username]=comments_text
	return video


a = create_youtube_video("hello","jjwboe")
print(a) 
a = like(a)
print(a)
a = dislike(a)
print(a)
a = add_comment(a,"eitan","commentss")
print(a)
for i in range(495):
	like(a)
print(a)
	