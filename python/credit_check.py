summed_array = 0
def credit_check(cc_number):
    global summed_array
    summed_array = 0
    # Convert the string credit card number to an int list
    cc_listing = list(map(int, cc_number))
    # Loop through the list starting at the 2nd idx and stepping by 2
    for cc_num in range(0, len(cc_listing), 2):
        # Double and replace the value in the list
        cc_listing[cc_num] *= 2
    # Now loop through for all values over 10
    # Now we loop the 
    for modified_num in range(0, len(cc_listing)):
        # Now we check if the value is 10 or greater
        if cc_listing[modified_num] >= 10:
            # We split the current element to do math
            res = [int(x) for x in str(cc_listing[modified_num])]
            # Math
            cc_listing[modified_num] = res[0] + res[1]
        # Math the final sum of the array of numbers after all modifications
        summed_array += cc_listing[modified_num]
    # Return print of the modified list
    return "The number is valid!" if summed_array % 10 == 0 else "The number is invalid!"

# Your Luhn Algorithm Here
# Expected Output:
# If it is valid, print "The number is valid!"
# If it is invalid, print "The number is invalid!"