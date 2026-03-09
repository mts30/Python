import os
import shutil
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

caminho = r"C:/Users/lucaa/Downloads"

TIPOS = {
    "Imagens": [".png", ".jpg", ".jpeg", ".gif", ".webp", ".jfif"],
    "PDFs": [".pdf"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Programas": [".exe", ".msi"],
    "Compactados": [".zip", ".rar"]
}


class Organizador(FileSystemEventHandler):

    def on_created(self, event):
        if event.is_directory:
            return

        arquivo = event.src_path

        # Ignora arquivo temporário
        if arquivo.endswith(".tmp") or arquivo.endswith(".crdownload"):
            return

        # espera o arquivo estabilizar
        time.sleep(2)

        # Verifica se o arquivo ainda existe
        if not os.path.exists(arquivo):
            return

        # Separa o nome e o tipo do arquivo
        nome, extensao = os.path.splitext(arquivo)

        destino = None

        # Caso a extensao exista na variavel TIPOS, o arquivo é enviado para lá
        for pasta, extensoes in TIPOS.items():
            if extensao.lower() in extensoes:
                destino = os.path.join(caminho, pasta)
                break

        # Caso a extensao nao exista na variavel TIPOS, o arquivo é enviado para a pasta 'Download/Outros'
        if destino is None:
            destino = os.path.join(caminho, "Outros")

        # Cria a pasta caso ela não exista
        if not os.path.exists(destino):
            os.makedirs(destino)

        try:
            novo_caminho = os.path.join(destino, os.path.basename(arquivo))
            shutil.move(arquivo, novo_caminho)
            print(f"Arquivo movido para {destino}")

        except Exception as e:
            print("Erro ao mover arquivo:", e)


if __name__ == "__main__":

    evento = Organizador()
    observador = Observer()

    observador.schedule(evento, caminho, recursive=False)

    observador.start()

    print("Organizador automático rodando...")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observador.stop()

    observador.join()
