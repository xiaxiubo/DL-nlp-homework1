import jieba
import math

# 统计所有的标点符号和英文字符
punctuation = "!\"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~！？｡。＂" \
           "＃＄％＆＇()＊＋，－／：；＜＝＞＠［＼］＾＿｀｛｜｝‘’" \
           "～｟｠｢｣､、〃《》「」『』【】〔〕（）〖〗〘〙〚〛〜〝〞“”〟〰\n\u3000" \
              "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ "


def remove_punctuation(something):  # 移除列表中的标点符号
    new_l = []
    for s in something:
        if s not in punctuation:
            new_l.append(s)
    return new_l


def book_read():  # 将所有的book读取，使用jieba进行分词，再去除其中的标点
    books_name = open('source/inf.txt').read()
    book_list = books_name.split(",")

    all_words = []
    all_chars = []
    i = 0

    for book in book_list:
        i += 1
        f = open('source/'+book+'.txt', encoding="UTF-8")
        txt = f.read()
        seg_list = jieba.lcut(txt, cut_all=False)
        seg = remove_punctuation(seg_list)
        all_words.extend(seg)
        all_chars.extend(list(txt))
        print('读取进度{}/16'.format(i))
    return all_words, all_chars


def entropy_fig():  # 计算基于字与词的信息熵，使用最简单的词袋模型，各词的概率即为频率
    words, chars = book_read()
    words.sort()
    chars.sort()
    print('所统计的中文字数共有：', len(chars))
    print('所统计的中文词数共有：', len(words))

    # 计算词的信息熵
    last_word = words[0]
    times = 0
    entropy_word = 0
    words_num = len(words)
    for word in words:
        this_word = word
        if this_word == last_word:
            times += 1
            continue
        else:
            px = times / words_num  # 使用频率计算概率
            entropy_word += -px * math.log2(px)
            times = 1
        last_word = this_word
    px = times / words_num
    entropy_word += -px * math.log2(px)  # 计算最后一个单词的信息熵

    # 计算字的信息熵
    last_char = chars[0]
    times = 0
    entropy_char = 0
    chars_num = len(chars)
    for char in chars:
        this_char = char
        if this_char == last_char:
            times += 1
            continue
        else:
            px = times / chars_num  # 使用频率计算概率
            entropy_char += -px * math.log2(px)
            times = 1
        last_char = this_char
    px = times / chars_num
    entropy_char += -px * math.log2(px)  # 计算最后一个字的信息熵

    return entropy_word, entropy_char

if __name__ == '__main__':
    en_words, en_chars = entropy_fig()
    print('计算出的中文字信息熵为', en_chars)
    print('计算出的中文词信息熵为', en_words)
