import sys
import os
import json
from tqdm import tqdm

#output_dir = ""
#json_dict = {}
#sandhied_forms_num = 0
#sandhied_form = ""
#position = [] #	list of int
#unsegmented_form = [] #	list of string
#lemma = [] #	list of string
#upos = [] #	list of string (empty)
#xpos = [] #	list of string
#morph = [] #	list of string
#head = [] #	list of string (empty)
#deprel = [] #	list of string (empty)
#deps = [] #	list of string (empty)
#misc = [] #	list of string (empty)
#lemma_id = [] #	list of int
#segmented_form = [] #	list of string
#sem_ids = [] #	list of string

#position_inner = []
#unsegmented_form_inner = []
#lemma_inner = []
#upos_inner = []
#xpos_inner = []
#morph_inner = []
#head_inner = []
#deprel_inner = []
#deps_inner = []
#misc_inner = []
#lemma_id_inner = []
#segmented_form_inner = []
#sem_ids_inner = []

#def convert_to_wx(txt):
#    

def get_dictionary(dict_file_name):
    dict_ = {}
    dict_file = open(dict_file_name, 'r', encoding="utf-8")
    all_text = dict_file.read()
    all_lines = list(filter(None, all_text.split("\n")))
    for line in all_lines:
        val_dict = {}
        split_line = line.split("\t")
        id_ = split_line[0]
        val_dict["lemma_id"] = id_
#        val_dict["lemma"] = split_line[1]
        val_dict["grammar"] = split_line[2]
        val_dict["preverbs"] = split_line[3]
        val_dict["meanings"] = split_line[4]
        dict_[id_] = val_dict
    return dict_

def refresh_json(json_dict):
    new_json_dict = {}
    new_json_dict["text"] = json_dict.get("text", "")
    new_json_dict["text_id"] = json_dict.get("text_id", "")
    new_json_dict["chapter"] = json_dict.get("chapter", "")
    new_json_dict["chapter_id"] = json_dict.get("chapter_id", "")
    return new_json_dict


def convert_to_json(filename, dictionary, output_dir):
    json_dict = {}
    sandhied_forms_num = 0
    sandhied_form = ""
    position = [] #	list of int
    unsegmented_form = [] #	list of string
    word_form = [] # list of string
    lemma = [] #	list of string
    upos = [] #	list of string
    xpos = [] #	list of string (empty)
    morph = [] #	list of string
    head = [] #	list of string (empty)
    deprel = [] #	list of string (empty)
    deps = [] #	list of string (empty)
    misc = [] #	list of string 
    lemma_id = [] #	list of int
    segmented_form = [] #	list of string
    sem_ids = [] #	list of string
    occ_ids = [] #	list of string
    grammar = [] #	list of string
    punctuation = [] #	list of string
    segmented_form_reconstructed = [] #	list of string
    meanings = [] #	list of string
    preverbs = [] #	list of string
    is_mantra = [] #	list of string
    annotator = []
    
    position_inner = []
