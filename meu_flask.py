from flask import Flask

# Declara a criação do app em Flask
app = Flask(__name__)

# Nossa primeira rota: esta é a página inicial
@app.route('/') # Toda rota precisa ter uma função em seguida
def home():
    return """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>Bem-vindo</title>

<style>
*{
    margin:0;
    padding:0;
    box-sizing:border-box;
    font-family:'Segoe UI',sans-serif;
}

body{
    height:100vh;
    display:flex;
    justify-content:center;
    align-items:center;
    overflow:hidden;
    background:linear-gradient(
        135deg,
        #0f172a 0%,
        #1e1b4b 40%,
        #312e81 100%
    );
}

.background{
    position:absolute;
    inset:0;
}

.circle{
    position:absolute;
    border-radius:50%;
    filter:blur(80px);
    opacity:.5;
    animation:float 8s infinite ease-in-out;
}

.circle:nth-child(1){
    width:300px;
    height:300px;
    background:#3b82f6;
    top:10%;
    left:10%;
}

.circle:nth-child(2){
    width:250px;
    height:250px;
    background:#8b5cf6;
    bottom:10%;
    right:10%;
    animation-delay:2s;
}

.circle:nth-child(3){
    width:200px;
    height:200px;
    background:#06b6d4;
    top:50%;
    left:60%;
    animation-delay:4s;
}

.card{
    position:relative;
    z-index:10;
    text-align:center;
    padding:60px;
    min-width:600px;
    border-radius:32px;
    background:rgba(255,255,255,0.08);
    backdrop-filter:blur(15px);
    border:1px solid rgba(255,255,255,0.15);
    box-shadow:
        0 20px 60px rgba(0,0,0,.35),
        0 0 40px rgba(59,130,246,.2);
}

.logo{
    width:90px;
    height:90px;
    margin:0 auto 25px;
    border-radius:24px;
    background:linear-gradient(135deg,#3b82f6,#8b5cf6);
    display:flex;
    justify-content:center;
    align-items:center;
    color:white;
    font-size:38px;
    font-weight:bold;
    animation:pulse 2.5s infinite;
}

h1{
    color:white;
    font-size:3.5rem;
    margin-bottom:15px;
    font-weight:700;
}

.highlight{
    background:linear-gradient(90deg,#60a5fa,#a78bfa);
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
}

p{
    color:rgba(255,255,255,.85);
    font-size:1.2rem;
    margin-top:10px;
}

.cursor{
    display:inline-block;
    color:#60a5fa;
    animation:blink .8s infinite;
}

.btn{
    display:inline-block;
    margin-top:35px;
    border:none;
    padding:14px 32px;
    border-radius:14px;

    font-size:16px;
    font-weight:600;
    text-decoration:none;

    color:white;

    background:linear-gradient(
        135deg,
        #3b82f6,
        #8b5cf6
    );

    transition:.3s;
}

.btn:hover{
    transform:translateY(-3px) scale(1.03);
    box-shadow:0 10px 30px rgba(99,102,241,.5);
}

@keyframes pulse{
    0%,100%{
        transform:scale(1);
    }
    50%{
        transform:scale(1.08);
    }
}

@keyframes float{
    0%,100%{
        transform:translateY(0);
    }
    50%{
        transform:translateY(-40px);
    }
}

@keyframes blink{
    50%{
        opacity:0;
    }
}

@media(max-width:768px){
    .card{
        min-width:auto;
        width:90%;
        padding:40px 25px;
    }

    h1{
        font-size:2.3rem;
    }
}
</style>
</head>

<body>

<div class="background">
    <div class="circle"></div>
    <div class="circle"></div>
    <div class="circle"></div>
</div>

<div class="card">
    <div class="logo">✦</div>

    <h1>
        <span id="typing"></span>
        <span class="cursor">|</span>
    </h1>

    <p>
        Sua plataforma está pronta. Explore, crie e transforme dados em resultados.
    </p>

    /sobre class="btn">Sobre</a>
</div>

<script>
const text = "Bem-vindo";
const typing = document.getElementById("typing");

let i = 0;

function write(){
    if(i < text.length){
        typing.innerHTML += text.charAt(i);
        i++;
        setTimeout(write, 120);
    }else{
        typing.innerHTML =
        '<span class="highlight">' + text + '</span>';
    }
}

write();
</script>

</body>
</html>
"""

