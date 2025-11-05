document.addEventListener('DOMContentLoaded', () => {
    const loginToggle = document.getElementById('login-toggle');
    const signupToggle = document.getElementById('signup-toggle');
    const loginForm = document.getElementById('login-form');
    const signupForm = document.getElementById('signup-form');

    // Função para mostrar o formulário de Login
    loginToggle.addEventListener('click', () => {
        loginForm.classList.remove('hidden');
        signupForm.classList.add('hidden');
        loginToggle.classList.add('active');
        signupToggle.classList.remove('active');
    });

    // Função para mostrar o formulário de Cadastro
    signupToggle.addEventListener('click', () => {
        signupForm.classList.remove('hidden');
        loginForm.classList.add('hidden');
        signupToggle.classList.add('active');
        loginToggle.classList.remove('active');
    });

    // Opcional: Adicionar lógica básica de submissão (prevenir o recarregamento da página)
    loginForm.addEventListener('submit', (e) => {
        e.preventDefault();
        alert('Tentativa de Login (Apenas demonstração)');
    });

    signupForm.addEventListener('submit', (e) => {
        e.preventDefault();
        alert('Tentativa de Cadastro (Apenas demonstração)');
    });
});