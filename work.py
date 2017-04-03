import random
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
articles = ['a','an','the','and']
spam = []
ham = []
spam_train = []
ham_train = []
spam_validation = []
ham_validation = []
spam_test = []
ham_test = []
train_file = open("train.txt","r")
test_file = open("test.txt","r")
validation_file = open("validation.txt","r")
with train_file as f:
    for line in f:
        temp = []
        for word in line.split():
            temp.append(word)
        #type = temp[0]
        type = temp.pop(0)
        if(type == 'ham'):
            ham.append(temp)
        elif(type == 'spam'):
            spam.append(temp)
spam_words = []
for line in spam:
    for word in line:
        spam_words.append(word)
ham_words = []
for line in ham:
    for word in line:
        ham_words.append(word)
classes = len(list(set(spam_words)))+ len(list(set(ham_words)))
k = 4
p_spam = (len(spam)+k)/((len(spam)+float(len(ham)))+k*2)
p_ham = (len(ham)+k)/((len(spam)+float(len(ham)))+k*2)
n = 0
work_file = open("final_test.txt","r")
result_file = open("result.txt","w")
with work_file as f:
    error = 0
    
    for line in f:
        sentence = ""
        i = 0
        probability_spam = []
        probability_ham = []
        for word in line.split():
            #if i != 0:
            probability_spam.append((spam_words.count(word)+k)/(float(len(spam_words))+float(k*classes)))
            probability_ham.append((ham_words.count(word)+k)/(len(ham_words)+float(k*classes)))
            sentence +=word+" "
            i = i+1
        numerador = p_spam
        for x in probability_spam:
            # if(numerador*x) < 1.0e-150:
            #     numerador *= 1000
            numerador *=x
        denominador = p_ham
        for x in probability_ham:
            denominador *=x
        if numerador == 0:
            print numerador
        denominador = numerador + denominador
        
        
        p_total = numerador/denominador
        if p_total > 0.5:
            #print line.split()[0] +" calc: spam" + str(p_total)
            result_file.write("spam \t "+ sentence+"\n")
        else:
            #print line.split()[0] +" calc: ham" + str(p_total)
            result_file.write("ham \t "+ sentence+"\n")
        n +=1
    print "Work done!"
    f.close()
