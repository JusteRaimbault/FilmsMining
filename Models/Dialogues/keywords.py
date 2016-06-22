
# relevant n-gram extraction

import nltk












# construct kw occurence dico
def construct_occurrence_dico(lines) :
    print('Constructing occurence dictionnaries...')

    l_kw_dico = dict()
    kw_l_dico = dict()
    for line in lines :
        line_id = line[0]
        keywords = extract_keywords(line[1])
        for k in keywords :
            if k not in kw_l_dico : kw_l_dico[k]= []
            kw_l_dico[k].append(line_id)

            if line_id not in l_kw_dico : l_kw_dico[line_id] = []
            l_kw_dico[line_id].append(k)
    return([l_kw_dico,kw_l_dico])


# tagged of the form (word,TAG)
def potential_multi_term(tagged) :
    res = True
    for tag in tagged :
        res = res and (tag[1]=='NN' or tag[1]=='NNP' or tag[1] == 'VBG' or tag[1] =='NNS'or tag[1] =='JJ' or tag[1] =='JJR')
    return res

# extract n-grams from raw text
def extract_keywords(raw_text):
    stemmer = nltk.PorterStemmer()
    # Tokens
    tokens = nltk.word_tokenize(raw_text)
    # filter undesirable words and format
    words = [w.replace('\'','') for w in tokens if len(w)>=3]
    text = nltk.Text(words)

    tagged_text = nltk.pos_tag(text)

    # multi-term
    multiterms = set()
    for i in range(len(tagged_text)) :
        for l in range(1,3):
            if i+l < len(tagged_text) :
                tags = [tagged_text[k] for k in range(i,i+l)]
                if potential_multi_term(tags) :
                    multistem = [str.lower(stemmer.stem(tagged_text[k][0]).encode('ascii','ignore')) for k in range(i,i+l)]
                    #multistem.sort(key=str.lower)
                    multiterms.add(reduce(lambda s1,s2 : s1+' '+s2,multistem))

    return list(multiterms)
