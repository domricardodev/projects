// Variáveis para contar quantas vezes deu "cara" e "coroa"
let heads = 0; // Contador de "cara"
let tails = 0; // Contador de "coroa"

// Seleciona o elemento HTML que representa a moeda
let coin = document.querySelector(".coin");

// Seleciona o botão que faz a moeda girar
let flipBtn = document.querySelector("#flip-button");

// Seleciona o botão que reseta o jogo
let resetBtn = document.querySelector("#reset-button");

// Adiciona um evento de clique ao botão "Girar Moeda"
flipBtn.addEventListener("click", () => {
  // Gera um número aleatório (0 ou 1) para simular o giro da moeda
  let i = Math.floor(Math.random() * 2);

  // Reseta a animação da moeda para garantir que ela gire novamente
  coin.style.animation = 'none';

  // Se o número gerado for 1, significa "cara"
  if (i) {
    // Após 100ms, aplica a animação de giro para "cara"
    setTimeout(function () {
      coin.style.animation = 'spin-heads 3s forwards';
    }, 100);

    // Incrementa o contador de "cara"
    heads++;
  }
  // Se o número gerado for 0, significa "coroa"
  else {
    // Após 100ms, aplica a animação de giro para "coroa"
    setTimeout(function () {
      coin.style.animation = 'spin-tails 3s forwards';
    }, 100);

    // Incrementa o contador de "coroa"
    tails++;
  }

  // Após 3 segundos (tempo da animação), atualiza os contadores na tela
  setTimeout(updateStats, 3000);

  // Desabilita o botão de girar por 3 segundos para evitar cliques repetidos
  disableButton();
});

// Função para atualizar os contadores de "cara" e "coroa" na tela
function updateStats() {
  // Atualiza o texto do elemento que mostra quantas vezes deu "cara"
  document.querySelector('#heads-count').textContent = `Cara: ${heads}`;

  // Atualiza o texto do elemento que mostra quantas vezes deu "coroa"
  document.querySelector('#tails-count').textContent = `Coroa: ${tails}`;
}

// Função para desabilitar o botão de girar por 3 segundos
function disableButton() {
  // Desabilita o botão
  flipBtn.disabled = true;

  // Após 3 segundos, reabilita o botão
  setTimeout(function () {
    flipBtn.disabled = false;
  }, 3000);
}

// Adiciona um evento de clique ao botão "Resetar"
resetBtn.addEventListener('click', () => {
  // Para a animação da moeda
  coin.style.animation = 'none';

  // Zera os contadores de "cara" e "coroa"
  heads = 0;
  tails = 0;

  // Atualiza os contadores na tela para mostrar 0
  updateStats();
});
