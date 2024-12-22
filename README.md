# Poison
![bandicam 2024-12-22 14-32-21-240](https://github.com/user-attachments/assets/01250901-602f-4f6e-a6c0-4cee1683ca4f)

O projeto Poison é uma ferramenta desenvolvida para identificar vulnerabilidades de Execução Remota de Código (RCE) em sites. Escrito em Python, o script permite que usuários testem URLs específicas, executando comandos no servidor alvo para verificar possíveis falhas de segurança.

Funcionalidades Principais:

- Teste de RCE: O script permite que o usuário forneça uma URL e um comando para verificar se o site é vulnerável a RCE.

- Entrada de Usuário: Utiliza a biblioteca argparse para receber parâmetros do usuário, como a URL alvo e o comando a ser executado.

- Requisições HTTP: Emprega a biblioteca requests para enviar requisições HTTP GET ao servidor alvo.

## Como Baixar e executar
```bash
git clone https://github.com/Israelzkn/Poison
cd Poison
pip install requests
python poison.py -u <URL_ALVO> -c <COMANDO>
```
