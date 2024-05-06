import math

def decode(message_file):
    # Read the encoded message from the file
    with open(message_file, 'r') as file:
        lines = file.readlines()
    
    # Initialize an empty list to store the words in the pyramid
    pyramid_dic = {}
    
    # Iterate over each line in the file to build the pyramid
    for line in lines:
        # Split the line into number and word
        num, word = line.strip().split(' ', 1)

        # Append the num and word to the pyramid_dic list
        pyramid_dic[int(num)] = word

        
    # Sort the num and word to the sorted_dic list
    sorted_dic = dict(sorted(pyramid_dic.items()))

    # Put the sorted_dic into a pyramid in order 
    pyramid = []
    i = 1
    rows = int((-1+math.sqrt(1-4*1*(-2)*(len(sorted_dic))))/2)
    while i <= rows:
        temp = int(i*(i+1)/2)
        pyramid.append(list(sorted_dic.keys())[:temp])
        i += 1 
    
    # Extract the last number of each row in the pyramid and get the associated word
    message = ' '.join([str(pyramid[i-1][-1]) for i in range(1, len(pyramid)+1)])
    decoded_message = ' '.join([sorted_dic[int(num)] for num in message.split()])

    return decoded_message

def main():
    # File containing the encoded message
    message_file = input("Enter the filename containing the encoded message: ")
    
    # Decode the message
    decoded_message = decode(message_file)
    
    # Print the decoded message
    print(decoded_message)

if __name__ == "__main__":
    main()
