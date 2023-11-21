import cx_Oracle
cx_Oracle.init_oracle_client(lib_dir=r"C:\instantclient_21_12")
""" """ 
def getConnection():
    try:
        connection = cx_Oracle.connect("RM98819", "260104", "oracle.fiap.com.br/ORCL")
        """  connection = cx_Oracle.connect(user="RM98819", password="260104", host="oracle.fiap.com.br", port="1521", service="ORCL") """
        print("\nconexão: ", connection.version)
        return connection
    except Exception as e:
        print(f'Erro ao obter conexão: {e}')

'''1. Pesquisando por ID '''
def findyById_tb1():
    
    conn= getConnection()
    cursor = conn.cursor()
    id_escolhido = int(input('Digite o ID desejado: '))
    sql_id = f"""
    SELECT * FROM tb_usuario WHERE id_usuario = {id_escolhido}
"""

    try:
        cursor.execute(sql_id)
        print("ID encontrado com sucesso!")
        result = cursor.fetchall()
        for row in result:
            print(row)
        
    except Exception as e:
        print(f'ID escolhido não encontrado: {e}')
    finally:
        cursor.close
        conn.close    

def findyById_tb2():
    
    conn= getConnection()
    cursor = conn.cursor()
    id_escolhido = int(input('Digite o ID desejado: '))
    sql_id = f"""
    SELECT * FROM tb_paciente WHERE id_paciente = {id_escolhido}
"""

    try:
        cursor.execute(sql_id)
        print("ID encontrado com sucesso!")
        result = cursor.fetchall()
        for row in result:
            print(row)
    except Exception as e:
        print(f'ID escolhido não encontrado: {e}')
    finally:
        cursor.close
        conn.close    

def findyById_tb3():
    
    conn= getConnection()
    cursor = conn.cursor()
    id_escolhido = int(input('Digite o ID desejado: '))
    sql_id = f"""
    SELECT * FROM tb_refeicao WHERE id_refeicao = {id_escolhido}
"""

    try:
        cursor.execute(sql_id)
        print("ID encontrado com sucesso!")
        result = cursor.fetchall()
        for row in result:
            print(row)
    except Exception as e:
        print(f'ID escolhido não encontrado: {e}')
    finally:
        cursor.close
        conn.close    

def findyById_tb4():
    
    conn= getConnection()
    cursor = conn.cursor()
    id_escolhido = int(input('Digite o ID desejado: '))
    sql_id = f"""
    SELECT * FROM tb_historico_glicemia WHERE id_historico_glicemia = {id_escolhido}
"""

    try:
        cursor.execute(sql_id)
        print("ID encontrado com sucesso!")
        result = cursor.fetchall()
        for row in result:
            print(row)
    except Exception as e:
        print(f'ID escolhido não encontrado: {e}')
    finally:
        cursor.close
        conn.close    

def findyById_tb5():
    
    conn= getConnection()
    cursor = conn.cursor()
    id_escolhido = int(input('Digite o ID desejado: '))
    sql_id = f"""
    SELECT * FROM tb_alimento WHERE id_alimento = {id_escolhido}
"""

    try:
        cursor.execute(sql_id)
        print("ID encontrado com sucesso!")
        result = cursor.fetchall()
        for row in result:
            print(row)
    except Exception as e:
        print(f'ID escolhido não encontrado: {e}')
    finally:
        cursor.close
        conn.close    


'''2. Pesquisando tudo! '''
def getAll_tb1():

    conn= getConnection()
    cursor = conn.cursor()

    sql_getAll = """
    SELECT * FROM tb_usuario
    """

    try:
        cursor.execute(sql_getAll)
        result = cursor.fetchall()
        
        # Imprime os resultados
        for row in result:
            print(row)
            
    except Exception as e:
        print(f'Erro ao trazer informações da tabela: {e}')
    finally:
        cursor.close()
        conn.close()