#    unsegmented_form_inner = []
    word_form_inner = []
    lemma_inner = []
    upos_inner = []
    xpos_inner = []
    morph_inner = []
    head_inner = []
    deprel_inner = []
    deps_inner = []
    misc_inner = []
    lemma_id_inner = []
    segmented_form_inner = []
    sem_ids_inner = []
    occ_ids_inner = []
    grammar_inner = []
    punctuation_inner = []
    segmented_form_reconstructed_inner = []
    meanings_inner = []
    preverbs_inner = []
    is_mantra_inner = []
    annotator_inner = []
    
    in_file = open(filename, "r", encoding='utf-8')
    line = in_file.readline()
    while(line):
        s_line = line.strip()
        if s_line == "":
            if (not ("sent_id" in json_dict.keys())):
                line = in_file.readline()
                continue
            else:
                json_dict["position"] = position
                json_dict["unsegmented_form"] = unsegmented_form
                json_dict["word_form"] = word_form
                json_dict["stem"] = lemma
                json_dict["upos"] = upos
                json_dict["xpos"] = xpos
                json_dict["morph"] = morph
                json_dict["head"] = head
                json_dict["deprel"] = deprel
                json_dict["deps"] = deps
                json_dict["misc"] = misc
                json_dict["stem_id"] = lemma_id
                json_dict["word"] = segmented_form
                json_dict["sem_ids"] = sem_ids
                json_dict["word_reconstructed"] = segmented_form_reconstructed
                json_dict["occ_ids"] = occ_ids
                json_dict["grammar"] = grammar
                json_dict["punctuation"] = punctuation
                json_dict["meanings"] = meanings
                json_dict["preverbs"] = preverbs
                json_dict["is_mantra"] = is_mantra
                json_dict["annotator"] = annotator
                
                json_file_rel_loc = str(output_dir + json_dict["sent_id"] + ".json")
                json_path = os.path.join(os.getcwd(), json_file_rel_loc)
                
                with open(json_path, 'w', encoding='utf-8') as out_file:
                    json.dump(json_dict, out_file, ensure_ascii=False)
                
                json_dict = refresh_json(json_dict)
                position = []
                unsegmented_form = []
                word_form = []
                lemma = []
                upos = []
                xpos = []
                morph = []
                head = []
                deprel = []
                deps = []
                misc = []
                lemma_id = []
                segmented_form = []
                sem_ids = []
                occ_ids = []
                segmented_form_reconstructed = []
                punctuation = []
                grammar = []
                meanings = []
                preverbs = []
                is_mantra = []
                annotator = []
                sandhied_forms = 0
                line = in_file.readline()
                continue
        
        if "## " in s_line:
            split_line = s_line.split(":")
            if "## text:" in s_line:
                json_dict["text"] = split_line[1].strip()
            elif "## text_id:" in s_line:
                json_dict["text_id"] = split_line[1].strip()
            elif "## chapter:" in s_line:
                json_dict["chapter"] = split_line[1].strip()
            elif "## chapter_id:" in s_line:
                json_dict["chapter_id"] = split_line[1].strip()
            else:
                pass
        elif "# " in s_line:
            split_line = s_line.split("=")
            if "# text " in s_line:
                json_dict["joint_sentence"] = split_line[1].strip()
            elif "# sent_id " in s_line:
                json_dict["sent_id"] = split_line[1].strip()
            elif "# sent_counter " in s_line:
                json_dict["sent_counter"] = split_line[1].strip()
            elif "# sent_subcounter " in s_line:
                json_dict["sent_sub_counter"] = split_line[1].strip()
            elif "# layer" in s_line:
                json_dict["layer"] = split_line[1].strip()
            elif "# citation_text" in s_line:
                json_dict["citation_text"] = split_line[1].strip()
            elif "# citation_chapter" in s_line:
                json_dict["citation_chapter"] = split_line[1].strip()
            else:
                pass
        else:
            split_entries = s_line.split("\t")
            split_line = []
            for i in split_entries:
                if i == "_":
                    split_line.append("")
                else:
                    split_line.append(i)
            if "-" in split_line[0]:
                limits = split_line[0].split("-")
                diff = int(limits[1]) - int(limits[0])
                sandhied_forms_num = diff + 1
                sandhied_form = split_line[1]
                line = in_file.readline()
                continue
            
            if sandhied_forms_num > 0:
                position_inner.append(split_line[0])
#                unsegmented_form_inner.append(sandhied_form)
                word_form_inner.append(split_line[1])
                lemma_inner.append(split_line[2])
                upos_inner.append(split_line[3])
                xpos_inner.append(split_line[4])
                morph_inner.append(split_line[5])
                head_inner.append(split_line[6])
                deprel_inner.append(split_line[7])
                deps_inner.append(split_line[8])
                misc_inner.append(split_line[9])
                
                split_misc = split_line[9].split("|")
                temp_dict = {}
                for item in split_misc:
                    split_item = item.split("=")
                    temp_dict[split_item[0]] = split_item[1]
                
                lemma_id_inner.append(temp_dict.get("LemmaId", ""))
                segmented_form_inner.append(temp_dict.get("Unsandhied", ""))
                segmented_form_reconstructed_inner.append(temp_dict.get("UnsandhiedReconstructed", ""))
                occ_ids_inner.append(temp_dict.get("OccId", ""))
                sem_ids_inner.append(temp_dict.get("WordSem", ""))
                punctuation_inner.append(temp_dict.get("Punctuation", ""))
                is_mantra_inner.append(temp_dict.get("IsMantra", ""))
                annotator_inner.append(temp_dict.get("Annotator", ""))
                
                dictionary_dict = dictionary.get(temp_dict.get("LemmaId", ""), {})
                
                grammar_inner.append(dictionary_dict.get("grammar", ""))
                preverbs_inner.append(dictionary_dict.get("preverbs", ""))
                meanings_inner.append(dictionary_dict.get("meanings", ""))
                
                if not sandhied_forms_num == 1:
                    sandhied_forms_num -= 1
                    line = in_file.readline()
                    continue
                
                position.append(position_inner)
                unsegmented_form.append(sandhied_form)
                word_form.append(word_form_inner)
                lemma.append(lemma_inner)
                upos.append(upos_inner)
                xpos.append(xpos_inner)
                morph.append(morph_inner)
                head.append(head_inner)
                deprel.append(deprel_inner)
                deps.append(deps_inner)
                misc.append(misc_inner)
                lemma_id.append(lemma_id_inner)
                segmented_form.append(segmented_form_inner)
                segmented_form_reconstructed.append(segmented_form_reconstructed_inner)
                occ_ids.append(occ_ids_inner)
                sem_ids.append(sem_ids_inner)
                punctuation.append(punctuation_inner)
                is_mantra.append(is_mantra_inner)
                annotator.append(annotator_inner)
                grammar.append(grammar_inner)
                preverbs.append(preverbs_inner)
                meanings.append(meanings_inner)
                
                position_inner = []
