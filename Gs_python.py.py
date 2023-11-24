import cx_Oracle
import matplotlib.pyplot as plt
import json
import tkinter as tk
from tkinter import filedialog
import webbrowser
from datetime import datetime

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
def findyById_tb1(consultas,id_user):
    
    conn= getConnection()
    cursor = conn.cursor()
    sql_id = f"""
    SELECT * FROM tb_usuario WHERE id_usuario = {id_user}
"""

    try:
        cursor.execute(sql_id)
        print('\n------------------------------------------------\n')
        print("\nUsuario encontrado com sucesso!\n")
        result = cursor.fetchall()
        for row in result:
            consulta = {
                'Id Usuario': row[0],
                'Email': row[1],
                'Senha': row[2],
                'Id Paciente': row[3]
            }
            print(consulta)
            consultas.append(consulta)
        
    except Exception as e:
        print('\n------------------------------------------------\n')
        print(f'Usuario não encontrado: {e}')
    finally:
        cursor.close
        conn.close    

def findyById_tb2(consultas,res_id):
    
    conn= getConnection()
    cursor = conn.cursor()
    sql_id = f"""
    SELECT * FROM tb_paciente WHERE id_paciente = {res_id}
"""

    try:
        cursor.execute(sql_id)
        print('\n------------------------------------------------\n')
        print("\nPaciente encontrado com sucesso!\n")
        result = cursor.fetchall()
        for row in result:
            consulta = {
                'Id Paciente': row[0],
                'Nome Completo': row[1],
                'data_nascimento': row[2].strftime('%d/%m/%Y') if row[2] else None,
                'Relacao insulina': row[3],
                'Valor Maximo de Glicemia':[4],
                'Valor Minimo de Glicemia':[5]
            }
            print(consulta)
            consultas.append(consulta)
    except Exception as e:
        print('\n------------------------------------------------\n')
        print(f'Paciente não encontrado: {e}')
    finally:
        cursor.close
        conn.close    

def findyById_tb3(consultas,res_id):
    
    conn= getConnection()
    cursor = conn.cursor()
    sql_id = f"""
    SELECT * FROM tb_refeicao WHERE id_paciente = {res_id}
"""

    try:
        cursor.execute(sql_id)
        print('\n------------------------------------------------\n')
        print("\nRefeiçoes encontradas com sucesso!\n")
        result = cursor.fetchall()
        for row in result:
            consulta = {
                'Id refeicao': row[0],
                'Total de Carboidrato': row[1],
                'Total de Insulina': row[2],
                'Id Paciente': row[3]
            }
            print(consulta)
            consultas.append(consulta)
    except Exception as e:
        print('\n------------------------------------------------\n')
        print(f'Refeições não encontradas: {e}')
    finally:
        cursor.close
        conn.close    

def findyById_tb4(consultas,res_id):
    
    conn= getConnection()
    cursor = conn.cursor()
    sql_id = f"""
    SELECT * FROM tb_historico_glicemia WHERE id_paciente = {res_id}
"""

    try:
        cursor.execute(sql_id)
        print('\n------------------------------------------------\n')
        print("\nHistorico de Glicemia encontrado com sucesso!\n")
        result = cursor.fetchall()
        for row in result:
            consulta = {
                'Id Historico de glicemia': row[0],
                'Valor destro': row[1],
                'Id Paciente': row[2]
            }
            print(consulta)
            consultas.append(consulta)
    except Exception as e:
        print('\n------------------------------------------------\n')
        print(f'Historico de Glicemia não encontrado: {e}')
    finally:
        cursor.close
        conn.close    

def findyById_tb5(consultas):
    
    conn= getConnection()
    cursor = conn.cursor()
    id_escolhido = int(input('Digite o ID desejado: '))
    sql_id = f"""
    SELECT * FROM tb_alimento WHERE id_alimento = {id_escolhido}
"""

    try:
        cursor.execute(sql_id)
        print('\n------------------------------------------------\n')
        print("\nAlimento encontrado com sucesso!\n")
        result = cursor.fetchall()
        for row in result:
            consulta = {
                'Id Alimento': row[0],
                'Tipo Alimento': row[1],
                'Quantidade de carboidratos em Gramas': row[2]
            }
            print(consulta)
            consultas.append(consulta)
    except Exception as e:
        print('\n------------------------------------------------\n')
        print(f'Alimento não encontrado: {e}')
    finally:
        cursor.close
        conn.close    

""" -------------------------------------- """

'''2. Pesquisando tudo! '''
def getAll_tb1(consultas):

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
            consulta = {
                'Id Usuario': row[0],
                'Email': row[1],
                'Senha': '*' * len(row[2]),
                'Id Paciente': row[3]
            }
            print('\n------------------------------------------------\n')
            print(consulta)
            consultas.append(consulta)
            
    except Exception as e:
        print('\n------------------------------------------------\n')
        print(f'Erro ao trazer informações da tabela: {e}')
    finally:
        cursor.close()
        conn.close()

