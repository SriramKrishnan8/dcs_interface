import sys
import os
import json
from tqdm import tqdm

script, directory_name, out, missed = sys.argv

def get_sent_details(file_path):
    json_path = os.path.join(os.getcwd(), file_path)
    json_input = open(json_path,'r',encoding='utf-8')
    data = json.load(json_input)
    json_input.close()
    
    sent_id = data["sent_id"]
    sentence = data["joint_sentence"]
    
    return (str(sent_id) + "\t" + str(sentence))

sent_file = open(out, "a+", encoding='utf-8')
missed_file = open(missed, "a+", encoding='utf-8')

all_files_lst = os.listdir(directory_name)
all_files = list(filter(None, all_files_lst))

sentences = []
missed = []

for x in tqdm(range(len(all_files))):
    i = os.path.join(directory_name, all_files[x])
    if os.path.isfile(i):
        write_info = get_sent_details(i)
        sentences.append(write_info)
    else:
        missed.append(str(all_files[x]))

sent_file.write("\n".join(sentences))
missed_file.write("\n".join(missed))

sent_file.close()
missed_file.close()
