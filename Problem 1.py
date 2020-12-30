# Multiples of 3 and 5
# This program create a list of all multiples of 3 and 5 less than or equal to the input target given by the user
# and output their sum.

# given factors
factor1 = 3
factor2 = 5

# receive input target from user
target = int(input())

# list to hold the multiples
multiples = []

# counters for the given factors
counter1 = 0
counter2 = 0


# main function
def main(multiples_list):
    # call count_multiples function to count by each factor
    count_multiples(counter1, factor1)
    count_multiples(counter2, factor2)

    # remove duplicate multiples in the list
    multiples_list = list(dict.fromkeys(multiples_list))
    print(sum(multiples_list))


# "count_multiples" function counts by the factor up to the target adding adding each multiple to a list
def count_multiples(counter, factor):
    while counter < target:
        multiples.append(counter)
        counter += factor


# main function call
main(multiples)
