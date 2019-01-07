#Open video file
with open('C:\\Users\\hello\\Desktop\\SyncVidWork\\bbb_360p_c.ts', 'rb') as f:
    syncdata = f.read(1).hex()
    #print (syncdata)
    if syncdata == '47':
       #print(syncdata)
           
       count = 0
       syncdata1 = 1
       #If not the end of the file, loop
       while syncdata1 != '':
          #Move to next header
          syncdata = f.seek(187, 1)
          #Read first byte of next header
          syncdata1 = f.read(1).hex()
          #If read 47 hex continue
          if syncdata1 == '47':
              print(syncdata1)
              count += 1
              print(count)
          if count == 5:
              break

    #Read bytes in chunks to put inside array to find PID
    s1 = f.seek(0)
    #Loop for the first 188 bytes
    for i in range(188):
        print(i)
        #w1 = [f.read(1).hex()]
        #print(w1)
        w1 = (f.read(1).hex())
        print(w1)
    