def getAll_tb2(consultas):
    
    conn= getConnection()
    cursor = conn.cursor()
    sql_getAll = """
    SELECT * FROM tb_paciente
        """

    try:
        cursor.execute(sql_getAll)
        result = cursor.fetchall()
        for row in result:
            consulta = {
                'Id Paciente': row[0],
                'Nome Completo': row[1],
                'data_nascimento': row[2].strftime('%d/%m/%Y') if row[2] else None,
                'Relacao insulina': row[3],
                'Valor Maximo de Glicemia':[4],
                'Valor Minimo de Glicemia':[5]
            }
            print('\n------------------------------------------------\n')
            print(consulta)
            consultas.append(consulta)
    except Exception as e:
        print('\n------------------------------------------------\n')
        print(f'Erro aao trazer informaçoes da tabela: {e}')
    finally:
        cursor.close
        conn.close 

def getAll_tb5(consultas):
    
    conn= getConnection()
    cursor = conn.cursor()
    sql_getAll = """
    SELECT * FROM tb_alimento
        """

    try:
        cursor.execute(sql_getAll)
        result = cursor.fetchall()
        for row in result:
            consulta = {
                'Id Alimento': row[0],
                'Tipo Alimento': row[1],
                'Quantidade de carboidratos em Gramas': row[2]
            }
            print('\n------------------------------------------------\n')
            print(consulta)
            consultas.append(consulta)
    except Exception as e:
        print('\n------------------------------------------------\n')
        print(f'Erro aao trazer informaçoes da tabela: {e}')
    finally:
        cursor.close
        conn.close 
""" -------------------------------------- """

'''3. Apagando por ID! '''
def deleteById_tb1(id_user):
    conn= getConnection()
    cursor = conn.cursor()
    
    sql_id = f"""
    DELETE FROM tb_usuario WHERE id_usuario = {id_user}
"""
    try:
        cursor.execute(sql_id)
        conn.commit()
        print('\n------------------------------------------------\n')
        print(f'Informações do ID {id_user} apagado com sucesso!')
    except Exception as e:
        print('\n------------------------------------------------\n')
        print(f'Erro ao deletar as informações do ID {id_user}: {e}')
    finally:
        cursor.close
        conn.close 

def deleteById_tb2(res_id):
    conn= getConnection()
    cursor = conn.cursor()
    sql_id = f"""
    DELETE FROM tb_paciente WHERE id_paciente = {res_id}"""
    
    try:
        cursor.execute(sql_id)
        conn.commit()
        print('\n------------------------------------------------\n')
        print(f'Informações do ID {res_id} apagado com sucesso!')
    except Exception as e:
        print('\n------------------------------------------------\n')
        print(f'Erro ao deletar as informações do ID {res_id}: {e}')
    finally:
        cursor.close
        conn.close 

def deleteById_tb3(res_id):
    conn= getConnection()
    cursor = conn.cursor()
    sql_id = f"""
    DELETE FROM tb_refeicao WHERE id_usuario = {res_id}
)"""
    try:
        cursor.execute(sql_id)
        conn.commit()
        print('\n------------------------------------------------\n')
        print(f'Informações do ID {res_id} apagado com sucesso!')
    except Exception as e:
        print('\n------------------------------------------------\n')
        print(f'Erro ao deletar as informações do ID {res_id}: {e}')
    finally:
        cursor.close
        conn.close 

def deleteById_tb4(res_id):
    conn= getConnection()
    cursor = conn.cursor()
    sql_id = f"""
    DELETE FROM tb_historico_glicemia WHERE id_usuario = {res_id}
"""
    try:
        cursor.execute(sql_id)
        conn.commit()
        print('\n------------------------------------------------\n')
        print(f'Informações do ID {res_id} apagado com sucesso!')
    except Exception as e:
        print('\n------------------------------------------------\n')
        print(f'Erro ao deletar as informações do ID {res_id}: {e}')
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
        conn.commit()
        print('\n------------------------------------------------\n')
        print(f'Informações do ID {id_escolhido} apagado com sucesso!')
    except Exception as e:
        print('\n------------------------------------------------\n')
        print(f'Erro ao deletar as informações do ID {id_escolhido}: {e}')
    finally:
        cursor.close
        conn.close 
""" -------------------------------------- """