def getAll_tb2():
    
    conn= getConnection()
    cursor = conn.cursor()
    sql_getAll = """
    SELECT * FROM tb_paciente
        """

    try:
        cursor.execute(sql_getAll)
        result = cursor.fetchall()
        for row in result:
            print(row)
    except Exception as e:
        print(f'Erro aao trazer informaçoes da tabela: {e}')
    finally:
        cursor.close
        conn.close 

def getAll_tb3():
    
    conn= getConnection()
    cursor = conn.cursor()
    sql_getAll = """
    SELECT * FROM tb_refeicao
        """

    try:
        cursor.execute(sql_getAll)
        result = cursor.fetchall()
        for row in result:
            print(row)
    except Exception as e:
        print(f'Erro aao trazer informaçoes da tabela: {e}')
    finally:
        cursor.close
        conn.close 

def getAll_tb4():
    
    conn= getConnection()
    cursor = conn.cursor()
    sql_getAll = """
    SELECT * FROM tb_historico_glicemia
        """

    try:
        cursor.execute(sql_getAll)
        result = cursor.fetchall()
        for row in result:
            print(row)
    except Exception as e:
        print(f'Erro aao trazer informaçoes da tabela: {e}')
    finally:
        cursor.close
        conn.close 

def getAll_tb5():
    
    conn= getConnection()
    cursor = conn.cursor()
    sql_getAll = """
    SELECT * FROM tb_alimento
        """

    try:
        cursor.execute(sql_getAll)
        result = cursor.fetchall()
        for row in result:
            print(row)
    except Exception as e:
        print(f'Erro aao trazer informaçoes da tabela: {e}')
    finally:
        cursor.close
        conn.close 


'''3. Apagando por ID! '''
def deleteById_tb1():
    conn= getConnection()
    cursor = conn.cursor()
    id_escolhido = int(input('Digite o ID desejado: '))
    sql_id = f"""
    DELETE FROM tb_usuario WHERE id_usuario = {id_escolhido}
"""
    try:
        cursor.execute(sql_id)
        print(f'Informações do ID {id_escolhido} apagado com sucesso!')
    except Exception as e:
        print(f'Erro ao deletar as informações do ID {id_escolhido}: {e}')
    finally:
        cursor.close
        conn.close 

def deleteById_tb2():
    conn= getConnection()
    cursor = conn.cursor()
    id_escolhido = int(input('Digite o ID desejado: '))
    sql_id = f"""
    DELETE FROM tb_paciente WHERE id_paciente = {id_escolhido}
"""
    try:
        cursor.execute(sql_id)
        print(f'Informações do ID {id_escolhido} apagado com sucesso!')
    except Exception as e:
        print(f'Erro ao deletar as informações do ID {id_escolhido}: {e}')
    finally:
        cursor.close
        conn.close 

def deleteById_tb3():
    conn= getConnection()
    cursor = conn.cursor()
    id_escolhido = int(input('Digite o ID desejado: '))
    sql_id = f"""
    DELETE FROM tb_refeicao WHERE id_refeicao = {id_escolhido}
)"""
    try:
        cursor.execute(sql_id)
        print(f'Informações do ID {id_escolhido} apagado com sucesso!')
    except Exception as e:
        print(f'Erro ao deletar as informações do ID {id_escolhido}: {e}')
    finally:
        cursor.close
        conn.close 

def deleteById_tb4():
    conn= getConnection()
    cursor = conn.cursor()
    id_escolhido = int(input('Digite o ID desejado: '))
    sql_id = f"""
    DELETE FROM tb_historico_glicemia WHERE id_historico_glicemia = {id_escolhido}
"""
    try:
        cursor.execute(sql_id)
        print(f'Informações do ID {id_escolhido} apagado com sucesso!')
    except Exception as e:
        print(f'Erro ao deletar as informações do ID {id_escolhido}: {e}')
    finally:
        cursor.close
        conn.close 

