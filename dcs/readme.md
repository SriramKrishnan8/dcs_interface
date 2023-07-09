# Conversion of DCS from conllu to JSON format

## Data

The directory ./data/conllu contains two subdirectories: ./files and ./lookup.

The subdirectory ./files contains the texts in CoNLL-U format (see https://universaldependencies.org/format.html). Each text is in a separate folder, and each chapter (i.e. what is defined as chapter in the DCS) in a separate file.
The file name "Aṣṭāṅgahṛdayasaṃhitā-0007-AHS, Sū., 8-1162" means: Text=Aṣṭāṅgahṛdayasaṃhitā", chapter seven ("0007"), citation form of the chapter name="AHS, Sū., 8", chapter id="1162"
Note that format of the CoNLL-U files has changed in the latest release (Aug 9, 2022) and now conforms to the UD standard.

The subdirectory ./lookup contains lexicographic information (dictionary.csv), details about word senses (subfield WordSem in field 10 of a conllu line; file word-senses.csv) and a short explanation of the POS tags (pos.csv).

## Code

The directory ./code contains the codebase for playing with the DCS data.

### To convert the DCS analyses into a JSON format.

```
cd code/
sh conllu_to_json.sh
```

conllu\_to\_json.sh calls run\_for\_all.py for all files in ../data/conllu/files/, which again calls make\_json.py. make\_json.py goes through each line of the conllu file and builds the JSON.

### To generate the DCS sentences:

```
python3 get_dcs_sentences.py ../data/json/json_data/ ../data/json/dcs_sentences.tsv ../data/json/dcs_sentences_missed.tsv
```

(NOTE: Further cleaning is necessary to make this set of sentences usable. Some characters like ﾱﾲﾡﾰ￞ are present in the texts which require unicode compatibility and clarity!)

To find if there are any special characters:

```
grep -v -E "[^aāiīuūṛṝḷeoṃṁḥkgṅcjñṭḍṇtdnpbmyrlvśṣsh'0123456789_\t \n]" ../data/json/dcs_sentences.tsv > ../data/json/dcs_sentences_wrong_characters.tsv
```

### To generate the parallel corpus of unsegmented-segmented sentences:

```
python3 get_parallel_corpus.py ../data/json/dcs_sentences.tsv ../data/json/json_data/ ../data/json/dcs_parallel_corpus.tsv
```

This returns the following:

(dcs\_sent\_id, dcs\_joint\_sentence, dcs\_marked\_word\_form, dcs\_predicted\_word\_form, segment\_uconstructed\_bool)

For general usage fields 1,2 and 3 can be used. But for some of the words, the terminal sandhies are not handled. Using the predicted forms also might result into incorrect segmentations. Hence, to validate the segments and also to generate correct segments, an alignment of DCS analyses has been carried out with [Sanskrit Heritage Segmenter's](http://www.sanskrit.inria.fr) analyses at [dcs_sh_alignment](https://github.com/SriramKrishnan8/dcs_sh_alignment)


## License

The data in this directory are licensed under the Creative Common BY 4.0 (CC BY 4.0) license.
