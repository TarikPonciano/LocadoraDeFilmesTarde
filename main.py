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
            print('''
1.  Blade Runner (1982) - Um clássico de Ridley Scott que explora temas de identidade e humanidade em um futuro distópico.

2.  2001: A Space Odyssey (1968) - Dirigido por Stanley Kubrick, este épico é conhecido por sua visão inovadora sobre a exploração espacial e a inteligência artificial.

3.  Matrix (1999) - Um marco no gênero, com uma trama que questiona a natureza da realidade e apresenta cenas de ação icônicas.

4.  Interstellar (2014) - Dirigido por Christopher Nolan, combina uma história emocionante com conceitos complexos sobre espaço e tempo.

5.  Ex Machina (2014) - Um thriller psicológico que aborda a inteligência artificial e a ética em torno dela.

6.  Inception (2010) - Também de Christopher Nolan, mistura sonhos e realidade de maneira engenhosa e visualmente impressionante.

7.  O Exterminador do Futuro (1984) - Um filme de James Cameron que mistura ação e ficção científica com a ideia de máquinas do futuro enviadas ao passado.

8.  O Hospedeiro (2006) - Um filme sul-coreano que combina ficção científica com horror, sobre um monstro mutante que ameaça uma família.

9.  Contato (1997) - Baseado no livro de Carl Sagan, este filme explora a possibilidade de contato com civilizações alienígenas.

10. Gattaca (1997) - Um thriller que examina um futuro onde a engenharia genética determina o valor e o potencial das pessoas.
''')

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
            pass
        elif escolha == 16:
            pass
        else:
            print("Gênero inválido!")
        
        
    
    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")

if __name__ == "__main__":
    main()