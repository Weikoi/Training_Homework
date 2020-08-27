
def splitting(file):
    pass


def mapping(file):
    pass


def shuffling(file):
    pass


def reducing(file):
    pass


def get_result(file):
    pass


if __name__ == '__main__':
    from collections import Counter

    with open("./hamlet.txt") as f:
        word_list = []
        for line in f:
            if line == "\n":
                pass
            else:
                line_dict = {}
                for word in line.split():
                    word = word.strip(",!?.;':-[]|&")
                    word = word.lower()
                    if not word:
                        continue
                    word_list.append(word)

        word_dict = {}
        for word in word_list:
            if word not in word_dict:
                word_dict[word] = [1]
            else:
                word_dict[word].append(1)

        word_stas = {}
        for k, v in word_dict.items():
            # print(k, v)
            word_stas[k] = sum(v)

        kv_list = []
        for k, v in word_stas.items():
            kv_list.append((k, v))

        for i in sorted(kv_list):
            print(i[0], i[1])
