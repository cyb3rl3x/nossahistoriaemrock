# 🎸 Nossa História em Rock

Site romântico para casal, em estilo rock'n'roll, feito em Streamlit.

## Como usar

1. **Adicione suas fotos** na pasta `assets/`:
   - `hero.jpg` (foto de capa, fullscreen)
   - `foto1.jpg`, `foto2.jpg`, `foto3.jpg`, `foto4.jpg` (galeria "Nossos Momentos")

2. **Edite o conteúdo** no topo do arquivo `app.py`, na seção
   `EDITE AQUI O CONTEÚDO DO CASAL`:
   - Nomes (`NOME_ELA`, `NOME_ELE`)
   - Data de início do relacionamento (`DATA_INICIO`)
   - URL pública do site (`URL_SITE`, usada para gerar o QR Code)
   - Eventos da "Nossa Turnê" (linha do tempo)
   - Fotos e legendas de "Nossos Momentos"
   - Setlist com links de embed do Spotify
   - Curiosidades do "Backstage"
   - Mensagens da "Surpresa" aleatória
   - Texto da "Carta"
   - Mensagem final

3. **Rodar localmente**:

```bash
pip install -r requirements.txt
streamlit run app.py
```

4. **Publicar no Streamlit Cloud**:
   - Suba este repositório no GitHub (incluindo a pasta `assets/`)
   - Acesse https://streamlit.io/cloud
   - Conecte o repositório e selecione `app.py` como arquivo principal
   - Após publicar, atualize `URL_SITE` no `app.py` com o link gerado
     e republique para o QR Code funcionar corretamente.

## Como pegar o link de embed do Spotify

1. Abra a música no Spotify (app ou web)
2. Clique em "..." → "Compartilhar" → "Incorporar faixa"
3. Copie a URL que aparece dentro de `src="..."` (formato:
   `https://open.spotify.com/embed/track/ID_DA_MUSICA`)
4. Cole no campo `spotify` da música correspondente em `SETLIST`

## Estrutura

```
site_rock_casal/
├── app.py
├── requirements.txt
├── .streamlit/
│   └── config.toml
└── assets/
    ├── style.css
    ├── hero.jpg      (adicionar)
    ├── foto1.jpg     (adicionar)
    ├── foto2.jpg     (adicionar)
    ├── foto3.jpg     (adicionar)
    └── foto4.jpg     (adicionar)
```
