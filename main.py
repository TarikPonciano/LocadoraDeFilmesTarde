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
            pass
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