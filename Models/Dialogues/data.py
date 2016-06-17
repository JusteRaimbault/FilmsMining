
import nltk,json
import utils



def load_data(lines_file,conversations_file) :
    # construct dico lineID -> {characterid,charactername,movieid,text}
    lines_dico={}
    for line in utils.read_csv(lines_file,' +++$+++ ') :
        lines_dico[line[0]]={'characterid':line[1],'charactername':line[3],'movieid':line[2],'text':line[4]}
    # construct the film dico : id -> [dialogues = [text1,text2...]]
    films={}
    for dialogue in utils.read_csv(conversations_file,' +++$+++ ') :
        filmid=dialogue[2]
        if filmid not in films : films[filmid]=[]
        #print dialogue[3]
        #lineids = json.loads(dialogue[3])# issue with json string ?
        lineids = dialogue[3].replace('[','').replace(']','').replace('\'','').replace(' ','').split(',')
        films[filmid].append([lines_dico[lineid]['text'] for lineid in lineids])
    return films


# test
#films = load_data('/Users/Juste/Documents/ComplexSystems/FilmsMining/Data/cornell_movie-dialogs_corpus/movie_lines.txt','/Users/Juste/Documents/ComplexSystems/FilmsMining/Data/cornell_movie-dialogs_corpus/movie_conversations.txt')

#for d in films[films.keys()[0]]:
#    print d
