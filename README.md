# video-desc
Extrai metadados de arquivos de vídeo para edição posterior.

Este programa utiliza Python 3, [Python-Magic](https://github.com/ahupp/python-magic) e o pacote de programas para edição de software FFmpeg para obtenção das informações sobre os vídeos (utilizando o comando ffprobe).

Para obter o FFmpeg utilize as instruções contidas em: http://ffmpeg.org/download.html

Exemplo de saída do script:

    Lendo diretório:  /home/otavio/Vídeos/2016/2016_02_08-Printrbot44
    video/quicktime
    f3067274_ftyp.mov - 00h20m00.10s
    application/xml
    Arquivo: printrbot44.kdenlive não é um vídeo.
    video/mp4
    printrbot44.mp4 - 00h16m58.48s
    video/quicktime
    image/jpeg
    Arquivo: MAH00651.THM não é um vídeo.
    video/quicktime
    DSC_5688.MOV - 00h00m13.71s
    audio/mp4
    Arquivo: MAH00651.MP4 não é um vídeo.

TODO
 - ordenar os arquivos alfabeticamente
 - incluir informação da câmera utilizada
 - internacionalizar
 - possibilitar a escolha dos dados a incluir (duração, câmera, data, hora de gravação)
 - GUI ?
