
import historia

estado_jogo = {
    "capitulo_atual": 1,
    "ambientes_visitados": [],
    "decisao_final": None
}

# 1. Abertura
historia.abrir_capitulo(estado_jogo)

# 2. Apresentação do DOC01
historia.apresentar_doc01()

# 3. Conversa com Karla
historia.apresentar_conversa_karla()

escolha = input("\nEscolha 1 ou 2: ")

resultado = historia.apresentar_reacao_karla(escolha)

print("Classificação da escolha:", resultado)

# 4. Conversa opcional com ORÁCULO
historia.apresentar_conversa_oraculo()

# 5. Apresentação do DOC02
historia.apresentar_doc02()

# 6. Simular visita aos dois ambientes
estado_jogo["ambientes_visitados"] = [
    "Laboratório",
    "Sala de Segurança"
]

# 7. Encerramento
resultado = historia.encerrar_capitulo(estado_jogo)

print("\nCapítulo encerrado?", resultado)

# 8. Verificar possibilidade de avanço
print("Pode avançar?",
      historia.pode_avancar_capitulo(estado_jogo))
