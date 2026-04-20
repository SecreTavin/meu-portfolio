"""
SUMMARY:
Estudante de Ciência da Computação, apaixonado por desenvolvimento backend e automação. 
Com experiência em Python, SQL e frameworks como Django e FastAPI, estou sempre buscando novos desafios para aplicar minhas habilidades e aprender mais. 
Disponível para oportunidades que me permitam crescer e contribuir com soluções inovadoras.
"""
from PIL import Image
from typing import List, Dict
import json

try:

    foto = Image.open("/Users/octavioarruda232/Desktop/ -3.jpg") 
    foto.show()
except Exception:
    print("FileNotFoundError: Foto de perfil não encontrada.")

class INFORMACAO:
    NOME = "Octávio Augusto Arruda dos Prazeres"
    AGE = "21"
    TITULO = "Computer Science Student | Backend Developer | Mathematician Enthusiast"
    EMAIL = "arrudaoctavio178@gmail.com"
    CONTATO = "+55 (31) 9 9578-8205"
    LOCALIZACAO = {
        "cidade": "Nova Lima",
        "estado": "Minas Gerais",
        "pais": "Brasil"
    }
    STATUS = "Em busca de estágio ou oportunidades de desenvolvimento backend, para aplicar meus conhecimentos e crescer profissionalmente."

class REDES_SOCIAIS:

    LINKEDIN = "https://www.linkedin.com/in/octavio-prazeres/"
    GITHUB = "https://github.com/SecreTavin"

class SKILLS:
    LINGUAGENS = ["Python", "SQL", "JavaScript", "Swift"]
    FRAMEWORKS = ["Django", "FastAPI", "Flask", "Matlab"]
    FERRAMENTAS = ["Docker", "Kubernetes", "AWS", "Git", "Linux", "SAP", "PowerBI", "DBeaver"]
    TECNOLOGIAS = ["REST APIs", "Microservices", "PostgreSQL"]
    IDIOMAS = ["Português (Nativo)", "Inglês (Avançado)"]

class EDUCACAO:
    def graduacao(self):
        curso = "Ciência da Computação"
        instituicao = "Centro Universitário UNA"
        periodo = ("2025", "2029")
        return curso, instituicao, periodo
    
    def ensino_medio(self):
        escola = "Escola Estadual Augusto de Lima"
        periodo = ("2022")
        return escola, periodo
    
    def Aprendizagem_mecânica(self):
        curso = "Aprendizagem em manutenção industrial mecânica"
        instituicao = "SENAI"
        periodo = ("2022", "2023")
        return curso, instituicao, periodo
    
    def robotica(self):
        curso = "Iniciação profissional a Robótica"
        instituicao = "SENAI"
        periodo = ("2024")
        return curso, instituicao, periodo
    
    def python(self):
        curso = "Python"
        instituicao = "Santander open academy"
        periodo = ("2025")
        return curso, instituicao, periodo
    
    def AI(self):
        curso = "Artificial Intelligence Fundamentals"
        instituicao = "IBM"
        periodo = ("2025")
        return curso, instituicao, periodo
    
    def english(self):
        curso = "English(EUA)"
        instituicao = "KNN Idiomas Brasil"
        periodo = ("2025 até o momento")
        return curso, instituicao, periodo
    
class EXPERIENCIA:

    def aprendizagem(self):
        cargo = "Mecânico de manutenção industrial - Aprendiz"
        empresa = "RHIMagnesita"
        periodo = ("2022", "2023")
        responsabilidades = [
            "Manutenção preventiva e corretiva de equipamentos industriais",
            "Leitura e interpretação de desenhos técnicos",
            "Colaboração com equipes multidisciplinares para garantir a eficiência operacional"
        ]
        return cargo, empresa, periodo, responsabilidades
    
    def efetivo(self):
        cargo = "Mecânico de manutenção industrial - mecânico I"
        empresa = "RHIMagnesita"
        periodo = ("2024 até o momento")
        responsabilidades = [
            "Manutenção preventiva e corretiva de equipamentos industriais",
            "Leitura e interpretação de desenhos técnicos",
            "Colaboração com equipes multidisciplinares para garantir a eficiência operacional"
        ]
        return cargo, empresa, periodo, responsabilidades