def deleteById_tb5():
    conn= getConnection()
    cursor = conn.cursor()
    id_escolhido = int(input('Digite o ID desejado: '))
    sql_id = f"""
    DELETE FROM tb_alimento WHERE id_alimento = {id_escolhido}
"""
    try:
        cursor.execute(sql_id)
        print(f'Informações do ID {id_escolhido} apagado com sucesso!')
    except Exception as e:
        print(f'Erro ao deletar as informações do ID {id_escolhido}: {e}')
    finally:
        cursor.close
        conn.close 


'''4. Apagando tudo! '''
def deleteAll_tb1():
    conn= getConnection()
    cursor = conn.cursor()
    sql_getAll = """
    DELETE FROM tb_usuario
        """

    try:
        cursor.execute(sql_getAll)
        print(sql_getAll)
    except Exception as e:
        print(f'Erro ao deletar as informações da tabela: {e}')
    finally:
        cursor.close
        conn.close 

def deleteAll_tb2():
    conn= getConnection()
    cursor = conn.cursor()
    sql_getAll = """
    DELETE FROM tb_paciente
        """

    try:
        cursor.execute(sql_getAll)
        print(sql_getAll)
    except Exception as e:
        print(f'Erro ao deletar as informações da tabela: {e}')
    finally:
        cursor.close
        conn.close 

def deleteAll_tb3():
    conn= getConnection()
    cursor = conn.cursor()
    sql_getAll = """
    DELETE FROM tb_refeicao
        """

    try:
        cursor.execute(sql_getAll)
        print(sql_getAll)
    except Exception as e:
        print(f'Erro ao deletar as informações da tabela: {e}')
    finally:
        cursor.close
        conn.close 

def deleteAll_tb4():
    conn= getConnection()
    cursor = conn.cursor()
    sql_getAll = """
    DELETE FROM tb_historico_glicemia
        """

    try:
        cursor.execute(sql_getAll)
        print(sql_getAll)
    except Exception as e:
        print(f'Erro ao deletar as informações da tabela: {e}')
    finally:
        cursor.close
        conn.close 

def deleteAll_tb5():
    conn= getConnection()
    cursor = conn.cursor()
    sql_getAll = """
    DELETE FROM tb_alimento
        """

    try:
        cursor.execute(sql_getAll)
        print(sql_getAll)
    except Exception as e:
        print(f'Erro ao deletar as informações da tabela: {e}')
    finally:
        cursor.close
        conn.close 


'''5. Update! '''
def update_tb1():
    conn= getConnection()
    cursor = conn.cursor()
    id_escolhido = int(input('Digite o ID desejado: '))

    updateInfo = []
    nome = input('nome: ')
    updateInfo.append(nome)

    sql_update = f"""
    UPDATE tb_usuario
    SET nome = {updateInfo[0]}, email = 'novo@email.com'
    WHERE id_usuario = {id_escolhido}
"""

    try:
        cursor.execute(sql_update)
        print(sql_update)
        print("Informações Atualizadas com sucesso!")
    except Exception as e:
        print(f'erro ao atualizar as informações: {e}')
    finally:
        cursor.close
        conn.close 

def update_tb2():
    conn= getConnection()
    cursor = conn.cursor()
    id_escolhido = int(input('Digite o ID desejado: '))

    updateInfo = []
    nome = input('nome: ')
    updateInfo.append(nome)

    sql_update = f"""
    UPDATE tb_paciente
    SET nome = {updateInfo[0]}, email = 'novo@email.com'
    WHERE id_paciente = {id_escolhido}
"""

    try:
        cursor.execute(sql_update)
        print(sql_update)
        print("Informações Atualizadas com sucesso!")
    except Exception as e:
        print(f'erro ao atualizar as informações: {e}')
    finally:
        cursor.close
        conn.close 

def update_tb3():
    conn= getConnection()
    cursor = conn.cursor()
    id_escolhido = int(input('Digite o ID desejado: '))

    updateInfo = []
    nome = input('nome: ')
    updateInfo.append(nome)

    sql_update = f"""
    UPDATE tb_refeicao
    SET nome = {updateInfo[0]}, email = 'novo@email.com'
    WHERE id_refeicao = {id_escolhido}
"""

    try:
        cursor.execute(sql_update)
        print(sql_update)
        print("Informações Atualizadas com sucesso!")
    except Exception as e:
        print(f'erro ao atualizar as informações: {e}')
    finally:
        cursor.close
        conn.close 

