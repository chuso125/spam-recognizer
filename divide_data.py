import random
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
articles = ['a','an','the','and']
stop_words = ["a", "about", "above", "above", "across", "after", "afterwards", "again", "against", "all", "almost", "alone", "along", "already", "also","although","always","am","among", "amongst", "amoungst", "amount",  "an", "and", "another", "any","anyhow","anyone","anything","anyway", "anywhere", "are", "around", "as",  "at", "back","be","became", "because","become","becomes", "becoming", "been", "before", "beforehand", "behind", "being", "below", "beside", "besides", "between", "beyond", "bill", "both", "bottom","but", "by", "call", "can", "cannot", "cant", "co", "con", "could", "couldnt", "cry", "de", "describe", "detail", "do", "done", "down", "due", "during", "each", "eg", "eight", "either", "eleven","else", "elsewhere", "empty", "enough", "etc", "even", "ever", "every", "everyone", "everything", "everywhere", "except", "few", "fifteen", "fify", "fill", "find", "fire", "first", "five", "for", "former", "formerly", "forty", "found", "four", "from", "front", "full", "further", "get", "give", "go", "had", "has", "hasnt", "have", "he", "hence", "her", "here", "hereafter", "hereby", "herein", "hereupon", "hers", "herself", "him", "himself", "his", "how", "however", "hundred", "ie", "if", "in", "inc", "indeed", "interest", "into", "is", "it", "its", "itself", "keep", "last", "latter", "latterly", "least", "less", "ltd", "made", "many", "may", "me", "meanwhile", "might", "mill", "mine", "more", "moreover", "most", "mostly", "move", "much", "must", "my", "myself", "name", "namely", "neither", "never", "nevertheless", "next", "nine", "no", "nobody", "none", "noone", "nor", "not", "nothing", "now", "nowhere", "of", "off", "often", "on", "once", "one", "only", "onto", "or", "other", "others", "otherwise", "our", "ours", "ourselves", "out", "over", "own","part", "per", "perhaps", "please", "put", "rather", "re", "same", "see", "seem", "seemed", "seeming", "seems", "serious", "several", "she", "should", "show", "side", "since", "sincere", "six", "sixty", "so", "some", "somehow", "someone", "something", "sometime", "sometimes", "somewhere", "still", "such", "system", "take", "ten", "than", "that", "the", "their", "them", "themselves", "then", "thence", "there", "thereafter", "thereby", "therefore", "therein", "thereupon", "these", "they", "thickv", "thin", "third", "this", "those", "though", "three", "through", "throughout", "thru", "thus", "to", "together", "too", "top", "toward", "towards", "twelve", "twenty", "two", "un", "under", "until", "up", "upon", "us", "very", "via", "was", "we", "well", "were", "what", "whatever", "when", "whence", "whenever", "where", "whereafter", "whereas", "whereby", "wherein", "whereupon", "wherever", "whether", "which", "while", "whither", "who", "whoever", "whole", "whom", "whose", "why", "will", "with", "within", "without", "would", "yet", "you", "your", "yours", "yourself", "yourselves", "the"]
spam = []
ham = []
spam_train = []
ham_train = []
spam_validation = []
ham_validation = []
spam_test = []
ham_test = []
train_file = open("train.txt","w")
test_file = open("test.txt","w")
validation_file = open("validation.txt","w")
with open('test_corpus.txt','r') as f:
    for line in f:
        temp = []
        for word in line.split():
            no_punct = ""
            for char in word:
                #remove punctuations
                if char not in punctuations:
                    no_punct = no_punct + char
            #remove stop words articles and single letters
            if no_punct not in stop_words and no_punct not in articles and len(no_punct) >1:
                temp.append(no_punct)
        type = temp[0]
        if(type == 'ham'):
            ham.append(temp)
        elif(type == 'spam'):
            spam.append(temp)
    #create the train file
    temp_spam = []
    temp_spam.extend(spam)
    for i in range(0,int(len(temp_spam)*0.8)):
        spam_train.append(temp_spam.pop(random.randint(0,len(temp_spam)-1)))
    for line in spam_train:
        temp2 = ""
        for word in line:
            temp2+=word+" "
        temp2 = temp2[:-1]+"\n"
        train_file.write(temp2)
    temp_ham = []
    temp_ham.extend(ham)
    for i in range(0,int(len(temp_ham)*0.8)):
        ham_train.append(temp_ham.pop(random.randint(0,len(temp_ham)-1)))
    for line in ham_train:
        temp2 = ""
        for word in line:
            temp2+=word+" "
        temp2 = temp2[:-1]+"\n"
        train_file.write(temp2)
    train_file.close()
    #create the test file
    temp2_spam = []
    temp2_spam.extend(temp_spam)
    for i in range(0,int(len(temp2_spam)*0.5)):
        spam_test.append(temp2_spam.pop(random.randint(0,len(temp2_spam)-1)))
    for line in spam_test:
        temp2 = ""
        for word in line:
            temp2+=word+" "
        temp2 = temp2[:-1]+"\n"
        test_file.write(temp2)
    temp2_ham = []
    temp2_ham.extend(temp_ham)
    for i in range(0,int(len(temp2_ham)*0.5)):
        ham_test.append(temp2_ham.pop(random.randint(0,len(temp2_ham)-1)))
    for line in ham_test:
        temp2 = ""
        for word in line:
            temp2+=word+" "
        temp2 = temp2[:-1]+"\n"
        test_file.write(temp2)
    test_file.close()
    #create the validation file
    spam_validation.extend(temp2_spam)
    for line in spam_validation:
        temp2 = ""
        for word in line:
            temp2+=word+" "
        temp2 = temp2[:-1]+"\n"
        validation_file.write(temp2)
    ham_validation.extend(temp2_ham)
    for line in ham_validation:
        temp2 = ""
        for word in line:
            temp2+=word+" "
        temp2 = temp2[:-1]+"\n"
        validation_file.write(temp2)
    validation_file.close()