def deleteAll_tb5():
    conn= getConnection()
    cursor = conn.cursor()
    sql_getAll = """
    DELETE FROM tb_alimento
        """

    try:
        cursor.execute(sql_getAll)
        conn.commit()
        print('\n------------------------------------------------\n')
        print('Alimentos Deletados')
    except Exception as e:
        print('\n------------------------------------------------\n')
        print(f'Erro ao deletar as informações da tabela: {e}')
    finally:
        cursor.close
        conn.close 
""" -------------------------------------- """

'''5. Update! '''
def update_tb1(id_user):
    conn= getConnection()
    cursor = conn.cursor()
    req = 0
    while req == 0:
        sql_id = f"""
        SELECT * FROM tb_usuario WHERE id_usuario = {id_user}
        """

        try:
            cursor.execute(sql_id)
            print('\n------------------------------------------------\n')
            print("\nID encontrado com sucesso!\n")
            result = cursor.fetchall()
            for row in result:
                print(row)

            print('''O que deseja alterar?
                
                [1] - Email.
                [2] - Senha.
                [3] - Sair.
                
                ''')
            
            op = int(input('Opção desejada: '))
            if op >= 1 or op <=2 :
                match op:
                    case 1:
                        email = input('email: ')

                        sql_update = """
                        UPDATE tb_usuario
                        SET email = :email
                        WHERE id_usuario = :id
                        """

                        try:
                            cursor.execute(sql_update, (email, id_user))
                            print("Informações Atualizadas com sucesso!")
                            conn.commit()
                        except Exception as e:
                            print('\n------------------------------------------------\n')
                            print(f'Erro ao atualizar as informações: {e}')
                    case 2:
                        senha = input('Senha Nova: ')

                        sql_update = """
                        UPDATE tb_usuario
                        SET senha = :senha
                        WHERE id_usuario = :id
                        """

                        try:
                            cursor.execute(sql_update, (senha, id_user))
                            print("Informações Atualizadas com sucesso!")
                            conn.commit()
                        except Exception as e:
                            print('\n------------------------------------------------\n')
                            print(f'Erro ao atualizar as informações: {e}')
                    case 3:
                        break
                req = 1
        except Exception as e:
            print('\n------------------------------------------------\n')
            print(f'ID escolhido não encontrado: {e}')
            req = 0

def update_tb2(res_id):
    conn= getConnection()
    cursor = conn.cursor()
    req = 0
    while req == 0:
        sql_id = f"""
        SELECT * FROM tb_paciente WHERE id_paciente = {res_id}
        """

        try:
            cursor.execute(sql_id)
            print('\n------------------------------------------------\n')
            print("\nID encontrado com sucesso!\n")
            result = cursor.fetchall()
            for row in result:
                print(row)

            res = 0
            while res == 0:
                print('''O que deseja alterar?
                    
                    [1] - Nome completo.
                    [2] - Data de nascimento.
                    [3] - RELACAO INSULINA CARBOIDRATO.
                    [4] - MAX_GLICEMIA
                    [5] - MIN_GLICEMIA
                    ''')
                
                op = int(input('Opção desejada: '))
                if op >= 1 or op <=5 :
                    match op:
                        case 1:
                            nome = input('Nome: ')

                            sql_update = """
                            UPDATE tb_paciente
                            SET NM_COMPLETO = :nome
                            WHERE id_paciente = :id
                            """

                            try:
                                cursor.execute(sql_update, (nome, res_id))
                                print('\n------------------------------------------------\n')
                                print("Informações Atualizadas com sucesso!")
                                conn.commit()
                            except Exception as e:
                                print('\n------------------------------------------------\n')
                                print(f'Erro ao atualizar as informações: {e}')
                        case 2:
                            dt = input('Data de Nascimento[dd/mm/aaaa]: ')

                            sql_update = """
                            UPDATE tb_paciente
                            SET DT_NASCIMENTO = TO_DATE(:dt, 'DD/MM/YYYY')
                            WHERE id_paciente = :id
                            """

                            try:
                                cursor.execute(sql_update, (dt, res_id))
                                print('\n------------------------------------------------\n')
                                print("Informações Atualizadas com sucesso!")
                                conn.commit()
                            except Exception as e:
                                print('\n------------------------------------------------\n')
                                print(f'Erro ao atualizar as informações: {e}')
                        case 3:
                            rep = 0
                            while rep == 0:
                                insulina_carbo = input('Insulina_carbo: ')
                                if not insulina_carbo.isdigit():
                                    print('Digite um valor válido! ')
                                else:
                                    sql_update = """
                                    UPDATE tb_paciente
                                    SET RELACAO_INSULINA_CARBOIDRATO = :insulina_carbo
                                    WHERE id_paciente = :id
                                    """
                                    try:
                                        cursor.execute(sql_update, (insulina_carbo, res_id))
                                        print('\n------------------------------------------------\n')
                                        print("Informações Atualizadas com sucesso!")
                                        conn.commit()
                                        rep = 1
                                    except Exception as e:
                                        print('\n------------------------------------------------\n')
                                        print(f'Erro ao atualizar as informações: {e}')
                        case 4:
                            rep = 0
                            while rep == 0:
                                glicemia_max = input('Max Glicemia: ')
                                if not glicemia_max.isdigit():
                                    print('Digite um valor válido! ')
                                else:
                                    sql_update = """
                                    UPDATE tb_paciente
                                    SET MAX_GLICEMIA = :glicemia_max
                                    WHERE id_paciente = :id
                                    """
                                    try:
                                        cursor.execute(sql_update, (glicemia_max, res_id))
                                        print('\n------------------------------------------------\n')
                                        print("Informações Atualizadas com sucesso!")
                                        conn.commit()
                                        rep = 1
                                    except Exception as e:
                                        print('\n------------------------------------------------\n')
                                        print(f'Erro ao atualizar as informações: {e}')

                        case 5:
                            rep = 0
                            while rep == 0:
                                glicemia_min = input('Min Glicemia: ')
                                if not glicemia_min.isdigit():
                                    print('Digite um valor válido! ')
                                else:
                                    sql_update = """
                                    UPDATE tb_paciente
                                    SET MIN_GLICEMIA = :glicemia_min
                                    WHERE id_paciente = :id
                                    """
                                    try:
                                        cursor.execute(sql_update, (glicemia_min, res_id))
                                        print('\n------------------------------------------------\n')
                                        print("Informações Atualizadas com sucesso!")
                                        conn.commit()
                                        rep = 1
                                    except Exception as e:
                                        print('\n------------------------------------------------\n')
                                        print(f'Erro ao atualizar as informações: {e}')
                    res = 1
                
                elif not int:
                    print('digite um valor valido! ')
                    res = 0
                else:
                    print('Opção invalida!')
                    res = 0

            req = 1
        except Exception as e:
            print('\n------------------------------------------------\n')
            print(f'ID escolhido não encontrado: {e}')
            req = 0

