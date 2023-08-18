for value in range(6):
    print(value);

numbers = list(range(1, 6)); #this is a list, list()
print(numbers);

#even numbers between 1 and 10
even_numbers = list(range(2, 11, 2)); #this is a list, list()
print(even_numbers);

#below is a function that squares numbers 1-10 and adds them to an array/list
#squares = [value**1 for value in range(1,11)]; ...same as code below
squares = [];

def square_sequence(list_arr):
    for value in range(1, 11):
        square = value ** 2;
        list_arr.append(square);
    print(list_arr);

square_sequence(squares);

#min/max/sum functions in use
nums = [1,2,3,4,5,6,7,8,9,0];
print(f"minimum of nums is {min(nums)}, \nmaximum of nums is {max(nums)}, \nand sum of nums is {sum(nums)}.");