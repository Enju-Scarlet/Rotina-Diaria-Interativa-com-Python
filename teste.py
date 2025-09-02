# Acordando
print("Bom dia, flor do dia!\n")

hora_acordar = input("O sol raiou e que horas você acordou?")
hora = float(hora_acordar)
def horario(h):
    horas = int(h)
    minutos = int((h - horas) * 60)
    return f"{horas:02d}:{minutos:02d}"

print(f"Acordo às {horario(hora)} e me preparo psicológicamente para a mesma rotina de sempre!\n")

# Após Acordar
print("Levanto da cama e vou ao banheiro pra lavar o rosto;")
print("Vou a cozinha para tomar meu café da manhã;\n")

# Trabalho
hora += 0.34
print(f"Às {horario(hora)} começo meu trabalho pelo celular;\n")

# Almoço
hora += 3.67
print(f"Às {horario(hora)} é a hora que eu paro e vou almoçar;")
print("Tente descobrir qual o almoço de hoje?\n1. A comida mais tradicional brasileira: arroz, feijão, macarrão e frango;\n2. Uma pizza;\n3. Caviar e lagosta;")

comida = int(input("Qual foi o almoço de hoje (1, 2 ou 3)?"))
if comida == 1:
    print("Óbvio, o que mais seria? Até mesmo carne é um sonho ultimamente.\n")
elif comida == 2:
    print("Bem que eu queria, mas a falta de dinheiro não me permite, então vai comida básica da média dos brasileiro mesmo!\n")
elif comida == 3:
    print("Aí você sonhou bem alto! Nunca nem vi na minha frente, imagina comer esse tipo de comida. Vou no meu frango mesmo!\n")
else:
    print("Eu sei que é difícil de encarar a realidade, mas passar fome também não é uma opção.\n")

print("Acabei de almoçar, mas eu finalizei o trabalho da manhã?\n1. Sim;\n2. Não;")

opcao = int(input("Então, qual a sua escolha (1 ou 2)?"))
if opcao == 1:
    print("Perfeito! Então, eu vou aproveitar o tempo livre para a digestão enquanto assisto meus animes, até dar o horário de ir pro PC.\n")
elif opcao == 2:
    print("Então, é melhor eu terminar antes que eu vá pro PC!\n")
else:
    print("Que indecisão, mas a vida continua... Vou para o PC de qualquer jeito!\n")

# Depois do Almoço
hora += 1.0
print(f"Às {horario(hora)} vou para o PC e faço o resto do trabalho que não consigo fazer pelo celular;")
print("Finalizando-os faço outras coisas que estão pendentes. Dentre elas, são: \n1. Vou estudar/fazer atividades da Faculdade;\n2. Vou fazer outros trabalhos;\n")

pendencia = int(input("O que eu devo fazer (1 ou 2)?"))
if pendencia == 1:
    print("Nossa, como estou estudiosa! Então, vamos lá, antes que os prazos se expirem!\n")
elif pendencia == 2:
    print("Trabalhos, trabalhos e mais trabalhos. A vida não é fácil!\n")
else:
    print("A minha vontade de fazer alguma coisa é pouca, mas precisa ser feito!\n")

# Final da Tarde
hora += 4.0
duracao = hora + 0.5
print(f"Às {horario(hora)} vou lavar a louça e termino por volta das {horario(duracao)}")
print("Ou seja... hora de lanchar! Preparo meu café com biscoitos e pronto!\n")

# Pela Noite
hora += 4.5
print("Após o lanche, relaxo no PC pelo resto do dia;")
print(f"Às {horario(hora)} desligo o meu PC, pois é hora de jantar!")
print("Após isso, espero um tempo para a digestão, escovo os dentes e preparo a minha cama para me deitar!\n")

# Hora de Dormir
hora += 1.0
print(f"Às {horario(hora)} me deito para dormir e assim poder viver o amanhã com a mesma rotina de sempre!\n")