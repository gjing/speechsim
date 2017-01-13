import pickle
import random
import time

# test_dict = {'count':0, 'words':{}}
# words format will be {word: {'count': int, 'nextword': {}}}
# nextword format will be {word: count}
def simulate(filename, lines):
    sim_dict = {}
    with open(filename, 'rb') as pickled_logs:
        sim_dict = pickle.load(pickled_logs)
    for i in range(0, lines):
        line = ''
        # get first word
        target_num = random.randrange(1, sim_dict['count'] + 1)
        current_count = 0
        current_word = ''
        for word in sim_dict['words']:
            current_count += sim_dict['words'][word]['count']
            if current_count > target_num:
                current_word = word
                line+=word.title()
                # get next word
                current_count = 0
                next_target_num = random.randrange(1, sim_dict['words'][word]['count'] + 1)
                for nextword, freq in sim_dict['words'][word]['nextword'].iteritems():
                    current_count+=freq
                    if current_count > next_target_num:
                        current_word = nextword
                        break
                break
        # get next word until linebreak
        while current_word != 'ENDLINE':
            line += ' '
            line += current_word
            current_count = 0
            next_target_num = random.randrange(1, sim_dict['words'][current_word]['count'] + 1)
            for nextword, freq in sim_dict['words'][current_word]['nextword'].iteritems():
                current_count+=freq
                if current_count > next_target_num:
                    current_word = nextword
                    break
        print line

simulate('pickled_logs.p', 10)
print 'done'
