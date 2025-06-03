import streamlit as st
import streamlit as st
from datetime import datetime
import time

st.set_page_config(page_title="Leh & Vini", page_icon="heart-1.ico")

# Data de início do relacionamento
data_inicio = datetime(2024, 12, 24, 23, 6, 0)  # exemplo: 10 de maio de 2023, às 20h30


@st.dialog("<3")
def caixa_modal(texto):
    st.write(texto)
@st.dialog("Você aceita ser minha princesa pro resto da vida novamente??🥰")
def pedido_namoro():
    if st.button("Sim, para sempre", use_container_width= True):
        st.write('Te amo muito minha linda!!😊❤️')
# Using "with" notation
with st.sidebar:
    # Fotos de vocês dois aqui <3
    st.header("O ínicio de tudo ❤️", divider= "blue")
    st.image("conversa 2-735.jpg",
             caption='(15 de agosto de 2024) No meu aniversário me deparei com essa sua mensagem me parabenizando. Logo me veio uma memória de que havia apertado sua mão naquele dia em um culto na Sede, onde ainda não nos falavamos, mas acredito que ali seria um incentivo para o ínicio de nossa história...❤️')
    st.header("", divider= "blue")
    st.image("conversa1-735.jpg",
             caption='(17 de agosto de 2024) Aqui onde tudo começou, dois dias após meu aniversário, você comentou na postagem do nosso laion, e quem diria que a partir daí tudo começaria a mudar na nossas vidas, as batidas do meu coração elevaram a cada minuto que falava com você e ali mesmo demonstramos o nosso interesse um pelo outro, a partir dali começei a apresentar você ao Senhor nas minhas orações mais sinceras...❤️')
    st.header("", divider= "blue")
    st.image("foto-V&L-736px.png",
             caption='(19 de Outubro de 2024) O dia que nos vimos pela "primeira" vez em um Night Power na Sul, após alguns meses se falando por chat , te encontrei desde nosso primeiro aperto de mão com uma troca de sorrisos na inauguração da nova Logos Sede, neste dia (apesar de ciente do sentimento recíproco um pelo outro) eu ainda temia, pois estava receoso do que estava por acontecer, não estava tão esperançoso, mas neste dia a melhor parte do meu dia foi olhar nos seus olhos que brilhavam ao olhar para mim, eu os admirava, e a cada olhar neles eu podia ver minha face refletida em seus belos olhos e uma chama de esperança e amor se acendia dentro de mim...❤️')
    st.header("", divider= "blue")
    st.image("conversa3-735.jpg",
             caption='(25 de Dezembro de 2024) Aqui mandei uma mensagem de Feliz Natal para você, mandei essa mensagem pois já fazia meses sem nos falar. Como visto na mensagem ,durante este tempo, eu ainda não havia deixado o sentimento que tinha por você de lado, nunca o deixei e vi que era recíproco. A partir daí em diante através das nossas conversas eu vi que você foi a melhor coisa que me aconteceu nessa vida há muito tempo...❤️')
    st.header("", divider= "blue")
    st.image("foto_love-735.jpg",
             caption='(9 de Janeiro de 2025) Essa foto significa muito para mim, pois vejo que Deus sempre agiu em nossas vidas, nesse dia ele fez tudo perfeito, nos vimos depois de meses e com um sentimento certeiro e formado do amor que nos rodeia, ali já não estava mais inseguro do que sentia, mas sim a certeza de queria te amar até o fim dos séculos. Tive a oportunidade de conhecer seus pais e aumentar mais a vontade de fazer parte dessa família linda. Deixamos nossos pais conversando e isso me alegrou, pois enquanto eles se conheciam, tivemos a oportunidade de conversar face a face, pude olhar nos seus olhos que iluminavam minha alma, e sentir a leveza de sua prensença a mim, senti seu cheiro, batemos um bom papo, e ali a coisa começou a se desenrolar kkkk. Ali eu pude ter a certeza de que Deus já havia começado a escrever a nossa história juntos desde a fundação do mundo há milhares de anos atrás...❤️')
    st.header("O amor está no ar...❤️", divider= "blue")
    st.image("IMG-1-735px.jpg",
             caption="Entre 24 a 26 de Janeiro de 2025...💞")
    st.image("IMG-2-735px.jpg",
             caption="Entre 24 a 26 de Janeiro de 2025...💞")
    st.image("IMG-3-735px.jpg",
             caption="Entre 24 a 26 de Janeiro de 2025...💞")
    st.image("IMG-4-735px.jpg",
             caption='O AMOR ESTÁ NO ARR!!❤️ Esses foram os 3 dias que passei ao seu lado, junto de seus pais e sua família, amei cada segundo que passei ao seu lado, pude refletir no quão boa, perfeita e agradável é a vontade de Deus para as nossas vidas. Tive a oportunidade de dar o meu primeiro beijo na mulher da minha vida, pela primeira vez na minha vida pude ter a certeza e sentir beijar os lábios da pessoa certa que um dia será a mãe dos nossos filhos, percebi nesses dias seu cuidado a mim desde os pequenos detalhes, seu olhar me encantava a cada vez que eu os admirava, nossa troca de olhares e sorrisos, nossas palavras de afirmações, momento de qualidade, conversa até tarde da noite, troca de afetos, o boa noite acompanhado de um beijo, cada vez que eu te chamei de linda, nossas mãos entrelaçadas, me fizeram te conhecer e amar cada vez mais a benção que o Senhor colocou no meu caminho, te admiro meu bem, amo o seu jeito único de ser e agir, esses dias de muitos que virão pela frente ficarão eternizados em nossas memórias, quero viver cada momento ao seu lado como se fosse o último. Meu choro após esses dias foram de alegria, gratidão e saudades por querer mais e mais estar perto do amor da minha vida, mas sei que não nos faltará momentos, e sei que um dia realizaremos nossos sonhos e poderemos enfim viver para sempre um ao lado do outro até o fim. A cada dia meu amor por você não somente se renova, mas também fica mais forte assim como as misericórdias e o amor do nosso Senhor em nossas vidas! Posso afirmar com toda conviccção de que você é a mulher da minha vida, minha primeira namorada, minha parceira, e minha última, e futura esposa, você hoje é minha oração diária, mas daqui a pouco eu vou te pedir em namoro, depois em noivado e por fim casar com você. Amar não é um sentimento, Amar é uma decisão, decisão de cuidar, de suportar, de estar sempre ao seu lado, de te amar assim como Cristo ama seu rebanho! Tenho a certeza de que estamos no caminho certo, esperando sempre em Deus com paciência e paz por cada etapa que está por vir, sempre pondo Ele na frente de tudo, estamos fazendo o certo, pode parecer que ás vezes está demorando, mas sabemos que na verdade Ele está caprichando em cada detalhe de nossas vidas e de nosso futuro juntos!!❤️ Eu te amo minha princesa, te amar, cuidar, valorizar e zelar pela sua vida a cada dia é o meu anseio, e isso não vai mudar até o fim da minha vida, eu amo te amar minha gatinha...!❤️')
    st.header("Celebrando sua formatura❤️", divider= "blue")
    st.image("IMG-20250304-WA0005.jpg",
             caption='07 de Fevereiro de 2025...💞')
    st.header("", divider= "blue")
    st.image("IMG-20250304-WA0000.jpg",
             caption='07 de Fevereiro de 2025...💞')
    st.header("", divider= "blue")
    st.image("IMG-20250304-WA0007.jpg",
             caption='07 de Fevereiro de 2025...💞')
    st.header("", divider= "blue")
    st.image("IMG-20250304-WA0009.jpg",
             caption='07 de Fevereiro de 2025...💞')
    st.header("", divider= "blue")
    st.image("IMG-20250304-WA0006.jpg",
             caption='07 de Fevereiro de 2025...💞')
    st.header("", divider= "blue")
    st.header("Mais e mais momentos...❤️", divider= "blue")
    st.image("735a.jpg",
             caption='14 de Fevereiro de 2025...💞')
    st.image("735b.jpg",
             caption='14 de Fevereiro de 2025...💞')
    st.image("735c.jpg",
             caption='14 de Fevereiro de 2025...💞')
    st.video("VID-20250215-WA0004.mp4")
    st.image("735k.jpg",
             caption='15 de Fevereiro de 2025...💞')
    st.image("735l.jpg",
             caption='15 de Fevereiro de 2025...💞')
    st.image("735m.jpg",
             caption='15 de Fevereiro de 2025...💞')
    st.image("735d.jpg",
             caption='15 de Fevereiro de 2025...💞')
    st.image("735e.jpg",
             caption='15 de Fevereiro de 2025...💞')
    st.image("735f.jpg",
             caption='16 de Fevereiro de 2025...💞')
    st.image("735g.jpg",
             caption='16 de Fevereiro de 2025...💞')
    st.image("735h.jpg",
             caption='16 de Fevereiro de 2025...💞')
    st.image("735i.jpg",
             caption='16 de Fevereiro de 2025...💞')
    st.video("despedida.mp4.mp4")
    st.image("735j.jpg",
             caption='16 de Fevereiro de 2025...💞')
    st.header("Dias antes do retiro💞", divider= "blue")
    st.image("IMG-20250222-WA0100.jpg",
             caption='22 de Fevereiro de 2025...💞')
    st.header("", divider= "blue")
    st.image("IMG-20250222-WA0101.jpg",
             caption='22 de Fevereiro de 2025...💞')
    st.header("5 Dias cheios de Deus, alegria, amor e emoção ao seu lado!!❤️", divider= "blue")
    st.image("IMG-20250305-WA0254.jpg", 
             caption='28 de Fevereiro a 04 Março de 2025...💞')
    st.header("", divider= "blue")
    st.image("IMG-20250305-WA0246.jpg", 
             caption='28 de Fevereiro a 04 Março de 2025...💞')
    st.header("", divider= "blue")
    st.image("IMG-20250305-WA0248.jpg", 
             caption='28 de Fevereiro a 04 Março de 2025...💞')
    st.header("", divider= "blue")
    st.image("IMG-20250305-WA0251.jpg", 
             caption='28 de Fevereiro a 04 Março de 2025...💞')
    st.header("", divider= "blue")
    st.image("IMG-20250305-WA0236.jpg", 
             caption='28 de Fevereiro a 04 Março de 2025...💞')
    st.header("", divider= "blue")
    st.image("IMG-20250305-WA0235.jpg", 
             caption='28 de Fevereiro a 04 Março de 2025...💞')
    st.header("", divider= "blue")
    st.image("IMG-20250305-WA0233.jpg", 
             caption='28 de Fevereiro a 04 Março de 2025...💞')
    st.header("", divider= "blue")
    st.image("IMG-20250304-WA0012.jpg", 
             caption='28 de Fevereiro a 04 Março de 2025...💞')
    st.header("", divider= "blue")
    st.image("IMG-20250304-WA0017.jpg", 
             caption='28 de Fevereiro a 04 Março de 2025...💞')
    st.header("", divider= "blue")
    st.image("IMG-20250304-WA0016.jpg", 
             caption='28 de Fevereiro a 04 Março de 2025...💞')
    st.header("", divider= "blue")
    st.image("WhatsApp Image 2025-05-31 at 18.53.43.jpeg",
             caption='...💞')
    st.header("", divider= "blue")
    st.image("WhatsApp Image 2025-05-31 at 18.53.43 (1).jpeg",
             caption='...💞')
    st.header("", divider= "blue")
    st.image("WhatsApp Image 2025-05-31 at 18.53.43 (2).jpeg",
             caption='...💞')
    st.header("", divider= "blue")
    st.image("WhatsApp Image 2025-05-31 at 18.53.43 (3).jpeg",
             caption='...💞')
    st.header("", divider= "blue")
    st.image("WhatsApp Image 2025-05-31 at 18.53.43 (4).jpeg",
             caption='...💞')
    st.header("", divider= "blue")
    st.image("WhatsApp Image 2025-05-31 at 18.53.43 (5).jpeg",
             caption='...💞')
    st.header("", divider= "blue")
    st.image("WhatsApp Image 2025-05-31 at 18.53.43 (7).jpeg",
             caption='...💞')
    st.header("", divider= "blue")
    st.video("WhatsApp Video 2025-05-31 at 18.53.43 (1).mp4")
    st.header("", divider= "blue")
    st.image("WhatsApp Image 2025-05-31 at 18.53.43 (9).jpeg",
             caption='...💞')
    st.header("", divider= "blue")
    st.image("WhatsApp Image 2025-05-31 at 18.53.43 (10).jpeg",
             caption='...aaaaaaaaaa💞💞')
    st.header("", divider= "blue")
    st.image("WhatsApp Image 2025-05-31 at 18.53.43 (11).jpeg",
             caption='...💞')
    st.header("", divider= "blue")
    st.image("WhatsApp Image 2025-05-31 at 18.53.43 (12).jpeg",
             caption='...💞')
    st.header("", divider= "blue")
    st.video("WhatsApp Video 2025-05-31 at 18.53.43 (2).mp4")
    st.header("", divider= "blue")
    st.image("WhatsApp Image 2025-05-31 at 18.53.43 (13).jpeg",
             caption='Juntos até o fim...!!💞')
    st.header("", divider= "blue")
    st.image("recadinho_735px.png",
             caption='')
    st.header("", divider= "blue")
    

