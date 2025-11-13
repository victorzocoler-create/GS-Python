#limpa o texto para melhor experiencia do usuario
def limpar_texto(texto):
    texto = texto.lower()
    
    
    texto = texto.replace("á", "a")
    texto = texto.replace("à", "a")
    texto = texto.replace("â", "a")
    texto = texto.replace("ã", "a")
    texto = texto.replace("é", "e")
    texto = texto.replace("ê", "e")
    texto = texto.replace("í", "i")
    texto = texto.replace("ó", "o")
    texto = texto.replace("ô", "o")
    texto = texto.replace("õ", "o")
    texto = texto.replace("ú", "u")
    texto = texto.replace("ü", "u")
    texto = texto.replace("ç", "c")
    
    
    for p in "!@#$%¨&*()_-+=´`^~[]{};:.,<>?/|\\\"'":
        texto = texto.replace(p, "")
    
    
    texto = texto.strip()
    
    return texto


# descreve os empregos do futuro
def descricao_emprego(nome):
    if nome == 1:
        print("\n-O Cientista de Dados é o profissional responsável por coletar, organizar e analisar grandes volumes de informações para ajudar empresas a tomar decisões inteligentes. Ele usa linguagens como Python, R e SQL, além de ferramentas como Power BI e Tableau, para criar modelos de previsão e identificar padrões que orientam estratégias de negócio.\n-Normalmente, forma-se em Ciência de Dados, Estatística, Engenharia da Computação ou áreas semelhantes, com cursos que duram em média 4 anos, embora existam formações mais curtas, como especializações e bootcamps de 6 meses a 2 anos.\n-É uma das carreiras mais promissoras do futuro, com forte demanda no mercado global e salários que podem ultrapassar R$ 25.000 para profissionais experientes.")
    
    elif nome == 2:
        print("\n-O Engenheiro de Software projeta, desenvolve e mantém sistemas e aplicativos. Ele transforma ideias em programas, define tecnologias e garante segurança e eficiência.\n-Geralmente faz graduação de 4 a 5 anos em Engenharia de Software ou áreas de TI. Usa linguagens como Python, Java e JavaScript, além de trabalhar com bancos de dados, nuvem e controle de versões.\n-É uma carreira altamente valorizada e com grande demanda, com salários que podem ultrapassar R$ 25.000 para profissionais experientes.")

    elif nome == 3:
        print("\n-O Especialista em Cibersegurança protege sistemas, redes e dados contra ataques e invasões digitais. Ele identifica vulnerabilidades, cria barreiras de proteção e responde a incidentes de segurança.\n-A formação costuma ser em Segurança da Informação, Ciência da Computação ou Engenharia de Software, com duração média de 4 anos.Esse profissional domina redes, criptografia, firewalls, testes de invasão e normas de segurança.\n-É uma das carreiras mais promissoras do futuro, com alta demanda global e salários que podem chegar a R$ 30.000 em cargos sêniores.")
    
    elif nome == 4:
        print("\n-O Arquiteto de Nuvem é o profissional responsável por planejar, criar e gerenciar estruturas de computação em nuvem, como AWS, Azure e Google Cloud. Ele garante que os sistemas sejam escaláveis, seguros e econômicos.\n-A formação costuma ser em Engenharia de Software, Ciência da Computação ou Sistemas de Informação, com duração média de 4 a 5 anos.\n-Domina tecnologias de servidores virtuais, containers, segurança em nuvem e automação. É uma das profissões mais valorizadas do setor de tecnologia, com salários que podem ultrapassar R$ 28.000 para especialistas experientes.")
    

def ajuda():
    lista = []
    empregosF = ["Cientista de Dados","Engenheiro de Software","Especialista em Cibersegurança","Arquiteto de Nuvem","Engenheiro de Automação","Engenheiro Ambiental","Profissional de Telemedicina","Engenheiro Biomédico","Gestor de Inovação e Startups","Analista de Dados de Mercado"]
    
    while True:
                
                print()
                for i in range(0,10):
                    print(f"{i+1}.{empregosF[i]}")
            
            
                resposta = int(input("\nSe algum desses lhe interessar digite seu numero para informações, se não digite '0':"))
                
                
                
                if resposta in range(1,10):
                    
                    descricao_emprego(resposta)

                    salvar = input("\nVocê quer ver outro e salvar esse em uma lista? (sim/não):")
                    salvar = limpar_texto(salvar)
                    if salvar == "sim":
                        lista.append(empregosF[resposta-1])
                        print("Salvo com sucesso!")
                    else:
                        print("Ok, muito obrigado!")
                        print(f"Sua lista de empregos que você se interessou ficou assim {lista}. Espero ter te ajudado com esse problema atual que afeta alguns empregos. Até mais!!")
                        break

                                
                elif resposta == 0:
                    print("Ok, muito obrigado!")
                    print(f"Sua lista de empregos que você se interessou ficou assim {lista}. Espero ter te ajudado com esse problema atual que afeta alguns empregos. Até mais!!")
                    break
                    
                else:
                    print("Emprego não encontrado...")



# analisa o indice de atumatização do emprego
def principal(emprego):
    empregosA = ["Assistente administrativo","Secretário","Secretária","Digitador","Digitadora","Operador de call center","Recepcionista","Agente de telemarketing","Operador de linha de montagem","Inspetor de qualidade","Embalador industrial","Trabalhador fabril","Caixa de banco", "Assistente de contabilidade","Analista de crédito básico","Atendente de loja","Operador de caixa","Repositor de prateleira","Motorista de caminhão","Motoboy","Entregador","Operador de empilhadeira","Faxineiro industrial","Zelador","Trabalhador de manutenção básica","Operador de SAC","Agente de suporte técnico básico","Vendedor por telefone"]

    empregosM = ["Técnico em informática","Técnico em administração","Técnico em contabilidade","Técnico em logística","Técnico em recursos humanos","Técnico em enfermagem","Técnico em segurança do trabalho","Auxiliar de laboratório","Auxiliar de produção","Auxiliar de almoxarifado","Assistente de vendas","Assistente de marketing","Auxiliar de escritório","Operador de máquinas","Operador de CNC","Motorista profissional","Eletricista industrial","Mecânico de manutenção","Soldador","Técnico em eletrônica","Técnico em mecatrônica","Técnico em edificações","Técnico em telecomunicações","Agente de viagens","Corretor de imóveis","Supervisor de equipe","Despachante","Agente de segurança patrimonial","Técnico em redes de computadores","Técnico em química"]

    


    emprego = limpar_texto(emprego)
    empregosA = [limpar_texto(i) for i in empregosA]
    empregosM = [limpar_texto(i) for i in empregosM]
    
    
    
    
    if emprego in empregosA:
        print("\nchance de automatizão ALTA!")
        print("-Mas não se preocupe, aqui estão os principais 10 empregos bons para o futuro.")
        ajuda()
        
        
    elif emprego in empregosM:
        print("\nChance de automatizão MEDIA")
        print("você está no meio, então é bom tomar cuidado, aqui estão os principais 10 empregos bons para o futuro. ")
        ajuda()
    
    else:
        print("\nChance de automatizão BAIXA")                   
                                            

        


   
                    



        



job = input("digite seu emprego:")
principal(job)