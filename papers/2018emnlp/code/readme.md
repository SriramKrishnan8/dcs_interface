# Sanskrit Sandhi and Compound Splitter

To run (apply) the pre-trained model in data/models:

```
python3 apply.py file.txt
```

where file.txt should contain the test sentences (line-by-line) in IAST format. The maximum acceptable input character limit is 128.

But rcnn model does not handle certain terminal sandhis. Also, some segments require post-processing of the output which is available at handle\_rcnn\_out.py. In order to incorporate it, run the following:

```
sh run_rccn.sh test_sentence_iast_sample.tsv test_segmentation_iast_sample.tsv iast
```

The first argument is the file containing input sentences. The second argument is the file into which the output is to be stored. The third argument is the output notation, which is one of: "dev, iast, wx, slp, vel, hk, itrans, tex". For transliteration to be effective, please install devtrans:

```
pip3 install devtrans
```
