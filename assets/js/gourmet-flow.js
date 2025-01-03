const navItems = document.querySelectorAll('.nav-item');

const thisitem = document.getElementById("Game");
thisitem.classList.toggle('active')

// 遍历所有导航项，并添加点击事件监听
navItems.forEach(item => {
    item.addEventListener('click', function() {
        // 移除其他nav-item的active类
        navItems.forEach(nav => nav.classList.remove('active'));

        // 给当前点击的nav-item添加active类
        this.classList.add('active');
    });
});