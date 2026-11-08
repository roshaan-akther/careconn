document.addEventListener('DOMContentLoaded', () => {
  // auto-dismiss flash messages
  document.querySelectorAll('.flash').forEach((el) => {
    setTimeout(() => { el.style.transition = 'opacity .4s'; el.style.opacity = '0'; setTimeout(() => el.remove(), 450); }, 4000);
  });
  // close mobile sidebar on outside click
  document.addEventListener('click', (e) => {
    const sb = document.getElementById('sidebar');
    if (sb && sb.classList.contains('open') && !sb.contains(e.target) && !e.target.closest('.menu-toggle')) {
      sb.classList.remove('open');
    }
  });
});
