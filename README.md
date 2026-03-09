# Organizador Automático de Downloads em Python

Este projeto é um script em Python que organiza automaticamente os arquivos da pasta **Downloads**.  
Sempre que um novo arquivo é baixado, o programa detecta o tipo do arquivo e o move para a pasta correspondente.

## Funcionalidades

- Monitora a pasta **Downloads** em tempo real
- Detecta quando novos arquivos são adicionados
- Organiza automaticamente por tipo de arquivo
- Cria pastas automaticamente caso elas não existam
- Ignora arquivos temporários gerados durante downloads
- Evita erros causados por downloads incompletos

## 📁 Estrutura de organização

Os arquivos são separados nas seguintes categorias:

- **Imagens** → `.png`, `.jpg`, `.jpeg`, `.gif`, `.webp`, `.jfif`
- **PDFs** → `.pdf`
- **Vídeos** → `.mp4`, `.mkv`, `.avi`
- **Programas** → `.exe`, `.msi`
- **Compactados** → `.zip`, `.rar`
- **Outros** → qualquer tipo não listado

## 🛠 Tecnologias utilizadas

- Python
- Biblioteca `watchdog` para monitoramento do sistema de arquivos
- Bibliotecas padrão do Python (`os`, `shutil`, `time`)
