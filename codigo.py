login = input("Digite seu login: ")
senha = input("Digite sua senha: ")

if login == "admin" and senha == "1234":
   print("Acesso permitido, bem-vindo ao sistema.")

   nome = input("Digite seu nome: ")
   print(f"Olá, {nome},bem-vindo ao sistema. ")

   idade = int(input("Digite sua idade: "))

   if idade >= 18: 
      print(f"seja bem-vindo ao banco,{nome}!")
      cpf = input("Digite seu CPF: ")
      print(f"Cadastro concluído para {nome}. CPF:{cpf}")

      saldo = 1250.00
   while True:
      print("\nEscolha uma opção:")
      print("1 - Ver saldo")
      print("2 - Sacar dinheiro")
      print("3 - Depositar dinheiro")
      print("0 - Sair")

      opcao = int(input("Digite a opção desejada: "))

      if opcao == 1:
         print(f"Seu saldo é de R${saldo:.2f}")

      elif opcao ==2: 
         valor = int(input("Quanto deseja sacar? "))
         if valor <= saldo: 
             saldo -= valor 
             print(f"Saque de R${valor:.2f} realizado com sucesso.")
             print(f"Seu saldo atual: R${saldo:.2f}") 
         
         else:
             print("Saldo insuficiente.")

      elif opcao == 3:
         valor = float(input("Quanto deseja depositar?"))
         saldo += valor 
         print(f"Deposito de R$ {valor:.2f} realizado com sucesso.")
         print(f"Saldo atual: R$ {saldo:.2f}")
         
      elif opcao == 0:
         print("Encerrando o sistema... Até logo!")
         break

      else:
         print("Opção inválida.")

   else: 
      print(f"{nome}, Você precisa ter pelo menos 18 anos para abrir uma conta.")
else:
   print("Senha ou login incorretos, tente novamente.")
   

   
  



      


   
      
      
    
    
         



  