@app.route('/sobre')
def sobre():
    return """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>Sobre o Projeto</title>

<style>

*{
    margin:0;
    padding:0;
    box-sizing:border-box;
    font-family:'Segoe UI',sans-serif;
}

body{
    min-height:100vh;
    display:flex;
    justify-content:center;
    align-items:center;
    overflow:hidden;
    background:linear-gradient(
        135deg,
        #0f172a,
        #1e1b4b,
        #312e81
    );
}

.background{
    position:absolute;
    inset:0;
}

.glow{
    position:absolute;
    border-radius:50%;
    filter:blur(90px);
    opacity:.4;
}

.glow:nth-child(1){
    width:350px;
    height:350px;
    background:#3b82f6;
    top:-80px;
    left:-80px;
    animation:float 8s infinite ease-in-out;
}

.glow:nth-child(2){
    width:300px;
    height:300px;
    background:#8b5cf6;
    bottom:-60px;
    right:-60px;
    animation:float 10s infinite ease-in-out reverse;
}

.container{
    position:relative;
    z-index:2;
    width:900px;
    max-width:90%;
}

.card{
    background:rgba(255,255,255,.08);
    backdrop-filter:blur(18px);
    border:1px solid rgba(255,255,255,.12);
    border-radius:32px;
    padding:50px;
    text-align:center;

    box-shadow:
        0 20px 60px rgba(0,0,0,.35),
        0 0 40px rgba(59,130,246,.15);

    animation:fadeUp 1s ease;
}

.icon{
    width:100px;
    height:100px;
    margin:0 auto 25px;

    border-radius:24px;

    display:flex;
    align-items:center;
    justify-content:center;

    background:linear-gradient(
        135deg,
        #3b82f6,
        #8b5cf6
    );

    font-size:48px;
    color:white;

    animation:pulse 3s infinite;
}

h1{
    color:white;
    font-size:3rem;
    margin-bottom:15px;
}

.highlight{
    background:linear-gradient(
        90deg,
        #60a5fa,
        #a78bfa
    );

    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
}

.description{
    color:rgba(255,255,255,.85);
    font-size:1.15rem;
    line-height:1.8;
    max-width:700px;
    margin:0 auto;
}

.techs{
    margin-top:35px;

    display:flex;
    justify-content:center;
    flex-wrap:wrap;
    gap:12px;
}

.badge{
    padding:10px 18px;
    border-radius:999px;

    background:rgba(255,255,255,.08);

    border:1px solid rgba(255,255,255,.12);

    color:white;
    font-size:.95rem;

    transition:.3s;
}

.badge:hover{
    transform:translateY(-3px);
    background:rgba(255,255,255,.12);
}

.footer{
    margin-top:30px;
    color:#93c5fd;
    font-weight:600;
    letter-spacing:.5px;
}

@keyframes pulse{
    0%,100%{
        transform:scale(1);
    }
    50%{
        transform:scale(1.08);
    }
}

@keyframes float{
    0%,100%{
        transform:translateY(0);
    }
    50%{
        transform:translateY(-30px);
    }
}

@keyframes fadeUp{
    from{
        opacity:0;
        transform:translateY(30px);
    }

    to{
        opacity:1;
        transform:translateY(0);
    }
}

@media(max-width:768px){

    h1{
        font-size:2rem;
    }

    .card{
        padding:35px 25px;
    }

}

</style>
</head>

<body>

<div class="background">
    <div class="glow"></div>
    <div class="glow"></div>
</div>

<div class="container">

    <div class="card">

        <div class="icon">
            🐍
        </div>

        <h1>
            Projeto desenvolvido em
            <span class="highlight">Python</span>
        </h1>

        <p class="description">
            Este site foi criado utilizando principalmente a linguagem Python,
            aplicando conceitos fundamentais e avançados de desenvolvimento.
            O projeto foi desenvolvido durante o curso
            <strong>Programação Básica e Avançada em Python</strong>,
            oferecido pelo <strong>Grupo HDI</strong>, com foco na construção
            de aplicações modernas, organização de código e boas práticas de programação.
        </p>

        <div class="techs">
            <div class="badge">Python</div>
            <div class="badge">HTML</div>
            <div class="badge">CSS</div>
            <div class="badge">JavaScript</div>
            <div class="badge">Web Development</div>
        </div>

        <div class="footer">
            🚀 Aprendizado • Desenvolvimento • Inovação
        </div>

    </div>

</div>

<script>

const badges = document.querySelectorAll('.badge');

badges.forEach((badge, index) => {

    badge.style.opacity = "0";
    badge.style.transform = "translateY(15px)";

    setTimeout(() => {
        badge.style.transition = ".5s";
        badge.style.opacity = "1";
        badge.style.transform = "translateY(0)";
    }, 150 * index);

});

</script>

</body>
</html>
"""

