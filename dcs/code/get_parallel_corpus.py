import sys
import os
import json
from tqdm import tqdm

script, inp, input_dir, output = sys.argv

misc_keys = []

def get_data(sent_id):
    file_path = os.path.join((os.getcwd() + "/" + input_dir), (sent_id + ".json"))
    json_input = open(file_path, "r", encoding='utf-8')
    data = json.load(json_input)
    json_input.close()
    return data

#def get_detail(sent_id, detail, lst):
#    data = get_data(sent_id)
#    detail_value = data.get(detail, ([] if lst else ""))
#    return detail_value

#def get_misc(sent_id):
#    value = get_detail(sent_id, "misc", True)
#    for i in value:
#        for j in i:
#            all_entries = j.split("|")
#            for k in all_entries:
#                items = k.split("=")
#                if not (items[0] in misc_keys):
#                    misc_keys.append(items[0])

def get_pc(sent_id):
    data = get_data(sent_id)
    joint_sentence = data.get("joint_sentence", "")
    dcs_word_form = data.get("word_form", [])
    dcs_morph = data.get("morph", [])
    dcs_word = data.get("word", [])
    dcs_unsandhied_reconstructed = data.get("word_reconstructed", [])
    
    dcs_segmented_sentence = ""
    dcs_segmented_sentence_new = ""
    unsandhied_reconstructed = []
    
    if (len(dcs_word) > 0):
#    if (len(dcs_word_form) > 0) and (len(dcs_word) > 0):
        for i in range(len(dcs_word)):
            for j in range(len(dcs_word[i])):
                morph = dcs_morph[i][j]
                dcs_segmented_sentence += dcs_word_form[i][j]
                dcs_segmented_sentence_new += dcs_word[i][j]
                if "Case=Cpd" in morph:
                    dcs_segmented_sentence += "-"
                    dcs_segmented_sentence_new += "-"
                else:
                    dcs_segmented_sentence += " "
                    dcs_segmented_sentence_new += " "
                
                if dcs_unsandhied_reconstructed[i][j] == "True":
                    unsandhied_reconstructed.append("True")
                else:
                    unsandhied_reconstructed.append("False")
    return "\t".join((sent_id, joint_sentence, dcs_segmented_sentence, dcs_segmented_sentence_new, ",".join(unsandhied_reconstructed)))
#    return "\t".join((sent_id, joint_sentence, dcs_segmented_sentence_new))
    
        
input_file = open(inp, "r", encoding="utf-8")
output_file = open(output, "w", encoding="utf-8")

all_new_lines = []

print_string = ""
text = input_file.read()
all_lines = text.split("\n")
lines = list(filter(None, all_lines))
for i in tqdm(range(len(lines))):
    sent_id = (lines[i].split("\t"))[0]
    all_new_lines.append(get_pc(sent_id))

output_file.write("\n".join(all_new_lines))