with st.container(border=True):
    
    st.header("Seja bem vinda, este site é 100% ""inspirado em você minha princesa!!😊❤️", divider="blue")
    st.subheader("Nem o mais lindo verso de uma música capaz de demonstrar o que sinto por você minha gatinha...❤️")
    st.audio("Cidade Negra - Onde Você Mora？ (DVD Acústico MTV).mp3", format="audio/mpeg",loop=False)
    st.audio("Final Feliz - Jorge Vercilo.mp3", format="audio/mpeg", loop=False)
    st.audio("3 X 4 (Ao Vivo).mp3", format="audio/mpeg", loop=False)
    st.header("Aperte em cada '❤️' para explorar:", divider="blue")


    col1, col2, col3, col4, col5, col6, col7, col8, col9, col10 = st.columns(10)
    with col1:
        btn1 = st.button(
            "❤️",
            use_container_width= True, key=1)
        if btn1:
            caixa_modal('A saudade só me faz te amar mais e mais a cada segundo...💘')
    with col2:
        btn2 = st.button(
                "❤️",
                use_container_width=True, key=2)
        if btn2:
            caixa_modal('Anseio te ver logo logo e te falar o quanto eu te amo de todas as maneiras possíveis!!💘')
    with col3:
        btn3 = st.button("❤️",
                use_container_width=True, key=3)
        if btn3:
            # Arrumar aqui
            caixa_modal('Estar com você me leva a um universo paralelo onde só existem você e eu...💘')
    with col4:
        btn4 = st.button(
                "❤️",
                use_container_width=True, key=4)
        if btn4:
            pedido_namoro()
    with col5:
        btn5 = st.button(
                "❤️",
                use_container_width=True, key=5)
        if btn5:
            caixa_modal('Conto os segundos para estar ao seu lado..❤️')
    with col6:
        btn6 = st.button(
            "❤️",
            use_container_width=True, key=6)
        if btn6:
            caixa_modal('Meu coração é seu, sou todo seu minha princesa!!💘')
    with col7:
        btn7 = st.button(
            "❤️",
            use_container_width=True, key=7)
        if btn7:
            caixa_modal('Deus, eu e você sempre!!❤️')
    with col8:
        btn8 = st.button(
            "❤️",
            use_container_width=True, key=8)
        if btn8:
            caixa_modal('Mesmo distante... eu te sinto perto a cada segundo com seu cuidado e amor💖')
    with col9:
        btn9 = st.button(
            "❤️",
            use_container_width=True, key=9)
        if btn9:
            caixa_modal('Por você eu esperaria até o final dos tempos...💖')
    with col10:
        btn10 = st.button(
            "❤️",
            use_container_width=True, key=10)
        if btn10:
            caixa_modal('Nada e nem ninguém poderá tirar meu amor de você! Eu te amo até o fim dos tempos minha querida...💖')

