

def CalcScore(text1, text2):
    #计算两个文本的相似度通常可以使用文本嵌入向量和相似度度量方法。以下是一个Python示例，使用Python中的gensim库和余弦相似度来计算两个文本的相似度：
    from gensim.models import Word2Vec
    from sklearn.metrics.pairwise import cosine_similarity
    import numpy as np
    # 为了演示目的，我们将使用一个小的Word2Vec模型
    # 你可以根据需要使用更大的预训练模型
    sentences = [text1, text2]

    # 分词并训练Word2Vec模型
    tokenized_sentences = [sentence.split() for sentence in sentences]
    model = Word2Vec(tokenized_sentences, vector_size=100, window=5, min_count=1, sg=0)

    # 获取文本的嵌入向量
    vector1 = np.mean([model.wv[word] for word in tokenized_sentences[0]], axis=0)
    vector2 = np.mean([model.wv[word] for word in tokenized_sentences[1]], axis=0)

    # 计算余弦相似度
    similarity = cosine_similarity([vector1], [vector2])
    similarity = cosine_similarity([vector2], [vector1])

    print("文本1和文本2的相似度:", similarity[0][0]) # 文本1和文本2的相似度: -0.010839179

    #这段代码将两个文本转化为Word2Vec嵌入向量，然后计算它们之间的余弦相似度。请注意，为了获得更准确的结果，你可以使用更大的预训练Word2Vec模型，如GloVe或FastText，或使用BERT等现代的深度学习模型。
    return similarity[0][0]

def DiffTwoText(text1, text2):
    import difflib

    # text1 = "这是第一个文本的示例~ "
    # text2 = "这是第二个文本哈示例~ "
    # ['- 这是第一个文本的示例~', '?    ^   ^\n', '+ 这是第二个文本哈示例~', '?    ^   ^\n']

    # text1 = "这是第一个文本的示例~ "
    # text2 = "这是第二个文本哈示例！"
    # # ['- 这是第一个文本的示例~', '+ 这是第二个文本哈示例！']
    #
    # text1 = "这是第一个文本的示例~"
    # text2 = "这是第二个文本哈事例！"
    # # ['- 这是第一个文本的示例~', '+ 这是第二个文本哈示例！']


    # 使用difflib库查找差异
    d = difflib.Differ()
    diff = list(d.compare(text1.split(), text2.split()))
    print(diff)
    print(diff[0]);
    # print(diff[0].index("一"))
    print(diff[1]);
    # print(diff[1].index('^'), type( diff[1].index('^') ))
    # print(diff[2])
    # print(diff[3]); print(diff[3].index('^',6 ), len(diff[3]))

    foundIdx = 0
    foundList = []
    while( foundIdx >= 0 ):
        print("Try>",foundIdx)
        foundIdx = diff[3].index('^',foundIdx )
        print("Found>",foundIdx)
        foundList.append(foundIdx)
        foundIdx = foundIdx + 1
        if(len(diff[3])-1 <= foundIdx): # no <=
            break
    print(foundList)

    # 提取不同的字段
    added = " ".join(word[2:] for word in diff if word.startswith('+ '))
    removed = " ".join(word[2:] for word in diff if word.startswith('- '))

    print("文本1中的不同字段:", removed)
    print("文本2中的不同字段:", added)

    return foundList


if __name__ == '__main__':
    text1 = "这是第一个文本的示例。"
    text2 = "这是第二个文本的示例! "
    score = CalcScore( text1, text2)
    two = DiffTwoText( text1, text2)

    print("Func>", score)
    print("Func>", two)
    pass