"""Getting Started Example for Python 2.7+/3.3+"""
"""Getting Started Example for Python 2.7+/3.3+"""
import boto3
from contextlib import closing
import os
import sys


def get_audio(path):
	candidate = {}
	polly = boto3.client('polly')
	with open(os.path.join(path, 'Englishwords.txt'), 'r') as f:
		string = f.read()
		tmp = string.split('\n')
		for item in tmp:
			if len(item) > 0:
				cand = item.split('\t')
				print(cand)
				candidate[cand[0]] = cand[1]
	for key in candidate.keys():
		index = key.rfind('/')
		index1 = key.find('_thumbnail')
		filename = key[index+1:index1]
		text = candidate[key]
		if len(text) > 0:
			try:
				    # Request speech synthesis
				response = polly.synthesize_speech(Text=text, OutputFormat="mp3", VoiceId="Joanna")
			except:
				    # The service returned an error, exit gracefully
				print(error)
					
					#sys.exit(-1)
				# Access the audio stream from the response
			if "AudioStream" in response:
				    # Note: Closing the stream is important as the service throttles on the
				    # number of parallel connections. Here we are using contextlib.closing to
				    # ensure the close method of the stream object will be called automatically
				    # at the end of the with statement's scope.
				with closing(response["AudioStream"]) as stream:
					output = os.path.join(path, filename+".mp3")
					try:
				            # Open a file for writing the output as a binary stream
						with open(output, "wb") as file:
							file.write(stream.read())
					except IOError as error:
				            # Could not write to file, exit gracefully
						print(error)
							

			else:
				    # The response didn't contain audio data, exit gracefully
				print("Could not stream audio")

def get_audio_command(text, path, n):
	polly = boto3.client('polly')
		
	try:
		# Request speech synthesis
		response = polly.synthesize_speech(Text=text, OutputFormat="mp3", VoiceId="Joanna")
	except:
		# The service returned an error, exit gracefully
		print("error")			
		sys.exit(-1)
				# Access the audio stream from the response
	if "AudioStream" in response:
	    # Note: Closing the stream is important as the service throttles on the
	    # number of parallel connections. Here we are using contextlib.closing to
	    # ensure the close method of the stream object will be called automatically
		# at the end of the with statement's scope.
		with closing(response["AudioStream"]) as stream:
			output = os.path.join(path, "speech"+str(n)+".mp3")
			try:
			    # Open a file for writing the output as a binary stream
				with open(output, "wb") as file:
					file.write(stream.read())
					print(output)
			except IOError as error:
	        	# Could not write to file, exit gracefully
				print("error")
							

	else:
		# The response didn't contain audio data, exit gracefully
		print("Could not stream audio")
			