def update_tb4():
    conn= getConnection()
    cursor = conn.cursor()
    id_escolhido = int(input('Digite o ID desejado: '))

    updateInfo = []
    nome = input('nome: ')
    updateInfo.append(nome)

    sql_update = f"""
    UPDATE tb_historico_glicemia
    SET nome = {updateInfo[0]}, email = 'novo@email.com'
    WHERE id_historico_glicemia = {id_escolhido}
"""

    try:
        cursor.execute(sql_update)
        print(sql_update)
        print("Informações Atualizadas com sucesso!")
    except Exception as e:
        print(f'erro ao atualizar as informações: {e}')
    finally:
        cursor.close
        conn.close 

def update_tb5():
    conn= getConnection()
    cursor = conn.cursor()
    id_escolhido = int(input('Digite o ID desejado: '))

    updateInfo = []
    nome = input('nome: ')
    updateInfo.append(nome)

    sql_update = f"""
    UPDATE tb_alimento
    SET nome = {updateInfo[0]}, email = 'novo@email.com'
    WHERE id_alimento = {id_escolhido}
"""

    try:
        cursor.execute(sql_update)
        print(sql_update)
        print("Informações Atualizadas com sucesso!")
    except Exception as e:
        print(f'erro ao atualizar as informações: {e}')
    finally:
        cursor.close
        conn.close 


'''6. informações passadas pelo usuario! '''
def informacao_paciente():
    infoPaciente = []

    nm_completo = input('Nome completo: ')
    infoPaciente.append(nm_completo)

    dt_nascimento = input('Data de nascimento dd/mm/aaaa: ')
    infoPaciente.append(dt_nascimento)

    relacao_insulina_carboidrato = input('')
    infoPaciente.append(relacao_insulina_carboidrato)

    max_glicemia = input('maximo de glicemia')
    infoPaciente.append(max_glicemia)

    min_glicemia = input('minimo de glicemia')
    infoPaciente.append(min_glicemia)

    return infoPaciente

def informacao_refeicao():
    infoRefeicao = []

    qt_total_carbo = input('Quantidade total de carboidrato: ')
    infoRefeicao.append(qt_total_carbo)

    qt_total_insulina = input('Quantidade total de insulina: ')
    infoRefeicao.append(qt_total_insulina)

    return infoRefeicao

def informacao_historico_glicemia():
    historico_glicemia = []

    vl_destro = input('Nome completo: ')
    historico_glicemia.append(vl_destro)


    return historico_glicemia

def informacao_alimento():
    alimento = []

    tipo_alimento = input('tipo de alimento ex[Arroz branco]: ')
    alimento.append(tipo_alimento)

    qt_carbo_grama = input('Quantidade de carboidrato em gramas: ')
    alimento.append(qt_carbo_grama)

    return alimento


'''6. Insert! '''
def insert_login(cad_email_usuario,cad_senha_usuario):
    conn = getConnection()
    cursor = conn.cursor()
    
    sql_query = "INSERT INTO tb_usuario (id_usuario , email, senha) VALUES (:0, :1, :2)"

    try:
        cursor.execute("SELECT seq_usuario.NEXTVAL FROM dual")
        nextval_result = cursor.fetchone()
        
        if nextval_result:
            usuario_id = nextval_result[0]

            
            cursor.execute(sql_query, (usuario_id, cad_email_usuario, cad_senha_usuario))
            conn.commit()
            print("Registro de usuario inserido com sucesso. ID do usuario:", usuario_id)

        else:
            print("Erro ao obter o próximo valor da sequência")

    except Exception as e:
        print(f'Erro ao inserir o registro de usuario: {e}')
    finally:
        cursor.close()
        conn.close()

