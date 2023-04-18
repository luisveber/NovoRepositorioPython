tokens = ["teste"]
with open('qrcode.txt','r') as reader:
    tokens_reader = reader.readlines()
tokens_reader = [item.replace('\n','') for item in tokens_reader]
with open('qrcode.txt','a') as writer:
    writer.write("\n")
    writer.write('\n'.join(set.difference(set(tokens), set(tokens_reader))))
    
try:
    with open('qrcode.txt', 'r') as reader:
        tokens_reader = reader.readlines()
  
        with open('qrcode.txt', 'w') as fw:
            for line in tokens_reader:
                if line.strip('\n') != '':
                    fw.write(line)
    
except:
    print("Oops! someting error")



