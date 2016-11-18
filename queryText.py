import wolframalpha
import sys

# Get a free API key here http://products.wolframalpha.com/api/
# This is a fake ID, go and get your own, instructions on my blog.
app_id='8E2HX9-2E5LW7U8VK'

client = wolframalpha.Client(app_id)

#query = ' '.join(sys.argv[1:])
filename = sys.argv[-1]
with open(filename, 'rb') as queryfile:
	query = queryfile.read().replace('\n', '')
	res = client.query(query)
	try:
	#	print(list(res.pods))
		s = list(res.pods)[1]
		#print(s)
		if len(s) > 0:
			texts = ""
#			print(type(s))
#			print(s)
			pod = s["subpod"]
	#		print(pod)
			if pod["plaintext"]:
				texts = pod["plaintext"]
			else:
				texts = "I have no answer for that"
# to skip ascii character in case of error
			texts = texts.encode('ascii', 'ignore')
			print(texts)
		else:
			print("Sorry, I am not sure.")
	except BaseException as e:
		print("Oops, Something went wrong. Please try another question {}".format(e))
