sent="Hello, I am prathap, I am from AP. I did Btech from JNTU. I am doing job now, So i am getting salary"
word_list=[word.strip(",|.|!").lower() for word in sent.split()]
print(word_list)
words_dict={}

for word in word_list:
    if word not in words_dict:
        words_dict[word]=0
    words_dict[word]+=1
print(words_dict)