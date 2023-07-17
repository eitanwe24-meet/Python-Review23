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


def print_video(video): #Bonus
	print(video["title"])
	print(video["description"])
	print(f"likes: {video['likes']}, dislikes: {video['dislikes']}")
	i = 1
	for comment in video["comments"]:
		print(f"{i}. {comment}")
	# title
	# description
	# likes: 4, dislikes: 0
	# comments:
	# 	1. 
	# 	2
	# 	3
	# 	4


a = create_youtube_video("hello","jjwboe")
a = like(a)
a = dislike(a)
a = add_comment(a,"eitan","commentss")
for i in range(495):
	like(a)
	

print_video(a)