def insert_paciente(infoPaciente,resultado):
    conn = getConnection()
    cursor = conn.cursor()
    
    sql_query = "INSERT INTO tb_pessoa_fisica (id_paciente , nm_completo, dt_nascimento, relacao_insulina_carboidrato, max_glicemia, min_glicemia, id_usuario) VALUES (:0,:1, TO_DATE(:2, 'dd/mm/yyyy'), :3, :4, :5, :6)"

    try:

        cursor.execute("SELECT seq_paciente.NEXTVAL FROM dual")
        nextval_result = cursor.fetchone()
        
        if nextval_result:
            paciente_id = nextval_result[0]

            
            cursor.execute(sql_query, (paciente_id,infoPaciente[0], infoPaciente[1], infoPaciente[2], infoPaciente[3], infoPaciente[4], resultado[0]))
            conn.commit()
            print("Registro de paciente inserido com sucesso. ID do cliente:", paciente_id)

            cursor.execute("SELECT seq_Pessoa.currval FROM dual")
            result = cursor.fetchone()
            if result:
                lgi = result[0]
                return lgi
            else:
                    print(f"Erro ao obter o último valor gerado pela sequência: {e}")
        else:
            print("Erro ao obter o próximo valor da sequência")

    except Exception as e:
        print(f'Erro ao inserir o registro de cliente: {e}')
    finally:
        cursor.close()
        conn.close()

def insert_refeicao(infoRefeicao, lgi):
    conn = getConnection()
    cursor = conn.cursor()

    sql_query = "INSERT INTO tb_refeicao (id_refeicao, qt_total_carbo, qt_total_insulina, id_paciente ) VALUES (:0, :1, :2, :3)"

    try:
        
        cursor.execute("SELECT seq_refeicao.NEXTVAL FROM dual")
        nextval_result = cursor.fetchone()
        
        if nextval_result:
            refeicao_id = nextval_result[0]

            cursor.execute(sql_query, (refeicao_id, infoRefeicao[0], infoRefeicao[1], lgi))
            conn.commit()
            print("Registro de refeição efetuado com sucesso. ID da reifeição:", refeicao_id)
        else:
            print("Erro ao obter o próximo valor da sequência")
    except Exception as e:
        print(f'Erro ao cadastrar refeição: {e}')
    finally:
        cursor.close()
        conn.close()

def insert_historico_glicemia(historico_glicemia, lgi):
    conn = getConnection()
    cursor = conn.cursor()

    sql_query = "INSERT INTO tb_historico_glicemia (id_historico_glicemia, vl_destro, id_paciente ) VALUES (:0, :1, :2)"

    try:
        
        cursor.execute("SELECT seq_historico_glicemia.NEXTVAL FROM dual")
        nextval_result = cursor.fetchone()
        
        if nextval_result:
            glicemia_id = nextval_result[0]

            cursor.execute(sql_query, (glicemia_id, historico_glicemia[0], historico_glicemia[1], lgi))
            conn.commit()
            print("Registro de historico de glicemia efetuado com sucesso. ID do historico de glicemia:", glicemia_id)
        else:
            print("Erro ao obter o próximo valor da sequência")
    except Exception as e:
        print(f'Erro ao cadastrar historico de glicemia: {e}')
    finally:
        cursor.close()
        conn.close()

def insert_alimento(alimento):
    conn = getConnection()
    cursor = conn.cursor()

    sql_query = "INSERT INTO tb_alimento (id_alimento, tipo_alimento, qt_carbo_grama ) VALUES (:0, :1, :2)"

    try:
        
        cursor.execute("SELECT seq_alimento.NEXTVAL FROM dual")
        nextval_result = cursor.fetchone()
        
        if nextval_result:
            alimento_id = nextval_result[0]

            cursor.execute(sql_query, (alimento_id, alimento[0], alimento[1]))
            conn.commit()
            print("Registro de alimento efetuado com sucesso. ID da alimento:", alimento_id)
        else:
            print("Erro ao obter o próximo valor da sequência")
    except Exception as e:
        print(f'Erro ao cadastrar alimento: {e}')
    finally:
        cursor.close()
        conn.close()