""" -------------------------------------- """

'''6. informações passadas pelo usuario! '''
def informacao_paciente():
    infoPaciente = []
    print('\n------------------------------------------------\n')
    nm_completo = input('Nome completo: ')
    infoPaciente.append(nm_completo)

    dt_nascimento = input('Data de nascimento dd/mm/aaaa: ')
    infoPaciente.append(dt_nascimento)

    relacao_insulina_carboidrato = float(input('relacao insulina carboidrato: '))
    infoPaciente.append(relacao_insulina_carboidrato)

    max_glicemia = int(input('maximo de glicemia: '))
    infoPaciente.append(max_glicemia)

    min_glicemia = int(input('minimo de glicemia: '))
    infoPaciente.append(min_glicemia)

    return infoPaciente

def informacao_refeicao(res_id):
    conn= getConnection()
    cursor = conn.cursor()
    sql_id = f"""
    SELECT * FROM tb_paciente WHERE id_paciente = {res_id}
"""

    try:
        cursor.execute(sql_id)
        print('\n------------------------------------------------\n')
        print("\nPaciente encontrado com sucesso!\n")
        result = cursor.fetchall()
        print(result[0][3])
        consulta = result[0][3]

        i = 1
        resultado = 0
        resultado_carb = 0
        while i == 1:
            print('''Selecione o alimento que deseja incluir na refeição:
                [1] - Arroz branco.
                [2] - feijão carioca.
                [3] - macarrão
                [4] - frango
                [5] - Carne Bovina
                [6] - Carne de porco
                [7] - Peixe
                [8] - Ovo
                [9] - Batata
                [10] - Batata Doce''')


            escolha = int(input('Alimento: '))

            match escolha:
                case 1:
                    print("Quantas carboidrato de Arroz ")
                    carb = float(input('quantidade: '))
                    mut = carb * 0.26
                    print(mut)
                    div = mut / consulta
                case 2:
                    print("Quantas carboidrato de Feijão carioca ")
                    carb = float(input('quantidade: '))
                    mut = carb * 0.13
                    div = mut / consulta
                case 3:
                    print("Quantas carboidrato de Macarrão ")
                    carb = float(input('quantidade: '))
                    mut = carb * 0.77
                    div = mut / consulta
                case 4:
                    print("Quantas carboidrato de Frango ")
                    carb = float(input('quantidade: '))
                    mut = carb * 0.2
                    div = mut / consulta
                case 5:
                    print("Quantas carboidrato de Carne Bovina ")
                    carb = float(input('quantidade: '))
                    mut = carb * 0.3
                    div = mut / consulta
                case 6:
                    print("Quantas carboidrato de Carne de Porco ")
                    carb = float(input('quantidade: '))
                    mut = carb * 0.4
                    div = mut / consulta
                case 7:
                    print("Quantas carboidrato de Peixe ")
                    carb = float(input('quantidade: '))
                    mut = carb * 0.28
                    div = mut / consulta
                case 8:
                    print("Quantas carboidrato de Ovo ")
                    carb = float(input('quantidade: '))
                    mut = carb * 0.2
                    div = mut / consulta
                case 9:
                    print("Quantas carboidrato de Batata ")
                    carb = float(input('quantidade: '))
                    mut = carb * 0.2
                    div = mut / consulta
                case 10:
                    print("Quantas carboidrato de Batata Doce ")
                    carb = float(input('quantidade: '))
                    mut = carb * 0.18
                    div = mut / consulta
            resultado_carb += mut
            resultado += div

            print('''Deseja Add mais Alimento?
                [1] - sim
                [2] - Não
                ''')
            i = int(input('Opção desejada: '))



        infoRefeicao = []

        qt_total_carbo = resultado_carb
        infoRefeicao.append(qt_total_carbo)

        qt_total_insulina = resultado
        infoRefeicao.append(qt_total_insulina)

    except Exception as e:
        print('\n------------------------------------------------\n')
        print(f'Paciente não encontrado: {e}')

    


    return infoRefeicao

