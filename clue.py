from random import *
import random
from collections import deque

personajes = ["Profesor Plum", "Miss Scarlet", "Sr. Mustard", "Sra. Sutton", "Profesora Higgins"]
lugares = ["Biblioteca", "Salón de baile", "Comedor", "Salón de Billar", "Invernadero"]
armas = ["Candelabro", "Hacha", "Llave inglesa", "Palo de billar", "Cuchillo"]

h1 = deque([])
h2 = deque([])
h3 = deque([])
h4 = deque([])
h5 = deque([])

def createHistory():
    pista:str
    pista2:str
    random.shuffle(personajes)
    random.shuffle(lugares)
    random.shuffle(armas)

    for q in sample([personajes], k =1):
        h1.append(q[0])
        h2.append(q[1])
        h3.append(q[2])
        h4.append(q[3])
        h5.append(q[4])
    for q in sample([lugares], k =1):
        h1.append(q[0])
        h2.append(q[1])
        h3.append(q[2])
        h4.append(q[3])
        h5.append(q[4])
    for q in sample([armas], k =1):
        h1.append(q[0])
        h2.append(q[1])
        h3.append(q[2])
        h4.append(q[3])
        h5.append(q[4])
    rPista = random.randrange(1,4,1)
    while True:
        rPista2 = random.randrange(1,4,1)
        if rPista2 != rPista:
            if rPista2 == 1:
                if h1[0] == 'Profesor Plum' or h1[0] == 'Sr. Mustard':
                    pista2 = "El sospechoso es hombre"
                else: pista2 = "El sospechoso es mujer"
            elif rPista2 == 2:
                if h1[1] == 'Biblioteca' or h1[1] == 'Invernadero':
                    pista2 = "El cuerpo se encontro en un lugar poco concurrido"
                else: pista2 = "El cuerpo se encontro en un lugar muy concurrido"
            elif rPista2 == 3:
                if h1[2] == 'Cuchillo' or h1[2] == 'Hacha':
                    pista2 = "Se sabe que fue asesinado con un objeto filoso"
                else: pista2 = "Se sabe que fue asesinado tras multiples golpes"
            break

    if rPista == 1:
        if h1[0] == 'Profesor Plum' or h1[0] == 'Sr. Mustard':
            pista = "El sospechoso es hombre"
        else: pista = "El sospechoso es mujer"
    elif rPista == 2:
        if h1[1] == 'Biblioteca' or h1[1] == 'Invernadero':
            pista = "El cuerpo se encontro en un lugar poco concurrido"
        else: pista = "El cuerpo se encontro en un lugar muy concurrido"
    elif rPista == 3:
        if h1[2] == 'Cuchillo' or h1[2] == 'Hacha':
            pista = "Se sabe que fue asesinado con un objeto filoso"
        else: pista = "Se sabe que fue asesinado tras multiples golpes"
    random.shuffle(personajes)
    random.shuffle(lugares)
    random.shuffle(armas)
    return pista, pista2

def getPersonObject(pObject):
    if pObject == h1[0]:
        person = h1
    if pObject == h2[0]:
        person = h2
    if pObject == h3[0]:
        person = h3
    if pObject == h4[0]:
        person = h4
    if pObject == h5[0]:
        person = h5
    return person

