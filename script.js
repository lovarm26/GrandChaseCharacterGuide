function toggleTheme() {
    document.body.classList.toggle('bg-light');
    document.body.classList.toggle('text-dark');
    document.querySelectorAll('.bg-secondary').forEach(el => el.classList.toggle('bg-light'));
    document.querySelectorAll('.text-light').forEach(el => el.classList.toggle('text-dark'));
}

function filterCharacters() {
    const query = document.getElementById('searchInput').value.toLowerCase();
    document.querySelectorAll('.character-card').forEach(card => {
        const name = card.getAttribute('data-name').toLowerCase();
        card.style.display = name.includes(query) ? 'block' : 'none';
    });
}