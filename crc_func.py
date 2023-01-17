def xor(x, y):
    res = []
    for i in range(1, len(y)): 
        if x[i] == y[i]: #flip bits when nesscary
            res.append('0')
        else:
            res.append('1')
    return ''.join(res)

def crc(data, G):

    msb = len(G) # get length of the divisor so we can segement the data  
    seg = data[0 : msb] # segment data sub array
    # print("In crc\n")
    # print(data)
    #loop=0
    while  msb < len(data): #start divission algorithim 
 
        if seg[0] == '1': #if divided in  xor to get next segment of focus
            seg= xor(G, seg) + data[msb] #carry down next bit
 
        else:  #if does not divide in the xor with 0 
            seg = xor('0'*msb, seg) + data[msb] #carry down next bit

        #seg = seg[1:]
        #loop+=1  
        msb+=1 
        #print(seg[1:])
    R = seg[1:]
    return R

def encoder(data, G):

    lenght_G = len(G)   
    data_crc = data + '0'*(lenght_G-1)  # add extra zeros for crc
    remainder =crc(data_crc, G) #find the reminder of the crc
    encodeddata = data + str(remainder) #add this remainder onto the end
    return encodeddata    

def decoder(data, G):
    lenght_G = len(G)   
    data_crc = data + '0'*(lenght_G-1)  # add extra zeros for crc
    remainder =crc(data_crc, G) #find the reminder of the crc
    return str(remainder)