def getQuestion(number: int, sospechoso: str):
    i:int = 1
    txt:str
    print("Opciones: ")
    if number == '1':
        for p in personajes:
            if p != sospechoso:
                print(f'\t {i}) {p}')
            else: print(f'\t {i}) --------')
            i = i+1
        i=1
        us_input: int = input('Viste a: ')
        person = getPersonObject(personajes[int(us_input)-1])
        print("\nPreguntar por... \nOpciones: \n\t 1) Lugar \n \t 2) Arma")
        us_input2: int = input('Tu: ')
        if(us_input2 == '1'):
            print("\nOpciones:")
            txt = "En el lugar"
            for l in lugares:
                print(f'\t {i}) {l}')
                i = i+1
        if(us_input2 == '2'):
            print("\nOpciones:")
            txt = "Con el objeto"
            for a in armas:
                print(f'\t {i}) {a}')
                i = i+1
        us_input3: int = input(f'{txt}: ')
        if us_input2 == '1':
            if person[1] == lugares[int(us_input3)-1]:
                print(f"\n{sospechoso}: Si, yo vi a {person[0]} {txt} {lugares[int(us_input3)-1]}\n")
            else: return print(f"\n{sospechoso}: No vi nada de eso\n")
        if us_input2 == '2':
            if person[2] == armas[int(us_input3)-1]:
                print(f"\n{sospechoso}: Si, yo vi a {person[0]} {txt} {armas[int(us_input3)-1]}\n")
            else: return print(f"\n{sospechoso}: No vi nada de eso\n")
    if number == '2':
        print("\t 1) Preguntar por esta persona \n\t 2) Preguntar por alguien mas")
        us_input: int = input('Tu: ')
        print("\nOpciones:")
        if us_input == '1':
            person = getPersonObject(sospechoso)        
            print(f"\n{sospechoso}: Yo estaba en {person[1]}\n")
            return
        if us_input == '2':
            for p in personajes:
                if p != sospechoso:
                    print(f'\t {i}) {p}')
                else: print(f'\t {i}) --------')
                i = i+1
            i=1
            us_input: int = input('Viste a: ')
            print("\nOpciones:")
            txt = "En el lugar"
            for l in lugares:
                print(f'\t {i}) {l}')
                i = i+1
            us_input3: int = input(f'{txt}: ')
            person = getPersonObject(personajes[int(us_input)-1])
            if lugares[int(us_input3)-1] == person[1]:
                print(f"\n{sospechoso}: Si, vi a {person[0]} {txt} {lugares[int(us_input3)-1]}\n")
            else: print(f"\n{sospechoso}: No, no vi nada de eso\n")
            return
    if number == '3':
        print("\t 1) Preguntar por esta persona \n\t 2) Preguntar por alguien mas")
        us_input: int = input('Tu: ')
        print("\nOpciones:")
        if us_input == '1':
            person = getPersonObject(sospechoso)        
            print(f"\n{sospechoso}: Yo tenia el objecto {person[2]}\n")
            return
        if us_input == '2':
            for p in personajes:
                if p != sospechoso:
                    print(f'\t {i}) {p}')
                else: print(f'\t {i}) --------')
                i = i+1
            i=1
            us_input: int = input('Viste a: ')
            print("\nOpciones:")
            txt = "Con el objecto"
            for l in armas:
                print(f'\t {i}) {l}')
                i = i+1
            us_input3: int = input(f'{txt}: ')
            person = getPersonObject(personajes[int(us_input)-1])
            if armas[int(us_input3)-1] == person[2]:
                print(f"\n{sospechoso}: Si, vi a {person[0]} {txt} {armas[int(us_input3)-1]}\n")
            else: print(f"\n{sospechoso}: No, no vi nada de eso\n")
            return

def main():
    pista,pista2 = createHistory()
    # print(f'fue {h1[0]} en {h1[1]} con {h1[2]}')
    print(f'\nEl anfitrion ha sido asesinado, descubre quien lo mato \n - Tienes dos preguntas para hacerle a cada sospechoso\n - Pista: {pista}\n - Pista: {pista2}\n')
    for i in personajes:
        print(f'\tHablando con: {i}\n')
        for j in range(1,3):
            print('Que quieres preguntar? \n 1) Persona \n 2) Lugar \n 3) Arma\n')
            us_input: int = input('Tu: ')
            
            getQuestion(us_input,i)

    print("\n\t|\tLlego el momento de nombrar al culpable\t|\n")
    print("Quien fue el asesino?\n")
    i = 1
    for p in personajes:
        print(f'\t {i}) {p}')
        i = i+1
    i=1
    us_input: int = input('Tu: ')
    print("En donde fue asesinado?\n")
    for l in lugares:
        print(f'\t {i}) {l}')
        i = i+1
    i=1
    us_input2: int = input('Tu: ')
    print("Con que fue asesinado?\n")
    for a in armas:
        print(f'\t {i}) {a}')
        i = i+1
    i=1
    us_input3: int = input('Tu: ')

    if personajes[int(us_input)-1] == h1[0] and lugares[int(us_input2)-1] == h1[1] and armas[int(us_input3)-1] == h1[2]:
        print("\n\n\t| \tLograste atrapar al culpable, bien hecho\t |\n\n")
    else: print(f"\n\n\t| \tParece que te has equivocado\t |\n\nLa respuesta correcta era: Fue\n{h1[0]} en {h1[1]} con {h1[2]}")
            
if __name__ == '__main__':
    main()