def counting(input_array):
    result = []
    
    for x in input_array:
        # Changes the integer to a string
        if isinstance(x, int):
            letter_count = len(str(x))
        # Just continues since it's a string
        else:
            letter_count = len(x)
        
        # Append the letter count to the result list
        result.append(letter_count)
        
    return result

def main():
    input_array = ["hello", "python", "dumb"]
    print("Input:", input_array)
    
    # Print the output
    print("Output:", counting(input_array))

if __name__ == "__main__":
    main()