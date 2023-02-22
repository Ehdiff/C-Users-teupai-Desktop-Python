#Os cálculos pra conversão das medidas
def celsius_to_fahrenheit(celsius):
    return(celsius*1.8) + 32

def fahrenheit_to_celsius(fahrenheit):
    return(fahrenheit-32) / 1.8

def meters_to_feet(metros):
    return(metros*3.281)

def feet_to_meters(pés):
    return(pés/3.281)
#-------------------------------------------------------------------------------------------------------------------------------------------
#"Menu" do conversor e funcionalidades pra interação
while True:
    print("Conversor de medidas super legal :D")
    print("Escolha a opção de conversão ->")
    print("1. Celsius para fahrenheit")
    print("2. Fahrenheit para Celsius")
    print("3. Metros para pés")
    print("4. Pés para metros")
    print("5. Sair")

#Configuração dos botão
    escolha = input("Digite sua opção ->")
    #Função pra sair do conversor
    if escolha == "5":
        break
    
    #Botões e mostra dos resultados 
    if escolha == "1":
        celsius = float(input("Digite a temperatura em Celsius: "))
        print(f"{celsius} graus Celsius é igual a {celsius_to_fahrenheit(celsius)} graus Fahrenheit")
    elif escolha == "2":
        fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
        print(f"{fahrenheit} graus Fahrenheit é igual a {fahrenheit_to_celsius(fahrenheit)} graus Fahrenheit")
    elif escolha == "3":
        metros = float(input("Digite o comprimento em metros: "))
        print(f"{metros} metros é igual a {meters_to_feet(metros)} pés")
    elif escolha ==  "4":
        pés = float(input("Digite o comprimento em pés: "))
        print(f"{pés} pés é igual a {feet_to_meters(pés)} metros")
    else: 
        print("Opção inválida, tente de novo.")
        break