#                unsegmented_form_inner = []
                word_form_inner = []
                lemma_inner = []
                upos_inner = []
                xpos_inner = []
                morph_inner = []
                head_inner = []
                deprel_inner = []
                deps_inner = []
                misc_inner = []
                lemma_id_inner = []
                segmented_form_inner = []
                segmented_form_reconstructed_inner = []
                occ_ids_inner = []
                sem_ids_inner = []
                punctuation_inner = []
                is_mantra_inner = []
                annotator_inner = []
                grammar_inner = []
                preverbs_inner = []
                meanings_inner = []
                sandhied_form = ""
                
                sandhied_forms_num -= 1
            else:
                position.append([split_line[0]])
                unsegmented_form.append(split_line[1])
                word_form.append([split_line[1]])
                lemma.append([split_line[2]])
                upos.append([split_line[3]])
                xpos.append([split_line[4]])
                morph.append([split_line[5]])
                head.append([split_line[6]])
                deprel.append([split_line[7]])
                deps.append([split_line[8]])
                misc.append([split_line[9]])
                
                split_misc = split_line[9].split("|")
                temp_dict = {}
                for item in split_misc:
                    split_item = item.split("=")
                    temp_dict[split_item[0]] = split_item[1]
                
                lemma_id.append([temp_dict.get("LemmaId", "")])
                segmented_form.append([temp_dict.get("Unsandhied", "")])
                segmented_form_reconstructed.append([temp_dict.get("UnsandhiedReconstructed", "")])
                occ_ids.append([temp_dict.get("OccId", "")])
                sem_ids.append([temp_dict.get("WordSem", "")])
                punctuation.append([temp_dict.get("Punctuation", "")])
                is_mantra.append([temp_dict.get("IsMantra", "")])
                annotator.append([temp_dict.get("Annotator", "")])
                
                dictionary_dict = dictionary.get(temp_dict.get("LemmaId", ""), {})
                
                grammar.append([dictionary_dict.get("grammar", "")])
                preverbs.append([dictionary_dict.get("preverbs", "")])
                meanings.append([dictionary_dict.get("meanings", "")])
        
        line = in_file.readline()
    
    if (not ("sent_id" in json_dict.keys())):
        return
    
    json_dict["position"] = position
    json_dict["unsegmented_form"] = unsegmented_form
    json_dict["word_form"] = word_form
    json_dict["stem"] = lemma
    json_dict["upos"] = upos
    json_dict["xpos"] = xpos
    json_dict["morph"] = morph
    json_dict["head"] = head
    json_dict["deprel"] = deprel
    json_dict["deps"] = deps
    json_dict["misc"] = misc
    json_dict["word"] = segmented_form
    json_dict["stem_id"] = lemma_id
    json_dict["sem_ids"] = sem_ids
    json_dict["word_reconstructed"] = segmented_form_reconstructed
    json_dict["occ_ids"] = occ_ids
    json_dict["grammar"] = grammar
    json_dict["punctuation"] = punctuation
    json_dict["meanings"] = meanings
    json_dict["preverbs"] = preverbs
    json_dict["is_mantra"] = is_mantra
    json_dict["annotator"] = annotator
    
    json_file_rel_loc = str(output_dir + json_dict["sent_id"] + ".json")
    json_path = os.path.join(os.getcwd(), json_file_rel_loc)
    with open(json_path, 'w', encoding='utf-8') as out_file:
        json.dump(json_dict, out_file, ensure_ascii=False)


def make_json_from_conllu(file_name, output_dir):
    dictionary_file = "lookup/dictionary.csv"
    dictionary = get_dictionary(dictionary_file)
    convert_to_json(file_name, dictionary, output_dir)        

#make_json_from_conllu("files/Bṛhadāraṇyakopaniṣad/Bṛhadāraṇyakopaniṣad-0006-BĀU, 2, 1-9109.conllu_parsed", "temp/")
