import urllib
import json

url_request = "http://www.wdyl.com/profanity?q=";
path = "xxx_path_to_file_xxx";

def read_test(path_to_file):
	text_file = open(path_to_file);
	contents_of_file = text_file.read();
	text_file.close();
	check_profanity(contents_of_file);


def check_profanity(text):
	connection = urllib.urlopen(url_request+text);
	output = connection.read();
	connection.close();
	parsed_json = json.loads(output);
	result = parsed_json["response"];
	if(result == "true"):
		print("ALERT ALERT!!")
	else:
		print("No biggie")

read_test(path);

