"""
Creating A Search Engine
sentence = ['This is good','Python is good','Pyhton is not a pyhton snake ']
input : "Python"
output:
3 results found :
1.Pyhton is not a pyhton snake
2.Python is good
3.This is good
"""
# --------------------------------------------------------------------------------
def search(sentence1,sentence2):
    words1 = sentence1.split(" ")
    words2 = sentence2.split(" ")
    score =0
    for word1 in words1:
        for word2 in words2:
            # print(f"Matching {word1} with {word2}")
            if word1.lower()==word2.lower():
                score +=1
    return score


if __name__ == '__main__':
    Sentences = ['This is good','Python is good','Python is not a python snake']
    query = input("Please enter the query string:\n")
    score = [search(query,sentence)for sentence in Sentences]
    sortedSentScore =[sentScore for sentScore in sorted(zip(score,Sentences),reverse=True)]
    # print(sortedSentScore)
    print(f"{len(sortedSentScore)} results found!!!")
    for score, item in sortedSentScore:
        print(f" \"{item}\" : with score of {score}.")