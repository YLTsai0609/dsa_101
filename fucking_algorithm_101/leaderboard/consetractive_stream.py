"""
easy

https://stackoverflow.com/questions/59036027/the-number-stream-detection

optimial tc : O(N)
"""

# v2 build hash table
# tc : O(N) when building hash table
# sc : O(N) when building hash table
# tc : O(1) when check con_stream
def hash_table_sol(strParam):
    con_stream_table = {}
    curr_digit = -1  # not possible value for this question
    curr_cnt = 0
    for d in strParam:
        if curr_digit != d:
            # store previous digit
            con_stream_table[curr_digit] = curr_cnt
            curr_cnt = 0

            # found new digit
            curr_digit = d
            con_stream_table[d] = 1  # clean previous records, add fresh records
        curr_cnt += 1
    # for debug
    # print(con_stream_table)
    for d, con_stream in con_stream_table.items():
        if con_stream >= d:
            return True
    return False


# v1, optimal
def StringChallenge(strParam):
    # from 2 ~ 9, generate sbstring 22, 333, ... 999999999
    for i in range(2, 9 + 1):
        con_stream = str(i) * i
        if con_stream in strParam:
            return True
    else:
        return False

    # code goes here
    # return strParam


# keep this function call here
# print(StringChallenge(input()))


if __name__ == "__main__":
    input_str = "55333555554"
    for sol in [hash_table_sol, StringChallenge]:
        print(sol(input_str))