def informacao_alimento():
    alimento = []
    print('\n------------------------------------------------\n')
    tipo_alimento = input('tipo de alimento ex[Arroz branco]: ')
    alimento.append(tipo_alimento)

    qt_carbo_grama = float(input('Quantidade de carboidrato em gramas: '))
    alimento.append(qt_carbo_grama)

    return alimento
""" -------------------------------------- """

'''6. Insert! '''
def insert_login(cad_email_usuario,cad_senha_usuario,lgi):
    conn = getConnection()
    cursor = conn.cursor()
    
    sql_query = "INSERT INTO tb_usuario (id_usuario , email, senha, id_paciente) VALUES (:0, :1, :2, :3)"

    try:
        cursor.execute("SELECT seq_usuario.NEXTVAL FROM dual")
        nextval_result = cursor.fetchone()
        
        if nextval_result:
            usuario_id = nextval_result[0]

            
            cursor.execute(sql_query, (usuario_id, cad_email_usuario, cad_senha_usuario, lgi))
            conn.commit()
            print("Registro de usuario inserido com sucesso. ID do usuario:", usuario_id)

        else:
            print("Erro ao obter o próximo valor da sequência")

    except Exception as e:
        print(f'Erro ao inserir o registro de usuario: {e}')
    finally:
        cursor.close()
        conn.close()

def insert_paciente(infoPaciente):
    conn = getConnection()
    cursor = conn.cursor()
    
    sql_query = "INSERT INTO tb_paciente (id_paciente , nm_completo, dt_nascimento, relacao_insulina_carboidrato, max_glicemia, min_glicemia) VALUES (:0,:1, TO_DATE(:2, 'dd/mm/yyyy'), :3, :4, :5)"

    try:

        cursor.execute("SELECT seq_paciente.NEXTVAL FROM dual")
        nextval_result = cursor.fetchone()
        
        if nextval_result:
            paciente_id = nextval_result[0]

            
            cursor.execute(sql_query, (paciente_id,infoPaciente[0], infoPaciente[1], infoPaciente[2], infoPaciente[3], infoPaciente[4]))
            conn.commit()
            print("Registro de paciente inserido com sucesso. ID do Paciente:", paciente_id)

            cursor.execute("SELECT seq_paciente.currval FROM dual")
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

def insert_refeicao(infoRefeicao, res_id):
    conn = getConnection()
    cursor = conn.cursor()

    sql_query = "INSERT INTO tb_refeicao (id_refeicao, qt_total_carbo, qt_total_insulina, id_paciente ) VALUES (:0, :1, :2, :3)"

    try:
        
        cursor.execute("SELECT seq_refeicao.NEXTVAL FROM dual")
        nextval_result = cursor.fetchone()
        
        if nextval_result:
            refeicao_id = nextval_result[0]

            cursor.execute(sql_query, (refeicao_id, infoRefeicao[0], infoRefeicao[1], res_id))
            conn.commit()
            print("Registro de refeição efetuado com sucesso. ID da reifeição:", refeicao_id)
        else:
            print("Erro ao obter o próximo valor da sequência")
    except Exception as e:
        print(f'Erro ao cadastrar refeição: {e}')
    finally:
        cursor.close()
        conn.close()

