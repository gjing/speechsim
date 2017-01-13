import pickle
import glob
import string

def get_files():
    return glob.glob("*.log")

test_dict = {'count':0, 'words':{}}
# words format will be {word: {'count': int, 'nextword': {}}}
# next format will be {word: count}


def print_log(names):
    for name in names:
        print name
        with open(name, 'r') as current_log:
            lines = current_log.readlines()
            for line in lines:
                line = line[:-1].split(' ')
                if len(line) > 2 and '<' in line[1] and '>' in line[1]:
                    for x in range(2, len(line)):
                        endline = False
                        word = line[x]
                        if '.' in word or '?' in word or x == len(line) -1:
                            endline = True
                        word = word.translate(None, string.punctuation).lower()
                        test_dict['count'] += 1
                        try:
                            test_dict['words'][word]['count'] += 1
                        except KeyError:
                            test_dict['words'][word] = {}
                            test_dict['words'][word]['count'] = 1
                            test_dict['words'][word]['nextword'] = {}
                            test_dict['words'][word]['nextword']['ENDLINE'] = 0
                        if endline:
                            test_dict['words'][word]['nextword']['ENDLINE'] += 1
                        else:
                            try:
                                test_dict['words'][word]['nextword'][line[x+1].translate(None, string.punctuation).lower()] += 1
                            except:
                                test_dict['words'][word]['nextword'][line[x+1].translate(None, string.punctuation).lower()] = 1
    with open("pickled_logs.p", 'wb') as pickled_logs:
        pickle.dump(test_dict, pickled_logs)
    return test_dict

print_log(get_files())