@app.route('/juliana')
def juliana():
    return """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>Sobre Mim</title>

<style>

*{
    margin:0;
    padding:0;
    box-sizing:border-box;
    font-family:'Segoe UI',sans-serif;
}

body{
    min-height:100vh;
    display:flex;
    justify-content:center;
    align-items:center;
    overflow:hidden;
    background:linear-gradient(
        135deg,
        #0f172a 0%,
        #1e1b4b 45%,
        #312e81 100%
    );
}

.background{
    position:absolute;
    inset:0;
}

.glow{
    position:absolute;
    border-radius:50%;
    filter:blur(90px);
    opacity:.45;
}

.glow:nth-child(1){
    width:350px;
    height:350px;
    background:#3b82f6;
    top:-50px;
    left:-80px;
    animation:float 8s ease-in-out infinite;
}

.glow:nth-child(2){
    width:280px;
    height:280px;
    background:#8b5cf6;
    bottom:-40px;
    right:-60px;
    animation:float 10s ease-in-out infinite reverse;
}

.card{
    position:relative;
    z-index:2;
    width:850px;
    max-width:95%;
    padding:50px;
    border-radius:32px;
    background:rgba(255,255,255,0.08);
    backdrop-filter:blur(18px);
    border:1px solid rgba(255,255,255,0.12);

    box-shadow:
        0 20px 60px rgba(0,0,0,.35),
        0 0 40px rgba(59,130,246,.15);

    animation:showCard 1s ease;
}

.header{
    display:flex;
    align-items:center;
    gap:25px;
    margin-bottom:35px;
}

.avatar{
    width:110px;
    height:110px;
    border-radius:50%;
    background:linear-gradient(
        135deg,
        #3b82f6,
        #8b5cf6
    );

    display:flex;
    align-items:center;
    justify-content:center;

    color:white;
    font-size:42px;
    font-weight:bold;

    box-shadow:0 0 30px rgba(99,102,241,.5);
}

.title h1{
    color:white;
    font-size:2.6rem;
    margin-bottom:6px;
}

.title p{
    color:rgba(255,255,255,.75);
    font-size:1rem;
}

.info-grid{
    display:grid;
    grid-template-columns:repeat(2,1fr);
    gap:18px;
}

.info-card{
    padding:18px;
    border-radius:18px;
    background:rgba(255,255,255,.05);
    border:1px solid rgba(255,255,255,.08);
    transition:.3s;
}

.info-card:hover{
    transform:translateY(-4px);
    background:rgba(255,255,255,.08);
}

.label{
    color:#93c5fd;
    font-size:.85rem;
    margin-bottom:6px;
    text-transform:uppercase;
    letter-spacing:1px;
}

.value{
    color:white;
    font-size:1.1rem;
    font-weight:500;
}

.bio{
    margin-top:30px;
    padding:25px;
    border-radius:20px;
    background:rgba(255,255,255,.04);
    border:1px solid rgba(255,255,255,.08);
}

.bio h2{
    color:white;
    margin-bottom:12px;
}

.bio p{
    color:rgba(255,255,255,.8);
    line-height:1.7;
}

.badge{
    display:inline-block;
    margin-top:20px;
    padding:10px 18px;
    border-radius:999px;

    background:linear-gradient(
        135deg,
        #3b82f6,
        #8b5cf6
    );

    color:white;
    font-weight:600;
    font-size:.9rem;
}

@keyframes float{
    0%,100%{
        transform:translateY(0);
    }
    50%{
        transform:translateY(-25px);
    }
}

@keyframes showCard{
    from{
        opacity:0;
        transform:translateY(20px);
    }
    to{
        opacity:1;
        transform:translateY(0);
    }
}

@media(max-width:768px){

    .header{
        flex-direction:column;
        text-align:center;
    }

    .info-grid{
        grid-template-columns:1fr;
    }

    .title h1{
        font-size:2rem;
    }

}

</style>
</head>

<body>

<div class="background">
    <div class="glow"></div>
    <div class="glow"></div>
</div>

<div class="card">

    <div class="header">

        <div class="avatar">
            JB
        </div>

        <div class="title">
            <h1 id="name">Juliana</h1>
            <p>Conheça um pouco mais sobre mim</p>
        </div>

    </div>

    <div class="info-grid">

        <div class="info-card">
            <div class="label">Nome</div>
            <div class="value">Juliana</div>
        </div>

        <div class="info-card">
            <div class="label">E-mail</div>
            <div class="value"></div>
        </div>

        <div class="info-card">
            <div class="label">Profissão</div>
            <div class="value">ANL MODEL PRECIF III</div>
        </div>

        <div class="info-card">
            <div class="label">Empresa</div>
            <div class="value">HDI</div>
        </div>

        <div class="info-card">
            <div class="label">Área</div>
            <div class="value">Dados e Gestão de Portfólio</div>
        </div>

    </div>

    <div class="bio">
        <h2>Sobre Mim</h2>

        <p>
            Sou uma profissional especializada em análise de dados e tomada
            de decisão baseada em informações estratégicas.
            Busco continuamente aprimorar processos, gerar eficiência
            e transformar dados em resultados relevantes para o negócio.
        </p>

        <div class="badge">
            ✨ Perfil Profissional
        </div>

    </div>

</div>

<script>

const cards = document.querySelectorAll('.info-card');

cards.forEach((card, index) => {

    card.style.opacity = "0";
    card.style.transform = "translateY(20px)";

    setTimeout(() => {
        card.style.transition = ".5s";
        card.style.opacity = "1";
        card.style.transform = "translateY(0)";
    }, 150 * index);

});

</script>

</body>
</html>
"""

#Rota com variáveis na URL
@app.route('/ola/<nome>')
def ola(nome):
    return f"<h2>Olá, {nome}</h2>"

# Iniciar o servidor
if __name__ == '__main__':
    app.run(debug=True)