def insert_historico_glicemia(medicoes, res_id):
    n = 0
    i = 0
    tamanho_lista = len(medicoes)
    print(tamanho_lista)
    print(medicoes)
    while n <= tamanho_lista:
        n+=1
        conn = getConnection()
        cursor = conn.cursor()
        

        sql_query = "INSERT INTO tb_historico_glicemia (ID_HISTORICO_GLICEMIA, VL_DESTRO, ID_PACIENTE ) VALUES ( :0, :1, :2)"

        try:
            cursor.execute("SELECT seq_historico_glicemia.NEXTVAL FROM dual")
            nextval_result = cursor.fetchone()
            
            if nextval_result:
                glicemia_id = nextval_result[0]
                print (glicemia_id)

                if isinstance(medicoes[i], (int, float)):
                    cursor.execute(sql_query, (glicemia_id, medicoes[i], res_id))
                else:
                    print(f"Valor inválido em medicoes[{i}]: {medicoes[i]}")
                conn.commit()
                print("Registro de historico de glicemia efetuado com sucesso. ID do historico de glicemia:", glicemia_id)
                i+=1
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
""" -------------------------------------- """

#login

def realizar_login():
    res = 1
    while res == 1:
        conn= getConnection()
        cursor = conn.cursor()

        email_usuario = input("Digite seu email: ")
        senha_usuario = input("Digite sua senha: ")

        sql_get = """
        SELECT id_paciente, id_usuario FROM TB_USUARIO
        WHERE email = :1
        AND senha = :2
        """

        try:
            # Consultar se há um usuário com o email e senha fornecidos
            cursor.execute(sql_get, (email_usuario, senha_usuario))
            resultado = cursor.fetchone()
            print(resultado)
            id_user = resultado[1]
            res_id = resultado[0]
            
            print("Login bem-sucedido!\n")
            menu(res_id,id_user)
            break

                
                
        except Exception as e:
            print(f'Erro ao realizar login: {e}')
            print("Email ou senha incorretos. Login falhou.")
            res = 1
            
        finally:
            cursor.close()
            conn.close()

def cadastro_login(lgi):
    cad_email_usuario = input("Digite seu email: ")
    rep_senha = 0
    while rep_senha == 0:
        cad_senha_usuario = input("Digite uma senha: ")
        senha_novamente = input("Digite a senha novamente: ")

        if cad_senha_usuario != senha_novamente:
            print('As senhas não são iguais! digite novamente')
            rep_senha = 0
        else:
            insert_login(cad_email_usuario,cad_senha_usuario,lgi)
            rep_senha = 1
""" -------------------------------------- """


# Menus
def menu_login():
    op = 0
    while op == 0:
        print("""

        Digite:

        1 - Efetuar login.
        2 - Cadastre-se.

        """)
        try:
            escolha = int(input('Digite a opção desejada: '))

            if escolha < 1 or escolha > 2:
                print('Opção invalida, digite novamente!')
                op = 0
            elif escolha == 1:
                realizar_login()
                break

            elif escolha == 2:
                cad = informacao_paciente()
                pg_id = insert_paciente(cad)
                cadastro_login(pg_id)
                print('\nAgora com o cadastro feito faça o login!')
                op = 0
            
        except ValueError:
            print('Opção inválida. Por favor, digite um número.')
            op = 0

def menu(res_id,id_user):
    consultas = infoJson()
    rep =1
    while rep == 1:
        print("""

    Selecione a opção desejada para ver as opções validas!

    1 - Pefil.
    2 - Paciente.
    3 - Refeição
    4 - Historico de Glicemia
    5 - SAIR

    """)
        op = 0
        while op == 0:
            try:
                escolha = int(input('Digite a opção desejada: '))

                if escolha < 1 or escolha > 5:
                    print('Opção invalida, digite novamente!')
                    op = 0
                elif escolha == 1:
                    tb1(consultas,res_id,id_user)
                    break

                elif escolha == 2:
                    tb2(consultas,res_id)
                    break

                elif escolha == 3:
                    tb3(res_id,consultas)
                    break

                elif escolha == 4:
                    tb4(res_id,consultas)
                    break
                elif escolha == 5:
                    print('''\n\n\nDeseja gerar os Arquivos Json de suas consuta ?
                    [1] - sim
                    [2] - Não''')
                    res = int(input('Opção escolhida'))

                    if res == 1:
                        try:
                            baixar_json(consultas)
                        except ValueError:
                            print('Você não possui o historico de Glicemia para gerar o Json.')
                    

                    """ print('''\n\n\nDeseja gerar grafico do seu historico de glicemia ?
                    [1] - sim
                    [2] - Não''')
                    resp = int(input('Opção escolhida'))

                    if resp == 1:
                        try:
                            mostrar_grafico_e_porcentagens(historico_glicemia)
                        except ValueError:
                            print('Você não possui o historico de Glicemia para gerar o Json.')
                    print('\nFinalizando sistema') """
                    rep = 0
                    break
                
            except ValueError:
                print('Opção inválida. Por favor, digite um número.')
                op = 0
            
