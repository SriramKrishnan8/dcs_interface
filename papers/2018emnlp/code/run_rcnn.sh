python3 apply.py $1 output.tsv
transliterate -d iast -e slp -i output.tsv -o output_slp.tsv
python3 handle_rcnn_out.py output_slp.tsv output_handled_slp.tsv
transliterate -d slp -e $3 -i output_handled_slp.tsv -o $2
rm output.tsv output_slp.tsv output_handled_slp.tsv
