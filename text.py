import re


def Find_word(file_name):

    text = ""
    with open('C:/Users/骚年/Desktop/'+file_name, 'r+') as f:
        text += f.read()
    text = re.split('[ :,\,,\n,.,&,(,),/]', text)  # 使用正则表达式和split分割

    dic = dict()
    for word in text:
        if word != '':
            word = word.lower()
            dic[word] = dic.get(word, 0) + 1  # 加入字典，计数

    for key in dic:
        print(key, "出现次数：", dic[key])


def Find_char(file_name):
    text = ""
    with open('C:/Users/骚年/Desktop/'+file_name, 'r+') as f:
        text += f.read()
    # text = re.split('[\n]', text)  # 使用正则表达式和split分割

    dic = dict()
    for c in text:
        if c != '\n' and c != ' ':
            if c.isalpha():
                c = c.lower()
            dic[c] = dic.get(c, 0) + 1  # 加入字典，计数

    for key in dic:
        print(key, "出现次数：", dic[key])


def Find_sentence(file_name):
    text = ""
    with open('C:/Users/骚年/Desktop/'+file_name, 'r+') as f:
        text += f.read()
    text = text.split('.')
    print('句子的数量为：', len(text))


def main():
    '''
    具体命令行界面要求如下：

    命令模式： wc.exe [参数] [文件名]

    例：wc.exe -c story.txt 统计字符数

        wc.exe -w story.txt 统计单词数

        wc.exe -s story.txt 统计单词数
    '''
    while True:

        print('请在一行内输入完整的命令，输入quit退出')

        a = input()
        if a == 'quit':
            break

        a = a.split(' ')
        py_name = a[0]
        cmd = a[1]
        file_name = a[2]

        if cmd == '-c':
            Find_char(file_name)
        elif cmd == '-w':
            Find_word(file_name)
        elif cmd == '-s':
            Find_sentence(file_name)


if __name__ == "__main__":
    main()