class PROJETOS:

    def sistema_monitoramento(self):
        nome = "Sistema de monitoramento de filtros de manga"
        stack = ["Python", "JavaScript", "MYSQL", "HTML", "CSS"]
        desc = "Sistema de cadastro e monitoramento de filtros de manga."
        link = "https://github.com/SecreTavin/Sistema-de-monitoramento-de-filtros-de-manga-industriais"
        return nome, stack, desc, link
    
    def system_pulse(self):
        nome = "System Pulse"
        stack = ["Swift"]
        desc = "utilitário nativo para macOS que monitora o uso da CPU em tempo real diretamente da barra de menus."
        link = "https://github.com/SecreTavin/System-Pulse"
        return nome, stack, desc, link
    
    def machine_learning(self):
        nome = "Pipeline de MachineLearning para prever gravidade de acidentes de trânsito. "
        stack = ["Python", "Scikit-learn", "Pandas", "Matplotlib", "Numpy", "Seaborn", "MySQL", "statsmodels", "scipy",
                 "randomizedsearchcv"]
        desc = "Projeto de machine learning para prever gravidade de acidentes de trânsito, utilizando um pipeline completo de pré-processamento," \
        " modelagem e avaliação de desempenho."
        link = "https://github.com/SecreTavin/analise-preditiva-acidentes-transito-V2"
        return nome, stack, desc, link
    

class API:
    def hire_me(self) -> Dict:
        return {
            "status": 200,
            "message": "Candidato pronto para o deploy! ⚡",
            "response_time": "Fast"
        }

def secret_talent():
    raise Exception("HiddenTalentError: This candidate has a secret talent that cannot be revealed! 🤫")

def display_resume():
    
    def header(title):
        print(f"\n{'='*10} {title} {'='*10}")

    # --- CABEÇALHO ---
    print(f"\n>>> INICIALIZANDO SISTEMA DE PERFIL: {INFORMACAO.NOME}")
    print(f"STATUS: {INFORMACAO.STATUS}")
    
    header("INFORMAÇÕES PESSOAIS")
    print(f"Título:  {INFORMACAO.TITULO}")
    print(f"Email:   {INFORMACAO.EMAIL}")
    print(f"Contato: {INFORMACAO.CONTATO}")
    print(f"Local:   {INFORMACAO.LOCALIZACAO['cidade']}, {INFORMACAO.LOCALIZACAO['estado']} - {INFORMACAO.LOCALIZACAO['pais']}")

    header("REDES SOCIAIS")
    print(f"GitHub:   {REDES_SOCIAIS.GITHUB}")
    print(f"LinkedIn: {REDES_SOCIAIS.LINKEDIN}")

    header("STACK & SKILLS")
    print(f"Linguagens:   {', '.join(SKILLS.LINGUAGENS)}")
    print(f"Frameworks:   {', '.join(SKILLS.FRAMEWORKS)}")
    print(f"Ferramentas:  {', '.join(SKILLS.FERRAMENTAS)}")
    print(f"Tecnologias:  {', '.join(SKILLS.TECNOLOGIAS)}")
    print(f"Idiomas:      {', '.join(SKILLS.IDIOMAS)}")

    header("EDUCAÇÃO")
    edu = EDUCACAO()
    formacoes = [edu.graduacao(), edu.python(), edu.AI(), edu.english(), edu.robotica(), edu.Aprendizagem_mecânica()]
    for item in formacoes:

        nome = item[0]
        inst = item[1]
        periodo = item[2] if len(item) > 2 else ""
        print(f"• {nome} | {inst} ({periodo})")

    header("EXPERIÊNCIA PROFISSIONAL")
    exp = EXPERIENCIA()
    experiencias = [exp.efetivo(), exp.aprendizagem()]
    for cargo, empresa, periodo, resps in experiencias:
        print(f"[{periodo}] {cargo} @ {empresa}")
        for r in resps:
            print(f"  - {r}")

    header("PROJETOS EM DESTAQUE")
    proj = PROJETOS()
    
    try:
        projetos = [proj.sistema_monitoramento(), proj.system_pulse()]
        for nome, stack, desc, link in projetos:
            print(f"PROJETO: {nome}")
            print(f"STACK:   {stack}")
            print(f"DESC:    {desc}")
            print(f"LINK:    {link}\n")
    except TypeError:
        print("Aviso: Verifique os 'returns' da classe PROJETOS.")

    header("SISTEMA API")
    api_response = API().hire_me()
    print(f"Resposta HTTP: {api_response['status']}")
    print(f"Mensagem:      {api_response['message']}")

    print("\n" + "="*40)
    print(">>> [LOG]: Currículo renderizado com sucesso.")
    print("="*40)

if __name__ == "__main__":
    display_resume()
