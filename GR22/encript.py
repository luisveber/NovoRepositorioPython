import cryptocode

chave = "1"
mensagem = "C:/EZCAD/Ezcad/Ezcad2.14.10(20180103)/EzCad2.exe"

MensagemCriptografada = cryptocode.encrypt(mensagem, chave)
print("Sua mensagem criptografada: " + MensagemCriptografada)

MensagemDescriptografada = cryptocode.decrypt(MensagemCriptografada, chave)
print("Sua mensagem descriptografada: " + MensagemDescriptografada)