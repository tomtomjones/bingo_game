import random

def generate_numbers():

    for i in range(1):
        t_start = 0
        t_end = 10
        numbers = []
        multiple_numbers = random.sample(range(0,9), 5) # we need 15 numbers, this controls the amount from the same number range.

        # make sure there is at least 1 number per bingo card column
        for i in range(9):
            range_number = 1
            if i in multiple_numbers:
                # makes sure one column has 3 numbers
                if i == multiple_numbers[0]:
                    range_number = 3
                else :
                    range_number = 2

            # Generates the bingo number, within specified 10s groups
            if t_start == 0: # we need this because a bingo number cannot be 0
                t_start = 1
                next_number = random.sample(range(t_start, t_end), range_number)
                t_start = 0
            else:
            

                next_number = random.sample(range(t_start, t_end), range_number)

            numbers.insert(0,next_number)
            
            t_start += 10
            t_end += 10

        return(numbers)


def bingo_row_sort(b_numbers, row1, row2, row3):
    bingo_numbers = b_numbers
    bingo_numbers = sorted(bingo_numbers, key=lambda l: (len(l), l),reverse=True)

    for i in range(3): # number of bingo card rows
        for j in range(5): # 5 numbers per row #len(bingo_numbers)
            if i == 0:
                row1.insert(0,bingo_numbers[j][0])
            if i == 1:
                row2.insert(0,bingo_numbers[j][0])
            if i == 2:
                for k in range(len(bingo_numbers)):
                    row3.insert(0,bingo_numbers[k][0])
                break # final row needs to be broken out of because the list index will get out of range in this j sub loop
            bingo_numbers[j].pop(0)
            
            bingo_numbers = [x for x in bingo_numbers if x != []] # removes the empty lists
    
# makes sure every row has 9 entries in the list
def pad_row(b_row):
    roww = b_row
    temp_row= []
    t_start = 0
    t_end = 10
    for i in range(len(roww)):
        
        number_check = roww[i]

        for j in range(10): # range(len(roww)):

            # print(number_check)

            if number_check >= t_start and number_check < t_end:
                temp_row.insert(0,number_check)
                # print(temp_row)
                t_start += 10
                t_end += 10
                break
            else :
                temp_row.insert(0,' ')
                # print(temp_row)        

                t_start += 10
                t_end += 10

    if len(temp_row) < 9:
        for i in range((9 - len(temp_row))):
            temp_row.insert(0,' ')
    
    return temp_row




def Bingo_card_generator():

    row1 = []
    row2 = []
    row3 = []

    bingo_numbers = generate_numbers()
    bingo_row_sort(bingo_numbers, row1, row2, row3)


    row1 = sorted(row1)
    row2 = sorted(row2)
    row3 = sorted(row3)

    row1 = pad_row(row1)
    row2 = pad_row(row2)
    row3 = pad_row(row3)

    row1.reverse()
    row2.reverse()
    row3.reverse()

    # print(row1,"\n", row2,"\n", row3)

    return [row1,row2,row3]

# normal bingo has 90 numbers but this only has 89, will fix someday. maybe not
def bingo_call_numbers():
    bingo_call = random.sample(range(1,90), 89)
    # print(bingo_call)
    return bingo_call

