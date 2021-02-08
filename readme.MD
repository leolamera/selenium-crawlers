# Selenoid Crawler

Selenoid foi desenvolvido por um grupo de desenvolvedores da Estônia, que trabalham na empresa Aerokube.
O Selenoid foi escrito em GoLang, pois as integrações entre o java nativo do selenium com os grids do Docker, na visão da Aerokube, não trazia a resposta necessária na escalabilidade.

## Como usar?

O primeiro passo é baixar o configuration manager do selenoid. Informando que esta é a instalação para Linux, caso você deseja instalar em outro ambiente, [aqui está o guia](https://aerokube.com/cm/latest/).

```bash
curl -s https://aerokube.com/cm/bash | bash
```

Sua tela ficará parecida com isto:

![](https://i.ibb.co/D4xW6My/Screenshot-from-2021-02-08-09-33-21.png)

Após o download do arquivo, vamos dar o start no configuration manager com o seguinte comando:

```bash
./cm selenoid start --vnc
```

Este comando instalará todas as dependências de imagens docker que ainda não estão baixas em nossas maquinas. No caso, os webdrivers das últimas versões do firefox, chrome e opera.

![](https://i.ibb.co/vz4bKsx/Screenshot-from-2021-02-08-09-38-01.png)

Para confirmar se o selenoid está realmente rodando, é só acessar http://localhost:4444/

![](https://i.ibb.co/ryXkQrC/Screenshot-from-2021-02-08-09-56-36.png)

E seu diretório devera estar assim:

```bash.
├── cm
├── main.py
├── readme.MD
└── requirements.txt
```

O próximo  passo é instalar a interface gráfica do selenoid. Informando

```bash
./cm selenoid-ui start
```

Para acessar a interface gráfica do selenoid é só acessar http://localhost:8080

![](https://i.ibb.co/4YVDLwL/Screenshot-from-2021-02-08-09-59-07.png)

Para iniciarmos uma sessão em um navegador, devemos clicar em **CAPABILITIES**.
Podemos escolher em qual linguagem queremos executar o driver e qual versão de qual navegador será usado.

![](https://i.ibb.co/WsjSW20/Screenshot-from-2021-02-08-09-59-32.png)

Agora colocamos no código python e executamos qualquer atividade possível com o driver usando o selenium.

![](https://i.ibb.co/bP3SbN0/Screenshot-from-2021-02-08-10-03-04.png)

Visualizamos o navegador controlado pelo nosso código no na interface gráfica.

![](https://i.ibb.co/YZgbmBv/Screenshot-from-2021-02-08-10-02-14.png)

Conseguimos parar os processos usando os seguintes comandos:

```bash
./cm selenoid stop
./cm selenoid-ui stop
```