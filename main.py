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
        
        if escolha == 1:
            print('Mad Max: Estrada da Fúria')
            print('John Wick')
            print('Duro de Matar')
            print('O Exterminador do Futuro')
            print('Gladiador')
            print('Velocidade Máxima')
            print('O Protetor')
            print('Missão: Impossível - Fallout')
            print('Kingsman: Serviço Secreto')
            print('Velocidade Máxima 2: Cruzeiro Total')
        
        elif escolha == 2:
            filmes = ("Indiana Jones e os Caçadores da Arca Perdida(1981)", 
                      "O Senhor dos Anéis: A Sociedade do Anel (2001)", 
                      "Jurassic Park (1993)", 
                      "Piratas do Caribe: A Maldição do Pérola Negra (2003)",
                      "A Múmia (1999)", 
                      "As Aventuras de Tintim (2011)",
                      "O Rei Leão (1994)",
                      "Mad Max: Estrada da Fúria (2015)",
                      "Jumanji: Bem-vindo à Selva (2017)",
                      "O Labirinto do Fauno (2006)",
                      )
            c = 1
            for filme in filmes:
                print(c ,end=" ")
                print(filme)
                c += 1

        elif escolha == 3:
            print('''
                    1. O Poderoso Chefão (1972)
                    2. A Lista de Schindler (1993)
                    3. A Noviça Rebelde (1965)
                    4. Forrest Gump (1994)
                    5. O Senhor dos Anéis: O Retorno do Rei (2003)
                    6. Pulp Fiction (1994)
                    7. O Clube da Luta (1999)
                    8. O Grande Lebowski (1998)
                    9. Matrix (1999)
                    10. A Origem (2010)''')
        elif escolha == 4:
            drama = ['Sociedade dos Poetas Mortos', 'Mãos Talentosas', 'O Nome da Rosa', 'Gran Torino', 'Forrest Gump', 'Coração Valente', 'Shawshank Redemption', 'Gênio Indomável']
            for i in drama:
                print(i)
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
                 print(
                "Título: A Walk to Remember\nAno: 2002\nDescrição: A história de um jovem que se apaixona por uma garota com uma condição médica terminal.\n"
                "Título: The Notebook\nAno: 2004\nDescrição: Um romance épico que narra a história de um casal cuja paixão supera as dificuldades ao longo dos anos.\n"
                "Título: Pride and Prejudice\nAno: 2005\nDescrição: Adaptação do clássico de Jane Austen, sobre uma jovem que se apaixona por um homem que parece ser seu oposto.\n"
                "Título: La La Land\nAno: 2016\nDescrição: Um musical moderno sobre a história de amor entre uma aspirante a atriz e um músico jazz.\n"
                "Título: Titanic\nAno: 1997\nDescrição: Um romance dramático ambientado a bordo do infame navio, focando em um amor proibido entre duas pessoas de diferentes classes sociais.\n"
                "Título: Eternal Sunshine of the Spotless Mind\nAno: 2004\nDescrição: Um filme que explora o amor e a memória, onde um casal se submete a um procedimento para apagar as memórias de seu relacionamento.\n"
                "Título: Notting Hill\nAno: 1999\nDescrição: A história de um proprietário de livraria que se apaixona por uma famosa atriz.\n"
                "Título: Before Sunrise\nAno: 1995\nDescrição: Um romance que segue dois jovens que se encontram em um trem e passam uma noite mágica juntos em Viena.\n"
                "Título: 10 Things I Hate About You\nAno: 1999\nDescrição: Uma adaptação moderna de 'A Megera Domada' de Shakespeare, com uma história de amor entre adolescentes no ensino médio.\n"
                "Título: To All the Boys I've Loved Before\nAno: 2018\nDescrição: Uma comédia romântica sobre uma jovem cujas cartas de amor secretas são acidentalmente enviadas para todos os seus antigos crushes.\n"
            )
        elif escolha == 8:

            print(f'''1 - O Exorcista
2 - Psicose
3 - O Iluminado
4 - A Bruxa de Blair
5 - O Massacre da Serra Elétrica
6 - Hereditário
7 - Atividade Paranormal
8 - O Bebê de Rosemary
9 - A Noite dos Mortos-Vivos
10 - It: A Coisa''')
            
        elif escolha == 9:
            pass
        elif escolha == 10:
            print("1. Scooby doo")
            print("2. O Clube dos Cinco")
            print("3. A Verdade Nua e Crua")
            print("4. O Homem que Sabia Demais")
            print("5. O Enigma do Outro Mundo")
            print("6. Um lugar silenciosa")
            print("7. Memento")
            print("8. Briquedo Asass")
            print("9. Knives Out: Entre Facas e Segredos 2019")
            print("10. A Garota no Treem")
        elif escolha == 11:
            print("O Apartheid na África do Sul")
            print("13ª Emenda (13th)")
            print("O Céu de Outubro")
            print("Won't You Be My Neighbor?")
            print("Grizzly Man")
            print("Jiro Dreams of Sushi")
            print("Free Solo")
            print("O Dilema das Redes")
            print("O Enigma do Horizonte")
            print("13th")
            pass
        elif escolha == 12:
            print ('''"Toy Story" (1995)
                    "O Rei Leão" (1994)
                    "Procurando Nemo" (2003)
                    "Shrek" (2001)
                    "Frozen" (2013)
                    "Os Incríveis" (2004)
                    "Divertida Mente" (2015)
                    "Moana" (2016)
                    "Zootopia" (2016)
                    "Detona Ralph" (2012)''')      
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
