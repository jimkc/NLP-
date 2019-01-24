import nltk
from nltk.tag.stanford import StanfordPOSTagger as POS_Tag


##################################################################################
#Stanford Postagger
##################################################################################
# english-left3words-distsim.tagger is suggest by stanfordnlp as tagger
_path_to_pos_model = "/Users/jimfan/Desktop/UCSC/NLP/stanford-postagger-full-2018-10-16/models/english-left3words-distsim.tagger"
_path_to_pos_jar = "/Users/jimfan/Desktop/UCSC/NLP/stanford-postagger-full-2018-10-16/stanford-postagger.jar"

english_postagger = POS_Tag(model_filename=_path_to_pos_model, path_to_jar=_path_to_pos_jar)
tags = english_postagger.tag("HI, MY NAME IS JIM. HOW ARE YOU. I AM HAPPY!".split())
print (tags)