def tb1(consultas,res_id,id_user):
    op = 0
    while op == 0:
        print("""
    Qual operação deseja fazer?

    [1] - Informações de Usuario.
    [2] - Pesquisar Usuarios.
    [3] - Atualizar informações de Usuario.
    [4] - Deletar Usuario.
    [5] - Voltar
    """)
        
        try:
            escolha = int(input('Digite a opção desejada: '))

            if escolha < 1 or escolha > 5:
                print('Opção invalida, digite novamente!')
                op = 0
            

            elif escolha == 1:
                findyById_tb1(consultas,id_user)
                
            elif escolha == 2:
                getAll_tb1(consultas)

            elif escolha == 3:
                update_tb1(id_user)

            elif escolha == 4:
                deleteById_tb1(res_id,id_user)

            elif escolha == 5:
                break
            
            print('''
            Deseja fazer mais alguma operação em Usuario?

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
                        print('finalizando')
                        op = 1
                        break
                    elif opcao != 1 or opcao != 2:
                        print('Opção inválida.')
                        res = 0
            
            except ValueError:
                print('Opção inválida. Por favor, digite um número.')

        except ValueError:
            print('Opção inválida. Por favor, digite um número.')
            op = 0

def tb2(consultas,res_id):
    op = 0
    while op == 0:
        print("""
        Qual operação deseja fazer?

        [1] - Informações do Paciente.
        [2] - Consutar Pacientes.
        [3] - Atualizar informações de Paciente.
        [4] - Voltar
        
        """)
    
        try:
            escolha = int(input('Digite a opção desejada: '))

            if escolha < 1 or escolha > 4:
                print('Opção invalida, digite novamente!')
                op = 0

            elif escolha == 1:
                findyById_tb2(consultas,res_id)
                
            elif escolha == 2:
                getAll_tb2(consultas)

            elif escolha == 3:
                update_tb2(res_id)

            elif escolha == 4:
                break

            print('''
            Deseja fazer mais alguma coisa em Paciente?

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
                        print('finalizando')
                        op = 1
                        break
                    elif opcao != 1 or opcao != 2:
                        print('Opção inválida.')
                        res = 0
            
            except ValueError:
                print('Opção inválida. Por favor, digite um número.')


        except ValueError:
            print('Opção inválida. Por favor, digite um número.')
            op = 0

def tb3(res_id,consultas):
    op = 0
    while op == 0:
        print("""
        Qual operação deseja fazer?

        1 - Inserir Refeição.
        2 - Cunsutar Refeições.
        3 - Deletar Refeiçao por Id.
        4 - Voltar.
        """)
        try:
            escolha = int(input('Digite a opção desejada: '))

            if escolha < 1 or escolha > 4:
                print('Opção invalida, digite novamente!')
                op = 0
            
            elif escolha == 1:
                infoRefeicao= informacao_refeicao(res_id)
                insert_refeicao(infoRefeicao, res_id)

            elif escolha == 2:
                findyById_tb3(consultas, res_id)

            elif escolha == 3:
                deleteById_tb3()

            elif escolha == 4:
                break
            opcao = 1
            while opcao == 1:
                print('''
                Deseja fazer mais alguma em refeição?

                1 - sim
                2 - não
                
                ''')
                try: 
                    res = 0
                    while res == 0:
                        opcao = int(input('Digite a opção desejada: '))

                        if opcao == 1:
                            res = 1
                            opcao = 0
                            op = 0
                        elif opcao == 2:
                            print('finalizando')
                            op = 1
                            break
                        elif opcao != 1 or opcao != 2:
                            print('Opção inválida.')
                            res = 0
                
                except ValueError:
                    print('Opção inválida. Por favor, digite um número.')


        except ValueError:
            print('Opção inválida. Por favor, digite um número.')
            op = 0

def tb4(res_id,consultas):
    op = 0
    while op == 0:
        print("""
    Qual operação deseja fazer?

    1 - Inserir Historico de Glicemia.
    2 - Cunsutar Historico de Glicemia.
    3 - Deletar Historico de Glicemia por Id.
    4 - Voltar
    """)
    
        try:
            escolha = int(input('Digite a opção desejada: '))

            if escolha < 1 or escolha > 4:
                print('Opção invalida, digite novamente!')
                op = 0
            
            elif escolha == 1:
                medicoes = cadastrar_medicoes()

                # Mostrar o gráfico e as porcentagens
                mostrar_grafico_e_porcentagens(medicoes)
                
                insert_historico_glicemia(medicoes, res_id)

            elif escolha == 2:
                findyById_tb4(consultas,res_id)
            
            elif escolha == 3:
                deleteById_tb4()

            elif escolha == 4:
                break

            print('''
            Deseja fazer mais alguma operação em Historico de Glicemia?

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
                        print('finalizando')
                        op = 1
                        break
                    elif opcao != 1 or opcao != 2:
                        print('Opção inválida.')
                        res = 0
            
            except ValueError:
                print('Opção inválida. Por favor, digite um número.')

        except ValueError:
            print('Opção inválida. Por favor, digite um número.')
            op = 0

def tb5(consultas):
    op = 0
    while op == 0:
        print("""
    Qual operação deseja fazer?

    1 - Inserir Alimento.
    2 - Cunsutar Alimento Por Id.
    3 - Consutar todos os Alimentos.
    4 - Atualizar Alimentos.
    5 - Deletar Alimento por Id.
    6 - Deletar todos os Alimentos.
    """)
        
        try:
            escolha = int(input('Digite a opção desejada: '))

            if escolha < 1 or escolha > 5:
                print('Opção invalida, digite novamente!')
                op = 0
            
            elif escolha == 1:
                alimento = informacao_alimento()
                insert_alimento(alimento)

            elif escolha == 2:
                findyById_tb5(consultas)
                
            elif escolha == 3:
                getAll_tb5(consultas)

            elif escolha == 4:
                deleteById_tb5()

            elif escolha == 5:
                deleteAll_tb5()

            print('''
            Deseja fazer mais alguma operação em Alimento?

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
                        print('finalizando')
                        op = 1
                        break
                    elif opcao != 1 or opcao != 2:
                        print('Opção inválida.')
                        res = 0
            
            except ValueError:
                print('Opção inválida. Por favor, digite um número.')

        except ValueError:
            print('Opção inválida. Por favor, digite um número.')
            op = 0
""" -------------------------------------- """

def serialize(obj):
    if isinstance(obj, datetime):
        return obj.__str__()

def salvar_em_json(consultas):
    # Cria um arquivo temporário para salvar as consultas
    with open('temp_consultas.json', 'w') as arquivo_json:
        json.dump(consultas, arquivo_json, indent=2, default=serialize)
    print("Resultados temporários salvos em 'temp_consultas.json'.")

# Função para baixar o arquivo JSON, permitindo que o usuário escolha o diretório
def baixar_json(consultas):
    # Consulta dados no banco de dados

    # Salva os resultados temporários em um arquivo JSON
    salvar_em_json(consultas)

    # Pede ao usuário para escolher o diretório de destino
    root = tk.Tk()
    root.withdraw()  # Esconde a janela principal
    caminho_destino = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("Arquivos JSON", "*.json")])

    # Verifica se o usuário cancelou a seleção
    if not caminho_destino:
        print("Operação cancelada.")
        return

    # Move o arquivo temporário para o caminho escolhido pelo usuário
    import shutil
    shutil.move('temp_consultas.json', caminho_destino)

    # Abre o navegador padrão do sistema para o usuário visualizar ou baixar o arquivo
    webbrowser.open('file://' + caminho_destino)

