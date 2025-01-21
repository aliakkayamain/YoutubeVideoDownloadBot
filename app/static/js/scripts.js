const modeToggle = document.getElementById('modeToggle');
const themeStylesheet = document.getElementById('themeStylesheet');
    
// Başlangıç modu kontrol et
const currentMode = localStorage.getItem('mode') || 'light';
themeStylesheet.href = `/static/css/${currentMode}Mode.css`;
modeToggle.checked = currentMode === 'dark';

// Mod değiştirici buton
modeToggle.addEventListener('change', () => {
    const newMode = modeToggle.checked ? 'dark' : 'light';
    themeStylesheet.href = `/static/css/${newMode}Mode.css`;
    localStorage.setItem('mode', newMode);
});