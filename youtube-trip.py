from lxml import html
import requests
import csv
from random import randint
import time

def main():
	#input the youtube url
	youtube_url = 'https://www.youtube.com/watch?v=AiYShDwsujc'

	#str(input("Paste youtube video url ---> "))

	#how many hops
	repetition = int(input("How many hops? --> "))

	#clear video_log file
	with open('videos_log.csv', 'w') as csvfile:
	    	newFileWriter = csv.writer(csvfile)
	    	newFileWriter.writerow(["id","title","duration","url"])

	#hopping over videos
	for i in range(repetition):
		
		#get the youtube video site
		page = requests.get(youtube_url)
		
		#parse to html
		tree = html.fromstring(page.content)
		
		#get the list of handles of suggested videos
		next_video_url_handle_list = tree.xpath("//ul[@id='watch-related']/li/div[@class='content-wrapper']//a/@href")
		
		#get pseudo-random next video url
		random_int = randint(0, len(next_video_url_handle_list)-1)
		next_video_url = 'https://www.youtube.com' + next_video_url_handle_list[random_int]

		#get the list of titles of suggested videos 
		next_video_title_list = tree.xpath(("//ul[@id='watch-related']/li[" + str(random_int) + "]/div[@class='content-wrapper']//span[@class='title']//text()"))
		next_video_title = tryGettingString(next_video_title_list, 0)

		#get the list of durations of suggested videos	
		next_video_duration_list = tree.xpath(("//ul[@id='watch-related']/li[" + str(random_int) + "]/div[@class='thumb-wrapper']//span[@class='video-time']//text()"))
		next_video_duration = tryGettingString(next_video_duration_list, 0)

		#switch the urls
		youtube_url = next_video_url

		#output to terminal
		print i 
		print next_video_title
		print next_video_duration
		print next_video_url
		print "--------------"

		#log vidoes to csv
		#columns: id, title, duration, url
		with open('videos_log.csv', 'a') as csvfile:
	    		newFileWriter = csv.writer(csvfile, delimiter=',')
	    		newFileWriter.writerow([i, next_video_title, next_video_duration, next_video_url])

#a method to get a string from the fetched lists. Sometimes they are blank or not encoded in UTF-8 and main() would crash.
def tryGettingString(fetched_list, position):
	try:
 		string = fetched_list[position].encode('utf-8').strip()
		return string
	except: 
 		return ""

if __name__ == "__main__":
 	main()
