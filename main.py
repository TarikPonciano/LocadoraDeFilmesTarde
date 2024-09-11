def exibir_menu():
    print("Escolha um gênero de filme:")
    print("1. Ação")
    print("2. Aventura")
    print("3. Comédia")
    print("4. Drama")
    print("5. Ficção Científica")
    print("6. Fantasia")
    print("7. Romance")
    print("8. Terror")
    print("9. Suspense")
    print("10. Mistério")
    print("11. Documentário")
    print("12. Animação")
    print("13. Musical")
    print("14. Policial")
    print("15. Guerra")
    print("16. Histórico")

def main():
    exibir_menu()
    
    try:
        escolha = int(input("Digite o número do gênero escolhido: "))
        
        #Faça modificações apenas na seção do seu número
        #Faça o print de 10 filmes do gênero selecionado
        if escolha == 1:
            pass
        elif escolha == 2:
            pass
        elif escolha == 3:
            pass
        elif escolha == 4:
            pass
        elif escolha == 5:
            pass
        elif escolha == 6:
            pass
        elif escolha == 7:
            pass
        elif escolha == 8:
            pass
        elif escolha == 9:
            pass
        elif escolha == 10:
            pass
        elif escolha == 11:
            pass
        elif escolha == 12:
            pass
        elif escolha == 13:
            pass
        elif escolha == 14:
            pass
        elif escolha == 15:
            filmes_de_guerra = print('''
                                     
            Título: O Resgate do Soldado Ryan (1998)
            ---------------------------------------------------------------------------------------
            Sinopse: Durante a Segunda Guerra Mundial, 
            um grupo de soldados americanos é enviado para encontrar 
            e resgatar um paraquedista cujos irmãos foram mortos em combate.
                                     
   
            Título: Dunkerque (2017)
            ---------------------------------------------------------------------------------------
            Sinopse: Baseado na evacuação de Dunkirk em 1940, 
            o filme retrata a luta desesperada de soldados 
            britânicos e aliados para escapar das forças alemãs que os cercam.
   
                                     
            Título: A Lista de Schindler (1993)
            --------------------------------------------------------------------------------------
            Sinopse: A história real de Oskar Schindler, 
            um empresário que salvou mais de mil judeus durante o Holocausto, 
            comprando-os como trabalhadores para suas fábricas.
            
  
            Título: Até o Último Homem (2016)
            --------------------------------------------------------------------------------------
            Sinopse: Baseado na verdadeira história de Desmond Doss, 
            um objetor de consciência que, sem portar armas, 
            salvou 75 homens durante a Batalha de Okinawa na Segunda Guerra Mundial.
                                     

            Título: Corações de Ferro (2014)
            --------------------------------------------------------------------------------------
            Sinopse: Durante os últimos dias da Segunda Guerra Mundial,
            um sargento de tanque e sua equipe enfrentam desafios 
            extremos enquanto lutam contra forças alemãs."
    
                                     
            Título: Falcão Negro em Perigo (2001)
            --------------------------------------------------------------------------------------
            Sinopse: Retrata a batalha de Mogadíscio, na Somália, 
            onde forças especiais americanas enfrentaram uma resistência feroz 
            durante uma missão de captura de líderes rebeldes.
                                     
    
            Título: O Jogo da Imitação (2014)
            --------------------------------------------------------------------------------------
            Sinopse: A história de Alan Turing, 
            um matemático que ajudou a decifrar os códigos de 
            guerra nazistas e desempenhou um papel crucial na vitória dos Aliados.
                                     
   
            Título: O Menino do Pijama Listrado (2008)
            --------------------------------------------------------------------------------------
            Sinopse: Um jovem garoto, filho de um oficial nazista, 
            forma uma amizade inocente com um menino judeu preso em um campo de concentração, 
            levando a uma trágica descoberta.
                                     
   
            Título: O Pianista (2002)
            --------------------------------------------------------------------------------------
            Sinopse: A história de Władysław Szpilman, 
            um pianista polonês judeu que sobrevive ao Holocausto em Varsóvia,
            enfrentando enormes desafios e perdas pessoais.
                                     
    
            Título: A Queda! As Últimas Horas de Hitler (2004)
            --------------------------------------------------------------------------------------
            Sinopse: Retrata os últimos dias de Adolf Hitler e a queda do Terceiro Reich 
            em um drama que se passa em seu bunker durante o colapso de Berlim.
    
              ''')
            pass
        elif escolha == 16:
            pass
        else:
            print("Gênero inválido!")
        
        
    
    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")

if __name__ == "__main__":
    main()