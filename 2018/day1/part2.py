def parse_input(dtype=str):

    return [dtype(line.rstrip('\n')) for line in open('input.txt')]

data = parse_input(dtype=int)

def cum_sum(input_, freq_list_=[]):
    freq_ = input_[0]
    freq_list_.append(freq_)
    found_freq = None
    for k in range(1,len(input_)):
        freq_ += input_[k]
        if freq_  in freq_list_:
            found_freq = freq_
            break
        freq_list_.append(freq_)
    return freq_list_, found_freq

freq_list, found_freq = cum_sum(data)

itr = 0

found_freq = None

while found_freq  is None:

    print "Iteration \t", itr

    freq_list, found_freq = cum_sum( [freq_list[-1]] + data, freq_list)

    itr += 1


print "The first repeat frequency is \t", found_freq