#login

def login():
    

    if realizar_login(email_usuario, senha_usuario):
        print("Login bem-sucedido!\n")
        menu()
    else:
        print("Email ou senha incorretos. Login falhou.")

def realizar_login():
    

    conn= getConnection()
    cursor = conn.cursor()

    email_usuario = input("Digite seu email: ")
    senha_usuario = input("Digite sua senha: ")

    sql_get = f"""
    SELECT * FROM tb_usuario
    """

    try:
        # Consultar se há um usuário com o email e senha fornecidos
        cursor.execute(sql_get)
        resultado = cursor.fetchone()

        if resultado is not None:
            print("Login bem-sucedido!\n")
            menu()
            return True, resultado[0]  
        else:
            print(resultado)
            return False  # Login falhou
            
    except Exception as e:
        print(f'Erro ao realizar login: {e}')
    finally:
        cursor.close()
        conn.close()

def cadastro_login():
    cad_email_usuario = input("Digite seu email: ")
    rep_senha = 0
    while rep_senha == 0:
        cad_senha_usuario = input("Digite uma senha: ")
        senha_novamente = input("Digite a senha novamente: ")

        if cad_senha_usuario != senha_novamente:
            print('As senhas não são iguais! digite novamente')
            rep_senha = 0
        else:
            insert_login(cad_email_usuario,cad_senha_usuario)



# Menus
def menu():
    print("""

Qual operação deseja fazer?

1 - TB1
2 - TB2
3 - TB3
4 - TB4
5 - TB5

""")
    op = 0
    while op == 0:
        try:
            escolha = int(input('Digite a opção desejada: '))

            if escolha < 1 or escolha > 5:
                print('Opção invalida, digite novamente!')
                op = 0
            elif escolha == 1:
                tb1()

            elif escolha == 2:
                tb2()

            elif escolha == 3:
                tb3()

            elif escolha == 4:
                tb4()

            elif escolha == 5:
                tb5()
            
        except ValueError:
            print('Opção inválida. Por favor, digite um número.')
            op = 0

def tb1():
    op = 0
    while op == 0:
        print("""
    Qual operação deseja fazer?

    1 - Consutar Por Id.
    2 - Consutar tabela inteira.
    3 - Fazer Update de informação
    4 - Deletar por Id.
    5 - Deletar todas as informaçoes da tabela.
    """)
        
        try:
            escolha = int(input('Digite a opção desejada: '))

            if escolha < 1 or escolha > 5:
                print('Opção invalida, digite novamente!')
                op = 0
            

            elif escolha == 1:
                findyById_tb1()
                
            elif escolha == 2:
                getAll_tb1()

            elif escolha == 3:
                update_tb1()

            elif escolha == 4:
                deleteById_tb1()

            elif escolha == 5:
                deleteAll_tb1()
            
            print('''
    Deseja fazer mais alguma operação nessa tebela?

    1 - sim
    2 - não
            
            ''')
            try: 
                res = 0
                while res == 0:
                    opcao = int(input('Digite a opção desejada: '))

                    if opcao == 1:
                        res = 1
                        op = 0
                    
                    elif opcao == 2:
                        print('''
    Deseja fazer alguma operação em tebela?

    1 - sim
    2 - não
                        
                        ''')
                        try: 
                            resposta = 0
                            while resposta == 0:
                                opc = int(input('Digite a opção desejada: '))

                                if opc == 1:
                                    menu()
                                    resposta == 1
                                    res = 1
                                    op = 1
                                    
                                elif opc == 2:
                                    break

                                elif opc != 1 or opc != 2:
                                    print('Opção invalida, digite novamente!')

                        except ValueError:
                            print('Opção inválida. Por favor, digite um número.')

            except ValueError:
                print('Opção inválida. Por favor, digite um número.')


        except ValueError:
            print('Opção inválida. Por favor, digite um número.')
            op = 0