def cadastrar_medicoes():
    medicoes = []
    while True:
        try:
            valor = float(input("Digite a medição do dia (ou digite qualquer letra para parar): "))
            medicoes.append(valor)
        except ValueError:
            break
    return medicoes
"""
"""
def mostrar_grafico_e_porcentagens(medicoes):
    limite_minimo = 70
    limite_maximo = 150

    dentro_do_alvo = sum(limite_minimo < m <= limite_maximo for m in medicoes)
    fora_do_alvo = sum(m <= limite_minimo or m > limite_maximo for m in medicoes)
    total_medicoes = len(medicoes)

    porcentagem_dentro = (dentro_do_alvo / total_medicoes) * 100
    porcentagem_fora = (fora_do_alvo / total_medicoes) * 100

    plt.figure(figsize=(8, 6))
    plt.plot(medicoes, marker='o', linestyle='-')
    plt.axhline(y=limite_minimo, color='r', linestyle='--', label='Limite Mínimo')
    plt.axhline(y=limite_maximo, color='g', linestyle='--', label='Limite Máximo')
    plt.xlabel('Dias')
    plt.ylabel('Medições')
    plt.title('Medições de Glicose ao Longo do Tempo')
    plt.legend()
    plt.grid(True)
    plt.show()

    print(f"Porcentagem de medições dentro do alvo: {porcentagem_dentro:.2f}%")
    print(f"Porcentagem de medições fora do alvo: {porcentagem_fora:.2f}%")

# Solicitar as medições



def infoJson():
    consultas = []
    return consultas
""" bem = print('bem vindo')
teste = print('ola') """
""" login() """
menu_login()