st.title("⏳💖 Tempo juntos:")

# 💖 CSS romântico
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Pacifico&family=Roboto:wght@300;700&display=swap');

    .titulo {
        font-family: 'Pacifico', cursive;
        font-size: 3.2em;
        text-align: center;
        background: linear-gradient(90deg, #ff4081, #ff80ab);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 30px;
        animation: pulse 2s infinite;
    }

    .contador {
        font-family: 'Roboto', sans-serif;
        font-size: 1.8em;
        background: #fff0f5;
        padding: 30px;
        border-radius: 25px;
        border: 2px solid #f48fb1;
        box-shadow: 0 8px 20px rgba(255, 105, 180, 0.2);
        text-align: center;
        color: #880e4f;
        transition: all 0.3s ease-in-out;
        margin-top: 20px;
    }

    .contador strong {
        color: #c2185b;
        font-weight: bold;
    }

    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.05); }
        100% { transform: scale(1); }
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="title"></div>', unsafe_allow_html=True)

# Local reservado para o contador
contador = st.empty()

while True:
    agora = datetime.now()
    diferenca = agora - data_inicio

    # Quebra da diferença total
    total_segundos = int(diferenca.total_seconds())
    anos = total_segundos // (365*24*60*60)
    dias_restantes = total_segundos % (365*24*60*60)

    dias = dias_restantes // (24*60*60)
    horas_restantes = dias_restantes % (24*60*60)

    horas = horas_restantes // 3600
    minutos_restantes = horas_restantes % 3600

    minutos = minutos_restantes // 60
    segundos = minutos_restantes % 60

    contador.markdown(
        f"""
        <div class="contador">
        Estamos juntos há:<br><br>
        <strong>{anos}</strong> ano(s), <strong>{dias}</strong> dia(s),<br>
        <strong>{horas}</strong> hora(s), <strong>{minutos}</strong> minuto(s), <strong>{segundos}</strong> segundo(s) 💖
        </div>
        """,
        unsafe_allow_html=True
    )

    time.sleep(1)
