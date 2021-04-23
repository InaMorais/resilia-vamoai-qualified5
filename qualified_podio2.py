def podio_olimpico(tempo_de_chegada_1,tempo_de_chegada_2,tempo_de_chegada_3,corred1,corred2,corred3):
    cheg1 = tempo_de_chegada_1
    cheg2 = tempo_de_chegada_2
    cheg3 = tempo_de_chegada_3
    corred1 = corred1
    corred2 = corred2
    corred3 = corred3

    

    if cheg1 < cheg2 and cheg1 < cheg3:
        if cheg2 < cheg3:
            return f'1 - {corred1} - {cheg1} minutos\n' \
                f'2 - {corred2} - {cheg2} minutos\n' \
                f'3 - {corred3} - {cheg3} minutos\n'
        elif cheg3< cheg2:
            return f'1 - {corred1} - {cheg1} minutos\n' \
                f'2 - {corred3} - {cheg3} minutos\n' \
                f'3 - {corred2} - {cheg2} minutos\n'
    elif cheg2 < cheg1 and cheg2 < cheg3:
        if cheg1 < cheg3:
            return f'1 - {corred2} - {cheg2} minutos\n' \
            f'2 - {corred1} - {cheg1} minutos\n' \
            f'3 - {corred3} - {cheg3} minutos\n'
        elif cheg3< cheg1:
           return f'1 - {corred2} - {cheg2} minutos\n' \
            f'2 - {corred3} - {cheg3} minutos\n' \
            f'3 - {corred1} - {cheg1} minutos\n'
    elif cheg3 < cheg1 and cheg3 < cheg2:
        if cheg1 < cheg2:
          return  f'1 - {corred3} - {cheg3} minutos\n' \
            f'2 - {corred1} - {cheg1} minutos\n' \
            f'3 - {corred2} - {cheg2} minutos\n'
        elif cheg2< cheg1:
            return f'1 - {corred3} - {cheg3} minutos\n' \
            f'2 - {corred2} - {cheg2} minutos\n' \
            f'3 - {corred1} - {cheg1} minutos\n'