def tb2():
    op = 0
    while op == 0:
        print("""
        Qual operação deseja fazer?

        1 - Inserir dados na tabela.
        2 - Cunsutar Por Id.
        3 - Consutar tabela inteira.
        4 - Fazer Update de informação
        5 - Deletar por Id.
        6 - Deletar todas as informaçoes da tabela.
        """)
    
        try:
            escolha = int(input('Digite a opção desejada: '))

            if escolha < 1 or escolha > 6:
                print('Opção invalida, digite novamente!')
                op = 0
            
            elif escolha == 1:
                informacao_paciente()

            elif escolha == 2:
                findyById_tb2()
                
            elif escolha == 3:
                getAll_tb2()

            elif escolha == 4:
                update_tb2()

            elif escolha == 5:
                deleteById_tb2()

            elif escolha == 6:
                deleteAll_tb2()

            print('''Deseja fazer mais alguma operação nessa tebela?

            1 - sim
            2 - não
            
            ''')
            try: 
                res = 0
                while res == 0:
                    opcao = int(input('Digite a opção desejada: '))

                    if opcao == 1:
                        op = 0
                    
                    elif opcao == 2:
                        print('''Deseja fazer alguma operação em tebela?

                        1 - sim
                        2 - não
                        
                        ''')
                        try: 
                            resposta = 0
                            while resposta == 0:
                                opc = int(input('Digite a opção desejada: '))

                                if opc == 1:
                                    menu()
                                    
                                elif opc == 2:
                                    break

                                elif opc != 1 or opc != 2:
                                    print('Opção invalida, digite novamente!')

                        except ValueError:
                            print('Opção inválida. Por favor, digite um número.')

            except ValueError:
                print('Opção inválida. Por favor, digite um número.')


        except ValueError:
            print('Opção inválida. Por favor, digite um número.')
            op = 0

def tb3():
    op = 0
    while op == 0:
        print("""
        Qual operação deseja fazer?

        1 - Inserir dados na tabela.
        2 - Cunsutar Por Id.
        3 - Consutar tabela inteira.
        4 - Fazer Update de informação
        5 - Deletar por Id.
        6 - Deletar todas as informaçoes da tabela.
        """)
        try:
            escolha = int(input('Digite a opção desejada: '))

            if escolha < 1 or escolha > 6:
                print('Opção invalida, digite novamente!')
                op = 0
            
            elif escolha == 1:
                informacao_refeicao()

            elif escolha == 2:
                findyById_tb3()
                
            elif escolha == 3:
                getAll_tb3()

            elif escolha == 4:
                update_tb3()

            elif escolha == 5:
                deleteById_tb3()

            elif escolha == 6:
                deleteAll_tb3()
            print('''Deseja fazer mais alguma operação nessa tebela?

            1 - sim
            2 - não
            
            ''')
            try: 
                res = 0
                while res == 0:
                    opcao = int(input('Digite a opção desejada: '))

                    if opcao == 1:
                        op = 0
                    
                    elif opcao == 2:
                        print('''Deseja fazer alguma operação em tebela?

                        1 - sim
                        2 - não
                        
                        ''')
                        try: 
                            resposta = 0
                            while resposta == 0:
                                opc = int(input('Digite a opção desejada: '))

                                if opc == 1:
                                    menu()
                                    
                                elif opc == 2:
                                    break

                                elif opc != 1 or opc != 2:
                                    print('Opção invalida, digite novamente!')

                        except ValueError:
                            print('Opção inválida. Por favor, digite um número.')

            except ValueError:
                print('Opção inválida. Por favor, digite um número.')


        except ValueError:
            print('Opção inválida. Por favor, digite um número.')
            op = 0

def tb4():
    op = 0
    while op == 0:
        print("""
    Qual operação deseja fazer?

    1 - Inserir dados na tabela.
    2 - Cunsutar Por Id.
    3 - Consutar tabela inteira.
    4 - Fazer Update de informação
    5 - Deletar por Id.
    6 - Deletar todas as informaçoes da tabela.
    """)
    
        try:
            escolha = int(input('Digite a opção desejada: '))

            if escolha < 1 or escolha > 6:
                print('Opção invalida, digite novamente!')
                op = 0
            
            elif escolha == 1:
                informacao_historico_glicemia()

            elif escolha == 2:
                findyById_tb4()
                
            elif escolha == 3:
                getAll_tb4()

            elif escolha == 4:
                update_tb4()

            elif escolha == 5:
                deleteById_tb4()

            elif escolha == 6:
                deleteAll_tb4()

            print('''Deseja fazer mais alguma operação nessa tebela?

            1 - sim
            2 - não
            
            ''')
            try: 
                res = 0
                while res == 0:
                    opcao = int(input('Digite a opção desejada: '))

                    if opcao == 1:
                        op = 0
                    
                    elif opcao == 2:
                        print('''Deseja fazer alguma operação em tebela?

                        1 - sim
                        2 - não
                        
                        ''')
                        try: 
                            resposta = 0
                            while resposta == 0:
                                opc = int(input('Digite a opção desejada: '))

                                if opc == 1:
                                    menu()
                                    
                                elif opc == 2:
                                    break

                                elif opc != 1 or opc != 2:
                                    print('Opção invalida, digite novamente!')

                        except ValueError:
                            print('Opção inválida. Por favor, digite um número.')

            except ValueError:
                print('Opção inválida. Por favor, digite um número.')


        except ValueError:
            print('Opção inválida. Por favor, digite um número.')
            op = 0

def tb5():
    op = 0
    while op == 0:
        print("""
    Qual operação deseja fazer?

    1 - Inserir dados na tabela.
    2 - Cunsutar Por Id.
    3 - Consutar tabela inteira.
    4 - Fazer Update de informação
    5 - Deletar por Id.
    6 - Deletar todas as informaçoes da tabela.
    """)
        
        try:
            escolha = int(input('Digite a opção desejada: '))

            if escolha < 1 or escolha > 6:
                print('Opção invalida, digite novamente!')
                op = 0
            
            elif escolha == 1:
                informacao_alimento()

            elif escolha == 2:
                findyById_tb5()
                
            elif escolha == 3:
                getAll_tb5()

            elif escolha == 4:
                update_tb5()

            elif escolha == 5:
                deleteById_tb5()

            elif escolha == 6:
                deleteAll_tb5()

            print('''Deseja fazer mais alguma operação nessa tebela?

            1 - sim
            2 - não
            
            ''')
            try: 
                res = 0
                while res == 0:
                    opcao = int(input('Digite a opção desejada: '))

                    if opcao == 1:
                        op = 0
                    
                    elif opcao == 2:
                        print('''Deseja fazer alguma operação em tebela?

                        1 - sim
                        2 - não
                        
                        ''')
                        try: 
                            resposta = 0
                            while resposta == 0:
                                opc = int(input('Digite a opção desejada: '))

                                if opc == 1:
                                    menu()
                                    
                                elif opc == 2:
                                    break

                                elif opc != 1 or opc != 2:
                                    print('Opção invalida, digite novamente!')

                        except ValueError:
                            print('Opção inválida. Por favor, digite um número.')

            except ValueError:
                print('Opção inválida. Por favor, digite um número.')


        except ValueError:
            print('Opção inválida. Por favor, digite um número.')
            op = 0

def menu_login():
    op = 0
    while op == 0:
        print("""

        Qual operação deseja fazer?

        1 - Efetuar login.
        2 - Cadastre-se.

        """)
        try:
            escolha = int(input('Digite a opção desejada: '))

            if escolha < 1 or escolha > 2:
                print('Opção invalida, digite novamente!')
                op = 0
            elif escolha == 1:
                login()

            elif escolha == 2:
                cadastro_login()
                print('\nAgora com o cadastro feito faça o login!')
                op = 0
            
        except ValueError:
            print('Opção inválida. Por favor, digite um número.')
            op = 0


realizar_login()
